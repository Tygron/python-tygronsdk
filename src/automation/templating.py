from ..connectors import ConnectorTygronSession, ConnectorTygronApi

from typing import Callable
import time

class Templating:

    def __init__( self ):
        #super().__init__();
        return;





    def save_project_as( self, conn_api: ConnectorTygronApi, session_id: int, domain: str, project_name: str, clear_map: bool = False ):
        attempts = 25
        last_err = None
        for i in range(attempts):
            attempt_name = project_name + ('' if i==0 else '-'+str(i))
            try:
                response = conn_api.request(
                    method='POST',
                    url='event/io/save_project_as',
                    data=[ session_id, domain, attempt_name, clear_map ]
                )
                if response.is_success():
                    return attempt_name
            except Exception as err:
                last_err = err
                continue
        raise last_err
            
    def delete_project( self, conn_api: ConnectorTygronApi, project_name: str ):
    
        return None

    def generate_map( self, conn_session: ConnectorTygronSession, size_x: int, size_y: int, location_x: float, location_y: float, polygon = None ):
        
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
            
        err_count = self.wait_for_project_generation( conn_session )
        
        if (err_count == -1):
            raise Exception('Project generation did not start') 
        if (err_count > 0):
            raise Exception('Project generation experienced '+count+ ' errors') 
        
        return
    
    def wait_for_project_generation( self, conn_session: ConnectorTygronSession ):
        
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
            
        return self.wait_for( wait_function )
     



     
    def recalculate( self, conn_session: ConnectorTygronSession, reset: bool = True ):
        conn_session.request(
                method='POST',
                url='event/editorindicator/reset_indicators',
                data=[ reset ]
            )
        return self.wait_for_recalculate( conn_session )
     
    def wait_for_recalculate( self, conn_session: ConnectorTygronSession ):
        def wait_function():
            try:
                response = conn_session.request(
                        method='POST',
                        url='update',
                        data={"SETTINGS":0}
                    )
                return response.is_success()
            except Exception as err:
                if (err.arg[0].get_http_status_code == 504):
                    return None
                raise err
            
        return self.wait_for( wait_function )
    



    
    def wait_for( self, wait_function: Callable, interval_in_seconds: int = 5 ):
        result = None
        while( result == None ):
            time.sleep(interval_in_seconds)
            try:
                result = wait_function()
            except Exception as err:
                raise err
        return result
        