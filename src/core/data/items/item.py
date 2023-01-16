import inspect

class Item():

    #constant for reference to no other item
    NONE = -1;

    def __init__( self, data = {} ):
        super().__init__()
        self.set_data(data)
        return
    
    #Item type management
    
    @staticmethod
    def maplink_from( obj, assume_string_singular:bool = None ):
        if ( isinstance(obj, str) ):
            if ( assume_string_singular is False):
                return obj
            if ( assume_string_singular is True or (not (obj[-1].lower() == 's')) ):
                return obj+'s'
            return obj
        if ( inspect.isclass(obj) and issubclass(obj, Item) ):
            return obj.get_item_maplink()
        if ( isinstance(obj, Item) ):
            return obj.get_item_maplink()
        raise Exception( 'Could not obtain maplink from object of type '+type(obj) )
    
    @classmethod
    def get_item_type( cls ):
        return cls.__name__
        
    @classmethod
    def get_item_maplink( cls ):
        return cls.__name__ + 's'
        
    #Generic property management  
 
    def __getattr__(self, attr):
        if ( attr in self._data ):
            return self._data.get(attr)
        raise AttributeError( 'Item of type '+self.get_item_type()+' does not have a property named \''+str(attr)+'\'')
    
    def get(self, attr, default = None):
        if ( attr in self._data ):
            return self._data.get(attr)
        return default
    
    def set_data( self, data = {} ):
        if ( not '_data' in self.__dict__ ):
            self._data = {}
        self._data.update(data)
    
    def get_data( self ):
        return self._data
    
    #Baseline Item-specific attributes
    #   __getattr__ intended to capture any such specific properties automatically
    
    @property
    def id(self):
        return self._data.get( 'id', None )
    @property
    def version(self):
        return self._data.get( 'version', None )
        
    @property
    def name(self):
        return self._data.get( 'name', None )
    @property
    def active(self):
        return self._data.get( 'active', None )
        
    
    
    
    def get_printable_id( self ):
        return str(self.id) + ': ' + self.name
    
    def get_attribute_value( self, attribute: str, include_attribute: bool = True, include_maquette:bool = True, first_only: bool = False, default_zero: bool = True ):
        value = None
        if ( include_maquette ):
            if (not (self._data.get('maquetteOverride', None) is None)):
                if (not (self._data['maquetteOverride'].get(attribute, None) is None)):
                    value = self._data['maquetteOverride'][attribute]
        if ( include_attribute ):
            if (value == None):
                if (not (self._data.get('attributes', None) is None)):
                    if (not (self._data['attributes'].get(attribute, None) is None)):
                        value = self._data['attributes'][attribute]
        if ( value is None ):
            return 0 if default_zero else None
        if ( isinstance(value, list) and first_only ):
            return value[0]
        return value
    
    def get_attribute_length( self, attribute:str, include_attribute: bool = True, include_maquette:bool = True ):
        value = self.get_attribute_value(
                attribute = attribute,
                include_attribute = include_attribute,
                include_maquette = include_maquette,
                first_only = False,
                default_zero = False
            )
        if ( value is None):
            return 0
        if ( isinstance(value, list) ):
            return len(value)
        return 1