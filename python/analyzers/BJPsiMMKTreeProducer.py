from PhysicsTools.Heppy.analyzers.core.TreeAnalyzerNumpy import TreeAnalyzerNumpy
import ntuple
import ROOT

class BJPsiMMKTreeProducer(TreeAnalyzerNumpy):
    
    def beginLoop(self, setup):
        super(BJPsiMMKTreeProducer, self).beginLoop(setup)
        ntuple.bookParticle(self.tree, 'b')
        ntuple.bookParticle(self.tree, 'jpsi')
        ntuple.bookMuon(self.tree, 'mu1')
        ntuple.bookMuon(self.tree, 'mu2')
        ntuple.bookParticle(self.tree, 'k')

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
        
    def process(self, event):
        
        self.tree.reset()
        
        ntuple.fillParticle(self.tree, 'b', event.theb)
        ntuple.fillParticle(self.tree, 'jpsi', event.theb.jpsi())
        ntuple.fillMuon(self.tree, 'mu1'   , event.theb.l0())
        ntuple.fillMuon(self.tree, 'mu2'   , event.theb.l1())
        ntuple.fillParticle(self.tree, 'k', event.theb.k())

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
        
        self.tree.tree.Fill()

