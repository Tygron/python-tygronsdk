import inspect
from ..data.items import ItemMap

class EnvironmentInteractionWrapper():
    
    def __init__( self, interactions_module, connector, settings = {}, storage = {} ):
        self._connector = connector
        self.interactions_module = interactions_module
        self._settings = settings
        self._storage = storage
        
    def __getattr__( self, function_name ):
        function = getattr(self.interactions_module, function_name)
        settings = self._settings
        storage = self._storage
        
        def wrapper_function( *args, **kwargs ):

            args = [self._connector, *args]
            kwargs = {**settings, **kwargs}
            
            all_args = list(inspect.signature(function).parameters.keys())
            remaining_args = all_args[len(args):] if len(all_args) > len(args) else []
            
            kwarg_key_set = set(remaining_args) & set(kwargs.keys())
            kwargs = {k: kwargs[k] for k in kwarg_key_set}
            
            result = function( *args, **kwargs )
            
            return result
                
        return wrapper_function
    