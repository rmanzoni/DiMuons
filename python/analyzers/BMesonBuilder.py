import ROOT

from itertools import product

from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from PhysicsTools.Heppy.physicsobjects.Muon import Muon
from PhysicsTools.Heppy.physicsobjects.Particle import Particle
from PhysicsTools.Heppy.physicsobjects.PhysicsObject import PhysicsObject

from PhysicsTools.HeppyCore.utils.deltar import deltaR, deltaPhi, inConeCollection, bestMatch

from CMGTools.DiMuons.physicsobjects.BKLL import BKLL

import pprint 
import itertools

# load custom library to ROOT. This contains the kinematic vertex fitter class
ROOT.gSystem.Load('libCMGToolsDiMuons')
from ROOT import KVFitter as VertexFitter


class BMesonBuilder(Analyzer):

    def beginLoop(self, setup):
        super(BMesonBuilder, self).beginLoop(setup)
        # vertexing stuff
        self.vtxfit = VertexFitter()
        self.tks = ROOT.std.vector('reco::Track')()
        # event counter
        self.counters.addCounter('BMesonBuilder')
        count = self.counters.counter('BMesonBuilder')
        count.register('all events')
        count.register('>0 mu mu in jpsi window')
        count.register('>0 B cands')
        count.register('>0 cands in B window')

    def declareHandles(self):
        super(BMesonBuilder, self).declareHandles()
        self.handles['losttracks'] = AutoHandle('lostTracks'        , 'std::vector<pat::PackedCandidate>')
        self.handles['pfcands'   ] = AutoHandle('packedPFCandidates', 'std::vector<pat::PackedCandidate>')

    def process(self, event):
        super(BMesonBuilder, self).readCollections(event.input)
        
        self.counters.counter('BMesonBuilder').inc('all events')

        # get the tracks
        allpf      = map(PhysicsObject, self.handles['pfcands'   ].product())
        losttracks = map(PhysicsObject, self.handles['losttracks'].product())

        # merge the track collections
        event.alltracks = sorted([tt for tt in allpf + losttracks if tt.charge() != 0 and abs(tt.pdgId()) not in (11,13)], key = lambda x : x.pt(), reverse = True)

        # start building the candidates
        cands = []
        
        resonances = getattr(event, self.instance_label, 'resonances')

        if getattr(self.cfg_ana, 'jpsi_window', False):
            resonances = [ires for ires in resonances if abs(ires.mass()-3.0969)<1]
            if len(resonances)==0:
                return False
            self.counters.counter('BMesonBuilder').inc('>0 mu mu in jpsi window')

        # add a track
        for dilep, tk in product(resonances, event.alltracks):
            # pt and sanity checks on the track
            if not tk.bestTrack(): continue
            if tk.pt()<0.8: continue
            # the track must be close enough to the di-lepton candidate
            if deltaR(tk, dilep.p4()) > 1.5: continue
            # try to fit a vertex only if the track's close to the di-ele cand
            if max([abs(dilep.leg1.vz() - tk.vz()), abs(dilep.leg2.vz() - tk.vz())]) > 1.5: continue
            # remove double countings 
            if deltaR(tk, dilep.leg1)<0.01 or deltaR(tk, dilep.leg2)<0.01: continue

            # kaon mass
            tk.setMass(0.493677)
            tk.setPdgId(321 * tk.charge())
                        
            # clear the vectors
            self.tks.clear()
            # create a RecoChargedCandidate for each reconstructed lepton and flush it into the vector
            self.tks.push_back(dilep.leg1.bestTrack())
            self.tks.push_back(dilep.leg2.bestTrack())
            # push the track into the vector
            self.tks.push_back(tk.physObj.bestTrack())

            # fit it!
            vertex = self.vtxfit.Fit(self.tks)
            # check that the vertex is good
            if not vertex.isValid(): continue
            cands.append(BKLL(dilep.leg1, dilep.leg2, tk, vertex, event.beamspot))

        if len(cands)==0: return False

        self.counters.counter('BMesonBuilder').inc('>0 B cands')

        if getattr(self.cfg_ana, 'b_window', True):
            cands = [icand for icand in cands if abs(icand.mass()-5.279)<1]
            if len(cands)==0:
                return False
            self.counters.counter('BMesonBuilder').inc('>0 cands in B window')

        cands.sort(key=lambda x: (x.vtx().normalisedChiSquared()))
        event.theb = cands[0]        
        event.cands = cands        


