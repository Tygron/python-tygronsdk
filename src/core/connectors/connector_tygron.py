from .connector import Connector

import base64

class ConnectorTygron(Connector):

    def __init__( self ):
        super().__init__()
        self.set_platform( 'engine' )
        self.set_query_params({'f':'JSON'})
        self.set_request_format('JSON')
        return
 
    def apply_settings( self, settings = {}, **kwargs ):
        combined_settings = {**settings, **kwargs}
        local_settings = dict((k, combined_settings[k]) for k in [
                'platform',
                'host',
                'username',
                'password'
            ] if k in combined_settings)
        for key, value in local_settings.items():
            if key == 'platform':
                self.set_platform( value )
            elif key == 'host':
                self.set_host( value )    
            elif key == 'username':
                if ( 'password' in combined_settings ):
                    self.set_http_basic_authentication( value, local_settings['password'] )
                elif ( self.username != value ):
                    self.set_http_basic_authentication( None, None )
                self.set_username(value)
                
            elif key == 'password':
                continue
                
            else:
                setattr( self, key, local_settings[key] )
 
    def set_platform( self, platform ):
        self.set_host( platform + '.tygron.com' )
    
    def set_username( self, username ):
        self.username=username
