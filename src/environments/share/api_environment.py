from ...core import ApiEnvironment as CoreApiEnvironment

class ApiEnvironment(CoreApiEnvironment):

    def __init__( self, settings = {}, module = None, module_version:str = '' ):
        self._settings = settings
        self.module = module
        self.generate_module_references(self.module, module_version)
        
    def authenticate( self, authentication_details: dict = {}, **kwargs ) -> bool:
        auth_details = { **authentication_details, **kwargs }
        pass