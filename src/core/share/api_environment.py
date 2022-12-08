from ..core import ApiEnvironment as CoreApiEnvironment

class ApiEnvironment(CoreApiEnvironment):

    def __init__( self, settings = {}, **kwargs ):
        super().__init__( settings = settings )
        self.module
        self.connector
        
    def authenticate( self, authentication_details: dict = {}, **kwargs ) -> bool:
        auth_details = { **authentication_details, **kwargs }
        pass