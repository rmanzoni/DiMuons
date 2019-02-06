import ROOT
from PhysicsTools.Heppy.physicsobjects.Particle import Particle
from PhysicsTools.Heppy.physicsobjects.PhysicsObject import PhysicsObject

class Resonance(Particle):
    '''Resonance decaying into 2 particles.

    The interface of this class mimics the interface of the CMS Candidate class. 
    In this way Resonance objects or CMS Candidate objects can be processed 
    transparently. 
    '''

    def __init__(self, leg1, leg2, pdgid, status=3, sort_by_pt=False, mass1=-1, mass2=-1): 
        '''
        Parameters (stored as attributes):
        leg1,2 : first and second leg.
        pdgid  : pdg code of the resonance
        status : status code of the resonance
        '''
        if isinstance(leg1.physObj, ROOT.pat.PackedCandidate): leg1 = PhysicsObject(ROOT.pat.PackedCandidate(leg1.physObj))
        if isinstance(leg2.physObj, ROOT.pat.PackedCandidate): leg2 = PhysicsObject(ROOT.pat.PackedCandidate(leg2.physObj))

        if sort_by_pt:
            self.leg1 = leg1 if leg1.pt() >= leg2.pt() else leg2 
            self.leg2 = leg2 if leg1.pt() >= leg2.pt() else leg1
        else:
            self.leg1 = leg1 
            self.leg2 = leg2 
        if mass1>0: self.leg1.setMass(mass1)
        if mass2>0: self.leg2.setMass(mass2)
        self._p4 = leg1.p4() + leg2.p4()
        self._charge = leg1.charge() + leg2.charge()
        self._pdgid = pdgid
        self._status = status
    
    def p4(self):
        return self._p4

    def pt(self):
        return self._p4.pt()

    def energy(self):
        return self._p4.energy()

    def eta(self):
        return self._p4.eta()

    def phi(self):
        return self._p4.phi()

    def mass(self):
        return self._p4.mass()

    def charge(self):
        return self._charge

    def pdgId(self):
        return self._pdgid


