import PhysicsTools.HeppyCore.framework.config as cfg
import os

#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator

json = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/Final/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt'

creator = ComponentCreator()

DoubleMuonLowMass_2017B = creator.makeDataComponent("DoubleMuonLowMass_2017B", "/DoubleMuonLowMass/Run2017B-31Mar2018-v1/MINIAOD", "CMS", ".*root", json, useAAA=True)
DoubleMuonLowMass_2017C = creator.makeDataComponent("DoubleMuonLowMass_2017C", "/DoubleMuonLowMass/Run2017C-31Mar2018-v1/MINIAOD", "CMS", ".*root", json, useAAA=True)
DoubleMuonLowMass_2017D = creator.makeDataComponent("DoubleMuonLowMass_2017D", "/DoubleMuonLowMass/Run2017D-31Mar2018-v1/MINIAOD", "CMS", ".*root", json, useAAA=True)
DoubleMuonLowMass_2017E = creator.makeDataComponent("DoubleMuonLowMass_2017E", "/DoubleMuonLowMass/Run2017E-31Mar2018-v1/MINIAOD", "CMS", ".*root", json, useAAA=True)
DoubleMuonLowMass_2017F = creator.makeDataComponent("DoubleMuonLowMass_2017F", "/DoubleMuonLowMass/Run2017F-31Mar2018-v1/MINIAOD", "CMS", ".*root", json, useAAA=True)

DoubleMuonLowMass_2017 = [
    DoubleMuonLowMass_2017B,
    DoubleMuonLowMass_2017C,
    DoubleMuonLowMass_2017D,
    DoubleMuonLowMass_2017E,
    DoubleMuonLowMass_2017F,
]

Charmonium_2017B = creator.makeDataComponent("Charmonium_2017B", "/Charmonium/Run2017B-31Mar2018-v1/MINIAOD", "CMS", ".*root", json, useAAA=True)
Charmonium_2017C = creator.makeDataComponent("Charmonium_2017C", "/Charmonium/Run2017C-31Mar2018-v1/MINIAOD", "CMS", ".*root", json, useAAA=True)
Charmonium_2017D = creator.makeDataComponent("Charmonium_2017D", "/Charmonium/Run2017D-31Mar2018-v1/MINIAOD", "CMS", ".*root", json, useAAA=True)
Charmonium_2017E = creator.makeDataComponent("Charmonium_2017E", "/Charmonium/Run2017E-31Mar2018-v1/MINIAOD", "CMS", ".*root", json, useAAA=True)
Charmonium_2017F = creator.makeDataComponent("Charmonium_2017F", "/Charmonium/Run2017F-31Mar2018-v1/MINIAOD", "CMS", ".*root", json, useAAA=True)

Charmonium_2017 = [
    Charmonium_2017B,
    Charmonium_2017C,
    Charmonium_2017D,
    Charmonium_2017E,
    Charmonium_2017F,
]

# HLT_Mu7p5_Track2 (3.5, 7)

for isample in DoubleMuonLowMass_2017 + Charmonium_2017:
    isample.json = json
    isample.triggers  = ['HLT_Mu7p5_Track2_Jpsi_v%d'   %i for i in range(15)]
    isample.triggers += ['HLT_Mu7p5_Track3p5_Jpsi_v%d' %i for i in range(15)]
    isample.triggers += ['HLT_Mu7p5_Track7_Jpsi_v%d'   %i for i in range(15)]

