from ..data.events import Event

class EnvironmentEventWrapper():

    def __init__( self, event:Event, connector = None, settings = None, storage = None):
        self._event = event
        self._connector = connector
        self._settings = settings
        self._storage = storage
    
    def execute( self, **kwargs ):
        return self._connector.fire_event(self._event, **kwargs)
    
    def __call__( self, *args, **kwargs ):
        return self._event if (not self._event( *args, **kwargs )) is self._event else self
        
    def __getattr__( self, attr ):
        return getattr( self._event, attr )
    
    def __str__( self ):
        return '(Wrapped) ' + str(self._event)