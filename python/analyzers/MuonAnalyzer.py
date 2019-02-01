from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from PhysicsTools.Heppy.physicsobjects.Muon import Muon


class MuonAnalyzer(Analyzer):
    '''Just a simple jet analyzer, to be used in tutorials.'''

    def declareHandles(self):
        super(MuonAnalyzer, self).declareHandles()
        self.handles['muons'] = AutoHandle('slimmedMuons'                 , 'std::vector<pat::Muon>'    )        
        self.handles['pvs'  ] = AutoHandle('offlineSlimmedPrimaryVertices', 'std::vector<reco::Vertex>' )        

    def process(self, event):
        super(MuonAnalyzer, self).readCollections(event.input)
        event.muons = map(Muon, self.handles['muons'].product())
        event.pvs = self.handles['pvs'].product()
        for muon in event.muons:
            muon.isoot = self.isOotMuon(muon)
            muon.associatedVertex = event.pvs[0]
        
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
