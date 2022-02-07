from ..core import sdk as tygron

import sys

from collections import OrderedDict
from typing import Union
import json

class Trigger():

    @classmethod
    def exec(cls, args:list = None):
        if (args == None):
            args = sys.argv;

        if len(sys.argv) <= 3:
            raise IndexError('A host, and an api token must be provided as arguments. The trigger\'s file is the implicit first parameter. A parameter argument is optional.')
            
        trigger     = args[0]
        host        = args[1]
        apitoken    = args[2]
        parameters  = {}        

        if not len(args) <= 3:
            parameters  = json.loads(args[3])

        #print([host, apitoken, parameters])    

        trigger_object = cls(host, apitoken, parameters)
        trigger_object.trigger()  

        return trigger_object


    def run( self ):
        raise NotImplementedError('Run method of trigger '+self.__class__.__name__+' is not yet implemented.')
        

    def get_trigger_name( self ):
        return 'API Trigger - '+ type(self).__name__
        
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

    def __init__( self, host: str, apitoken: str = None, parameters: dict = {} ):
        self._parameters = parameters
        self._results = {}
        self._exception = None        

        self._sdk = tygron.sdk({
                'host': host
            })
        self._session_connection = self._sdk.create_connector_session()
        self._session_connection.set_api_token(apitoken)
    
    def trigger( self ):
        try:
            self.run()
        except Exception as e:
            self.set_exception(e)
