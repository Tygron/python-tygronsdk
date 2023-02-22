from .event_parameter import EventParameter

from typing import Type
from typing import List

import inspect

class Event():

    def __init__( self, event_domain:str = '', event_name:str = '', parameters:List[EventParameter] = [] ):
        super().__init__()
        self.event_name = str(event_name).lower()
        self.event_domain = str(event_domain).lower()
        self.parameters = parameters
        self.arguments = None;
        
    @staticmethod
    def generate_path( event_domain, event_name ):
        return str(event_domain + '/'+event_name).lower()
    
    def set_arguments( self, *args, **kwargs ):
        arguments = []
        for index, param in enumerate(self.parameters):
            arg = None if len(args) <= index else args[index]
            if ( (not (arg == None)) and hasattr(kwargs,param.arg_name) ):
                raise Exception( param.arg_name + ' already provided by positional argument')
            arg = kwargs.get(param.arg_name, arg)
            arguments.append( param.validate(arg) )
        self.arguments = arguments

    def get_arguments( self, mapped:bool = False ):
        if ( not mapped ):
            return [] if self.arguments is None else self.arguments
        parameters_arguments_map = {}
        for index, param in enumerate(self.parameters):
            arg = None
            if ( self.arguments == None ):
                pass
            elif ( len(self.arguments) <= index ):
                pass
            else:
                arg = self.arguments[index] 
            parameters_arguments_map[param.arg_name] = arg
        return parameters_arguments_map

    def get_path( self ):
        return self.generate_path(self.event_domain, self.event_name)
    
    
    def __call__( self, *args, **kwargs ):
        self.set_arguments(*args, **kwargs)
        return self
    
    def __str__( self ):
        return 'Event:' + self.get_path() + ' - ' + str(self.get_arguments(True))