from ..connectors import Connector
from ..data import events, objects

from ..interactions.users import Users

from ....utilities.strings import Strings

import json

class Sessions:

    @staticmethod
    def get_joinable_sessions( conn:Connector ):
        response = conn.fire_event( 
            events.io.get_my_joinable_sessions (
            ) )
        sessions = [objects.SessionData(session) for session in response.get_response_body_json()]   
            
        return sessions
        
    
    @staticmethod
    def start_project_session( conn: Connector, project_name:str, session_type:str = 'EDITOR', session_language:str = None, session_id:int = None, group_token:str = None ):
        response = conn.fire_event( 
            events.io.start (
                session_type, project_name, session_language, session_id, group_token
            ) )
            
        return response.get_response_body_json()
        
    @staticmethod
    def join_project_session( conn: Connector, session_id:int, client_type:str = 'EDITOR', computer_name:str = None, client_token:str = None ):
        response = conn.fire_event( 
            events.io.join (
                session_id, client_type, computer_name, client_token
            ) )
        join_session_data = response.get_response_body_json()
        
        if ( isinstance(join_session_data, dict) ):
            join_session_data['session_id'] = session_id
            join_session_data['api_token'] = join_session_data['apiToken']
            
        return join_session_data
        
    @staticmethod
    def close_project_session( conn: Connector, session_id:int, client_token:str, keep_open:bool = False ):
        response = conn.fire_event( 
            events.io.close (
                session_id, client_token, keep_open
            ) )
            
        return response.get_response_body_json()
        
    @staticmethod
    def kill_project_session( conn: Connector, session_id:int ):
        response = conn.fire_event( 
            events.io.kill (
                session_id
            ) )
        return response.get_response_body_json()

    @staticmethod
    def create_new_project_from_template( conn: Connector, template_name:str, new_project_name:str, session_language:str = None, attempts:int = 25 ):
        session_id = Sessions.start_project_session(
                conn = conn,
                project_name = template_name,
                session_language = session_language
            )
        try:
            created_project_name = Sessions.save_project_as(
                    conn = conn,
                    session_id = session_id,
                    new_project_name = new_project_name,
                    clear_map = True,
                    attempts = attempts
                )
            join_session_data = Sessions.join_project_session(
                    conn = conn,
                    session_id = session_id
                )
            join_session_data['new_project_name'] = created_project_name

        except Exception as err:
            Sessions.kill_project_session(
                conn = conn,
                session_id = session_id
            )
            raise err
            
        return join_session_data
 
 
    @staticmethod
    def save_project_as( conn: Connector, session_id: int, new_project_name: str, clear_map: bool = False, attempts:int = 25 ):
        domain = Users.get_my_domain_name(conn)
        
        last_err = None
        for i in range(attempts):
            attempt_name = new_project_name + ('' if i==0 else '-'+str(i))
            try:
                response = conn.fire_event( 
                    events.io.save_project_as (
                        session_id, domain, attempt_name, clear_map
                    ) )
                    
                if response.is_success():
                    return attempt_name
                else:
                    raise Exception( response );
            except Exception as err:
                last_err = Exception('Could not set name: '+new_project_name+', with '+str(attempts)+' attempts', err )
                continue
        raise last_err
 
    @staticmethod
    def save_project( conn: Connector, session_id: int ):
        response = conn.fire_event( 
            events.io.save_project (
                session_id
            ) )
        return response
 
    @staticmethod
    def set_session_keep_alive( conn: Connector, session_id: int, keep_alive = True):
        mode = 'NONE'
        if ( keep_alive ):
            mode = 'SHORT'
        
        response = conn.fire_event( 
            events.io.save_project (
                session_id,
                mode
            ) )
        return response