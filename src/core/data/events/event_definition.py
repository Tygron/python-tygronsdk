from .event import Event
from .event_parameter import EventParameter

from typing import List

class EventDefinition:

    def __init__( self, name:str = None, domain:str = None, parameters:List[EventParameter] = [] ):
        self.name = name
        self.domain = domain
        self.parameters = parameters
    
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = None if name is None else str(name).lower()
        
    @property
    def domain(self):
        return self._domain
    @domain.setter
    def domain(self, domain):
        self._domain = None if domain is None else str(domain).lower()
        
    @property
    def parameters(self):
        return self._parameters
    @parameters.setter
    def parameters(self, parameters):
        self._parameters = [] if parameters is None else parameters
        
    
    def __call__( self, *args, **kwargs ):
        event = Event(
            event_name = self.name,
            event_domain = self.domain,
            parameters = self.parameters
        )
        event.set_arguments(*args, **kwargs)
        return event
        
    def __str__( self ):            
        return '{domain}/{name}: [{params}]'.format(
                domain=self.domain,
                name=self.name,
                params=', '.join([str(p) for p in self.parameters])
            )