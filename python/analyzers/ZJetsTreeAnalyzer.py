from PhysicsTools.Heppy.analyzers.core.TreeAnalyzerNumpy import TreeAnalyzerNumpy
import ntuple

class ZJetsTreeAnalyzer(TreeAnalyzerNumpy):
    
    def beginLoop(self, setup):
        super(ZJetsTreeAnalyzer, self).beginLoop(setup)
        ntuple.bookParticle(self.tree, 'dimuon')
        ntuple.bookMuon(self.tree, 'mu1')
        ntuple.bookMuon(self.tree, 'mu2')

        ntuple.var(self.tree, 'bs_x')
        ntuple.var(self.tree, 'bs_y')
        ntuple.var(self.tree, 'bs_z')

        ntuple.var(self.tree, 'pv_x')
        ntuple.var(self.tree, 'pv_y')
        ntuple.var(self.tree, 'pv_z')

        ntuple.var(self.tree, 'sv_x')
        ntuple.var(self.tree, 'sv_y')
        ntuple.var(self.tree, 'sv_z')

        ntuple.var(self.tree, 'sv_2d_disp'      )
        ntuple.var(self.tree, 'sv_3d_disp'      )
        ntuple.var(self.tree, 'sv_2d_disp_error')
        ntuple.var(self.tree, 'sv_3d_disp_error')
        ntuple.var(self.tree, 'sv_2d_disp_sig'  )
        ntuple.var(self.tree, 'sv_3d_disp_sig'  )
        ntuple.var(self.tree, 'sv_2d_cos'       )
        
    def process(self, event):
        self.tree.reset()
        
        ntuple.fillParticle(self.tree, 'dimuon', event.dimuons[0])
        ntuple.fillMuon(self.tree, 'mu1'   , event.dimuons[0].leg1)
        ntuple.fillMuon(self.tree, 'mu2'   , event.dimuons[0].leg2)

        ntuple.fill(self.tree, 'bs_x', event.beamspot.x0())
        ntuple.fill(self.tree, 'bs_y', event.beamspot.y0())
        ntuple.fill(self.tree, 'bs_z', event.beamspot.z0())

        ntuple.fill(self.tree, 'pv_x', event.pv.x())
        ntuple.fill(self.tree, 'pv_y', event.pv.y())
        ntuple.fill(self.tree, 'pv_z', event.pv.z())

        if event.dimuons[0].vertex.isValid():
            ntuple.fill(self.tree, 'sv_x', event.dimuons[0].vertex.position().x())
            ntuple.fill(self.tree, 'sv_y', event.dimuons[0].vertex.position().y())
            ntuple.fill(self.tree, 'sv_z', event.dimuons[0].vertex.position().z())

            ntuple.fill(self.tree, 'sv_2d_disp'      , event.dimuons[0].disp2DFromBS.value())
            ntuple.fill(self.tree, 'sv_3d_disp'      , event.dimuons[0].disp3DFromBS.value())
            ntuple.fill(self.tree, 'sv_2d_disp_error', event.dimuons[0].disp2DFromBS.error())
            ntuple.fill(self.tree, 'sv_3d_disp_error', event.dimuons[0].disp3DFromBS.error())
            ntuple.fill(self.tree, 'sv_2d_disp_sig'  , event.dimuons[0].disp2DFromBS_sig)
            ntuple.fill(self.tree, 'sv_3d_disp_sig'  , event.dimuons[0].disp3DFromBS_sig)
            ntuple.fill(self.tree, 'sv_2d_cos'       , event.dimuons[0].disp2DFromBS_cos)
        
        self.tree.tree.Fill()

