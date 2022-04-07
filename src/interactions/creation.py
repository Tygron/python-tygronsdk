from ..core.connectors import ConnectorTygronSession
from ..interactions.session import Session
from ..utilities.timing import Timing


class Creation:

    @staticmethod
    def generate_map( conn_session: ConnectorTygronSession, size_x: int, size_y: int, location_x: float, location_y: float, polygon = None, timeout_in_seconds:int = 600  ):
        
        
        response = conn_session.request(
                method='POST',
                url='event/editor/clear_map', 
                data=[ True ]
            )
        if ( not response.is_success() ):
            raise Exception('Could not clear map', response)
        response = conn_session.request(
                method='POST',
                url='event/editor/set_initial_map_size', 
                data=[ size_x, size_y ]
            )
        if ( not response.is_success() ):
            raise Exception('Could not set initial map size', response)
        response = conn_session.request(
                method='POST',
                url='event/editor/start_map_creation', 
                data=[ location_x, location_y, polygon ]
            )
        if ( not response.is_success() ):
            raise Exception('Could not start map generation', response)
        
        err_count = Creation.wait_for_map_generation( conn_session, timeout_in_seconds )
        
        if (err_count == -1):
            raise Exception('Project generation did not start') 
        if (err_count > 0):
            raise Exception('Project generation experienced '+count+ ' errors') 
        
        return
 
    @staticmethod   
    def wait_for_map_generation( conn_session: ConnectorTygronSession, timeout_in_seconds:int = 600  ):
        
        def wait_function():
            Session.ping_session( conn_session )
            
            progress_items = []   
            
            try:
                response = conn_session.request(
                        method='GET',
                        url='items/progress'
                    )
             
                if ( not response.is_success() ):
                    raise Exception(response)
            except Exception as err:
                try:
                    #Calculating
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
                
            progress_items = response.get_response_body_json()
            if  (len(progress_items) == 0):
                return -1
            
            last_item = progress_items[-1]
            if (last_item['progress'] < 1):
                return None
            failed_progress_count = len( [elem for elem in progress_items if (not elem['failText'] == '')] )
            return failed_progress_count
            
        return Timing.wait_for( wait_function, timeout_in_seconds=timeout_in_seconds )