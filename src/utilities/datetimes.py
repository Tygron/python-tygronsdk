from datetime import datetime

from typing import Union

class Datetimes:
    
    @staticmethod
    def guess_is_timestamp_in_milliseconds( ts:int ):
        return ( ts > 10000000000 )
    
    @staticmethod
    def datetime_to_string_datetime( dt:Union[int,datetime] ):
        dt = Datetimes.timestamp_to_datetime(dt)
        return Datetimes.datetime_to_string(dt, '%Y-%m-%d %H:%M:%S')

    @staticmethod
    def datetime_to_string_date( dt:Union[int,datetime] ):
        dt = Datetimes.timestamp_to_datetime(dt)
        return Datetimes.datetime_to_string(dt, '%Y-%m-%d')
        
    @staticmethod
    def datetime_to_string_time( dt:Union[int,datetime] ):
        dt = Datetimes.timestamp_to_datetime(dt)
        return Datetimes.datetime_to_string(dt, '%H:%M:%S')
        
    @staticmethod
    def datetime_to_string( dt:Union[int,datetime], format:str = '%Y-%m-%d %H:%M:%S' ):
        dt = Datetimes.timestamp_to_datetime(dt)
        if ( dt == None ):
            return None
        return dt.strftime(format)
        
        
        
    @staticmethod
    def timestamp_to_datetime( ts:Union[int,datetime], millis:bool = None ):
        if ( isinstance(ts, datetime) ):
            return ts
        if ( ts is None ):
            return None
        if ( millis is None ):
            millis = Datetimes.guess_is_timestamp_in_milliseconds(ts)
        if ( millis ):
            ts = ts/1000
        return datetime.utcfromtimestamp(ts)