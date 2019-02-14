import FWCore.ParameterSet.Config as cms

from array import array

process = cms.Process("TagProbe")

process.load('FWCore.MessageService.MessageLogger_cfi')
process.source = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

print "+" * 100;

process.TnP_Muon_ID = cms.EDAnalyzer("TagProbeFitTreeAnalyzer",
    ## Input, output 
    InputFileNames     = cms.vstring(
         '/afs/cern.ch/work/m/manzoni/HNL/cmg/CMSSW_9_4_6_patch1/src/CMGTools/DiMuons/cfg/mc.root',
#          '/afs/cern.ch/work/m/manzoni/HNL/cmg/CMSSW_9_4_6_patch1/src/CMGTools/DiMuons/cfg/data.root',
    ), ## can put more than one
    OutputFileName     = cms.string("TnP_test.root"),
    InputTreeName      = cms.string("tree"), 
    InputDirectoryName = cms.string(""),  
    ## Variables for binning
    Variables = cms.PSet(
        jpsi_m        = cms.vstring("jpsi_m"       , "2.9"  , "3.3"   , "GeV/c^{2}"),
        
        ## tag variables
        mu1_pt          = cms.vstring("mu1_pt"       , "0"    , "1000"  , "GeV/c"    ),
        mu1_eta         = cms.vstring("mu1_eta"      , "-3"   , "3"     , ""         ),
        mu1_id_s        = cms.vstring("mu1_id_s"     , "-3"   , "3"     , ""         ),
        mu1_id_t        = cms.vstring("mu1_id_t"     , "-3"   , "3"     , ""         ),

        ## probe variables
        tk2_pt          = cms.vstring("tk2_pt"        , "0"    , "1000"  , "GeV/c"    ),
        tk2_eta         = cms.vstring("tk2_eta"       , "-3"   , "3"     , ""         ),
        mu2_pt          = cms.vstring("mu2_pt"        , "0"    , "1000"  , "GeV/c"    ),
        mu2_eta         = cms.vstring("mu2_eta"       , "-3"   , "3"     , ""         ),
        mu2_id_s        = cms.vstring("mu2_id_s"      , "-3"   , "3"     , ""         ),
        mu2_id_m        = cms.vstring("mu2_id_m"      , "-3"   , "3"     , ""         ),
        mu2_id_mm       = cms.vstring("mu2_id_mm"     , "-3"   , "3"     , ""         ),
        mu2_id_t        = cms.vstring("mu2_id_t"      , "-3"   , "3"     , ""         ),
        mu2_id_tnv      = cms.vstring("mu2_id_tnv"    , "-3"   , "3"     , ""         ),

        ## kaon variables
        k_pt            = cms.vstring("k_pt"          , "0"    , "1000"  , "GeV/c"    ),
        k_eta           = cms.vstring("k_eta"         , "-3"   , "3"     , ""         ),

        ## candidate variables
        sv_2d_disp      = cms.vstring("sv_2d_disp"    , "0"    , "1000"  , "cm"       ),
        sv_2d_disp_sig  = cms.vstring("sv_2d_disp_sig", "0"    , "1000"  , ""         ),
        sv_2d_cos       = cms.vstring("sv_2d_cos"     , "-1"   , "1"     , ""         ),
        sv_prob         = cms.vstring("sv_prob"       , "0"    , "1"     , ""         ),
        b_m             = cms.vstring("b_m"           , "4.8"  , "5.6"   , "GeV/c^{2}"),

    ),
    ## Flags you want to use to define numerator and possibly denominator
    Categories = cms.PSet(
    ),
    Expressions = cms.PSet(
        isMuonVar        = cms.vstring("isMuonVar"       , "mu2_pt>0                   ", "mu2_pt"              ),
        SoftVar          = cms.vstring("SoftVar"         , "mu2_pt>0 & mu2_id_s   > 0.5", "mu2_pt", "mu2_id_s"  ),
        MediumVar        = cms.vstring("MediumVar"       , "mu2_pt>0 & mu2_id_m   > 0.5", "mu2_pt", "mu2_id_m"  ),
        MediumMartinaVar = cms.vstring("MediumMartinaVar", "mu2_pt>0 & mu2_id_mm  > 0.5", "mu2_pt", "mu2_id_mm" ),
        TightVar         = cms.vstring("TightVar"        , "mu2_pt>0 & mu2_id_t   > 0.5", "mu2_pt", "mu2_id_t"  ),
        TightNoVtxVar    = cms.vstring("TightNoVtxVar"   , "mu2_pt>0 & mu2_id_tnv > 0.5", "mu2_pt", "mu2_id_tnv"),
    ),
    Cuts = cms.PSet(  # can only be used for the numerator definition :(
        isMuonCut        = cms.vstring("isMuon"       , "isMuonVar"       , "0.5"),
        SoftCut          = cms.vstring("Soft"         , "SoftVar"         , "0.5"),
        MediumCut        = cms.vstring("Medium"       , "MediumVar"       , "0.5"),
        MediumMartinaCut = cms.vstring("MediumMartina", "MediumMartinaVar", "0.5"),
        TightCut         = cms.vstring("Tight"        , "TightVar"        , "0.5"),
        TightNoVtxCut    = cms.vstring("TightNoVtx"   , "TightNoVtxVar"   , "0.5"),
    ),

    ## What to fit
    Efficiencies = cms.PSet(
        eff_pt_eta = cms.PSet(
            UnbinnedVariables = cms.vstring("jpsi_m"),
#             EfficiencyCategoryAndState = cms.vstring("mu_id_t", "pass"), ## Numerator definition
#             EfficiencyCategoryAndState = cms.vstring("TightNoVtxCut", "above"), ## Numerator definition
#             EfficiencyCategoryAndState = cms.vstring("MediumMartinaCut", "above"), ## Numerator definition
#             EfficiencyCategoryAndState = cms.vstring("TightCut", "above"), ## Numerator definition
            EfficiencyCategoryAndState = cms.vstring("MediumCut", "above"), ## Numerator definition
            BinnedVariables = cms.PSet(
                ## binning 
                mu2_pt          = cms.vdouble( 3.0, 6.0, 10.0, 20.0, 50.0),
                sv_2d_disp      = cms.vdouble( 0. , 0.2, 0.5, 1.0, 5.),
#                 abseta          = cms.vdouble(  0, 0.9, 1.2, 2.1, 2.4  ) ,
                
                ## flags and conditions required for the tag, 
                mu1_pt          = cms.vdouble( 7.5 , 9999 ), 
                mu1_eta         = cms.vdouble( -2.4, 2.4  ),
#                 mu1_id_s        = cms.vdouble(  0.5, 10   ),

                sv_prob         = cms.vdouble(  0.005, 1. ),
                sv_2d_cos       = cms.vdouble(  0.99 , 1. ),
                b_m             = cms.vdouble(  5.15 , 5.4),
#                 k_pt            = cms.vdouble(  2.0  , 1000.),
                
                ## flags and conditions required for the probe, 
                tk2_eta         = cms.vdouble( -2.4, 2.4 ),                
            ),
            BinToPDFmap = cms.vstring("vpvPlusExpo"), ## PDF to use, as defined below
        ),
# 				tag_nVertices = cms.vdouble( 0.5, 3.5, 6.5, 9.5, 12.5, 15.5, 18.5, 21.5, 24.5, 27.5, 30.5, 50 ),

    ),
    ## PDF for signal and background (double voigtian + exponential background)
    PDFs = cms.PSet(
        vpvPlusExpo = cms.vstring(
            "Gaussian::g1(jpsi_m, mean[3.09,3.0,3.2], sigma[0.03,0.02,0.08])",
            "Gaussian::g2(jpsi_m, mean[3.09,3.0,3.2], sigma2[0.06,0.04,0.18])",
            "SUM::signal( f1[0,1]*g1, g2 )",
            "Chebychev::backgroundPass(jpsi_m, cPass[0,-1,1])",
            "Chebychev::backgroundFail(jpsi_m, cFail[0,-1,1])",
#             "Exponential::backgroundPass(mass, lp[-0.4,-5,1])",
#             "Exponential::backgroundFail(mass, lf[-1.0,-5,1])",
            "efficiency[0.9,0,1]",
            "signalFractionInPassing[0.9]"
        ),
    ),
    ## How to do the fit
    binnedFit              = cms.bool(True),
    binsForFit             = cms.uint32(40),
    saveDistributionsPlot  = cms.bool(False),
    NumCPU                 = cms.uint32(1), ## leave to 1 for now, RooFit gives funny results otherwise
    SaveWorkspace          = cms.bool(False),
)



## efficiency as a function of eta
# process.TnP_Muon_ID.Efficiencies.eff_eta   = process.TnP_Muon_ID.Efficiencies.eff_pt_eta.clone()   
# process.TnP_Muon_ID.Efficiencies.eff_eta  .BinnedVariables.pt          = cms.vdouble(4.0, 9999)
# process.TnP_Muon_ID.Efficiencies.eff_eta  .BinnedVariables.eta         = cms.vdouble( -2.4, -2.1, -1.6, -1.2, -0.9, -0.3, -0.2, 0.2, 0.3, 0.9, 1.2, 1.6, 2.1, 2.4)
# process.TnP_Muon_ID.Efficiencies.eff_eta  .BinnedVariables.abseta      = cms.vdouble( -1, 200)

## efficiency as a function of pt
# process.TnP_Muon_ID.Efficiencies.eff_pt   = process.TnP_Muon_ID.Efficiencies.eff_pt_eta.clone()   
# process.TnP_Muon_ID.Efficiencies.eff_pt  .BinnedVariables.eta         = cms.vdouble( -2.4, 2.4)
# process.TnP_Muon_ID.Efficiencies.eff_pt  .BinnedVariables.abseta      = cms.vdouble( -1, 200)


## efficiency as a function of phi
# process.TnP_Muon_ID.Efficiencies.eff_phi   = process.TnP_Muon_ID.Efficiencies.eff_pt.clone()   
# process.TnP_Muon_ID.Efficiencies.eff_phi  .BinnedVariables.pt          = cms.vdouble(5.0, 9999)
# process.TnP_Muon_ID.Efficiencies.eff_phi  .BinnedVariables.phi         = cms.vdouble( [(0.32*i-3.2) for i in range(0,20)]) 

## efficiency 2D, as a function of eta and pT
# process.TnP_Muon_ID.Efficiencies.eff_pt_eta   = process.TnP_Muon_ID.Efficiencies.eff_pt.clone()   
# process.TnP_Muon_ID.Efficiencies.eff_pt_eta  .BinnedVariables.abseta   = cms.vdouble( 0, 1.4, 2.4)

## efficiency as a function of deltaR between tag and probe
# process.TnP_Muon_ID.Efficiencies.eff_dr   = process.TnP_Muon_ID.Efficiencies.eff_pt_eta.clone()   
# process.TnP_Muon_ID.Efficiencies.eff_dr  .BinnedVariables.pt           = cms.vdouble(4.0, 9999)
# process.TnP_Muon_ID.Efficiencies.eff_dr  .BinnedVariables.pair_drM1    = cms.vdouble(0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8)
# process.TnP_Muon_ID.Efficiencies.eff_dr  .BinnedVariables.abseta       = cms.vdouble( -1, 200)

## efficiency as a function of deltaR between tag and probe
# process.TnP_Muon_ID.Efficiencies.eff_dr_eta   = process.TnP_Muon_ID.Efficiencies.eff_pt_eta.clone()   
# process.TnP_Muon_ID.Efficiencies.eff_dr_eta  .BinnedVariables.pt           = cms.vdouble(4.0, 9999)
# process.TnP_Muon_ID.Efficiencies.eff_dr_eta  .BinnedVariables.pair_drM1    = cms.vdouble(0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8)
# process.TnP_Muon_ID.Efficiencies.eff_dr_eta  .BinnedVariables.abseta       = cms.vdouble(  0, 0.9, 1.2, 2.1, 2.4  ) 


## efficiency as a function of # of vertices
# process.TnP_Muon_ID.Efficiencies.eff_nvtx  = process.TnP_Muon_ID.Efficiencies.eff_pt.clone()         
# process.TnP_Muon_ID.Efficiencies.eff_nvtx .BinnedVariables.pt            = cms.vdouble( 5.0,  99999 )          
# process.TnP_Muon_ID.Efficiencies.eff_nvtx .BinnedVariables.tag_nVertices  = cms.vdouble( [3*i+3 for i in range(0,20)])          
# 

process.p1 = cms.Path(process.TnP_Muon_ID)
