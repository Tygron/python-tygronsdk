from . import EnvironmentEventWrapper

import inspect

class EnvironmentEventSetWrapper():

    def __init__( self, events_set, connector = None, settings = {}, storage = {} ):
        self._events = events_set
        self._connector = connector
        self._settings = settings
        self._storage = storage
        
    def __getattr__( self, event_name ):
        event_data = self._events.get_definition( name=event_name )

        if event_data is None:
            raise TypeError('No event of type '+str(event_name))

        settings = self._settings
        storage = self._storage
        
        return EnvironmentEventWrapper(
            event = event_data,
            connector = self._connector,
            settings = self._settings,
            storage = self._storage
        )