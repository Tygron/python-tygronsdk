from datetime import datetime


class Datetimes:
    
    def guess_is_timestamp_in_milliseconds( ts:int ):
        return ( ts > 10000000000 )
    
    @staticmethod
    def datetime_to_string_datetime( dt:datetime ):
        return Datetimes.datetime_to_string(dt, '%Y-%m-%d %H:%M:%S')

    @staticmethod
    def datetime_to_string_date( dt:datetime ):
        return Datetimes.datetime_to_string(dt, '%Y-%m-%d')
        
    @staticmethod
    def datetime_to_string_time( dt:datetime ):
        return Datetimes.datetime_to_string(dt, '%H:%M:%S')
        
    @staticmethod
    def datetime_to_string( dt:datetime, format:str = '%Y-%m-%d %H:%M:%S' ):
        if ( dt == None ):
            return None
        return dt.strftime(format)
        
        
        
    @staticmethod
    def timestamp_to_datetime( ts:int, millis:bool = None ):
        if ( ts == None ):
            return None
        if ( millis is None ):
            millis = Datetimes.guess_is_timestamp_in_milliseconds(ts)
        if ( millis ):
            ts = ts/1000
        return datetime.utcfromtimestamp(ts)