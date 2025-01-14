from ..... import utilities

class MaintenanceWindowData:
    
    def __init__( self, data = {}, **kwargs ):
        if ( isinstance(data,list) ):
            data = {
                'window_start': int(data[0]),
                'window_end': int(data[1]),
            }
        self._data = { **data, **kwargs }
    
    def __str__(self):
        if not self.is_set():
            return 'No maintenance window set'
        return 'Maintenance window from {start} until {end}, for a duration of {duration} seconds'.format(
                start=utilities.timing.get_readable_time(self.start_in_seconds),
                end=utilities.timing.get_readable_time(self.end_in_seconds),
                duration=self.duration_in_seconds,
            )
            
    @property
    def start_in_seconds(self):
        return self._data.get('window_start')/1000
    
    @property
    def end_in_seconds(self):
        return self._data.get('window_end')/1000
    
    @property
    def duration_in_seconds(self):
        return self.end_in_seconds - self.start_in_seconds
        
    def is_set(self):
        return (self.start_in_seconds > 0) and (self.end_in_seconds > 0)
        
    def time_to_start_in_seconds(self, current_time_in_seconds:int = None):
        if ( current_time_in_seconds is None ):
            current_time_in_seconds = utilities.timing.get_timestamp_seconds()
        return self.start_in_seconds - current_time_in_seconds
    
    def time_to_end_in_seconds(self, current_time_in_seconds:int = None):
        if ( current_time_in_seconds is None ):
            current_time_in_seconds = utilities.timing.get_timestamp_seconds()
        return self.end_in_seconds - current_time_in_seconds
            
        
    def is_upcoming(self, current_time_in_seconds:int = None, look_ahead_in_seconds:int = None):
        time_to_window = self.time_to_start_in_seconds(current_time_in_seconds)
        if ( look_ahead_in_seconds is None ):
            return time_to_window > 0
        else:
            return (time_to_window > 0) and (time_to_window < look_ahead_in_seconds)
            
    def is_completed(self, current_time_in_seconds:int = None):
        time_to_window_end = self.time_to_end_in_seconds(current_time_in_seconds)
        return time_to_window_end < 0
        
    def is_upcoming_or_active(self, current_time_in_seconds:int = None, look_ahead_in_seconds:int = None):
        return self.is_upcoming(current_time_in_seconds, look_ahead_in_seconds) or self.is_completed(current_time_in_seconds)
    