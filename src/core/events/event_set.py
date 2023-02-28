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
        
        self._definitions = {}
        self.groups = {}
        
        definitions = self._normalize_definitions( event_definitions )
        self._generate_definitions( definitions )
     
    @property
    def definitions( self ):
        return self._definitions
        
    def get_definition_names_as_grouped_list( self, include_empty:bool = False ):
        definitions = []
        for group_name, group_list in self.groups.items():
            for def_name in group_list:
                if ( (not(self._definitions[def_name] is None)) or include_empty ):
                    definitions.append(def_name)
        return definitions
    
    def get_definition( self, name ):
        definition = self._definitions.get( name , None )
        return definition
    
    def get_event( self, name ):
        name = str(name).lower()
        domain = str(self.domain).lower()
        event_path = Event.generate_path(domain, name)
        
        definition = self.get_definition( name )
        
        if ( definition is None ):
            raise Exception( 'No event known as ' + event_path )
        
        return Event(
            event_domain = domain,
            event_name = name,
            parameters = definition if isinstance(defintion,list) else definition.parameters
        )

    def _generate_definitions( self, definitions:dict = {} ):
        for event_definition_name, event_definition in definitions.items():
            self._store_definition( name=event_definition_name, definition=event_definition )
            if ( not ( event_definition is None ) ):
                setattr(self, event_definition_name, event_definition )
            
    def _store_definition( self, name:str = None, definition:EventDefinition = None ):
        group = None if (definition is None) else definition.group
        name = name if (definition is None) else definition.name
        
        self._definitions[name] = definition
            
        self.groups[group] = self.groups.get(group, [])
        self.groups[group].append(name)
        
            
    def _normalize_definitions( self, event_definitions:Union[dict,list]=[] ):
        defs = {}
        if ( isinstance(event_definitions, list) ):
            event_definitions = { k:v for k, v in enumerate(event_definitions) }
         
        for i, definition in event_definitions.items():
            if (definition is None):
                defs[i] = None
                continue
        
            if ( isinstance(definition, dict) ):
                definition = EventDefinition(**definition)
                
            if ( not isinstance(definition, EventDefinition) ):
                continue
                
            if ( definition.name is None ):
                definition.name = i
            if ( definition.domain is None ):
                definition.domain = self.domain
            defs[definition.name] = definition
        return defs