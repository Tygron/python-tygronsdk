from .event_parameter_listable import EventParameterListable
from typing import Type

class EventParameterMatrixable(EventParameterListable):
        
    def __init__( self, *args, **kwargs ):
        super().__init__( *args, **{**kwargs, 'aggregation':2} )
        
    def validate( self, value ):
        if ( type(value) == list ):
            for entry in value:
                super().validate(value)
            return value
        else:
            return super().validate(value)