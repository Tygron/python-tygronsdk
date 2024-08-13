from . import interactions
from . import events

from .. import utilities

import sys, inspect

class ApiEnvironment():

    def __init__( self, settings = {}, module = None, platform_version:str = '' ):
        self._settings = settings
        self.module = module
        self.generate_module_references(self.module, platform_version)

    @property
    def settings(self):
        return self._settings
    
    @settings.setter
    def settings(self, value):
        self._settings.update(**value)
            
            
    @property
    def module(self):
        module = None
        try:
            module = self._module
        except:
            thismodule = sys.modules[self.__module__]
            thispackage = sys.modules[thismodule.__package__]
            self.module = thispackage
            module = self._module
        return self._module
    
    @module.setter
    def module(self, value):
        if ( not hasattr(self, '_module') and value is not None ):
            self._module = value
        
        
    @property
    def connector(self):
        connector = None
        try :
            connector = self._connector
        except:
            self._connector = self.generate_connector( self._settings )
            connector = self._connector
        return self._connector

      
      
    def generate_connector( self, settings ):
        return self.module.Connector( settings )
    
    def authenticate( self, authentication_details: dict = {}, **kwargs ) -> bool:
        auth_details = { **authentication_details, **kwargs }
        pass
    
    
    
    def generate_module_references( self, module, platform_version ):
        interactions_module = getattr(module, 'interactions', None)
        self.generate_interaction_wrappers( interactions_module )
        
        events_module = getattr(module, 'data', module)
        events_module = getattr(events_module, 'events', events_module)
        events_module = events_module._get_platform_version(platform_version)
        self.generate_event_collection( events_module )
            
    def generate_interaction_wrappers( self, interactions_module ):
        if ( interactions_module == None):
            return
        objects = [interactions_module]
        if ( not inspect.isclass(interactions_module) ):
            objects = inspect.getmembers(interactions_module)
        for key, submodule in objects:
            if ( not inspect.isclass(submodule) ):
                continue
            
            if ( not hasattr(self, key) ):
                setattr( self, key, interactions.EnvironmentInteractionWrapper(
                        interactions_module = submodule,
                        connector = self.connector,
                        settings = self.settings
                    ) )
    
    def generate_event_collection( self, events_module ):
        self.events = getattr(self, 'events', events.EventSetCollection() )
        
        classes = utilities.modules.get_content_from_module(events_module, events.EventSet)

        for key, cls in classes.items():
            if ( not hasattr(self.events, key) ):
                setattr( self.events, key, events.EnvironmentEventSetWrapper(
                        events_set = cls,
                        connector = self.connector,
                        settings = self.settings
                    ) )