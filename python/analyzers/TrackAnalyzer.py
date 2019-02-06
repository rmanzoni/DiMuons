from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from PhysicsTools.Heppy.physicsobjects.PhysicsObject import PhysicsObject


class TrackAnalyzer(Analyzer):

    def beginLoop(self, setup):
        super(TrackAnalyzer, self).beginLoop(setup)
        self.counters.addCounter('TrackAnalyzer')
        count = self.counters.counter('TrackAnalyzer')
        count.register('all events')
        count.register('>0 selected tracks')

    def declareHandles(self):
        super(TrackAnalyzer, self).declareHandles()
        self.handles['losttracks'] = AutoHandle('lostTracks'        , 'std::vector<pat::PackedCandidate>')
        self.handles['pfcands'   ] = AutoHandle('packedPFCandidates', 'std::vector<pat::PackedCandidate>')

    def process(self, event):
        super(TrackAnalyzer, self).readCollections(event.input)

        self.counters.counter('TrackAnalyzer').inc('all events')

        # get the tracks
        allpf      = map(PhysicsObject, self.handles['pfcands'   ].product())
        losttracks = map(PhysicsObject, self.handles['losttracks'].product())

        # merge the track collections
        # do not exclude muons (and electrons)
        event.tracks = sorted([tt for tt in allpf + losttracks if tt.charge() != 0], key = lambda x : x.pt(), reverse = True)

        if getattr(self.cfg_ana, 'filter', False):
            event.tracks = [tk for tk in event.tracks if self.cfg_ana.filter(tk)]

        if len(event.tracks)==0:
            return False
            
        self.counters.counter('TrackAnalyzer').inc('>0 selected tracks')

