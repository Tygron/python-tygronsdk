from .....core.events import EventSet

from .....core.data.events import EventDefinition
from .....core.data.events import EventParameter

from typing import Type

definitions = {

    #Starting and stopping sessions
        'start' : EventDefinition(
                parameters=[
                        EventParameter('client_type', Type[str], True, 'EDITOR'),
                        EventParameter('project_name', Type[str]),
                        EventParameter('language', Type[str], False),
                        EventParameter('session_id', Type[int], False),
                        EventParameter('group_token', Type[str], False)
                    ]
            ),
        'join' : EventDefinition(
                parameters=[
                        EventParameter('session_id', Type[int] ),
                        EventParameter('client_type', Type[str], True, 'EDITOR'),
                        EventParameter('computer_name', Type[str], False),
                        EventParameter('client_token', Type[str], False),
                    ]
            ),
        'close' : EventDefinition(
                parameters=[
                        EventParameter('session_id', Type[int] ),
                        EventParameter('client_token', Type[str], False),
                        EventParameter('keep_open', Type[bool], False, False),
                    ]
            ),
        'kill' : EventDefinition(
                parameters=[
                        EventParameter('session_id', Type[int], True),
                    ]
            ),

    #Running sessions data
        'get_my_joinable_sessions' : EventDefinition(
                parameters=[
                    ]
            ),
        #'get_continuable_sessions' : EventDefinition(
        #       parameters=[
        #           ]
        #   ),
        'set_session_keep_alive' : EventDefinition(
                parameters=[
                        EventParameter('session_id', Type[int]),
                        EventParameter('keep_alive_mode', Type[str], False, 'SHORT'),
                        
                    ]
            ), 
        'get_session_keep_alive' : EventDefinition(
                parameters=[
                        EventParameter('session_id', Type[int]),
                    ]
            ),
            
    #Saving project data
        'add_project' : EventDefinition(
                parameters=[
                        EventParameter('project_name', Type[str]),
                        EventParameter('language', Type[str], False, 'EN'),
                        EventParameter('high_detail', Type[bool], False, True),
                    ]
            ), 
        'trash_project' : EventDefinition(
                parameters=[
                        EventParameter('project_name', Type[str]),
                        EventParameter('delete', Type[bool], False, True),
                    ]
            ), 
        'save_project' : EventDefinition(
                parameters=[
                        EventParameter('session_id', Type[int]),
                    ]
            ), 
        'save_project_as' : EventDefinition(
                parameters=[
                        EventParameter('session_id', Type[int]),
                        EventParameter('domain', Type[str]),
                        EventParameter('new_project_name', Type[str]),
                        EventParameter('clear_map', Type[bool], True, False),
                    ]
            ), 
        'add_project_version' : EventDefinition(
                parameters=[
                        EventParameter('session_id', Type[int]),
                        EventParameter('version_description', Type[str]),
                    ]
            ), 
        'set_project_version_decription' : EventDefinition(
                parameters=[
                        EventParameter('session_id', Type[int]),
                        EventParameter('version_id', Type[int]),
                        EventParameter('version_description', Type[str]),
                    ]
            ), 
        'remove_project_versions' : EventDefinition(
                parameters=[
                        EventParameter('session_id', Type[int]),
                        EventParameter('version_id', Type[int]),
                    ]
            ), 
        'save_session' : EventDefinition(
                parameters=[
                        EventParameter('session_id', Type[int]),
                        EventParameter('save_token', Type[str]),
                    ]
            ), 
            
    #Available projects data
        'get_project_data' : EventDefinition(
                parameters=[
                        EventParameter('project_name', Type[str]),
                    ]
            ), 
        'get_domain_visible_projects' : EventDefinition(
                parameters=[
                        EventParameter('domain', Type[str]),
                    ]
            ), 
        'get_domain_startable_projects' : EventDefinition(
                parameters=[
                        EventParameter('domain', Type[str]),
                    ]
            ), 
        'get_domain_startable_templates' : EventDefinition(
                parameters=[
                        EventParameter('domain', Type[str]),
                    ]
            ), 
        'get_project_saved_sessions' : EventDefinition(
                parameters=[
                        EventParameter('domain', Type[str]),
                        EventParameter('project_name', Type[str]),
                    ]
            ), 
            
    #Modify project data
        'set_project_name' : EventDefinition(
                parameters=[
                        EventParameter('old_project_name', Type[str]),
                        EventParameter('new_project_name', Type[str]),
                    ]
            ), 
        'set_project_language' : EventDefinition(
                parameters=[
                        EventParameter('project_name', Type[str]),
                        EventParameter('language', Type[str]),
                        EventParameter('availability', Type[bool], True, True),
                    ]
            ), 
        'set_project_disclaimer' : EventDefinition(
                parameters=[
                        EventParameter('project_name', Type[str]),
                        EventParameter('disclaimer', Type[str]),
                    ]
            ), 
        'set_project_template' : EventDefinition(
                parameters=[
                        EventParameter('project_name', Type[str]),
                        EventParameter('is_template', Type[bool]),
                    ]
            ), 
        'set_project_active_version' : EventDefinition(
                parameters=[
                        EventParameter('session_id', Type[int]),
                        EventParameter('version_id', Type[int]),
                    ]
            ), 
        'set_project_owner' : EventDefinition(
                parameters=[
                        EventParameter('project_name', Type[str]),
                        EventParameter('owner', Type[str]),
                    ]
            ), 
        'set_project_permission' : EventDefinition(
                parameters=[
                        EventParameter('project_name', Type[str]),
                        EventParameter('permission_type', Type[str]),
                        EventParameter('permission', Type[str]),
                    ]
            ), 
        'set_project_sub_domain' : EventDefinition(
                parameters=[
                        EventParameter('project_name', Type[str]),
                        EventParameter('sub_domain', Type[str]),
                    ]
            ), 
        
        
        
        
        'get_domain_usage' : EventDefinition(
                parameters=[
                        EventParameter('domain', Type[str]),
                        EventParameter('sub_domain', Type[str], False, 'All Sub Domains'),
                    ]
            ), 
        'get_failing_source_servers' : EventDefinition(
                parameters=[
                    ]
            ), 
        'get_server_time' : EventDefinition(
                parameters=[
                    ]
            ), 
        'remove_sub_domain' : EventDefinition(
                parameters=[
                        EventParameter('domain', Type[str]),
                        EventParameter('sub_domain', Type[str]),
                    ]
            ),
    }
    
event_set = EventSet(definitions)