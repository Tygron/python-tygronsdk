

class Item():

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
    
    def get_attribute_value( self, attribute: str, include_attribute: bool = True, include_maquette:bool = True, first_only: bool = False, default_zero: bool = True ):
        value = None
        if ( include_maquette ):
            if self.data.get('maquetteOverride', False)  != False:
                if self.data['maquetteOverride'].get(attribute, False) != False:
                    value = self.data['maquetteOverride'][attribute]
        if ( include_attribute ):
            if (value == None):
                if self.data.get('attributes', False)  != False:
                    if self.data['attributes'].get(attribute, False) != False:
                        value = self.data['attributes'][attribute]
        if ( value == None ):
            return 0 if default_zero else None
        if ( isinstance(value, list) and first_only ):
            return value[0]
        return value