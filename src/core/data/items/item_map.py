from .item import Item

from typing import Type

class ItemMap():


    def __init__( self, data = {}, as_items:bool = True, as_item:Type[Item] = None ):
        super().__init__()
        self._data = {}
        self._size = 0
        self._count = 0
        
        self._as_items = as_items or as_item != None
        self._item_type = as_item if as_item != None else Item
        
        self.set_data(data)
        
        return
        
    def set_data( self, data = {} ):
        if ( isinstance(data, list) ):
            list_data = data
            data = {}
            if ( self._as_items ):
                for entry in list_data:
                    data[int(entry['id'])] = self._item_type(entry)
            else:
                for entry in list_data:
                    data[int(entry['id'])] = entry
        elif ( isinstance(data, dict) ):
            pass
         
        self._data.update(data)
        
    def get_data( self ):
        return self._data
        
    def get( self, item_id: int = None):
        if ( item_id is None or item_id is Item.NONE ):
            return None
        return self._data.get( int(item_id), None )
    
    def size( self ):
        # size method mirrors Tygron's internal implementation of item maps
        if ( len(self._data.keys()) == 0 ):
            return 0
        return max( self._data.keys() )+1
    def count( self ):
        # count method returns the actual amount of objects stored in the item_map
        return sum(1 for e in self._data.items() if e)
        
    
    def __iter__( self ):
        return ItemMapIterator( self )
       
       
       
       
       
class ItemMapIterator:
    def __init__( self, item_map ):
        self._item_map = item_map
        self._index = 0

    def __iter__( self ):
        return self
    
    def __next__( self ):
        while ( self._index <= self._item_map.size() ):
            result = self._item_map.get( self._index )
            self._index+=1
            if ( result ):
                return result
        raise StopIteration