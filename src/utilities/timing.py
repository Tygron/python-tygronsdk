from typing import Callable
import time
import math


class Timing:

    @staticmethod
    def wait_for( wait_function: Callable, interval_in_seconds: int = 5, timeout_in_seconds: int = 300 ):
        result = None
        start_time = Timing.get_timestamp_seconds()
        while( result == None ):
            time.sleep(interval_in_seconds)
            try:
                result = wait_function() 
            except Exception as err:
                raise err
            if ( Timing.time_passed(start_time, time=timeout_in_seconds) ):
                raise Exception( 'Timeout after waiting for '+str(Timing.time_passed(start_time)) )
        return result

    @staticmethod
    def get_timestamp(milliseconds:bool):
        return Timing.get_timestamp_seconds() if not milliseconds else Timing.get_timestamp_milliseconds()
    
    @staticmethod
    def get_timestamp_seconds():
        return int( time.time() )

    @staticmethod        
    def get_timestamp_milliseconds():
        return int( math.ceil(time.time() * 1000) )
        
    @staticmethod
    def time_passed( start_time:int, time:int = None, milliseconds:bool = False ):
        time_remaining = Timing.time_remaining(start_time, time=time, milliseconds=milliseconds)
        now = Timing.get_timestamp_seconds() if not milliseconds else Timing.get_timestamp_milliseconds()
        if ( time == None ):
            return -(time_remaining)
        else:
            return time_remaining <= 0

    @staticmethod
    def time_remaining( start_time:int, time:int = 0, milliseconds:bool = False ):
        now = Timing.get_timestamp(milliseconds)

        return (start_time - now) + ( 0 if (time == None) else time )
            