from ..connectors import Connector
from ..data import events, objects

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
        projects = [objects.ProjectData(project) for project in response.get_response_body_json()] 
            
        return projects
    
    @staticmethod
    def get_startable_templates( conn: Connector ):
        domain = Users.get_my_domain_name(conn)
            
        response = conn.fire_event( 
            events.io.get_domain_startable_templates (
                domain
            ) )
        projects = [objects.ProjectData(project) for project in response.get_response_body_json()] 
            
        return projects




    @staticmethod
    def get_project( conn: Connector, project_name: str ):
        response = conn.fire_event( 
            events.io.get_project_data (
                project_name
            ) )
                
        return objects.ProjectData(response.get_response_body_json())


    @staticmethod
    def add_project( conn: Connector, new_project_name:str, language:str = 'EN', high_detail:bool = True ):
        response = conn.fire_event( 
                events.io.add_project (
                         project_name=new_project_name, 
                         language=language,
                         high_detail=high_detail
                    )
            )
        return objects.ProjectData(response.get_response_body_json())
 
    @staticmethod           
    def delete_project( conn: Connector, project_name: str, error_on_missing:bool = False ):
        try:
            Projects.get_project(conn=conn, project_name=project_name)
        except Exception as err:
            if (not error_on_missing):
                return False
            else:
                raise err
                
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