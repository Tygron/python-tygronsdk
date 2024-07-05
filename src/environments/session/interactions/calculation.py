from ..connectors import Connector
from ..data.items import Item
from .items import Items
from .... import utilities

class Calculation:

    @staticmethod
    def recalculate( conn:Connector, reset = False, scheduled = False, timeout_in_seconds:int = None, scheduled_timeout_in_seconds:int = None, wait_until_scheduled:bool = True ):
            
        for index, reset_x in enumerate( utilities.lists.coerce(reset) ):
            scheduled_x = utilities.lists.get(utilities.lists.coerce(scheduled), index, False)
            
            recalculation_timestamp_in_seconds=(utilities.timing.get_timestamp_seconds()+60)
            if ( scheduled_x == True ):
                        Calculation.recalculate_scheduled( conn, 
                        recalculation_timestamp_in_seconds  =   recalculation_timestamp_in_seconds, 
                        wait_until_scheduled                =   wait_until_scheduled, 
                        timeout_in_seconds                  =   scheduled_timeout_in_seconds or timeout_in_seconds or 3600
                    )
            else:
                    Calculation.recalculate_direct( conn, 
                        reset               = reset_x, 
                        timeout_in_seconds  = timeout_in_seconds or 600
                    )
    
    
    
    @staticmethod
    def recalculate_scheduled( conn:Connector, recalculation_timestamp_in_seconds:int = None, wait_until_scheduled = True, timeout_in_seconds:int = 3600 ):
        response = None
        try:
            response = conn.request(
                    method='POST',
                    url='event/editorsetting/set_scheduled_update',
                    data=[ recalculation_timestamp_in_seconds*1000 ],
                    timeout=min(timeout_in_seconds, 60)
                )
                #Explicitly setting a maximum timeout of 1 minute here, to prevent unreasonable waits and request timeouts
        except Exception as err:
            raise err
            
        if (wait_until_scheduled):
            response = Calculation.wait_for_recalculate( conn, timeout_in_seconds, wait_until_scheduled )
        return response
    
    @staticmethod
    def recalculate_direct( conn:Connector, reset: bool = True, timeout_in_seconds:int = 600 ):
        response = None
        try:
            response = conn.request(
                    method='POST',
                    url='event/editorindicator/reset_indicators',
                    data=[ reset ],
                    timeout=min(timeout_in_seconds, 60)
                )
                #Explicitly setting a maximum timeout of 1 minute here, to prevent unreasonable waits and request timeouts
        except Exception as err:
            #When dealing with long-running calculations, wait for beyond whatever intermediate timeout exists
            #TODO: Explicitly check whether the error was a timeout
            response = Calculation.wait_for_recalculate( conn, timeout_in_seconds, False )
        return response
    
    
    
    @staticmethod
    def check_awaiting_scheduled_calculation( conn: Connector, timeout_in_seconds=60 ):
        response_scheduled_time = Items.get( conn, 'Setting', 'SCHEDULED_UPDATE' )
        if ( response_scheduled_time is None):
            raise Exception('SCHEDULED_UPDATE setting not found')
        if (not response_scheduled_time.value == ''):
            return response_scheduled_time.value;
        return False
    
    
    
    @staticmethod
    def check_done_recalculating( conn:Connector, timeout_in_seconds:int = 600, wait_for_scheduled=False ):
        try:
            if (wait_for_scheduled):
                response_scheduled_time = Calculation.check_awaiting_scheduled_calculation(conn, timeout_in_seconds)
                if (not response_scheduled_time == False):
                    return None
            
            response_reachable = conn.request(
                    method='POST',
                    url='update',
                    data={"SETTINGS":0},
                    timeout=timeout_in_seconds
                )
            if ( not response_reachable.is_success() ):
                raise Exception(response_reachable)
            return response_reachable.is_success()
            
        except Exception as err:
            raise err
    
    
    
    @staticmethod
    def wait_for_recalculate( conn:Connector, timeout_in_seconds:int = 600, wait_until_scheduled:bool = False ):
        def wait_function():
            try:
                response = Calculation.check_done_recalculating(conn, timeout_in_seconds, wait_until_scheduled)
                return response
            except Exception as err:
                try:
                    #Still calculating
                    if (err.args[0].get_http_status_code() == 504):
                        return None
                        
                    #Session does not exist (or no more)
                    elif (err.args[0].get_http_status_code() == 497):
                        raise err
                    
                    #Special rule for unresponsive (but working) sessions
                    elif (err.args[0].get_http_status_code() == 'TIMEOUT'):
                        return None
                        
                except Exception as e:
                    pass
                raise err
            
        return utilities.timing.wait_for( wait_function, timeout_in_seconds=timeout_in_seconds )