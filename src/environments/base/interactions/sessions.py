from ..connectors import Connector
from ....utilities.strings import Strings

import json

class Sessions:

    @staticmethod
    def start_project_session( conn: Connector, project_name:str, session_type:str = 'EDITOR', session_language:str = None, session_id:int = None, group_token:str = None ):
        response = conn.request(
                method='POST',
                url='event/io/start',
                data=[ 
                        session_type,
                        project_name,
                        session_language,
                        session_id,
                        group_token
                    ]
            )
        return response.get_response_body_json()
        
    @staticmethod
    def join_project_session( conn: Connector, session_id:int, client_type:str = 'EDITOR', computer_name:str = None, client_token:str = None ):
        response = conn.request(
                method='POST',
                url='event/io/join',
                data=[ 
                        session_id,
                        client_type,
                        computer_name,
                        client_token
                    ]
            )
        return response.get_response_body_json()
        
    @staticmethod
    def close_project_session( conn: Connector, session_id:int, client_token:str = None, keep_open:bool = False ):
        response = conn.request(
                method='POST',
                url='event/io/close',
                data=[ 
                        session_id,
                        client_token,
                        keep_open
                    ]
            )
        return response.get_response_body_json()
        
    @staticmethod
    def kill_project_session( conn: Connector, session_id:int ):
        response = conn.request(
                method='POST',
                url='event/io/kill',
                data=[ 
                        session_id
                    ]
            )
        return response.get_response_body_json()
 
 
    @staticmethod
    def save_project_as( conn: Connector, session_id: int, domain: str, project_name: str, clear_map: bool = False, attempts:int = 25 ):
        last_err = None
        for i in range(attempts):
            attempt_name = project_name + ('' if i==0 else '-'+str(i))
            try:
                response = conn.request(
                    method='POST',
                    url='event/io/save_project_as',
                    data=[ session_id, domain, attempt_name, clear_map ]
                )
                if response.is_success():
                    return attempt_name
                else:
                    raise Exception( response, attempt_name );
            except Exception as err:
                last_err = Exception('Could not set name: '+attempt_name, err )
                continue
        raise last_err
 
    @staticmethod
    def save_project( conn: Connector, session_id: int ):
        response = conn.request(
                method='POST',
                url='event/io/save_project',
                data=[ session_id ]
            )
        return session_id