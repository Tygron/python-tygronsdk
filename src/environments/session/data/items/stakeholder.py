from . import Item

class Stakeholder(Item):

    def __init__( self, data = {} ):
        super().__init__( data )
        return
    
    @property
    def active(self):
        return self._data.get( 'active', self._data.get( 'human', None ) )