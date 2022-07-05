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
    def wait( interval_in_seconds: int = 5, wait_time: int = 300 ):
        start_time = Timing.get_timestamp_seconds()
        while( not Timing.time_passed(start_time, time=wait_time) ):
            time.sleep(interval_in_seconds)
        return True

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
    def get_readable_time( timestamp:int = None , time_format:str = '%Y-%m-%d %H-%M-%S'):
        if (timestamp == None):
            timestamp = Timing.get_timestamp_seconds()
        readable = time.strftime(time_format, time.localtime(timestamp))
        return readable
        
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
    
    '''
    Time formatting:
        https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
        https://stackabuse.com/how-to-format-dates-in-python/
        %a: Returns the first three characters of the weekday, e.g. Wed.
        %A: Returns the full name of the weekday, e.g. Wednesday.
        %B: Returns the full name of the month, e.g. September.
        %w: Returns the weekday as a number, from 0 to 6, with Sunday being 0.
        %m: Returns the month as a number, from 01 to 12.
        %p: Returns AM/PM for time.
        %y: Returns the year in two-digit format, that is, without the century. For example, "18" instead of "2018".
        %f: Returns microsecond from 000000 to 999999.
        %Z: Returns the timezone.
        %z: Returns UTC offset.
        %j: Returns the number of the day in the year, from 001 to 366.
        %W: Returns the week number of the year, from 00 to 53, with Monday being counted as the first day of the week.
        %U: Returns the week number of the year, from 00 to 53, with Sunday counted as the first day of each week.
        %c: Returns the local date and time version.
        %x: Returns the local version of date.
        %X: Returns the local version of time.
    '''