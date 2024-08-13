from ....core.interactions.interaction_set import InteractionSet

from ..connectors import Connector
from ..data import events, objects

from ..interactions.users import Users
from ..interactions.projects import Projects

from ....utilities.strings import Strings
from ....utilities.exceptions import Exceptions

import json

class Sessions(InteractionSet):

    @staticmethod
    def get_joinable_sessions( conn:Connector ):
        versioned_events = InteractionSet.versioned(conn, events)
        
        response = conn.fire_event( 
            versioned_events.io.get_my_joinable_sessions (
            ) )
        sessions = [objects.SessionData(session) for session in response.get_response_body_json()]   
            
        return sessions
    
    @staticmethod
    def get_joinable_session( conn:Connector, session_id:int = None ):
        sessions = Sessions.get_joinable_sessions(conn)
        
        for session in sessions:
            if (session.session_id == session_id):
                return session
        
    
    @staticmethod
    def start_project_session( conn: Connector, project_name:str, session_type:str = 'EDITOR', session_language:str = None, session_id:int = None, group_token:str = None ):
        versioned_events = InteractionSet.versioned(conn, events)
        
        response = conn.fire_event( 
            versioned_events.io.start (
                session_type, project_name, session_language, session_id, group_token
            ) )
            
        return response.get_response_body_json()
        
    @staticmethod
    def join_project_session( conn: Connector, session_id:int, client_type:str = 'EDITOR', computer_name:str = None, client_token:str = None ):
        versioned_events = InteractionSet.versioned(conn, events)
        
        response = conn.fire_event( 
            versioned_events.io.join (
                session_id, client_type, computer_name, client_token
            ) )
        join_session_data = response.get_response_body_json()
        
        if ( isinstance(join_session_data, dict) ):
            join_session_data['session_id'] = session_id
            join_session_data['api_token'] = join_session_data['apiToken']
            join_session_data['client_token'] = join_session_data['client']['clientToken']
            
        return join_session_data
        
    @staticmethod
    def close_project_session( conn: Connector, session_id:int, client_token:str, keep_open:bool = False, error_on_missing:bool = False ):
        versioned_events = InteractionSet.versioned(conn, events)
        
        if ( (not error_on_missing) and (Sessions.get_joinable_session(conn=conn, session_id=session_id) is None) ):
            return None
        response = conn.fire_event( 
            versioned_events.io.close (
                session_id, client_token, keep_open
            ) )
            
        return response.get_response_body_json()
        
    @staticmethod
    def kill_project_session( conn: Connector, session_id:int, error_on_missing:bool = False ):
        versioned_events = InteractionSet.versioned(conn, events)
        
        if ( (not error_on_missing) and (Sessions.get_joinable_session(conn=conn, session_id=session_id) is None) ):
            return None
        response = conn.fire_event( 
            versioned_events.io.kill (
                session_id
            ) )
        return response.get_response_body_json()

    @staticmethod
    def create_new_project_from_template( conn: Connector, template_name:str, new_project_name:str, session_language:str = None, attempts:int = 25 ):
        versioned_events = InteractionSet.versioned(conn, events)
        
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
    def create_new_project( conn: Connector, new_project_name:str, language:str = 'EN', high_detail:bool = True, attempts:int = 25 ):
        versioned_events = InteractionSet.versioned(conn, events)
        
        response = Projects.add_project(
                conn = conn,
                new_project_name = new_project_name, 
                language = language,
                high_detail = high_detail
            )
        created_project_name = response.file_name
        
        try:
            session_id = Sessions.start_project_session(
                    conn = conn,
                    project_name = response.file_name
                )
            try:    
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
        except Exception as err:
            Projects.delete_project(
                    conn = conn,
                    project_name = new_project_name
                )
            raise err
                
        return join_session_data
 
    @staticmethod
    def save_project_as( conn: Connector, session_id: int, new_project_name: str, clear_map: bool = False, attempts:int = 25 ):
        versioned_events = InteractionSet.versioned(conn, events)
        
        domain = Users.get_my_domain_name(conn)
        
        last_err = None
        for i in range(attempts):
            attempt_name = new_project_name + ('' if i==0 else str(i))
            try:
                response = conn.fire_event( 
                    versioned_events.io.save_project_as (
                        session_id, domain, attempt_name, clear_map
                    ) )
                    
                if response.is_success():
                    return attempt_name
                else:
                    raise Exception( response );
            except Exception as err:
                last_err = Exception('Could not set name: '+new_project_name+', with '+str(attempts)+' attempts', Exceptions.stringify(err) )
                continue
        raise last_err
 
    @staticmethod
    def save_project( conn: Connector, session_id: int ):
        versioned_events = InteractionSet.versioned(conn, events)
        
        response = conn.fire_event( 
            versioned_events.io.save_project (
                session_id
            ) )
        return response
 
    @staticmethod
    def set_session_keep_alive( conn: Connector, session_id: int, keep_alive = 'SHORT'):
        versioned_events = InteractionSet.versioned(conn, events)
        
        mode = keep_alive
        if (keep_alive is True):
            mode = 'SHORT'
        elif (keep_alive is False):
            mode = 'NEVER'
    
        response = conn.fire_event( 
            versioned_events.io.set_session_keep_alive (
                session_id,
                mode
            ) )
        return response
    
    @staticmethod
    def get_session_keep_alive( conn: Connector, session_id: int ):
        versioned_events = InteractionSet.versioned(conn, events)
        
        response = conn.fire_event(
            versioned_events.io.get_session_keep_alive (
                session_id
            ) )
        return response.get_response_body_json()