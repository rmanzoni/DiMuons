import PhysicsTools.HeppyCore.framework.config as cfg
import os

#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator

creator = ComponentCreator()

BToJPsiKMu_JpsiMuMu = creator.makeMCComponent('BToJPsiKMu_JpsiMuMu', '/BToJPsiKMu_JpsiMuMu_TuneCP5_13TeV-pythia8-evtgen/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM', 'CMS', '.*root', 1, useAAA=True)
