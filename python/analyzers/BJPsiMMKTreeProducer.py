from PhysicsTools.Heppy.analyzers.core.TreeAnalyzerNumpy import TreeAnalyzerNumpy
from PhysicsTools.HeppyCore.utils.deltar import deltaR, deltaPhi, inConeCollection, bestMatch

import ntuple
import ROOT

from itertools import product

class BJPsiMMKTreeProducer(TreeAnalyzerNumpy):
    
    def beginLoop(self, setup):
        super(BJPsiMMKTreeProducer, self).beginLoop(setup)
        
        ntuple.bookEvent(self.tree)
        
        ntuple.bookParticle(self.tree, 'b')
        ntuple.bookParticle(self.tree, 'jpsi')
        ntuple.bookMuon(self.tree, 'mu1')
        ntuple.bookParticle(self.tree, 'tk2')
        ntuple.bookMuon(self.tree, 'mu2') # muon matched to the track
        ntuple.bookParticle(self.tree, 'k')

        ntuple.var(self.tree, 'dr_mm')
        ntuple.var(self.tree, 'dr_jpsi_k')
        ntuple.var(self.tree, 'dr_jpsi_mu1')
        ntuple.var(self.tree, 'dr_jpsi_mu2')
        ntuple.var(self.tree, 'dr_mu1_k')
        ntuple.var(self.tree, 'dr_mu2_k')
        ntuple.var(self.tree, 'dphi_mm')

        ntuple.var(self.tree, 'dphi_jpsi_k')
        ntuple.var(self.tree, 'dphi_jpsi_mu1')
        ntuple.var(self.tree, 'dphi_jpsi_mu2')
        ntuple.var(self.tree, 'dphi_mu1_k')
        ntuple.var(self.tree, 'dphi_mu2_k')

        ntuple.var(self.tree, 'b_cone')

        ntuple.var(self.tree, 'bs_x')
        ntuple.var(self.tree, 'bs_y')
        ntuple.var(self.tree, 'bs_z')

        ntuple.var(self.tree, 'pv_x')
        ntuple.var(self.tree, 'pv_y')
        ntuple.var(self.tree, 'pv_z')

        ntuple.var(self.tree, 'sv_x')
        ntuple.var(self.tree, 'sv_y')
        ntuple.var(self.tree, 'sv_z')

        ntuple.var(self.tree, 'sv_chi2')
        ntuple.var(self.tree, 'sv_prob')

        ntuple.var(self.tree, 'sv_2d_disp'    )
        ntuple.var(self.tree, 'sv_2d_disp_err')
        ntuple.var(self.tree, 'sv_2d_disp_sig')
        ntuple.var(self.tree, 'sv_2d_cos'     )

        ntuple.var(self.tree, 'HLT_Mu7p5_Track2_Jpsi')
        ntuple.var(self.tree, 'HLT_Mu7p5_Track3p5_Jpsi')
        ntuple.var(self.tree, 'HLT_Mu7p5_Track7_Jpsi')

        ntuple.var(self.tree, 'HLT_Mu7p5_Track2_Jpsi_ps')
        ntuple.var(self.tree, 'HLT_Mu7p5_Track3p5_Jpsi_ps')
        ntuple.var(self.tree, 'HLT_Mu7p5_Track7_Jpsi_ps')
        
    def process(self, event):
        
        self.tree.reset()

        ntuple.fillEvent(self.tree, event)
                
        ntuple.fillParticle(self.tree, 'b', event.theb)
        ntuple.fillParticle(self.tree, 'jpsi', event.theb.jpsi())
        ntuple.fillMuon(self.tree, 'mu1'   , event.theb.l0())
        ntuple.fillParticle(self.tree, 'tk2'   , event.theb.l1())
        mu2, dR2 = bestMatch(event.theb.l1(), event.muons)
        if dR2<0.005*0.005 and mu2.physObj != event.theb.l0().physObj:
            ntuple.fillMuon(self.tree, 'mu2', mu2)

        ntuple.fillParticle(self.tree, 'k', event.theb.k())

        ntuple.fill(self.tree, 'dr_mm'        , deltaR(event.theb.l0()    , event.theb.l1()))
        ntuple.fill(self.tree, 'dr_jpsi_k'    , deltaR(event.theb.jpsi()  , event.theb.k() ))
        ntuple.fill(self.tree, 'dr_jpsi_mu1'  , deltaR(event.theb.jpsi()  , event.theb.l0()))
        ntuple.fill(self.tree, 'dr_jpsi_mu2'  , deltaR(event.theb.jpsi()  , event.theb.l1()))
        ntuple.fill(self.tree, 'dr_mu1_k'     , deltaR(event.theb.l0()    , event.theb.k() ))
        ntuple.fill(self.tree, 'dr_mu2_k'     , deltaR(event.theb.l1()    , event.theb.k() ))

        ntuple.fill(self.tree, 'dphi_mm'      , deltaPhi(event.theb.l0()  .phi(), event.theb.l1().phi()))
        ntuple.fill(self.tree, 'dphi_jpsi_k'  , deltaPhi(event.theb.jpsi().phi(), event.theb.k() .phi()))
        ntuple.fill(self.tree, 'dphi_jpsi_mu1', deltaPhi(event.theb.jpsi().phi(), event.theb.l0().phi()))
        ntuple.fill(self.tree, 'dphi_jpsi_mu2', deltaPhi(event.theb.jpsi().phi(), event.theb.l1().phi()))
        ntuple.fill(self.tree, 'dphi_mu1_k'   , deltaPhi(event.theb.l0()  .phi(), event.theb.k() .phi()))
        ntuple.fill(self.tree, 'dphi_mu2_k'   , deltaPhi(event.theb.l1()  .phi(), event.theb.k() .phi()))

        ntuple.fill(self.tree, 'b_cone'       , event.theb.bcone())

        ntuple.fill(self.tree, 'bs_x', event.beamspot.x0())
        ntuple.fill(self.tree, 'bs_y', event.beamspot.y0())
        ntuple.fill(self.tree, 'bs_z', event.beamspot.z0())

        ntuple.fill(self.tree, 'pv_x', event.pv.x())
        ntuple.fill(self.tree, 'pv_y', event.pv.y())
        ntuple.fill(self.tree, 'pv_z', event.pv.z())

        if event.theb.vtx().isValid():
            ntuple.fill(self.tree, 'sv_x', event.theb.vtx().position().x())
            ntuple.fill(self.tree, 'sv_y', event.theb.vtx().position().y())
            ntuple.fill(self.tree, 'sv_z', event.theb.vtx().position().z())

            ntuple.fill(self.tree, 'sv_chi2', event.theb.vtx().normalisedChiSquared())
            ntuple.fill(self.tree, 'sv_prob', ROOT.TMath.Prob(event.theb.vtx().normalisedChiSquared(), 1))

            ntuple.fill(self.tree, 'sv_2d_disp'      , event.theb.disp2d().value())
            ntuple.fill(self.tree, 'sv_2d_disp_err'  , event.theb.disp2d().error())
            ntuple.fill(self.tree, 'sv_2d_disp_sig'  , event.theb.ls2d())
            ntuple.fill(self.tree, 'sv_2d_cos'       , event.theb.vtxcos())

        for info, hlt in product(event.trigger_infos, ['HLT_Mu7p5_Track2_Jpsi', 'HLT_Mu7p5_Track3p5_Jpsi', 'HLT_Mu7p5_Track7_Jpsi']):
            if hlt in info.name:
                ntuple.fill(self.tree, hlt, info.fired)
                ntuple.fill(self.tree, hlt+'_ps', info.prescale)

#         ntuple.fill(self.tree, 'HLT_Mu7p5_Track2_Jpsi_v9'  , any([True for info in event.trigger_infos if info.name == 'HLT_Mu7p5_Track2_Jpsi_v9'   and info.fired]))
#         ntuple.fill(self.tree, 'HLT_Mu7p5_Track3p5_Jpsi_v9', any([True for info in event.trigger_infos if info.name == 'HLT_Mu7p5_Track3p5_Jpsi_v9' and info.fired]))
#         ntuple.fill(self.tree, 'HLT_Mu7p5_Track7_Jpsi_v9'  , any([True for info in event.trigger_infos if info.name == 'HLT_Mu7p5_Track7_Jpsi_v9'   and info.fired]))
# 
#         ntuple.fill(self.tree, 'HLT_Mu7p5_Track2_Jpsi_v9_ps'  , any([True for info in event.trigger_infos if info.name == 'HLT_Mu7p5_Track2_Jpsi_v9'   and info.fired]))
#         ntuple.fill(self.tree, 'HLT_Mu7p5_Track3p5_Jpsi_v9_ps', any([True for info in event.trigger_infos if info.name == 'HLT_Mu7p5_Track3p5_Jpsi_v9' and info.fired]))
#         ntuple.fill(self.tree, 'HLT_Mu7p5_Track7_Jpsi_v9_ps'  , any([True for info in event.trigger_infos if info.name == 'HLT_Mu7p5_Track7_Jpsi_v9'   and info.fired]))

        
        self.tree.tree.Fill()

