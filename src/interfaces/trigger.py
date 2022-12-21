from .. import sdk as tygron

import sys

import json

class Trigger():

    @classmethod
    def create(cls, args:list = None):
        if (args == None):
            args = sys.argv

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
        metadata['recommendedTimeout'] = self.get_recommended_timeout()
        metadata['recommendedTiming'] = self.get_recommended_timing()
        metadata['isOnlyModeEditor'] = self.is_only_mode_editor()
        metadata['isOnlyModeSession'] = self.is_only_mode_session()
        metadata['assets'] = self.get_documented_assets()
        metadata['parameters'] = self.get_documented_parameters()
        metadata['results'] = self.get_documented_results()
        metadata['instructionsInstallation'] = self.get_instructions_installation()
        metadata['instructionsUsage'] = self.get_instructions_usage()
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
    def get_recommended_timeout( self ):
        return None
    def get_recommended_timing( self ):
        return 'BEFORE'
    
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
    def get_instructions_installation( self ):
        return None
    def get_instructions_usage( self ):
        return None
    def get_usage_examples( self ):
        return None
    

    
        
    
    def is_session_in_right_mode( self ):
        if ( self.is_only_mode_editor() ):
            if (not self.sdk.session.session.is_session_state_editing() ):
                return False
        if ( self.is_only_mode_session() ):
            if (not self.sdk.session.session.is_session_state_session() ):
                return False
        return True
     
    def get_sdk( self ):
        return self.sdk
    def get_session_connection( self ):
        return self.sdk.session.connector
        
    def get_parameters( self ):
        return self._parameters
    def get_parameter( self, parameter, default = None ):
        return self._parameters.get(parameter, default)
    
    def get_results( self ):
        return self._results
    
    def add_result( self, key, parameter, replace:bool = False ):
        if not replace:
            new_key = str(key)
            while(new_key in self._results):
                #   When duplicate results occur, add a nonce to prevent overwriting earlier results
                #   Nonces are ignored by the Platform for events, and collisions are undefined for TQL
                new_key = str(key)+self.get_nonce()
            key = new_key
        self._results[key] = parameter    
    def add_results( self, results:dict = {}, replace:bool = False ):
        for key, result in results.items():
            self.add_result(key, result, replace)
    
    def get_nonce( self ):
        nonce_count = getattr(self, 'nonce_count', 0)
        self.nonce_count = nonce_count +1
        return '/nonce_'+str(nonce_count)
    
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

    def __init__( self, host: str = None, api_token: str = None, parameters: dict = {} ):
        self._parameters = parameters
        self._results = {}
        self._exception = None

        if ( not (host == None) and not (api_token == None) ):
            sdk = tygron.sdk({
                    'host': host
                })
            sdk.session.authenticate({ 'api_token' : api_token})
            self.sdk = sdk
    
    def is_ready_to_trigger( self ):
        return not (self.sdk == None)
    
    def trigger( self ):
        try:
            if ( not self.is_session_in_right_mode() ):
                return
            self.run()
        except Exception as e:
            self.set_exception(e)
