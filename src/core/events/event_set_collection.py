from .event_set import EventSet

import inspect

#Containing class/object for ApiEnvironments to hold their events
class EventSetCollection():

    def __init__( self, *event_sets_list, **event_sets_dict ):
        self.add_event_sets(*event_sets_list, **event_sets_dict)
        pass
    
    def add_event_sets( self, *event_sets_list, **event_sets_dict ):
        for event_set in event_sets_list:
            self.add_event_set(event_set)
        for event_domain, event_set in event_sets_dict.items():
            self.add_event_set(event_set, event_domain)
    
    def add_event_set( self, event_set:EventSet, event_domain:str = None ):
        event_domain = event_set.event_domain if event_domain == None else event_domain
        setattr( self, event_domain, event_set )