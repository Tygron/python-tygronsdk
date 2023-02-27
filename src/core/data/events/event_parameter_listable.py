from .event_parameter import EventParameter
from typing import Type

class EventParameterListable(EventParameter):
    
    def __init__( self, *args, **kwargs ):
        super().__init__(  *args, **{**kwargs, 'aggregation':1} )
    
    def validate( self, value ):
        if ( type(value) == list ):
            for entry in value:
                super().validate(value)
            return value
        else:
            return super().validate(value)