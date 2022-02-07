from ..core import sdk as tygron

from collections import OrderedDict
from typing import Union

class Trigger():

    def exec( cls ):
    
        if len(sys.argv) <= 3:
            raise IndexError('A trigger, a host, and an api token must be provided as arguments')
            
            
        trigger     = sys.argv[1]
        host        = sys.argv[2]
        apitoken    = sys.argv[3]
        
        if not len(sys.argv) <= 4:
            parameters  = sys.argv[4]


        #trigger_object = new cls(host, )
    
        return cls(name, date.today().year - year)        

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
 
    def __init__( self, host: str, apitoken: str = None, parameters: dict = {} ):
        self._parameters = parameters
        self._results = {}
        
        self._sdk = tygron.sdk({
                'host': host
            })
        self._session_connection = self._sdk.create_connector_session()
        self._session_connection.set_api_token(apitoken)


        
    def trigger( self ):
        
        self.run()
        
        return self._results