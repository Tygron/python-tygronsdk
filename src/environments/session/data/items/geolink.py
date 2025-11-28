from . import Item

class Geolink(Item):
   
    @property
    def matchings(self):
        return self._data.get( 'attributes', {} ) | self._data.get( 'matchings', {} )
    @property
    def mappings(self):
        return self._data.get( 'mapping', {} ) | self._data.get( 'mappings', {} )
    @property
    def additionals(self):
        return self._data.get( 'additionals', {} )
    
    @property
    def function_id(self):
        return self._data.get( 'functionID', Item.NONE )
        
    @property
    def priority(self):
        return self._data.get( 'priority', None )
        
    @property
    def geo_mode(self):
        return self._data.get( 'geomMode', None )
    @property
    def point_buffer(self):
        return self._data.get( 'pointBuffer', None )
    @property
    def line_buffer(self):
        return self._data.get( 'lineBuffer', None )
        