from ..core.connectors import ConnectorTygronSession
from ..utilities.timing import Timing


class Creation:

    @staticmethod
    def generate_map( conn_session: ConnectorTygronSession, size_x: int, size_y: int, location_x: float, location_y: float, polygon = None, timeout_in_seconds:int = 600  ):
        
        response = conn_session.request(
                method='POST',
                url='event/editor/clear_map', 
                data=[ True ]
            )
        response = conn_session.request(
                method='POST',
                url='event/editor/set_initial_map_size', 
                data=[ size_x, size_y ]
            )
        response = conn_session.request(
                method='POST',
                url='event/editor/start_map_creation', 
                data=[ location_x, location_y, polygon ]
            )
            
        err_count = Creation.wait_for_map_generation( conn_session, timeout_in_seconds )
        
        if (err_count == -1):
            raise Exception('Project generation did not start') 
        if (err_count > 0):
            raise Exception('Project generation experienced '+count+ ' errors') 
        
        return
 
    @staticmethod   
    def wait_for_map_generation( conn_session: ConnectorTygronSession, timeout_in_seconds:int = 600  ):
        
        def wait_function():
            progress_items = conn_session.request(
                    method='GET',
                    url='items/progress'
                ).get_response_body_json()
            if  (len(progress_items) == 0):
                return -1
            
            last_item = progress_items[-1]
            if (last_item['progress'] < 1):
                return None
            failed_progress_count = len( [elem for elem in progress_items if (not elem['failText'] == '')] )
            return failed_progress_count
            
        return Timing.wait_for( wait_function, timeout_in_seconds=timeout_in_seconds )