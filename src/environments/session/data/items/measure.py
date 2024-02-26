from . import Item

class Measure(Item):

    @property
    def building_ids(self):
        return self._data.get( 'buildingIDs', None )

    @property
    def center(self):
        return self._data.get( 'center', None )
        
    @property
    def client_action_events(self):
        return self._data.get( 'clientActionEvents', None )
        
    @property
    def server_action_events(self):
        return self._data.get( 'serverActionEvents', None )
        
    @property
    def leveel_spatials(self):
        return self._data.get( 'leveeSpatials', None )
        
    @property
    def terrain_spatials(self):
        return self._data.get( 'terrainSpatials', None )
        
    @property
    def upgrade_spatials(self):
        return self._data.get( 'upgradeSpatials', None )
        
        
    @property
    def state(self):
        return self._data.get( 'state', None )
        
    @property
    def owner_id(self):
        return self._data.get( 'ownerID', None )