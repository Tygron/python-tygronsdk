import tygronsdk
from ..utilities import init as init

class Script():
    
    def __init__( self ):
        self._logs = []
        self._print_log_function = print
    
    def start(self, **kwargs ):
        data = init.init_data( **kwargs )
        self.run( **data.data(data=True, credentials=True) )
        
    def run( self, **kwargs ):
        NotImplementedError( 'Script must implement run( self, **kwargs ) method' )
        
    def log(self, *args, sep=' ', end='\n', file=None, flush=False):
        message=sep.join([str(arg) for arg in args])+str(end)
        self._logs.append(message)
        if ( not (self._print_log_function is None) ):
            self._print_log_function(*args, sep=' ', end='\n', file=None, flush=False)
    def print(self, *args, sep=' ', end='\n', file=None, flush=False):
        self.log(self ,*args, sep=' ', end='\n', file=None, flush=False)
        
    def set_print_log_function( self, print_log_function:callable = None):
        self._print_log_function = print_log_function
        
        
