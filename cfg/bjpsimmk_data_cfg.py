import os
from collections import OrderedDict
import PhysicsTools.HeppyCore.framework.config as cfg
from CMGTools.DiMuons.samples.data import Charmonium_2017
from CMGTools.DiMuons.analyzers.TriggerAnalyzer import TriggerAnalyzer

# import Heppy analyzers:
from PhysicsTools.Heppy.analyzers.core.JSONAnalyzer      import JSONAnalyzer
from PhysicsTools.Heppy.analyzers.core.SkimAnalyzerCount import SkimAnalyzerCount
from PhysicsTools.Heppy.analyzers.core.EventSelector     import EventSelector
from PhysicsTools.Heppy.analyzers.objects.VertexAnalyzer import VertexAnalyzer
from PhysicsTools.Heppy.analyzers.core.PileUpAnalyzer    import PileUpAnalyzer



inputSample = Charmonium_2017[0]

# set to True if you want several parallel processes
multi_thread = False
production = True

if production:
    multi_thread = False

# just run on a few files, comment if you want the full thing
# inputSample.files = inputSample.files[3:4]
# inputSample.files = inputSample.files[2:12]
# inputSample.files = 'charmonium_test.root'
# selectedComponents  = [inputSample]

selectedComponents = Charmonium_2017

for sample in selectedComponents:
    if multi_thread: 
        sample.splitFactor = len(sample.files)
    else:
        sample.splitFactor = 1
    
    if production:
        sample.splitFactor = len(sample.files)


eventSelector = cfg.Analyzer(
    EventSelector,
    name='EventSelector',
    toSelect=[140900505]
)

jsonAna = cfg.Analyzer(
    JSONAnalyzer,
    name='JSONAnalyzer',
)

triggerAna = cfg.Analyzer(
    TriggerAnalyzer,
    name='TriggerAnalyzer',
    addTriggerObjects=True,
    requireTrigger=True,
    usePrescaled=True,
    unpackLabels=True,
)

vertexAna = cfg.Analyzer(
    VertexAnalyzer,
    name='VertexAnalyzer',
    fixedWeight=1,
    keepFailingEvents=False,
    verbose=False
)

pileUpAna = cfg.Analyzer(
    PileUpAnalyzer,
    name='PileUpAnalyzer',
    true=True
)


# a very simple muon analyzer
# read miniaod muons and wrap them in python muons
from CMGTools.DiMuons.analyzers.MuonAnalyzer import MuonAnalyzer
muons = cfg.Analyzer(
    MuonAnalyzer,
    'muons',
    filter = lambda x : x.isGlobalMuon() and x.pt()>3. and abs(x.eta())<2.5
    )

from CMGTools.DiMuons.analyzers.TrackAnalyzer import TrackAnalyzer
tracks = cfg.Analyzer(
    TrackAnalyzer,
    'tracks',
    filter = lambda x : x.pt()>2. and abs(x.eta())<2.5,
    )

paths_and_filters_mu = OrderedDict()
paths_and_filters_mu['HLT_Mu7p5_Track7_Jpsi'  ] = ('hltMu7p5Track7JpsiTrackMassFiltered'  , 83) # muon
paths_and_filters_mu['HLT_Mu7p5_Track3p5_Jpsi'] = ('hltMu7p5Track3p5JpsiTrackMassFiltered', 83) # muon
paths_and_filters_mu['HLT_Mu7p5_Track2_Jpsi'  ] = ('hltMu7p5Track2JpsiTrackMassFiltered'  , 83) # muon
from CMGTools.DiMuons.analyzers.LegTriggerMatcher import LegTriggerMatcher
muonsHLTmatcher = cfg.Analyzer(
    LegTriggerMatcher,
    collection='muons',
    paths_and_filters=paths_and_filters_mu,
    filter=True,
    )

paths_and_filters_tk = OrderedDict()
paths_and_filters_tk['HLT_Mu7p5_Track7_Jpsi'  ] = ('hltMu7p5Track7JpsiTrackMassFiltered'  , 91) # track
paths_and_filters_tk['HLT_Mu7p5_Track3p5_Jpsi'] = ('hltMu7p5Track3p5JpsiTrackMassFiltered', 91) # track
paths_and_filters_tk['HLT_Mu7p5_Track2_Jpsi'  ] = ('hltMu7p5Track2JpsiTrackMassFiltered'  , 91) # track
from CMGTools.DiMuons.analyzers.LegTriggerMatcher import LegTriggerMatcher
tracksHLTmatcher = cfg.Analyzer(
    LegTriggerMatcher,
    collection='tracks',
    paths_and_filters=paths_and_filters_tk,
    filter=True,
    )

from CMGTools.DiMuons.analyzers.ResonanceBuilder import ResonanceBuilder
dimuons = cfg.Analyzer(
    ResonanceBuilder,
    'dimuons',                            
    leg1_collection = 'muons_matched' , # input collection
    leg2_collection = 'tracks_matched', # input collection
    filter_func_leg1 = lambda x : x.isGlobalMuon() and x.pt()>3. and abs(x.eta())<2.5,   # filtering function for input objects
    filter_func_leg2 = lambda x : x.pt()>2. and abs(x.eta())<2.5,   # filtering function for input objects
    filter_func_res  = lambda x : abs(x.mass()-3.0969)<0.3 and x.charge()==0,   # filtering function for output objects
    pdgid = 443
    )
# filtering could be done in the SimpleJetAnalyzer above. 
# here, we illustrate the use of the generic Filter module
from PhysicsTools.HeppyCore.analyzers.Filter import Filter
sel_dimuons = cfg.Analyzer(
    Filter,
    'dimuons',
    input_objects = 'dimuons',
    filter_func = lambda x : abs(x.mass()-3.0969)<0.3, 
#     filter_func = lambda x : True, 
    )

from CMGTools.DiMuons.analyzers.BMesonBuilder import BMesonBuilder
thebees = cfg.Analyzer(
    BMesonBuilder,
    'dimuons',                            
    jpsi_window = True,
    b_window = True,
    min_pt = 1.5,
    )

# a simple tree with a Z candidate and the two leading jets (if any)
from CMGTools.DiMuons.analyzers.BJPsiMMKTreeProducer import BJPsiMMKTreeProducer
tree = cfg.Analyzer(
    BJPsiMMKTreeProducer
    )

# definition of a sequence of analyzers,
# the analyzers will process each event in this order
sequence = cfg.Sequence( [ 
#         eventSelector,
        jsonAna,
        triggerAna,
        vertexAna,
        pileUpAna,
        muons,
        tracks,
        muonsHLTmatcher,
        tracksHLTmatcher,
        dimuons,
        sel_dimuons,
        thebees,
        tree
        ] )

# finalization of the configuration object. 
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
config = cfg.Config( components = selectedComponents,
                     sequence = sequence, 
                     services = [],
                     events_class = Events)

print config

'''
heppy_batch.py -o production_charmonium bjpsimmk_data_cfg.py -B -b 'run_condor_simple.sh -t 1200 ./batchScript.sh'
'''

# if __name__ == '__main__':
#     # can either run this configuration through heppy, 
#     # or directly in python or ipython for easier development. 
#     # try: 
#     # 
#     #   ipython -i simple_example_cfg.py
#     # 
#     from PhysicsTools.Heppy.physicsutils.LorentzVectors import LorentzVector
# 
#     from PhysicsTools.HeppyCore.framework.looper import Looper 
#     looper = Looper( 'Loop', config, nPrint = 5, nEvents=100) 
#     looper.loop()
#     looper.write()
# 
#     # and now, let's play with the contents of the event
#     print looper.event
#     pz = LorentzVector()
#     for imu, mu in enumerate(looper.event.muons): 
#         print 'muon1', mu, 'abs iso=', mu.relIso()*mu.pt()
#         pz += mu.p4()
#     print 'z candidate mass = ', pz.M()
# 
#     # you can stay in ipython on a given event 
#     # and paste more and more code as you need it until 
#     # your code is correct. 
#     # then put your code in an analyzer, and loop again. 
# 
#     def next():
#         looper.process(looper.event.iEv+1)
# 


