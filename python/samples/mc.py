import PhysicsTools.HeppyCore.framework.config as cfg
import os

#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator

creator = ComponentCreator()

BToJPsiKMu_JpsiMuMu = creator.makeMCComponent('BToJPsiKMu_JpsiMuMu', '/BToJPsiKMu_JpsiMuMu_TuneCP5_13TeV-pythia8-evtgen/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM', 'CMS', '.*root', 1, useAAA=True)

BToJPsiKMu_JpsiMuMu.triggers  = ['HLT_Mu7p5_Track2_Jpsi_v9'  ]
BToJPsiKMu_JpsiMuMu.triggers += ['HLT_Mu7p5_Track3p5_Jpsi_v9']
BToJPsiKMu_JpsiMuMu.triggers += ['HLT_Mu7p5_Track7_Jpsi_v9'  ]

# BToJPsiKMu_JpsiMuMu.triggers  = ['HLT_Mu7p5_Track2_Jpsi_v%d'   %i for i in range(15)]
# BToJPsiKMu_JpsiMuMu.triggers += ['HLT_Mu7p5_Track3p5_Jpsi_v%d' %i for i in range(15)]
# BToJPsiKMu_JpsiMuMu.triggers += ['HLT_Mu7p5_Track7_Jpsi_v%d'   %i for i in range(15)]

BToJPsiK = creator.makeMCComponent('BToJPsiK', '/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM', 'CMS', '.*root', 1, useAAA=True)

BToJPsiK.triggers  = ['HLT_Mu7p5_Track2_Jpsi_v9'  ]
BToJPsiK.triggers += ['HLT_Mu7p5_Track3p5_Jpsi_v9']
BToJPsiK.triggers += ['HLT_Mu7p5_Track7_Jpsi_v9'  ]

# BToJPsiK.triggers  = ['HLT_Mu7p5_Track2_Jpsi_v%d'   %i for i in range(15)]
# BToJPsiK.triggers += ['HLT_Mu7p5_Track3p5_Jpsi_v%d' %i for i in range(15)]
# BToJPsiK.triggers += ['HLT_Mu7p5_Track7_Jpsi_v%d'   %i for i in range(15)]


# doc on triggers
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/LowptMuonStudies2017
