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
    def maplink_from( obj ):
        if ( isinstance(obj, str) ):
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
            if (self._data.get('maquetteOverride', None) != None):
                if (self._data['maquetteOverride'].get(attribute, None) != None):
                    value = self._data['maquetteOverride'][attribute]
        if ( include_attribute ):
            if (value == None):
                if (self._data.get('attributes', None)  != None):
                    if (self._data['attributes'].get(attribute, None) != None):
                        value = self._data['attributes'][attribute]
        if ( value == None ):
            return 0 if default_zero else None
        if ( isinstance(value, list) and first_only ):
            return value[0]
        return value