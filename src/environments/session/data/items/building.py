from . import Item

class Building(Item):

    @property
    def address_ids(self):
        return self._data.get( 'addressIDs', [] )
        
    @property
    def center(self):
        return self._data.get( 'center', None )
    @property
    def custom_geometries(self):
        return self._data.get( 'customGeometries', None )
    @property
    def demolisher_id(self):
        return self._data.get( 'demolisherID', Item.NONE )
    @property
    def function_id(self):
        return self._data.get( 'functionID', None )
        
    @property
    def measure_id(self):
        return self._data.get( 'measureID', Item.NONE )
        
    @property
    def model_version(self):
        return self._data.get( 'modelVersion', Item.NONE )
        
    @property
    def override_categories(self):
        return self._data.get( 'overrideCategories', None )
        
    @property
    def override_decals(self):
        return self._data.get( 'overrideDecals', None )
        
    @property
    def owner_id(self):
        return self._data.get( 'ownerID', Item.NONE )
        
    @property
    def permit_received(self):
        return self._data.get( 'permitReceived', None )
        
    @property
    def predecessor_id(self):
        return self._data.get( 'predecessorID', Item.NONE )
        
    @property
    def sections(self):
        return self._data.get( 'sections', [] )
        
    @property
    def source_ids(self):
        return self._data.get( 'sourceIDs', [] )
        
    @property
    def state(self):
        return self._data.get( 'state', 'NOTHING' )
        
    @property
    def upgrade_id(self):
        return self._data.get( 'upgradeID', Item.NONE )
        
    @property
    def upgrade_owner_id(self):
        return self._data.get( 'upgradeOwnerID', Item.NONE )
