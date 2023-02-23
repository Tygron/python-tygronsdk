from typing import Type
import json

class EventParameter:

    def __init__( self, 
            arg_name:str, 
            arg_type:Type, 
            required:bool = True, 
            arg_default = None,
            aggregation = 0,
            
            api_description:str = None,
            api_type = None,
            api_required:bool = None,
            api_default = None,
            api_aggregation = 0,
        ):
        
        self._data = {
            'arg_name' : arg_name,
            'arg_type' : arg_type,
            'required' : required,
            'arg_default' : arg_default,
            'aggregation' : aggregation,
            
            'api_description' : api_description,
            'api_type' : api_type,
            'api_required' : api_required,
            'api_default' : api_default,
            'api_aggregation' : api_aggregation,
        }
    
    @property
    def arg_name( self ):
        return self._data['arg_name']
    @property
    def arg_type( self ):
        return self._data['arg_type']
    @property
    def required( self ):
        return self._data['required']
    @property
    def arg_default( self ):
        return self._data['arg_default']
    @property
    def aggregation( self ):
        return self._data['aggregation']
    
    @property
    def api_description( self ):
        return self._data['api_description']
    @property
    def api_type( self ):
        return self._data['api_type']
    @property
    def api_required( self ):
        return self._data['api_required']
    @property
    def api_default( self ):
        return self._data['api_default']
    @property
    def api_aggregation( self ):
        return self._data['api_aggregation']
    
    @property
    def data( self ):
        return { **self._data }
    
    
    def validate( self, value, aggregation=0 ):
        if ( type(value) is list and aggregation < self.aggregation ):
            for entry in value:
                self.validate(entry, aggregation = aggregation+1 )
            return value
            
        if ( value == None and (self.arg_default == None) and self.required):
            raise TypeError( self.arg_name + ' is a required parameter' )
        if ( value == None ):
            return self.arg_default
        return value
        
    
    
    def __str__( self ):
        data = { index: str(d) for index, d in self._data.items() }
        return json.dumps( data )