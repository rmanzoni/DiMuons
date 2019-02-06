#!/bin/env python

def var( tree, varName, type=float ):
    tree.var(varName, type)

def fill( tree, varName, value ):
    tree.fill( varName, value )

# event information

def bookEvent(tree): 
    var(tree, 'run')
    var(tree, 'lumi')
    var(tree, 'event')
    var(tree, 'nvtx')
 
def fillEvent(tree, event):
    fill(tree, 'run', event.run)
    fill(tree, 'lumi', event.lumi)
    fill(tree, 'event', event.eventId)
    fill(tree, 'nvtx', len(event.pvs))


# simple particle

def bookParticle( tree, pName ):
    var(tree, '{pName}_pdgid'.format(pName=pName))
    var(tree, '{pName}_e'.format(pName=pName))
    var(tree, '{pName}_pt'.format(pName=pName))
    var(tree, '{pName}_eta'.format(pName=pName))
    var(tree, '{pName}_phi'.format(pName=pName))
    var(tree, '{pName}_m'.format(pName=pName))  
    var(tree, '{pName}_q'.format(pName=pName))

def fillParticle( tree, pName, particle ):
    fill(tree, '{pName}_pdgid'.format(pName=pName), particle.pdgId() )
    fill(tree, '{pName}_e'.format(pName=pName), particle.energy() )
    fill(tree, '{pName}_pt'.format(pName=pName), particle.pt() )
    fill(tree, '{pName}_eta'.format(pName=pName), particle.eta() )
    fill(tree, '{pName}_phi'.format(pName=pName), particle.phi() )
    fill(tree, '{pName}_m'.format(pName=pName), particle.mass() )
    fill(tree, '{pName}_q'.format(pName=pName), particle.charge() )

def bookMet(tree, pName):
    var(tree, '{pName}_pt'.format(pName=pName))
    var(tree, '{pName}_phi'.format(pName=pName))
    var(tree, '{pName}_sumet'.format(pName=pName))

def fillMet(tree, pName, met):
    fill(tree, '{pName}_pt'.format(pName=pName), met.pt())
    fill(tree, '{pName}_phi'.format(pName=pName), met.phi())
    fill(tree, '{pName}_sumet'.format(pName=pName), met.sumEt())

def bookGenTau(tree, pName, pfdiscs, calodiscs):
    bookJet(tree, pName)   
    bookTau(tree, '{pName}_calo'.format(pName=pName), calodiscs)
    bookTau(tree, '{pName}_pf'.format(pName=pName), pfdiscs)
    bookJet(tree, '{pName}_pfjet'.format(pName=pName))

def fillGenTau(tree, pName, tau):
    fillJet(tree, pName, tau)   
    fillTau(tree, '{pName}_calo'.format(pName=pName), tau.match_calo)
    fillTau(tree, '{pName}_pf'.format(pName=pName), tau.match_pf)
    fillJet(tree, '{pName}_pfjet'.format(pName=pName), tau.match_pfjet)

def bookMuon(tree, pName):
    bookParticle( tree, pName )
    var(tree, '{pName}_dxy'        .format(pName=pName))
    var(tree, '{pName}_dz'         .format(pName=pName))
    var(tree, '{pName}_reliso05'   .format(pName=pName))
    var(tree, '{pName}_reliso05_03'.format(pName=pName))
    var(tree, '{pName}_id_s'       .format(pName=pName))
    var(tree, '{pName}_id_l'       .format(pName=pName))
    var(tree, '{pName}_id_m'       .format(pName=pName))
    var(tree, '{pName}_id_mm'      .format(pName=pName))
    var(tree, '{pName}_id_t'       .format(pName=pName))
    var(tree, '{pName}_id_tnv'     .format(pName=pName))
    var(tree, '{pName}_id_hpt'     .format(pName=pName))
    var(tree, '{pName}_is_sa'      .format(pName=pName))
    var(tree, '{pName}_is_gl'      .format(pName=pName))
    var(tree, '{pName}_is_tk'      .format(pName=pName))
    var(tree, '{pName}_is_pf'      .format(pName=pName))
    var(tree, '{pName}_is_oot'     .format(pName=pName))
    var(tree, '{pName}_simType'    .format(pName=pName))

def fillMuon(tree, pName, muon):
    fillParticle( tree, pName, muon )
    fill(tree, '{pName}_dxy'        .format(pName=pName), muon.track().dxy()                                 ) # this is shit
    fill(tree, '{pName}_dz'         .format(pName=pName), muon.track().dz()                                  ) # this is shit
    fill(tree, '{pName}_reliso05'   .format(pName=pName), muon.relIsoR(R=0.4, dBetaFactor=0.5, allCharged=0) )
    fill(tree, '{pName}_reliso05_03'.format(pName=pName), muon.relIsoR(R=0.3, dBetaFactor=0.5, allCharged=0) )
    fill(tree, '{pName}_id_s'       .format(pName=pName), muon.isSoftMuon(muon.associatedVertex)             )
    fill(tree, '{pName}_id_l'       .format(pName=pName), muon.muonID('POG_ID_Loose')                        )
    fill(tree, '{pName}_id_m'       .format(pName=pName), muon.muonID('POG_ID_Medium')                       )
    fill(tree, '{pName}_id_mm'      .format(pName=pName), muon.martinaMedium                                 )
    fill(tree, '{pName}_id_t'       .format(pName=pName), muon.muonID('POG_ID_Tight')                        )
    fill(tree, '{pName}_id_tnv'     .format(pName=pName), muon.muonID('POG_ID_TightNoVtx')                   )
    fill(tree, '{pName}_id_hpt'     .format(pName=pName), muon.muonID('POG_ID_HighPt')                       )
    fill(tree, '{pName}_is_sa'      .format(pName=pName), muon.isStandAloneMuon()                            )
    fill(tree, '{pName}_is_gl'      .format(pName=pName), muon.isGlobalMuon()                                )
    fill(tree, '{pName}_is_tk'      .format(pName=pName), muon.isTrackerMuon()                               )
    fill(tree, '{pName}_is_pf'      .format(pName=pName), muon.isPFMuon()                                    )
    fill(tree, '{pName}_is_oot'     .format(pName=pName), muon.isoot                                         )
    fill(tree, '{pName}_simType'    .format(pName=pName), muon.simType()                                     )


def bookTau(tree, pName, discNames):
    bookParticle(tree, pName)   
    var(tree, '{pName}_nsigcharged'.format(pName=pName))
    var(tree, '{pName}_isolation'.format(pName=pName))
    for discName in discNames:
        var(tree, '{pName}_{disc}'.format(pName=pName,
                                          disc=discName))
        
def fillTau(tree, pName, tau):
    if not tau: return 
    fillParticle(tree, pName, tau)
    fill(tree, '{pName}_nsigcharged'.format(pName=pName), len(tau.signalCharged()))
    fill(tree, '{pName}_isolation'.format(pName=pName), tau.isolation())
    for discName, value in tau.discs.iteritems():
        fill(tree, '{pName}_{disc}'.format(pName=pName,
                                           disc=discName), value)


# jet

def bookComponent( tree, pName ):
    var(tree, '{pName}_e'.format(pName=pName))
    var(tree, '{pName}_pt'.format(pName=pName))
    var(tree, '{pName}_num'.format(pName=pName))

def fillComponent(tree, pName, component):
    fill(tree, '{pName}_e'.format(pName=pName), component.e() )
    fill(tree, '{pName}_pt'.format(pName=pName), component.pt() )
    fill(tree, '{pName}_num'.format(pName=pName), component.num() )
    
    
pdgids = [211, 22, 130, 11, 13]
    
def bookJet( tree, pName ):
    bookParticle(tree, pName )
    for pdgid in pdgids:
        bookComponent(tree, '{pName}_{pdgid:d}'.format(pName=pName, pdgid=pdgid))
    # var(tree, '{pName}_npart'.format(pName=pName))

def fillJet( tree, pName, jet ):
    if not jet: return
    fillParticle(tree, pName, jet )
    for pdgid in pdgids:
        component = jet.constituents.get(pdgid, None)
        if component is not None:
            fillComponent(tree,
                          '{pName}_{pdgid:d}'.format(pName=pName, pdgid=pdgid),
                          component )
        else:
            import pdb; pdb.set_trace()
            print jet

