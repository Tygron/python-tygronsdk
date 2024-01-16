from . import DataStore
from ..files import Files
from ..tygron_strings import TygronStrings

import json, base64

class CredentialsStore(DataStore):

    def __init__( self, data:dict = None, file:str = None ):
        self._credential_keys = [
                'username',
                'password',
                'api_token',
                
            ]
        self._data = {}
        self._source = None
        self.update( 
                data=data,
                file=file
            )
    
    @staticmethod
    def create( file:str = None ):
        return CredentialsStore( file=file )
    
    
    
    @property
    def username(self):
        return self._data.get('username', None)
    @property
    def password(self):
        return self._data.get('password', None)
    @property
    def api_token(self):
        return self._data.get('api_token', None)
    @property
    def session_id(self):
        api_token = self.api_token
        if ( api_token is None ):
            return None
        try:
            return TygronStrings.parse_session_id_from_api_token( api_token )
        except:
            return None
        
    
    def get_credentials( self ):
        return {k: v for k, v in {
            'username': self._data.get( 'username', None ),
            'password': self._data.get( 'password', None ),
            'api_token': self._data.get( 'api_token', None ),
        }.items() if v is not None}
    
    
    def parse_keys( self, data ):
        new_data = super().parse_keys( data )
        
        return { key: new_data.get(key, None) for key in self._credential_keys }
        
    def __str__(self):
        output = []
        if   ( self.username and self.password ):
            output.append('User '+str(self.username) + ' with password set')
        elif ( self.username ):
            output.append('User '+str(self.username) + ' without password set')
        elif ( self.password ):
            output.append('Password without known user')
            
        if   ( self.api_token ):
            output.append('API token for session ' + str(self.session_id) )
        
        return 'Credentials: ' + (', '.join(output))