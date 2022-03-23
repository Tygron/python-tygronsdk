from ..core.connectors import ConnectorTygronSession, ConnectorTygronApi

import json

class Projects:

    @staticmethod
    def save_project_as( conn_api: ConnectorTygronApi, session_id: int, domain: str, project_name: str, clear_map: bool = False, attempts:int = 25 ):
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
                else:
                    raise Exception( response, attempt_name );
            except Exception as err:
                last_err = Exception('Could not set name: '+attempt_name, err )
                continue
        raise last_err
 
    @staticmethod           
    def delete_project( conn_api: ConnectorTygronApi, project_name: str ):
        response = conn_api.request(
                method='POST',
                url='event/io/trash_project', 
                data=[ project_name, True ]
            );
        if response.is_success():
            return True
        else:
            raise Exception( response );
    @staticmethod           
    def undelete_project( conn_api: ConnectorTygronApi, project_name: str ):
        response = conn_api.request(
                method='POST',
                url='event/io/trash_project', 
                data=[ project_name, False ]
            );
        if response.is_success():
            return True
        else:
            raise Exception( response );