from .event import Event
from .event_parameter import EventParameter

from typing import List

class EventDefinition:

    def __init__( self, name:str = None, domain:str = None, parameters:List[EventParameter] = [], group:str = None ):
        self._data = {}
        
        self.name = name
        self.domain = domain
        self.parameters = parameters
        self.group = group
    
    @property
    def name(self):
        return self._data['name']
    @name.setter
    def name(self, name):
        self._data['name'] = None if name is None else str(name).lower()
        
    @property
    def domain(self):
        return self._data['domain']
    @domain.setter
    def domain(self, domain):
        self._data['domain'] = None if domain is None else str(domain).lower()
        
    @property
    def parameters(self):
        return self._data['parameters']
    @parameters.setter
    def parameters(self, parameters):
        self._data['parameters'] = [] if parameters is None else parameters
    
    @property
    def group(self):
        return self._data['group']
    @group.setter
    def group(self, group):
        self._data['group'] = '' if group is None else str(group)    
    
    @property
    def data( self ):
        return { **self._data }
        
        
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