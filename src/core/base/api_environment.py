from ..core import ApiEnvironment as CoreApiEnvironment

class ApiEnvironment(CoreApiEnvironment):
        
    def authenticate( self, authentication_details: dict = {}, **kwargs ) -> bool:
        auth_details = { **authentication_details, **kwargs }
        username = auth_details.get('username', None)
        key = auth_details.get('password', None)
        if ( key is None):
            key = auth_details.get('authentication_key', None)
        
        if ( username is None or key is None):
            return None
        
        self.connector.set_http_basic_authentication( username, key )
        
        success = self.connector.authenticate()
        
        return success