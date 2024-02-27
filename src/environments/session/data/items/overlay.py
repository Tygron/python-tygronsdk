from . import Item

class Overlay(Item):

    ATTRIBUTE_TIMEFRAMES = 'TIMEFRAMES'
    
    TYPE_RESULT_CHILD = 'RESULT_CHILD'
  
    @property
    def overlay_type(self):
        return self._data.get( 'type', None )
    @property
    def parent_id(self):
        return self._data.get( 'parentID', None )  

       
    
    def get_controlling_overlay_id( self ):
        if ( self.overlay_type == self.TYPE_RESULT_CHILD ):
            return self.parent_id
        return self.id
    
    def get_timeframes( self ):
        by_attribute_length = {
                'HEAT_STRESS' : 'DATES'
            }.get(self.overlay_type, None)
        if ( not by_attribute_length is None ):
            return self.get_attribute_length( attribute=by_attribute_length, include_attribute=True, include_maquette=False)
    
        by_attribute_value = {
                'AVG' : 'ATTRIBUTE_TIMEFRAMES',
            }.get(self.overlay_type, Overlay.ATTRIBUTE_TIMEFRAMES)
        if ( not by_attribute_value is None ):
            return self.get_attribute_value( attribute=by_attribute_value, include_attribute=True, include_maquette=False, first_only=True, default_zero=True)
                
        raise Exception( 'No (known) timeframes attribute exists for Overlay ' + self.get_printable_id() )
        
        
    def get_timeframe( self, index:int = -1 ):
        timeframes = self.get_timeframes( )
        if ( timeframes == None ):
            raise Exception( 'No (known) timeframes attribute exists for Overlay ' + self.get_printable_id() )
            
        if ( index < 0 ):
            target_timeframe = timeframes + index
        else:
            target_timeframe = index
        if ( target_timeframe < 0):
            raise Exception( 'Timeframe at index ' + str(index) + ' comes out to '+str(target_timeframe)+' before first timeframe at index 0 for Overlay ' + self.get_printable_id() )
        if ( target_timeframe >= timeframes):
            raise Exception( 'Timeframe at index ' + str(index) + ' comes out to '+str(target_timeframe)+' after last timeframe at index ' + (str(timeframes-1)) + ' for Overlay ' + self.get_printable_id() )
        return int(target_timeframe)
    
    def get_timeframes_range( self, indexes = True ):
        timeframes = []
        number_of_timeframes = self.get_timeframes()
        if (number_of_timeframes is None):
            raise Exception( 'Unable to establish timeframes range for Overlay '+self.get_printable_id()+', of type '+overlay_type )
        
        number_of_timeframes = int(number_of_timeframes)
        
        if ( indexes is True ):
            timeframes = list(range(0, number_of_timeframes))
        elif ( isinstance(indexes, int) ):
            timeframes = self.get_timeframe(indexes)
        elif ( isinstance(indexes, list) ):
            for index in indexes:
                if ( not isinstance(index, int) ):
                    continue
                timeframes.append( self.get_timeframes_range(index) )
        else:
            raise Exception( 'Unable to parse desired indexes: '+str(indexes) )
        return timeframes