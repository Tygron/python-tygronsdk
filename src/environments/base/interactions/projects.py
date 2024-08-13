from ....core.interactions.interaction_set import InteractionSet

from ..connectors import Connector
from ..data import events, objects

from ..interactions.users import Users
from ....utilities.strings import Strings
import json

class Projects(InteractionSet):

    @staticmethod
    def get_startable_projects( conn: Connector ):
        versioned_events = InteractionSet.versioned(conn, events)
        
        domain = Users.get_my_domain_name(conn)
            
        response = conn.fire_event( 
            versioned_events.io.get_domain_startable_projects (
                domain
            ) )
        projects = [objects.ProjectData(project) for project in response.get_response_body_json()] 
            
        return projects
    
    @staticmethod
    def get_startable_templates( conn: Connector ):
        versioned_events = InteractionSet.versioned(conn, events)
        
        domain = Users.get_my_domain_name(conn)
        
        response = conn.fire_event( 
            versioned_events.io.get_domain_startable_templates (
                domain
            ) )
        projects = [objects.ProjectData(project) for project in response.get_response_body_json()] 
            
        return projects




    @staticmethod
    def get_project( conn: Connector, project_name: str ):
        versioned_events = InteractionSet.versioned(conn, events)
        
        response = conn.fire_event( 
            versioned_events.io.get_project_data (
                project_name
            ) )
                
        return objects.ProjectData(response.get_response_body_json())


    @staticmethod
    def add_project( conn: Connector, new_project_name:str, language:str = 'EN', high_detail:bool = True ):
        versioned_events = InteractionSet.versioned(conn, events)
        
        response = conn.fire_event( 
                versioned_events.io.add_project (
                         project_name=new_project_name, 
                         language=language,
                         high_detail=high_detail
                    )
            )
        return objects.ProjectData(response.get_response_body_json())
 
    @staticmethod           
    def delete_project( conn: Connector, project_name: str, error_on_missing:bool = False ):
        versioned_events = InteractionSet.versioned(conn, events)
        
        try:
            Projects.get_project(conn=conn, project_name=project_name)
        except Exception as err:
            if (not error_on_missing):
                return False
            else:
                raise err
        
        event = None
        match conn.get_platform_version():
            case '2025':
                event =  versioned_events.io.set_project_trashed (
                project_name, True
            )
            case _:
                event =  versioned_events.io.trash_project (
                project_name, True
            )
        
        response = conn.fire_event( event )
        if response.is_success():
            return True
        else:
            raise Exception( response );
            
    @staticmethod           
    def undelete_project( conn: Connector, project_name: str, error_on_missing:bool = False ):
        versioned_events = InteractionSet.versioned(conn, events)
        
        try:
            Projects.get_project(conn=conn, project_name=project_name)
        except Exception as err:
            if (not error_on_missing):
                return False
            else:
                raise err
        
        event = None
        match conn.get_platform_version():
            case '2025':
                event =  versioned_events.io.set_project_trashed (
                project_name, False
            )
            case _:
                event =  versioned_events.io.trash_project (
                project_name, False
            )
        
        response = conn.fire_event( event )
        if response.is_success():
            return True
        else:
            raise Exception( response );