from typing import Type

class EventParameter:

    def __init__( self, arg_name:str, arg_type:Type, required:bool = True, arg_default = None ):
        self.arg_name = arg_name
        self.arg_type = arg_type
        self.required = required
        self.arg_default = arg_default
        
    def validate( self, value ):
        if ( value == None and (self.arg_default == None) and self.required):
            raise TypeError( self.arg_name + ' is a required parameter' )
        if ( value == None ):
            return self.arg_default
        return value