from ..core.connectors import ConnectorTygronSession
from ..utilities.timing import Timing

import json
import http.client

class Calculation:

    @staticmethod
    def recalculate( conn_session: ConnectorTygronSession, reset: bool = True, timeout_in_seconds:int = 600 ):
        response = None
        try:
            response = conn_session.request(
                    method='POST',
                    url='event/editorindicator/reset_indicators',
                    data=[ reset ]
                )
        except Exception as e:
            #When dealing with long-running calculations, wait for beyond whatever intermediate timeout exists
            #TODO: Explicitly check whether the error was a timeout
            response = Calculation.wait_for_recalculate( conn_session, timeout_in_seconds )
        return response
     
    def wait_for_recalculate( conn_session: ConnectorTygronSession, timeout_in_seconds:int = 600 ):
        def wait_function():
            try:
                response = conn_session.request(
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