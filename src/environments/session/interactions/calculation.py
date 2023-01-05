from ..connectors import Connector
from ....utilities.timing import Timing

from datetime import datetime
from typing import List

class Calculation:

    @staticmethod
    def recalculate_multiple_times( conn:Connector, recalculations_sequence:List[bool] = [True, False], recalculations_scheduled = [], timeout_in_seconds:int = None):
        for index, recalculation_type in enumerate(recalculations_sequence):
            scheduled = False
            if ( isinstance(recalculations_scheduled, List) ):
                if ( (len(recalculations_scheduled) > index) and (recalculations_scheduled[index] == True) ):
                    scheduled = True
            if ( isinstance(recalculations_scheduled, bool) ):
                scheduled = recalculations_scheduled
                
            if ( scheduled ):
                Calculation.recalculate_scheduled( conn )
            else:
                if ( timeout_in_seconds == None ):
                    Calculation.recalculate( conn, recalculation_type )
                else:
                    Calculation.recalculate( conn, recalculation_type, timeout_in_seconds )
                

    @staticmethod
    def recalculate( conn:Connector, reset: bool = True, timeout_in_seconds:int = 600 ):
        response = None
        try:
            response = conn.request(
                    method='POST',
                    url='event/editorindicator/reset_indicators',
                    data=[ reset ],
                    timeout=min(timeout_in_seconds, 60)
                )
                #Explicitly setting a maximum timmeout of 1 minute here, to prevent unreasonable waits and request timeouts
        except Exception as err:
            #When dealing with long-running calculations, wait for beyond whatever intermediate timeout exists
            #TODO: Explicitly check whether the error was a timeout
            response = Calculation.wait_for_recalculate( conn, timeout_in_seconds )
        return response
    
    def recalculate_scheduled( conn:Connector, recalculation_timestamp_in_seconds:int = None ):
        raise Exception('Scheduled recalculations are not yet implemented')
    
    @staticmethod
    def wait_for_recalculate( conn:Connector, timeout_in_seconds:int = 600 ):
        def wait_function():
            try:
                response = conn.request(
                        method='POST',
                        url='update',
                        data={"SETTINGS":0}
                    )
                if ( not response.is_success() ):
                    raise Exception(response)
                return response.is_success()
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
            
        return Timing.wait_for( wait_function, timeout_in_seconds=timeout_in_seconds )