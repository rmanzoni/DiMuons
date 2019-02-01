import os
import PhysicsTools.HeppyCore.framework.config as cfg
from CMGTools.DiMuons.samples.data import Charmonium_2017

inputSample = Charmonium_2017[0]

# set to True if you want several parallel processes
multi_thread = True

# just run on a few files, comment if you want the full thing
inputSample.files = inputSample.files[:5]

if multi_thread: 
    inputSample.splitFactor = len(inputSample.files)

selectedComponents  = [inputSample]

# a very simple muon analyzer
# read miniaod muons and wrap them in python muons
from CMGTools.DiMuons.analyzers.MuonAnalyzer import MuonAnalyzer
muons = cfg.Analyzer(
    MuonAnalyzer,
    'muons',
    )

from CMGTools.DiMuons.analyzers.ResonanceBuilder import ResonanceBuilder
dimuons = cfg.Analyzer(
    ResonanceBuilder,
    'dimuons',                            
    leg1_collection = 'muons',            # input collection
    leg2_collection = 'muons',            # input collection
    filter_func_leg1 = lambda x : x.isGlobalMuon() and x.pt()>3. and abs(x.eta())<2.5,   # filtering function for input objects
    filter_func_leg2 = lambda x : x.isGlobalMuon() and x.pt()>3. and abs(x.eta())<2.5,   # filtering function for input objects
    filter_func_res  = lambda x : abs(x.mass()-3.)<1 and x.charge()==0,   # filtering function for output objects
    pdgid = 443
    )

from CMGTools.DiMuons.analyzers.BMesonBuilder import BMesonBuilder
thebees = cfg.Analyzer(
    BMesonBuilder,
    'dimuons',                            
    jpsi_window = True,
    b_window = True,
    )

# a very simple jet analyzer
# read miniaod jets and wrap them in python jets
from CMGTools.DiMuons.analyzers.SimpleJetAnalyzer import SimpleJetAnalyzer
all_jets = cfg.Analyzer(
    SimpleJetAnalyzer,
    'all_jets',
    njets = 4, 
    filter_func = lambda x : True
    )

# filtering could be done in the SimpleJetAnalyzer above. 
# here, we illustrate the use of the generic Filter module
from PhysicsTools.HeppyCore.analyzers.Filter import Filter
sel_dimuons = cfg.Analyzer(
    Filter,
    'dimuons',
    input_objects = 'dimuons',
#     filter_func = lambda x : abs(x.mass()-3.1)<0.5, 
    filter_func = lambda x : True, 
    )


# a simple tree with a Z candidate and the two leading jets (if any)
from CMGTools.DiMuons.analyzers.BJPsiMMKTreeProducer import BJPsiMMKTreeProducer
tree = cfg.Analyzer(
    BJPsiMMKTreeProducer
    )


# definition of a sequence of analyzers,
# the analyzers will process each event in this order
sequence = cfg.Sequence( [ 
        muons,
        dimuons,
#         all_jets,
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

if __name__ == '__main__':
    # can either run this configuration through heppy, 
    # or directly in python or ipython for easier development. 
    # try: 
    # 
    #   ipython -i simple_example_cfg.py
    # 
    from PhysicsTools.Heppy.physicsutils.LorentzVectors import LorentzVector

    from PhysicsTools.HeppyCore.framework.looper import Looper 
    looper = Looper( 'Loop', config, nPrint = 5, nEvents=100) 
    looper.loop()
    looper.write()

    # and now, let's play with the contents of the event
    print looper.event
    pz = LorentzVector()
    for imu, mu in enumerate(looper.event.muons): 
        print 'muon1', mu, 'abs iso=', mu.relIso()*mu.pt()
        pz += mu.p4()
    print 'z candidate mass = ', pz.M()

    # you can stay in ipython on a given event 
    # and paste more and more code as you need it until 
    # your code is correct. 
    # then put your code in an analyzer, and loop again. 

    def next():
        looper.process(looper.event.iEv+1)



