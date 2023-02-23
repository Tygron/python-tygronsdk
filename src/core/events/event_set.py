from ..data.events import Event, EventDefinition
from ... import utilities

import inspect
from typing import Union

#This class defines the object which serves out events for a given type
class EventSet():

    def __init__( self, event_definitions:Union[dict,list]=None, domain:str = None ):
        if (domain is not None):
            self.domain = domain
        else:
            self.domain = utilities.files.get_filename(inspect.stack()[1].filename, False)
        self.domain = self.domain.lower()
        
        definitions = self._normalize_definitions( event_definitions )
        self._generate_definitions( definitions )
     
     
     
    def get_event( self, name ):
        name = str(name).lower()
        domain = str(self.domain).lower()
        event_path = Event.generate_path(domain, name)
        
        definition = self._definitions.get( name , None )
        
        if ( definition is None ):
            raise Exception( 'No event known as ' + event_path )
        
        return Event(
            event_domain = domain,
            event_name = name,
            parameters = definition if isinstance(defintion,list) else definition.parameters
        )
        
        try:
            definition
        except Exception as err:
            raise Exception('An exception while trying to retrieve event definition '+event_path+': '+str(err))
            
            

    def _generate_definitions( self, definitions:dict = {} ):
        self.definitions = getattr( self, 'definitions', {} )
        
        for event_definition_name, event_definition in definitions.items():
            self.definitions[event_definition_name] = event_definition
            setattr(self, event_definition_name, event_definition )
            
            
            
    def _normalize_definitions( self, event_definitions:Union[dict,list]=[] ):
        defs = {}
        if ( isinstance(event_definitions, list) ):
            event_definitions = { k:v for k, v in enumerate(event_definitions) }
         
        for i, definition in event_definitions.items():
            if ( isinstance(definition, dict) ):
                definition = EventDefinition(**definition)
            if ( definition.name is None ):
                definition.name = i
            if ( definition.domain is None ):
                definition.domain = self.domain
            defs[definition.name] = definition
            
        return defs