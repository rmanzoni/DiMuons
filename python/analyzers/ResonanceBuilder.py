import ROOT
# from PhysicsTools.HeppyCore.framework.analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from PhysicsTools.Heppy.physicsobjects.Muon import Muon
from PhysicsTools.Heppy.physicsobjects.Particle import Particle

from CMGTools.DiMuons.physicsobjects.Resonance import Resonance

import pprint 
import itertools

mass = {23: 91., 25: 125., 443: 3.09693}

# load custom library to ROOT. This contains the kinematic vertex fitter class
ROOT.gSystem.Load('libCMGToolsDiMuons')
from ROOT import KVFitter as VertexFitter

class ResonanceBuilder(Analyzer):
    '''Builds resonances from an input collection of particles. 

    Example configuration:

    from PhysicsTools.Heppy.analyzers.examples.ResonanceBuilder import ResonanceBuilder
    dimuons = cfg.Analyzer(
       ResonanceBuilder,
       'dimuons',                            
       leg1_collection = 'muons',            # input collection
       leg2_collection = 'muons',            # input collection
       filter_func_leg1 = lambda x : True,   # filtering function for input objects. here, take all.
       filter_func_leg2 = lambda x : True,   # filtering function for input objects. here, take all.
       pdgid = 23                            # pdgid for the resonances, here Z
       )

    This analyzer puts one collection in the event:
    event.dimuons : all resonances, sorted by their distance to the nominal mass
                    corresponding to the specified pdgid
    '''

    def beginLoop(self, setup):
        super(ResonanceBuilder, self).beginLoop(setup)
        # vertexing stuff
        self.vtxfit = VertexFitter()
#         self.tks = ROOT.std.vector('reco::TrackRef')()
        self.tks = ROOT.std.vector('reco::Track')()
        # event counter
        self.counters.addCounter('ResonanceBuilder')
        count = self.counters.counter('ResonanceBuilder')
        count.register('all events')
        count.register('>0 dimuon')
        count.register('>0 filtered dimuons')

    def declareHandles(self):
        super(ResonanceBuilder, self).declareHandles()
        self.handles['pvs'] = AutoHandle('offlineSlimmedPrimaryVertices', 'std::vector<reco::Vertex>' )        
        self.handles['bs' ] = AutoHandle('offlineBeamSpot'              , 'reco::BeamSpot'            )

    def process(self, event):
        super(ResonanceBuilder, self).readCollections(event.input)

        self.counters.counter('ResonanceBuilder').inc('all events')

        legs1 = getattr(event, self.cfg_ana.leg1_collection)
        legs2 = getattr(event, self.cfg_ana.leg2_collection)

        legs1 = [leg for leg in legs1 if self.cfg_ana.filter_func_leg1(leg)]
        legs2 = [leg for leg in legs2 if self.cfg_ana.filter_func_leg2(leg)]

        resonances = []
        for leg1, leg2 in itertools.product(legs1, legs2):
            if leg1.physObj == leg2.physObj:
                 continue
            ires = Resonance(leg1, leg2, self.cfg_ana.pdgid, 3, mass1=0.1057, mass2=0.1057)
#             ires = Resonance(leg1, leg2, self.cfg_ana.pdgid, 3)
            resonances.append( ires )
            
        if len(resonances)==0:
            return False

        self.counters.counter('ResonanceBuilder').inc('>0 dimuon')

        # filter
        resonances = [ires for ires in resonances if self.cfg_ana.filter_func_res(ires)]

        if len(resonances)==0:
            return False

        self.counters.counter('ResonanceBuilder').inc('>0 filtered dimuons')
                        
        for ires in resonances:
            self.tks.clear()
            if not ires.leg1.bestTrack(): continue
            if not ires.leg2.bestTrack(): continue
#             self.tks.push_back(ires.leg1.track())
#             self.tks.push_back(ires.leg2.track())
            self.tks.push_back(ires.leg1.bestTrack())
            self.tks.push_back(ires.leg2.bestTrack())
            ires.vertex = self.vtxfit.Fit(self.tks)

        # make vertex objects 
        pvs            = self.handles['pvs'].product(); event.pv = pvs[0]
        event.beamspot = self.handles['bs' ].product()

        # save vertex and displacement quantities
        for ires in resonances:
            
            if not ires.vertex.isValid(): continue

            ires.disp3DFromBS     = ROOT.VertexDistance3D().distance(ires.vertex.vertexState(), event.pv)
            ires.disp3DFromBS_sig = ires.disp3DFromBS.significance()
        
            # create an 'ideal' vertex out of the BS
            point = ROOT.reco.Vertex.Point(
                event.beamspot.position().x(),
                event.beamspot.position().y(),
                event.beamspot.position().z(),
            )
            error = event.beamspot.covariance3D()
            chi2 = 0.
            ndof = 0.
            bsvtx = ROOT.reco.Vertex(point, error, chi2, ndof, 2) # size? say 3? does it matter?
                                        
            ires.disp2DFromBS      = ROOT.VertexDistanceXY().distance(ires.vertex.vertexState(), bsvtx)
            ires.disp2DFromBS_sig  = ires.disp2DFromBS.significance()
            ires.prob              = ROOT.TMath.Prob(ires.vertex.normalisedChiSquared(), 1)
            # ires.prob              = ROOT.TMath.Prob(ires.vertex.chi2(), int(ires.vertex().ndof()))        

            perp = ROOT.math.XYZVector(ires.p4().px(),
                                       ires.p4().py(),
                                       0.)
        
            dxybs = ROOT.GlobalPoint(-1*((event.beamspot.x0() - ires.vertex.position().x()) + (ires.vertex.position().z() - event.beamspot.z0()) * event.beamspot.dxdz()), 
                                     -1*((event.beamspot.y0() - ires.vertex.position().y()) + (ires.vertex.position().z() - event.beamspot.z0()) * event.beamspot.dydz()),
                                      0)
        
            vperp = ROOT.math.XYZVector(dxybs.x(), dxybs.y(), 0.)
        
            cos = vperp.Dot(perp)/(vperp.R()*perp.R())
        
            ires.disp2DFromBS_cos = cos
                
        # sorting according to distance to nominal mass
        nominal_mass = mass[self.cfg_ana.pdgid]
        resonances.sort(key=lambda x: (abs(x.charge()), x.vertex.normalisedChiSquared()))
#         resonances.sort(key=lambda x: (abs(x.charge()), abs(x.mass()-3.0969)))

        setattr(event, self.instance_label, resonances)
        


