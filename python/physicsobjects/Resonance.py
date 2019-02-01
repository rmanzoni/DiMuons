from PhysicsTools.Heppy.physicsobjects.Particle import Particle

class Resonance(Particle):
    '''Resonance decaying into 2 particles.

    The interface of this class mimics the interface of the CMS Candidate class. 
    In this way Resonance objects or CMS Candidate objects can be processed 
    transparently. 
    '''

    def __init__(self, leg1, leg2, pdgid, status=3): 
        '''
        Parameters (stored as attributes):
        leg1,2 : first and second leg.
        pdgid  : pdg code of the resonance
        status : status code of the resonance
        '''
        self.leg1 = leg1 
        self.leg2 = leg2 
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


