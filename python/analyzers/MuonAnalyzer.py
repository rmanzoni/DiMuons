from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from PhysicsTools.Heppy.physicsobjects.Muon import Muon


class MuonAnalyzer(Analyzer):

    def beginLoop(self, setup):
        super(MuonAnalyzer, self).beginLoop(setup)
        self.counters.addCounter('MuonAnalyzer')
        count = self.counters.counter('MuonAnalyzer')
        count.register('all events')
        count.register('>0 selected muons')

    def declareHandles(self):
        super(MuonAnalyzer, self).declareHandles()
        self.handles['muons'] = AutoHandle('slimmedMuons'                 , 'std::vector<pat::Muon>'    )        
        self.handles['pvs'  ] = AutoHandle('offlineSlimmedPrimaryVertices', 'std::vector<reco::Vertex>' )        

    def process(self, event):
        super(MuonAnalyzer, self).readCollections(event.input)

        self.counters.counter('MuonAnalyzer').inc('all events')

        event.muons = map(Muon, self.handles['muons'].product())
        
        if getattr(self.cfg_ana, 'filter', False):
            event.muons = [mu for mu in event.muons if self.cfg_ana.filter(mu)]

        if len(event.muons)==0:
            return False
            
        self.counters.counter('MuonAnalyzer').inc('>0 selected muons')
        
        event.pvs = self.handles['pvs'].product()
        for muon in event.muons:
            muon.isoot = self.isOotMuon(muon)
            muon.associatedVertex = event.pvs[0]
            muon.martinaMedium = self.martinaMedium(muon)
        
    def isOotMuon(self, muon):
        '''
        returns True if the muon fires the out-of-time selection proposed by Piotr
        https://indico.cern.ch/event/695762/contributions/2853865/attachments/1599433/2535174/ptraczyk_201802_oot_fakes.pdf
        
        For in-time muons you want this to return False.
        '''
        cmb = muon.time()
        rpc = muon.rpcTime()
        
        # I guess one needs to understand which type of time is needed
        # there is an enum to do that
        # http://cmslxr.fnal.gov/source/DataFormats/MuonReco/interface/MuonTime.h#0007
        
        if rpc.direction == -1:
            rpc.time    = rpc.timeAtIpOutIn()
            rpc.timeerr = rpc.timeAtIpOutInErr()
        elif rpc.direction == 1:
            rpc.time = rpc.timeAtIpInOut()
            rpc.timeerr = rpc.timeAtIpInOutErr()
        else:
            # print 'WARNING: undefined muon direction, cannot understand RPC time'
            return False

        if cmb.direction == -1:
            cmb.time    = cmb.timeAtIpOutIn()
            cmb.timeerr = cmb.timeAtIpOutInErr()
        elif cmb.direction == 1:
            cmb.time = cmb.timeAtIpInOut()
            cmb.timeerr = cmb.timeAtIpInOutErr()
        else:
            # print 'WARNING: undefined muon direction, cannot understand CMB time'
            return False
        
        cmbok = (cmb.nDof>7)
        rpcok = (rpc.nDof>1 and rpc.timeerr==0)
        
        if rpcok:
            if abs(rpc.time)>10 and not (cmbok and abs(cmb.time)<10):
                return True
        else:
            if cmbok and (cmb.time>20 or cmb.time<-45):
                return True
        
        return False

    def martinaMedium(self, mu):
        isGoodGlobal = mu.isGlobalMuon()                           and \
                       mu.combinedQuality().chi2LocalPosition < 12 and \
                       mu.combinedQuality().trkKink < 20
        
        isMartinaMedium = mu.isLooseMuon() and \
                          mu.segmentCompatibility() > (0.303 if isGoodGlobal else 0.451)
        
        return isMartinaMedium

