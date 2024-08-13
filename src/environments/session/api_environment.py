from ...core import ApiEnvironment as CoreApiEnvironment

class ApiEnvironment(CoreApiEnvironment):

    def __init__( self, settings = {}, module = None, platform_version:str = '' ):
        self._settings = settings
        self.module = module
        self.generate_module_references(self.module, platform_version)
        
    def authenticate( self, authentication_details: dict = {}, **kwargs ) -> bool:
        auth_details = { **authentication_details, **kwargs }
        
        api_token = auth_details.get('api_token', None)
        if (api_token is None):
            return None
            
        self.connector.set_api_token(api_token)
        
        success = self.connector.authenticate()
        
        return success
        
        
        