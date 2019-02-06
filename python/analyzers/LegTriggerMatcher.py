from collections import OrderedDict
from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from PhysicsTools.HeppyCore.utils.deltar import deltaR, deltaPhi, inConeCollection, bestMatch


class LegTriggerMatcher(Analyzer):
    '''Match collection to selected trigger objects.
       Need to run TriggerAnalyzer earlier in the sequence.
    '''

    def beginLoop(self, setup):
        super(LegTriggerMatcher, self).beginLoop(setup)
        self.counters.addCounter('LegTriggerMatcher')
        count = self.counters.counter('LegTriggerMatcher')
        count.register('all events')
        count.register('matched events')

    def process(self, event):

        self.counters.counter('LegTriggerMatcher').inc('all events')

        dR2max = getattr(self.cfg_ana, 'dRmax', 0.1)**2
        collection = getattr(event, self.cfg_ana.collection)
        tomatch = self.cfg_ana.paths_and_filters
        
        for icoll in collection:
            if not hasattr(icoll, 'trig_obj'):
                icoll.trig_obj = OrderedDict()
        
        for ihlt, ifilter in tomatch.iteritems():
            infos = [info for info in event.trigger_infos if ihlt=='_'.join(info.name.split('_')[:-1])]
            if len(infos)!=1:
                continue 
            else:
                info = infos[0]           
            objects = info.objects

            objects = [obj for obj in objects if obj.filter(ifilter[0]) and obj.triggerObjectTypes()[0]==ifilter[1]]
            
            # temporary collection to save only trig matched objects
            tmp_coll = []
                   
            for icoll in collection:
                icoll.trig_obj[ifilter] = -1
                bestmatch, dR2 = bestMatch(icoll, objects)
                if dR2 < dR2max:
                    icoll.trig_obj[ifilter] = bestmatch
                    tmp_coll.append(icoll)
                
        if getattr(self.cfg_ana, 'filter', False):
            setattr(event, self.cfg_ana.collection + '_matched', tmp_coll)
    
        if len(tmp_coll)>0:
            self.counters.counter('LegTriggerMatcher').inc('matched events')

            