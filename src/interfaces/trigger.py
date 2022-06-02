from ..core import sdk as tygron

from ..interactions import Session

import sys

from collections import OrderedDict
from typing import Union
import json

class Trigger():

    @classmethod
    def create(cls, args:list = None):
        if (args == None):
            args = sys.argv

        '''
        if len(sys.argv) <= 3:
            raise IndexError('A host, and an api token must be provided as arguments. The trigger\'s file is the implicit first parameter. A parameter argument is optional.')
        '''
        trigger_object = None
        
        try:        
            trigger     = args[0]
            host        = args[1]
            apitoken    = args[2]
            parameters  = {}        

            if not len(args) <= 3:
                parameters  = json.loads(args[3])
                
            trigger_object = cls(host, apitoken, parameters)
            
        except IndexError: 
            trigger_object = cls()

        return trigger_object

    @classmethod
    def exec(cls, args:list = None):
        if (args == None):
            args = sys.argv
            
        if len(sys.argv) <= 3:
            raise IndexError('A host, and an api token must be provided as arguments. The trigger\'s file is the implicit first parameter. A parameter argument is optional.')
            
        trigger_object = cls.create(args)
        trigger_object.trigger()  

        return trigger_object
        
        
    def run( self ):
        raise NotImplementedError('Run method of trigger '+self.__class__.__name__+' is not yet implemented.')
        

    def get_trigger_name( self ):
        return 'API Trigger - '+ type(self).__name__
    
    
    def get_metadata( self ):
        metadata = {}
        metadata['description'] = self.get_description()
        metadata['descriptionShort'] = self.get_description_short()
        metadata['supportedTypes'] = self.get_supported_types()
        metadata['recommendedTiming'] = self.get_recommended_timing()
        metadata['recommendedTimeout'] = self.get_recommended_timeout()
        metadata['isOnlyModeEditor'] = self.is_only_mode_editor()
        metadata['isOnlyModeSession'] = self.is_only_mode_session()
        metadata['assets'] = self.get_documented_assets()
        metadata['parameters'] = self.get_documented_parameters()
        metadata['results'] = self.get_documented_results()
        metadata['examples'] = self.get_usage_examples()
        
        return metadata
    
    
    def get_description( self ):
        return None
    def get_description_short( self ):
        return None
    
    def is_secret( self ):
        return False
    def get_supported_types( self ):
        return []
    def get_recommended_timing( self ):
        return 'BEFORE'
    def get_recommended_timeout( self ):
        return None
    
    def is_only_mode_editor( self ):
        return False
    def is_only_mode_session( self ):
        return False 
        
    def get_documented_assets( self ):
        return None
    def get_documented_parameters( self ):
        return None
    def get_documented_results( self ):
        return None
    def get_usage_examples( self ):
        return None
    

    
        
    
    def is_session_in_right_mode( self ):
        if ( self.is_only_mode_editor() ):
            if (not Session.is_session_state_editing( self.get_session_connection() ) ):
                return False
        if ( self.is_only_mode_session() ):
            if (not Session.is_session_state_session( self.get_session_connection() ) ):
                return False
        return True
     
    def get_sdk( self ):
        return self._sdk  
    def get_session_connection( self ):
        return self._session_connection
        
    def get_parameters( self ):
        return self._parameters
    def get_parameter( self, parameter, default = None ):
        return self._parameters.get(parameter, default)
    
    def get_results( self ):
        return self._results
    
    def add_result( self, key, parameter, replace:bool = False ):
        if not replace:
            if key in self._results:
                del self._results[key]
        self._results[key] = parameter    
    def add_results( self, results:dict = {}, replace:bool = False ):
        for key, result in results.items():
            self.add_result(key, result, replace)
    
    def get_exception( self ):
        return self._exception

    def set_exception( self, exception:Exception ):
        self._exception = exception

    def get_results_structure( self ):
        return {
            'TQL' : self.get_results(),
            'EVENTS' : self.get_results(),
            'exception' : str(self.get_exception()) if self.get_exception() else None,
        }

    def __init__( self, host: str = None, apitoken: str = None, parameters: dict = {} ):
        self._parameters = parameters
        self._results = {}
        self._exception = None

        if ( not (host == None) and not (apitoken == None) ):
            self._sdk = tygron.sdk({
                    'host': host
                })
            self._session_connection = self._sdk.create_connector_session()
            self._session_connection.set_api_token(apitoken)
    
    def is_ready_to_trigger( self ):
        return not (self.get_session_connection() == None)
    
    def trigger( self ):
        try:
            if ( not self.is_session_in_right_mode() ):
                return
            self.run()
        except Exception as e:
            self.set_exception(e)
