from .....core.events import EventSet

from .....core.data.events import Event
from .....core.data.events import EventParameter

from typing import Type

class EventDefinitionsCollectionClass():


    #Starting and stopping sessions
    _start = [
            EventParameter('client_type', Type[str], True, 'EDITOR'),
            EventParameter('project_name', Type[str]),
            EventParameter('language', Type[str], False),
            EventParameter('session_id', Type[int], False),
            EventParameter('group_token', Type[str], False)
        ]
    _join = [
            EventParameter('session_id', Type[int] ),
            EventParameter('client_type', Type[str], True, 'EDITOR'),
            EventParameter('computer_name', Type[str], False),
            EventParameter('client_token', Type[str], False),
        ]
    _close = [
            EventParameter('session_id', Type[int] ),
            EventParameter('client_token', Type[str], False),
            EventParameter('keep_open', Type[bool], False, False),
        ]
    _kill = [
            EventParameter('session_id', Type[int], True),
        ]
    
    #Running sessions data
    _get_my_joinable_sessions = []
    #_get_continuable_sessions = [
    #        
    #    ]

    _set_session_keep_alive = [
            EventParameter('session_id', Type[int]),
            EventParameter('keep_alive_mode', Type[str], False, 'SHORT'),
    ]
    _get_session_keep_alive = [
            EventParameter('session_id', Type[int]),
        ]





    #Saving project data
    _add_project = [
            EventParameter('project_name', Type[str]),
            EventParameter('language', Type[str], False, 'EN'),
            EventParameter('high_detail', Type[bool], False, True),
        ]     
    _trash_project = [
            EventParameter('project_name', Type[str]),
            EventParameter('delete', Type[bool], False, True),
        ]
        
    _save_project = [
            EventParameter('session_id', Type[int]),
        ]
    _save_project_as = [
            EventParameter('session_id', Type[int]),
            EventParameter('domain', Type[str]),
            EventParameter('new_project_name', Type[str]),
            EventParameter('clear_map', Type[bool], True, False),
        ]
        
    _add_project_version = [
            EventParameter('session_id', Type[int]),
            EventParameter('version_description', Type[str]),
        ]
    _set_project_version_description = [
            EventParameter('session_id', Type[int]),
            EventParameter('version_id', Type[int]),
            EventParameter('version_description', Type[str]),
    ]
    _remove_project_version = [
            EventParameter('session_id', Type[int]),
            EventParameter('version_id', Type[int]),
        ]
        
    _save_session = [
            EventParameter('session_id', Type[int]),
            EventParameter('save_token', Type[str]),
        ]
        
    #Available projects data
    _get_project_data = [
            EventParameter('project_name', Type[str]),
        ]
    _get_domain_visible_projects = [
            EventParameter('domain', Type[str]),
        ]
    _get_domain_startable_projects = [
            EventParameter('domain', Type[str]),
        ]
    _get_domain_startable_templates = [
            EventParameter('domain', Type[str]),
        ]
    _get_project_saved_sessions = [
            EventParameter('domain', Type[str]),
            EventParameter('project_name', Type[str]),
        ]

    #Modify project data
    _set_project_name = [
            EventParameter('old_project_name', Type[str]),
            EventParameter('new_project_name', Type[str]),
        ]
    _set_project_language = [
            EventParameter('project_name', Type[str]),
            EventParameter('language', Type[str]),
            EventParameter('availability', Type[bool], True, True),
        ]
    _set_project_disclaimer = [
            EventParameter('project_name', Type[str]),
            EventParameter('disclaimer', Type[str]),
        ]
        
    _set_project_template = [
            EventParameter('project_name', Type[str]),
            EventParameter('is_template', Type[bool]),
        ]
    _set_project_active_version = [
            EventParameter('session_id', Type[int]),
            EventParameter('version_id', Type[int]),
        ]
        
    _set_project_owner = [
            EventParameter('project_name', Type[str]),
            EventParameter('owner', Type[str]),
        ]
    _set_project_permission = [
            EventParameter('project_name', Type[str]),
            EventParameter('permission_type', Type[str]),
            EventParameter('permission', Type[str]),
        ]
    _set_project_sub_domain = [
            EventParameter('project_name', Type[str]),
            EventParameter('sub_domain', Type[str]),
        ]
    
    
    
 
    _get_domain_usage = [
            EventParameter('domain', Type[str]),
            EventParameter('sub_domain', Type[str], False, 'All Sub Domains'),
        ]
        
    _get_failing_source_servers = []
    _get_server_time = []



    _remove_sub_domain = [
            EventParameter('domain', Type[str]),
            EventParameter('sub_domain', Type[str]),
        ]

Instance = EventSet(EventDefinitionsCollectionClass)