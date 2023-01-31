from ..files import Files
from ..tygron_strings import TygronStrings

import json, base64

class CredentialsTygron():

    def __init__( self, data:dict = None, file:str = None ):
        self._data = {}
        self.load( 
                data=data,
                file=file
            )
        self._source = None
    
    @staticmethod
    def create( file:str ):
        return CredentialsTygron( file=file )
    
    
    
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
    
    @property
    def source(self):
        return self._source
    
    def get_credentials( self ):
        return {k: v for k, v in {
            'username': self._data.get( 'username', None ),
            'password': self._data.get( 'password', None ),
            'api_token': self._data.get( 'api_token', None ),
        }.items() if v is not None}
    
    
    
    def load( self, data:dict = None, clear:bool = False, file:str = None ):
        if ( clear ):
            self._data = {}
            self._source = None
            
        if ( not (isinstance(data, dict) or isinstance(file,str) ) ):
            return
        
        if ( data is None ):
            data = self.load_from_file(file)
                
        if ( not isinstance(data, dict) ):
            raise Exception('Credentials file read succesfully, but did not contain valid data. Must be either a JSON, or key value pairs')           
 
        self._data.update( self.decode_keys(data) )
    
    
    
    def load_from_file( self, file:str = None ):
        if ( file is None ):
            return None
        try:
            data = Files.read_file_as_json( file )
        except json.decoder.JSONDecodeError:
            data = Files.read_file_as_key_values( file )
        return data
        
        
    
    def decode_keys( self, data ):
        new_data = {}
        for key, value in data.items():
            decoded_data = self.decode_base64_key(key, value)
            if ( len(decoded_data) > 0 ):
                new_data.update( decoded_data )
            else:
                new_data[key] = value
        return new_data
    
    def decode_base64_key( self, key, value ):
        b64term = 'base64'  if ( key.find('base64') >=0 )  else None
        b64term = 'b64'     if ( key.find('b64')    >=0 )  else b64term
        
        if ( b64term is None ):
            return {}
        try:
            decoded_value = base64.b64decode(value.encode('ASCII')).decode('ASCII')
        except UnicodeDecodeError:
            return {}
            
        b64_removable_term = '_'+b64term+'_' if ( key.find('_'+b64term+'_') >=0 ) else None
        replacement_term = '' if b64_removable_term is None else '_'
        if ( (b64_removable_term is None) and (key.find('_'+b64term) >=0) ):
            b64_removable_term = '_'+b64term
        if ( (b64_removable_term is None) and (key.find(b64term+'_') >=0) ):
            b64_removable_term = b64term+'_'
        
        proper_key = key.replace( b64_removable_term, replacement_term )
        
        return { proper_key : decoded_value}
        
        
    def keys(self):
        return self._data
    def __getitem__(self, key):
        return self._data[key]
    def __len__(self):
        return len(self._data)
    def __iter__(self):
        return iter(self._data)
        
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