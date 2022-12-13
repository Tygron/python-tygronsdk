from ..connectors import Connector
from ..data import events

from ..interactions.users import Users

from ....utilities.strings import Strings

import json

class Projects:

    @staticmethod
    def get_startable_projects( conn: Connector ):
        domain = Users.get_my_domain_name(conn)
            
        response = conn.fire_event( 
            events.io.get_domain_startable_projects (
                domain
            ) )
            
        return response.get_response_body_json()
    
    @staticmethod
    def get_startable_templates( conn: Connector ):
        domain = Users.get_my_domain_name(conn)
            
        response = conn.fire_event( 
            events.io.get_domain_startable_templates (
                domain
            ) )
            
        return response.get_response_body_json()




    @staticmethod
    def get_project( conn: Connector, project_name: str ):
        response = conn.fire_event( 
            events.io.get_project_data (
                project_name
            ) )
                
        return response.get_response_body_json()
 
    @staticmethod           
    def delete_project( conn: Connector, project_name: str ):
        response = conn.fire_event( 
            events.io.trash_project (
                project_name, True
            ) )
                
        if response.is_success():
            return True
        else:
            raise Exception( response );
            
    @staticmethod           
    def undelete_project( conn: Connector, project_name: str ):
        response = conn.fire_event( 
            events.io.trash_project (
                project_name, False
            ) )
                
        if response.is_success():
            return True
        else:
            raise Exception( response );