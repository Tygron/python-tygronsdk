from . import utilities

from . import core
from . import environments

class sdk():

    def __init__( self, settings = {}, **kwargs ):
              
        self._settings = {
            'platform' : 'engine',
            'computer_name' : 'Python SDK',
            'client_token' : utilities.strings.generate_random_token(),
            
            'session_id': None,
            'new_project_name' : None
        };
        
        self._on_exit_settings = {
            'save_project' : False,
            'save_created_project' : False,
            'close_session' : False,
            'kill_session' : False,
            'delete_created_project' : False
        }
        
        self.settings = {**settings,  **kwargs};
        
        self.create_environments()
        return;
    
    
    
    @property
    def settings(self):
        """Get all current settings of this SDK"""
        return self._settings
    @settings.setter
    def settings(self, value: dict):
        self._settings.update(**value)
        #TODO: propagate settings to environments

    @property
    def on_exit_settings(self):
        """Get all current instructions on what to do when the SDK exits."""
        return self._on_exit_settings
    @on_exit_settings.setter
    def on_exit_settings(self, value:dict ):
        self._on_exit_settings.update( **value )
        
    def configure_exit(self, value:dict = {}, **kwargs):
        self.on_exit_settings = { **value, **kwargs }
        
        
        
    def create_environments(self):
        self.base       = environments.base.ApiEnvironment( self.settings )
        self.session    = environments.session.ApiEnvironment( self.settings )
        self.share      = environments.share.ApiEnvironment( self.settings )
        
        self._environments = { 'base' : self.base, 'session' : self.session, 'share' : self.share }
        # self.session    = core.ApiEnvironment( settings= self.settings, module = sessionEnv )
        pass
    
    
        
    def authenticate( self, authentication_details: dict = {}, **kwargs ):
        auth_details = { **authentication_details, **kwargs }
        results = {}
        for name, env in self._environments.items():
            result = env.authenticate(auth_details)
            if ( not (result is None) ):
                results[name] = result
        return results
        
        
        
    def exit( self, exit_settings:dict = {} ):
        exit_settings = { **self.on_exit_settings, **exit_settings }
        errors = []
        
        if ( self.base.connector.authenticate() ):
            try:
                if (
                        (exit_settings['save_created_project'] and self.settings['new_project_name'])
                        or exit_settings['save_project']
                    ):
                    self.base.sessions.save_project()
            except Exception as err:
                errors.append(err)
                
            try:
                if ( exit_settings['close_session'] and self.settings['session_id']):
                    self.base.sessions.close_project_session( )
            except Exception as err:
                errors.append(err)
            try:
                if ( exit_settings['kill_session'] and self.settings['session_id']):
                    self.base.sessions.kill_project_session( )
            except Exception as err:
                errors.append(err)

            try:
                if ( exit_settings['delete_created_project'] and self.settings['new_project_name']):
                    self.base.projects.delete_project( self.settings['new_project_name'] )
            except Exception as err:
                errors.append(err)
        if ( len(errors) > 0 ):
            raise Exception( 'One or more exceptions occured while exiting the SDK.', *errors)