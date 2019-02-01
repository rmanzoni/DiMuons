import os
import PhysicsTools.HeppyCore.framework.config as cfg

# set to True if you want several parallel processes
multi_thread = False

# input component 
# several input components can be declared,
# and added to the list of selected components
# inputSample = cfg.MCComponent(
#     'jpsi',
#     files = [
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/JPsiToMuMu_Pt20to100-pythia8-gun/MINIAODSIM/PUMoriond17RAW_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/F6B0A31E-EDB6-E611-86BB-001E67A3F3DF.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/JPsiToMuMu_Pt20to100-pythia8-gun/MINIAODSIM/PUMoriond17RAW_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/DE10027A-59B7-E611-AB7C-001E675A6725.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/JPsiToMuMu_Pt20to100-pythia8-gun/MINIAODSIM/PUMoriond17RAW_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/3A062CF5-58B7-E611-8A1D-0CC47A78A42E.root',    
#         ]    
#     )

#  /BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM 
# inputSample = cfg.MCComponent(
#     'bplusjpsik',
#     files = [
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/80000/FAC871E9-BCF5-E611-8799-001E674FBA1D.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/80000/F8D5D0B4-5DED-E611-88A4-FA163EE81F7F.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/80000/EE961FC8-2EF4-E611-A75E-0CC47A78A2EC.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/80000/ECF1A9BD-8FEC-E611-AC97-FA163EA69255.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/80000/E87666D2-0DEF-E611-921F-001E67C9AF38.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/80000/E2BD18C4-A4F0-E611-ACCE-0CC47A4D76C6.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/80000/D81A6679-BDF5-E611-8228-A0000420FE80.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/80000/C48C8602-55F2-E611-9A78-549F35AC7E08.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/80000/8EBBEFF6-39EE-E611-B0CC-001E67504475.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/80000/8A57FB0C-ABF0-E611-945E-0025905A60B0.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/80000/6EA26062-BAF2-E611-9639-001E67E6F8E6.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/80000/6A67D5FE-93EC-E611-A81C-02163E00B70E.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/80000/5C1EB046-68ED-E611-83FB-02163E00C935.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/80000/4C6C3A93-A5F0-E611-82DB-02163E00B031.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/80000/4407BD02-86F4-E611-BEC9-02163E019D48.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/80000/243B42C4-C2F3-E611-AA3A-02163E013884.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/F8F2C3C3-88EE-E611-90EF-0CC47A4D769E.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/F6E4F4A1-42EF-E611-A703-02163E00AF67.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/EA5A5F74-88EE-E611-A779-0CC47A4D769E.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/E0F27716-58EF-E611-B1B3-0CC47A4C8E38.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/B0EF0FBF-C0F1-E611-B875-02163E0143F0.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/80EAC0D7-73F0-E611-8D0F-008CFA152104.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/7ECBCC73-AAEC-E611-A5A8-0025904B2C80.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/2AAF0B4E-A6ED-E611-84B8-02163E0131E1.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/2A50F146-58EE-E611-8E0B-FA163E2FDFB1.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/2412677A-4BF0-E611-B76F-0090FAA59114.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/0C50A7C6-9CEC-E611-846D-FA163E9702DD.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/110000/E2144A5B-E2F2-E611-8B6B-0025905A6066.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/110000/DA81F735-4BF2-E611-A434-008CFA0A5A10.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/110000/C64E9B11-36F2-E611-AA65-FA163E3DED0F.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/110000/C64C5197-29F2-E611-9DE2-0025905A48F2.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/110000/A869E27D-9FEC-E611-B141-FA163E47477B.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/110000/A66CA71E-90EF-E611-B9A6-FA163E63FEF4.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/110000/8C6C7C09-65F2-E611-B30E-0CC47AA99436.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/110000/84FB158E-29F2-E611-9E36-0CC47A4C8E22.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/110000/6C4B6B8B-BCED-E611-BCE6-FA163EF70EAD.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/110000/6AD0FD38-8AEE-E611-A7E8-FA163E672D97.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/110000/5AC45501-74F1-E611-846C-A0369F7FD528.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/110000/54A80311-B0EC-E611-9676-001E67E95C7E.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/110000/202FD9C1-E4F2-E611-A09F-02163E01287B.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/100000/DC44D1C8-63EE-E611-BED2-FA163E4D51D9.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/100000/D066DAA7-CCF0-E611-B1F6-0CC47A4D75F6.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/100000/AA9A2C9A-50ED-E611-867A-FA163E5C1826.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/100000/9CA4BD51-C1F1-E611-B4CB-0025905A60D2.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/100000/80DDF598-72EF-E611-B50C-02163E00AE3E.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/100000/80DBA627-55ED-E611-88CB-02163E00BB44.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/100000/808FE02D-C1F1-E611-8BF4-02163E01437C.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/100000/762EDB83-8DEF-E611-B0F5-FA163EDBBA73.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/100000/6A65693A-C1F1-E611-BED7-5065F381F291.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/100000/32E5ADE4-D9F2-E611-96CA-0090FAA57AE0.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/BToJPsiKMu_JpsiMuMu_TuneCUEP8M1_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/100000/14365F24-C1F1-E611-924B-002590A81EF0.root',
#         ]    
#     )
 
# /InclusiveBtoJpsitoMuMu_SoftQCDnonD_TuneCUEP8M1_woFilter_13TeV-pythia8-evtgen/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM 
# inputSample = cfg.MCComponent(
#     'bjpsi',
#     files = [
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/InclusiveBtoJpsitoMuMu_SoftQCDnonD_TuneCUEP8M1_woFilter_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/F63810AA-BFD0-E811-8465-0242AC130002.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/InclusiveBtoJpsitoMuMu_SoftQCDnonD_TuneCUEP8M1_woFilter_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/F6189BBF-C1D0-E811-A3A4-0242AC130002.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/InclusiveBtoJpsitoMuMu_SoftQCDnonD_TuneCUEP8M1_woFilter_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/B02E15A0-BFD0-E811-A73B-0242AC130002.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/InclusiveBtoJpsitoMuMu_SoftQCDnonD_TuneCUEP8M1_woFilter_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/AA96A46B-34D1-E811-97E9-E0071B7A6850.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/InclusiveBtoJpsitoMuMu_SoftQCDnonD_TuneCUEP8M1_woFilter_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/9E0914E7-BFD0-E811-B491-0242AC130002.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/InclusiveBtoJpsitoMuMu_SoftQCDnonD_TuneCUEP8M1_woFilter_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/789B9189-CFD0-E811-A011-0242AC130002.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/InclusiveBtoJpsitoMuMu_SoftQCDnonD_TuneCUEP8M1_woFilter_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/7260268E-C7D0-E811-929C-0242AC130002.root',
#         'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/InclusiveBtoJpsitoMuMu_SoftQCDnonD_TuneCUEP8M1_woFilter_13TeV-pythia8-evtgen/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/4E7476BD-D0D0-E811-8B7B-0242AC130002.root',
#         ]    
#     )


#  /BToJPsiKMu_JpsiMuMu_TuneCP5_13TeV-pythia8-evtgen/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM 
inputSample = cfg.MCComponent(
    'bplusjpsik2017',
    files = [
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/22CD6AC7-7BAA-E811-84CF-0CC47A5FBE21.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/30C9DBF1-7BAA-E811-968C-A4BF0102614D.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/38D8BBBB-88A5-E811-BACE-E0071B740D90.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/3E84852F-53AA-E811-B13E-1866DA879B33.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/48052C60-F7A8-E811-BA2F-002590D60038.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/50EF390D-8BA9-E811-AF65-F04DA27541CF.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/58C58BC5-F3A8-E811-942C-00269E95B014.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/6E49E2BE-7BAA-E811-8960-008CFA0A5614.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/70F7ABE3-69AA-E811-882F-B499BAAC0694.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/782CA3C0-7BAA-E811-817B-0CC47A1DF81C.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/7E3F45FC-5AA7-E811-B757-0CC47A57CBBC.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/8E26A0D9-DDA9-E811-9A58-A0369FD0B282.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/8EF4617B-58A3-E811-8BB5-0CC47A6C06C4.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/6286CC5D-FCA6-E811-8F7B-0090FAA575E0.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/881042ED-6BAA-E811-AB3B-002590D9D896.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/98E8D107-6BAA-E811-9B84-246E96D1AC20.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/1E973050-6CAA-E811-93C5-842B2B5C2299.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/1011822F-6BAA-E811-BBED-00266CFFBFC0.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/1C979261-6EAA-E811-B7B1-0CC47AFC3CA2.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/1C1A1CE9-6BAA-E811-96E8-0025901D0C50.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/14BBAB23-09A5-E811-8795-A4BF011595FC.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/125CE711-09A5-E811-9D5D-008CFA1113B4.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/0AA14593-50A5-E811-9BAD-001EC9ADCBEF.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/0EB44485-6BAA-E811-85DE-0026B94DBE0A.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/8C30EFE1-6EAA-E811-B975-002590DE6C48.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/FE5753D7-36A9-E811-AD61-0CC47A4D76D0.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/FAD60A91-F4A9-E811-B8C4-0CC47A7C3430.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/F45D67A6-FCA9-E811-B7DB-0025905BA736.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/F04D6257-2EA9-E811-8195-0025905A60E0.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/F02AD90C-2EAA-E811-91E2-D4AE529013D2.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/F0187753-F5AB-E811-AA98-001E675827DC.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/EE92139D-FDA9-E811-8D04-008CFA197AF4.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/EE1A578F-3BA9-E811-8B3B-48FD8E282975.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/E4D33B07-80A9-E811-B5DF-FA163E8C4B41.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/E27A5CF7-DDA9-E811-9B7C-901B0E6459DE.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/E263E0FA-F2AB-E811-A381-0CC47A7C3408.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/E25948DF-1CA9-E811-8719-509A4C748042.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/E0F19C4C-5BA9-E811-85FA-0CC47A78A42E.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/E0EE0FD5-21A9-E811-855F-0CC47AD98D6C.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/E0D372B4-AEA9-E811-9A87-0CC47AA47914.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/E007A454-AEA9-E811-A2E1-008CFA11138C.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/DA10C116-4FA9-E811-9B53-0CC47A78A426.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/D0EED07B-60A9-E811-A3DB-008CFAFFEA48.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/D0139B00-97A9-E811-B670-0025905B85B8.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/CAAD87BB-06A9-E811-BF1F-A0369FD0B130.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/CA96D0D0-3CA9-E811-9346-7CD30ACDC8DE.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/C8EA66D1-35A9-E811-80D9-002590D60038.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/C83B3C0A-B3A9-E811-9793-0CC47A4D7658.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/C6E21085-F3AB-E811-8CF7-B499BAAC064E.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/C472C6AC-7AAA-E811-96E7-3417EBE65E39.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/BE3080A7-F5A9-E811-AF62-008CFA11118C.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/B872882F-5CA9-E811-9B1F-0242AC130002.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/B6CCC306-19AA-E811-A80C-801844E55BCC.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/B222DFE2-52A9-E811-89BC-0CC47A7C3572.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/B02F2436-7DA9-E811-9D2B-0CC47A4C8ED8.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/AEF6AFCC-68A9-E811-B886-0CC47A745294.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/AEBC459B-52A9-E811-A07C-003048FFCBB2.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/AE91A4F9-D7AA-E811-9964-FA163E9AA340.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/AE7DED06-F4AB-E811-8F21-F04DA27541CF.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/AAB60F92-F3AB-E811-9DCC-0CC47AC08C34.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/AA99974E-24A9-E811-8FB6-A4BF011255B8.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/AA2E0D81-F3AB-E811-8177-0CC47A1E0466.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/A8CF9D65-F3AB-E811-A66D-003048F2B302.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/A882A5AC-FEA8-E811-87D5-5065F3816201.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/A8749144-33A9-E811-8BF0-0CC47A4DEF16.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/A4EABB35-28A9-E811-B98D-0CC47A4D9A3C.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/A4E87D11-5FA9-E811-837C-008CFA197CE4.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/A4D4713E-7AA9-E811-8D87-509A4C84EA6D.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/A2CF81F5-7DA9-E811-A21C-D067E5F914D3.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/9E212D20-4AAA-E811-891F-D48564592B02.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/9C930750-35A9-E811-A863-0025905B85BA.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/9C70CAD6-EBA8-E811-8FD7-0CC47A4DEE6A.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/9C708F7F-50A9-E811-A4F4-A4BF01125678.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/9C402CE2-26A9-E811-90A7-002590E2F9D4.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/9AB6C24C-39A9-E811-B891-0025905A60B6.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/9A19DEFF-43A9-E811-99FC-003048FFD71C.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/98FCF763-12A9-E811-BDD1-246E96D14B5C.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/9676965D-1BA9-E811-A0C2-0025905A6082.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/94F4E222-C9A9-E811-86CB-0CC47AD98C8C.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/923CF4D8-7AA9-E811-B2DF-0025905A48F0.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/90370839-0EA9-E811-8BE6-A4BF0112BE1E.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/9033261E-78A9-E811-853A-008CFA0646CC.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/8CC40DBB-39A9-E811-AAC9-001E677925AC.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/8C9503DF-B7A9-E811-8800-008CFA197448.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/8C93924E-02A9-E811-8C03-0CC47A2B06DC.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/8C1D83C9-D4A9-E811-AF81-008CFA5D275C.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/8AFD116D-88A9-E811-97A6-008CFA197B68.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/8A61DBF5-F2AB-E811-895B-0CC47AFB7D08.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/8A4A65F6-F2AB-E811-9162-0090FAA57490.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/88E39AF4-75A9-E811-A898-00269E95B17C.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/884EAE78-F3AB-E811-BBA2-001E673CC5C2.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/86D9C9F7-DBA9-E811-AB90-0CC47A4D762A.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/84821C3C-1CA9-E811-9AB4-0CC47A13D16E.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/84540B5B-F3AB-E811-9605-001E67A3F49D.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/844A447C-F3AB-E811-9D8B-A0369FD20730.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/80F6093E-76A9-E811-81F9-0CC47A7C340C.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/7ABC4481-C8AA-E811-A128-008CFA111290.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/7A0F54B4-70A9-E811-A348-0CC47A4C8E2E.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/78233369-66A9-E811-B92B-0CC47A7C351E.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/76CAE784-8CA9-E811-A1DC-0025905B8580.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/743AA936-A0AA-E811-9E1A-0242AC130002.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/72D1593B-C3AB-E811-B0B6-246E96D14AB0.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/726B3CEB-61A9-E811-8E5B-0025905A6110.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/6EF85C36-40A9-E811-BA02-90B11CBCFF8F.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/6C5A281B-94A9-E811-858C-0CC47A4C8E1C.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/6A0DF9A5-32A9-E811-8260-0CC47A6C115A.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/6899DE43-66A9-E811-97BC-0CC47A78A4BA.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/686A2074-82A9-E811-8230-0025905B8586.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/64C73676-9DA9-E811-AB8A-0CC47A4D76B2.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/64A99AE2-F4A9-E811-8DD4-7CD30ABD295A.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/64273FE4-D5A9-E811-88ED-00259048AC9A.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/9E8D890A-1FAA-E811-8E62-7CD30AD09DE4.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/62B8282F-30AA-E811-98F8-AC1F6B0DE342.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/60880386-36A9-E811-B979-002590E39D8A.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/5E11FEF4-F2AB-E811-B298-A4BF01125628.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/5C4C3F39-F3AB-E811-826F-5065F3812201.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/5A8123A1-49A9-E811-97D3-E0071B7A58F0.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/58B14B77-DFAA-E811-816A-0025905B85FE.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/5811A7D8-19A9-E811-8BF9-0CC47A4DECEE.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/54089DFD-56A9-E811-B3D3-A0369FE2C1B6.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/52DC038A-F6A8-E811-AE3E-A4BF01125E06.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/5085EBAF-5FA9-E811-BA79-001E67504685.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/50527671-F3AB-E811-88C8-0025908217DA.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/50318BBF-3BA9-E811-A877-001EC9ADFC1B.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/4E861F73-F3AB-E811-9F6F-801844DEED78.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/4C343235-66A9-E811-A1C4-246E96D149DC.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/4AA713E9-ECA8-E811-93CD-00000086FE80.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/3E9FDC08-4FA9-E811-BC4E-0CC47A7C3638.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/3CBA3DB9-06A9-E811-9945-90B11CBCFF5B.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/3C497708-76A9-E811-BE82-0025901D08D2.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/3AF78C80-5AA9-E811-AE9C-0025900B20E2.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/3A2018EC-49A9-E811-876D-0CC47A2B06DE.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/34216B79-F3AB-E811-A051-7CD30AB04FE6.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/341B8C3C-D7A8-E811-B70B-E0071B73C640.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/30B02555-4DA9-E811-A277-0CC47A74527A.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/308DCC2F-6CA9-E811-8A2B-0CC47A7C340C.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/2CB3FB4E-ABA9-E811-8B26-0025905A60F4.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/2C589312-BEAA-E811-B6CC-20CF3027A565.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/2C41CE59-90A9-E811-A7C8-0CC47A4C8E0E.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/2A4F2C64-C1A9-E811-9B77-008CFA197D74.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/2A2A4501-86A9-E811-937B-0CC47A78A426.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/28970DC4-B7A9-E811-9208-20CF3027A5AC.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/2893E813-8CA9-E811-BAB4-0CC47A57D086.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/268B889F-8BAB-E811-90E5-001E67581494.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/242F44BE-CAA9-E811-AEAB-0CC47A4C8E26.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/241F026F-E0A8-E811-AC90-5065F3819221.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/241A8F30-1EA9-E811-8065-0CC47AFB7DCC.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/22EEAD32-62A9-E811-9BAA-0CC47A78A496.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/1E589582-47A9-E811-ADD5-0CC47A4C8EEA.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/1C4F89F8-F7A8-E811-B392-A0369FE2C22E.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/1C491FFC-F2AB-E811-BC09-FA163E8A0AD4.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/18427E3A-22A9-E811-BABD-001E67444E48.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/18413512-71A9-E811-85C9-20CF3027A5A7.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/162EE3A8-41A9-E811-B0D4-003048FF13E6.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/14B3F970-4EA9-E811-A0F5-0CC47A7C34A6.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/12DC1A7E-3AA9-E811-8F5C-0025905A60B6.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/1231DBA0-48A9-E811-8D89-FA163ECF8401.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/123024E3-F2AB-E811-9D7B-7CD30AD099EE.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/10614DF0-99A9-E811-A6F9-008CFA165F34.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/0EB05846-0EAA-E811-BBD4-509A4C74D18D.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/0EAFD1E0-88A9-E811-AD21-0CC47A4D7664.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/0E9ABEAF-82A9-E811-885C-0CC47AFC3C72.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/0E00932E-01A9-E811-AAD2-0242AC130002.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/0CEB0EF2-3CA9-E811-88C5-0CC47A4D760A.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/0AAFBD47-30A9-E811-91B6-0CC47AFC3C86.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/086F683C-5FA9-E811-9C3B-002590D9D9E4.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/06C82CF9-4AA9-E811-A2A9-008CFA197B68.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/069894CB-5EA9-E811-94FE-0025905B85EE.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/066E9634-D3A8-E811-B3A3-E0071B73C650.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/0291E57A-F3AB-E811-9821-0CC47A5FBE25.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/0097DFFD-50AA-E811-8B23-A4BF0112BE0E.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/FEDAED7E-6BAA-E811-AA72-44A842B2D658.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/FCE14AE5-CBA4-E811-9893-002590FC5ACE.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/FA2059D2-6AAA-E811-86A2-0025905B858C.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/F4CC6FDA-CFA3-E811-B720-0CC47AF9B2E6.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/F43F2D0F-2DA5-E811-9DC9-44A842BECCD8.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/F40B0CBD-6AAA-E811-85AB-FA163EF5DEC9.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/F096851F-36A4-E811-86CC-0CC47ADAF3DA.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/EE14E1CB-14A6-E811-A9B9-060910000283.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/EC34081D-6BAA-E811-948B-0025904C68DA.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/D41C0096-6BAA-E811-9298-00259090829A.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/CC1AEC91-B6A9-E811-AB72-0242AC130002.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/CAC2D5D0-69AA-E811-BE12-509A4C748148.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/C28B1CF8-7BAA-E811-B2AC-0242AC130002.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/ACB3D9DA-6AAA-E811-B8E8-008CFA0B19E0.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/100000/AAD6E1E7-99A4-E811-9407-E0071B740D80.root',
        ]    
    )


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
from CMGTools.DiMuons.analyzers.ZJetsTreeAnalyzer import ZJetsTreeAnalyzer
tree = cfg.Analyzer(
    ZJetsTreeAnalyzer
    )


# definition of a sequence of analyzers,
# the analyzers will process each event in this order
sequence = cfg.Sequence( [ 
        muons,
        dimuons,
#         all_jets,
        sel_dimuons,
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



