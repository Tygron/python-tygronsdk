

class Item():

    #constant for reference to no other item
    NONE = -1;

    def __init__( self, data = {} ):
        super().__init__()
        self.data = {}
        self.set_data(data)
        return
        
    def set_data( self, data = {} ):
        self.data.update(data)
    
    def get_data( self ):
        return self.data
    
    def get_id( self ):
        return self.data.get( 'id', None )
    
    def get_name( self ):
        return self.data.get( 'name', None )
    
    
    
    
    def get_printable_id( self ):
        return str(self.get_id()) + ': ' + self.get_name()
    
    def get_attribute_value( self, attribute: str, include_attribute: bool = True, include_maquette:bool = True, first_only: bool = False, default_zero: bool = True ):
        value = None
        if ( include_maquette ):
            if (self.data.get('maquetteOverride', None) != None):
                if (self.data['maquetteOverride'].get(attribute, None) != None):
                    value = self.data['maquetteOverride'][attribute]
        if ( include_attribute ):
            if (value == None):
                if (self.data.get('attributes', None)  != None):
                    if (self.data['attributes'].get(attribute, None) != None):
                        value = self.data['attributes'][attribute]
        if ( value == None ):
            return 0 if default_zero else None
        if ( isinstance(value, list) and first_only ):
            return value[0]
        return value