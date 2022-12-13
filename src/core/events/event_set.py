from ..data.events import Event
from ... import utilities

import inspect

#This class defines the object which serves out events for a given type
class EventSet():

    def __init__( self, event_definitions_class, event_domain:str = None ):
    
        if (event_domain is not None):
            self.event_domain = event_domain
        else:
            self.event_domain = utilities.files.get_filename(inspect.getfile(event_definitions_class), False)
            
        self._events = event_definitions_class()

    def __getattr__( self, attr ):
        event_name = str(attr).lower()
        event_domain = str(self.event_domain).lower()
        event_path = Event.generate_path(event_domain, event_name)

        definition = None
        
        try:
            internal_attr_name = '_'+(event_name.lstrip('_'))
            if ( not (internal_attr_name == event_name) ):
                definition = getattr(self._events, internal_attr_name, None)
        except Exception as err:
            raise Exception('An exception while trying to retrieve event definition '+event_path+': '+str(err))
        
        if ( definition == None ):
            raise Exception( 'No event known as ' + event_path )
        return Event(
                event_domain = event_domain,
                event_name = event_name,
                parameters = definition
            )
