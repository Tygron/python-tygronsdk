from ..core import ApiEnvironment as CoreApiEnvironment

class ApiEnvironment(CoreApiEnvironment):

    def __init__( self, settings = {}, **kwargs ):
        super().__init__( settings = settings )
        self.module
        self.connector
        
    def authenticate( self, authentication_details: dict = {}, **kwargs ) -> bool:
        auth_details = { **authentication_details, **kwargs }
        
        api_token = auth_details.get('api_token', None)
        if (api_token is None):
            return None
            
        self.connector.set_api_token(api_token)
        
        success = self.connector.authenticate()
        
        return success
        
        
        