from . import Item

class Geoplugin(Item):
    
    @property
    def crs(self):
        return self._data.get( 'crs', None )
    
    @property
    def force_xy(self):
        return self._data.get( 'forceXY', None )
    
    @property
    def geolink_ids(self):
        return self._data.get( 'geoLinkIDs', [] )
    
    @property
    def id_attribute(self):
        return self._data.get( 'idAttribute', '' )
    
    @property
    def name_attribute(self):
        return self._data.get( 'nameAttribute', '' )
    
    @property
    def source_id(self):
        return self._data.get( 'sourceId', Item.NONE )
    
    @property
    def layer_name(self):
        return self._data.get( 'layerName', '' )
    
    @property
    def link_type(self):
        return self._data.get( 'linkType', None )
    
    @property
    def new_project(self):
        return self._data.get( 'newProject', None )