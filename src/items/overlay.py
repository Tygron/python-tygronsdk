from .item import Item

class Overlay(Item):

    ATTRIBUTE_TIMEFRAMES = 'TIMEFRAMES'
    
    TYPE_RESULT_CHILD = 'RESULT_CHILD'

    def __init__( self, data = {} ):
        super().__init__( data )
        return
    

    
    def get_overlay_type( self ):
        return self.data.get( 'type', None )
        
    def get_parent_id( self ):
        return self.data.get( 'parentID', None )
    
    
    
    def get_controlling_overlay_id( self ):
        if ( self.get_overlay_type() == self.TYPE_RESULT_CHILD ):
            return self.get_parent_id()
        return self.get_id()
    
    def get_timeframes( self ):
        timeframes = self.get_attribute_value( 
                self.ATTRIBUTE_TIMEFRAMES, 
                first_only = True,
                default_zero = False
           )
        return int(timeframes) if not timeframes == None else None
        
    def get_timeframe( self, index: int = -1 ):
        timeframes = self.get_timeframes( )
        if ( timeframes == None ):
            raise Exception( 'No ' + self.ATTRIBUTE_TIMEFRAMES + ' attribute exists for Overlay ' + self.get_printable_id() )
            
        if ( index < 0 ):
            target_timeframe = timeframes + index
        else:
            target_timeframe = index
        if ( target_timeframe < 0):
            raise Exception( 'Timeframe at index ' + str(index) + ' comes out to '+str(target_timeframe)+' before first timeframe at index 0 for Overlay ' + self.get_printable_id() )
        if ( target_timeframe >= timeframes):
            raise Exception( 'Timeframe at index ' + str(index) + ' comes out to '+str(target_timeframe)+' after last timeframe at index ' + (str(timeframes)-1) + ' for Overlay ' + self.get_printable_id() )
        return int(target_timeframe)