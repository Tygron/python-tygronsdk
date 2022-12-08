from .interactions import InteractionWrapper
import sys

class ApiEnvironment():

    def __init__( self, settings = {}, module = None ):
        self._settings = settings
        self.module = module

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
    
    def get_interaction_wrapper(self, interaction_module):
        try:
            submodule = self.module
            if ( not submodule is None and 'interactions' in  submodule.__dict__ ):
                submodule = getattr( submodule, 'interactions' )
            else:
                submodule = None
                
            if ( not submodule is None and interaction_module in  submodule.__dict__ ):
                submodule = getattr( submodule, interaction_module )
            else:
                submodule = None
                
            if ( not submodule is None ):
                return InteractionWrapper(
                        interactions_object = submodule,
                        connector = self.connector,
                        settings = self.settings
                    )
        except Exception as err:
            print(err)
            return None
    

    
    def __getattr__(self, attr):
        if ( not '_module' in self.__dict__ ):
            return super().__getattr__(attr)
        submodule = self.get_interaction_wrapper(attr)
        if ( not submodule is None ):
            return submodule
        
        #sys.modules(self.module)
        raise AttributeError('Environment does not have an attribute, submodule, or interaction named \''+str(attr)+'\'')
                
            
        