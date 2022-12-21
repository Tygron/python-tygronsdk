from . import Item

class Stakeholder(Item):
    
    @property
    def active(self):
        return self._data.get( 'active', self._data.get( 'human', None ) )