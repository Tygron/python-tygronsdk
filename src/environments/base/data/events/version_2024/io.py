from ......core.events import EventSet

from ......core.data.events import EventDefinition
from ......core.data.events import EventParameter

from typing import Type

definitions = {


    # Starting and stopping sessions
        'start' : EventDefinition(
                group='Starting and stopping sessions',
                parameters=[
                        EventParameter('session_type', ['EDITOR', 'MULTI', 'SINGLE'], True, 'EDITOR', 
                                        api_description='SessionType: SINGLE, MULTI, EDITOR;{"default": null, "values": ["EDITOR", "MULTI", "SINGLE"]}', api_type=['EDITOR', 'MULTI', 'SINGLE'], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('project_name', Type[str], 
                                        api_description='Project Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('language', None, False, 
                                        api_description='Language: NL, EN (optional)', api_type=None, api_required=False, api_default=None, api_aggregation=0,  ),
                        EventParameter('session_id', Type[int], False, 
                                        api_description='Preferred Session ID (optional)', api_type=Type[int], api_required=False, api_default=None, api_aggregation=0,  ),
                        EventParameter('group_token', Type[str], False, 
                                        api_description='Group token (optional)', api_type=Type[str], api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'join' : EventDefinition(
                group='Starting and stopping sessions',
                parameters=[
                        EventParameter('session_id', Type[int], 
                                        api_description='Session ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('client_type', ['EDITOR', 'LAUNCHER', 'PARTICIPANT', 'SERVER', 'SHARE', 'TOOLS'], True, 'EDITOR', 
                                        api_description='Application type;{"default": null, "values": ["EDITOR", "LAUNCHER", "PARTICIPANT", "SERVER", "SHARE", "TOOLS"]}', api_type=['EDITOR', 'LAUNCHER', 'PARTICIPANT', 'SERVER', 'SHARE', 'TOOLS'], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('computer_name', Type[str], False, 
                                        api_description='Your computer name, for easy identification (optional)', api_type=Type[str], api_required=False, api_default=None, api_aggregation=0,  ),
                        EventParameter('client_token', Type[str], False, 
                                        api_description='Your client token, for rejoining (optional)', api_type=Type[str], api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'close' : EventDefinition(
                group='Starting and stopping sessions',
                parameters=[
                        EventParameter('session_id', Type[int], 
                                        api_description='Session ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('client_token', Type[str], 
                                        api_description='Client Session token', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('keep_open', Type[bool], True, False, 
                                        api_description='Keep Session running, even if this was the last client;{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'kill' : EventDefinition(
                group='Starting and stopping sessions',
                parameters=[
                        EventParameter('session_id', Type[int], 
                                        api_description='Session ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'load_saved_session' : EventDefinition(
                group='Starting and stopping sessions',
                parameters=[
                        EventParameter('session_type', ['EDITOR', 'MULTI', 'SINGLE'], 
                                        api_description='Session Type:;{"default": null, "values": ["EDITOR", "MULTI", "SINGLE"]}', api_type=['EDITOR', 'MULTI', 'SINGLE'], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('project name', Type[str], 
                                        api_description='Project Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('session_name', Type[str], 
                                        api_description='Session name (e.g. Session on date X', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('save_name', Type[str], 
                                        api_description='Save Name (e.g. AUTOSAVE or specific moment in the Session)', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('group_token', Type[str], False, 
                                        api_description='Group token (only for MULTI user Sessions which share the same group) (optional)', api_type=Type[str], api_required=False, api_default=None, api_aggregation=0,  ),
                        EventParameter('preferred_session_id', Type[int], False, 
                                        api_description='Preferred Session ID (optional)', api_type=Type[int], api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Running session data
        'get_my_joinable_sessions' : EventDefinition(
                group='Running session data',
                parameters=[
                    ]
            ),
        'get_domain_sessions' : EventDefinition(
                group='Running session data',
                parameters=[
                    ]
            ),
        'set_session_keep_alive' : EventDefinition(
                group='Running session data',
                parameters=[
                        EventParameter('session_id', Type[int], 
                                        api_description='Session ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('keep_alive_mode', ['LONG', 'NEVER', 'SHORT'], 
                                        api_description='How long the Session must be kept alive;{"default": null, "values": ["LONG", "NEVER", "SHORT"]}', api_type=['LONG', 'NEVER', 'SHORT'], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'get_session_keep_alive' : EventDefinition(
                group='Running session data',
                parameters=[
                        EventParameter('session_id', Type[int], 
                                        api_description='Session ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Saving project data
        'add_project' : EventDefinition(
                group='Saving project data',
                parameters=[
                        EventParameter('project_name', Type[str], 
                                        api_description='Project Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('language', None, False, 
                                        api_description='Language (NL, EN)', api_type=None, api_required=False, api_default=None, api_aggregation=0,  ),
                        EventParameter('high_detail', Type[bool], False, 
                                        api_description='High Detail (<10m DEM, <5m grid)', api_type=Type[bool], api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'save_project' : EventDefinition(
                group='Saving project data',
                parameters=[
                        EventParameter('session_id', Type[int], 
                                        api_description='Session ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'save_project_as' : EventDefinition(
                group='Saving project data',
                parameters=[
                        EventParameter('session_id', Type[int], 
                                        api_description='Session ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('domain', Type[str], False, 
                                        api_description='Domain Name (optional, leave empty by default)', api_type=Type[str], api_required=False, api_default=None, api_aggregation=0,  ),
                        EventParameter('new_project_name', Type[str], 
                                        api_description='New Project Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('clear_map', Type[bool], 
                                        api_description='Save all data (set to false if you want to use the running Session as a template for a new Project);{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'save_session' : EventDefinition(
                group='Saving project data',
                parameters=[
                        EventParameter('session_id', Type[int], 
                                        api_description='Session ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('save_token', Type[str], 
                                        api_description='Randomly generated save token', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'add_project_version' : EventDefinition(
                group='Saving project data',
                parameters=[
                        EventParameter('session_id', Type[int], 
                                        api_description='Session ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('version_description', Type[str], 
                                        api_description='Version Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'remove_project_version' : EventDefinition(
                group='Saving project data',
                parameters=[
                        EventParameter('session_id', Type[int], 
                                        api_description='Session ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('version_id', Type[int], 
                                        api_description='Version of the Project', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'trash_project' : EventDefinition(
                group='Saving project data',
                parameters=[
                        EventParameter('project_name', Type[str], 
                                        api_description='Project Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('trashed', Type[bool], 
                                        api_description='Trashed;{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Available projects data
        'get_project_data' : EventDefinition(
                group='Available projects data',
                parameters=[
                        EventParameter('project_name', Type[str], 
                                        api_description='Project Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'get_visible_domain_projects' : EventDefinition(
                group='Available projects data',
                parameters=[
                    ]
            ),
        'get_my_startable_projects' : EventDefinition(
                group='Available projects data',
                parameters=[
                    ]
            ),
        'get_domain_startable_projects' : EventDefinition(
                group='Available projects data',
                parameters=[
                    ]
            ),
        'get_domain_startable_templates' : EventDefinition(
                group='Available projects data',
                parameters=[
                    ]
            ),
        'get_project_saved_sessions' : EventDefinition(
                group='Available projects data',
                parameters=[
                        EventParameter('domain', Type[str], False, 
                                        api_description='Domain Name (optional, leave empty by default)', api_type=Type[str], api_required=False, api_default=None, api_aggregation=0,  ),
                        EventParameter('project_name', Type[str], 
                                        api_description='Project Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Modify projects data
        'set_project_name' : EventDefinition(
                group='Modify projects data',
                parameters=[
                        EventParameter('old_project_name', Type[str], 
                                        api_description='Name of the Project to rename', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('new_project_name', Type[str], 
                                        api_description='New name for the Project', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_project_language' : EventDefinition(
                group='Modify projects data',
                parameters=[
                        EventParameter('project_name', Type[str], 
                                        api_description='Project Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('language', ['EN', 'NL'], 
                                        api_description='Project language: NL, EN;{"default": null, "values": ["EN", "NL"]}', api_type=['EN', 'NL'], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('availability', Type[bool], 
                                        api_description='Whether the language is available;{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_project_disclaimer' : EventDefinition(
                group='Modify projects data',
                parameters=[
                        EventParameter('project_name', Type[str], 
                                        api_description='Project Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('disclaimer', Type[str], 
                                        api_description='Disclaimer', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_project_template' : EventDefinition(
                group='Modify projects data',
                parameters=[
                        EventParameter('project_name', Type[str], 
                                        api_description='Project Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('is_template', Type[bool], 
                                        api_description='Whether the Project is a template;{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_project_active_version' : EventDefinition(
                group='Modify projects data',
                parameters=[
                        EventParameter('session_id', Type[str], 
                                        api_description='Project Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('version_id', Type[int], 
                                        api_description='Version of the Project', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_project_owner' : EventDefinition(
                group='Modify projects data',
                parameters=[
                        EventParameter('project_name', Type[str], 
                                        api_description='Project Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('owner', Type[str], 
                                        api_description='New owner', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_project_permission' : EventDefinition(
                group='Modify projects data',
                parameters=[
                        EventParameter('project_name', Type[str], 
                                        api_description='Project Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('permission_type', ['DOMAIN', 'OWNER', 'SUPPORT'], 
                                        api_description='Permission type: OWNER, DOMAIN, SUPPORT;{"default": null, "values": ["DOMAIN", "OWNER", "SUPPORT"]}', api_type=['DOMAIN', 'OWNER', 'SUPPORT'], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('permission', ['NONE', 'READ', 'WRITE'], 
                                        api_description='Permission: NONE, READ, WRITE;{"default": null, "values": ["NONE", "READ", "WRITE"]}', api_type=['NONE', 'READ', 'WRITE'], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_project_sub_domain' : EventDefinition(
                group='Modify projects data',
                parameters=[
                        EventParameter('project_name', Type[str], 
                                        api_description='Project Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('subdomain', Type[str], 
                                        api_description='Subdomain name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_project_version_description' : EventDefinition(
                group='Modify projects data',
                parameters=[
                        EventParameter(0, Type[int], 
                                        api_description='Session ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter(1, Type[int], 
                                        api_description='Version of the Project', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter(2, Type[str], 
                                        api_description='New version description', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Domain
        'get_domain_usage' : EventDefinition(
                group='Domain',
                parameters=[
                        EventParameter('domain', Type[str], False, 
                                        api_description='Domain Name (optional, leave empty by default)', api_type=Type[str], api_required=False, api_default=None, api_aggregation=0,  ),
                        EventParameter('subdomain', Type[str], False, 
                                        api_description='Subdomain Name (optional)', api_type=Type[str], api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'remove_sub_domain' : EventDefinition(
                group='Domain',
                parameters=[
                        EventParameter('domain', Type[str], False, 
                                        api_description='Domain Name (optional, leave empty by default)', api_type=Type[str], api_required=False, api_default=None, api_aggregation=0,  ),
                        EventParameter('subdomain', Type[str], 
                                        api_description='Sub Domain Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Validation
        'validate_project_name' : EventDefinition(
                group='Validation',
                parameters=[
                        EventParameter(0, Type[str], 
                                        api_description='Project Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'validate_start_params' : EventDefinition(
                group='Validation',
                parameters=[
                        EventParameter(0, Type[str], 
                                        api_description='Project Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter(1, Type[str], 
                                        api_description='Language: NL, EN', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Communication
        'send_domain_message' : EventDefinition(
                group='Communication',
                parameters=[
                        EventParameter(0, Type[str], 
                                        api_description='Message to send', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'get_domain_message' : EventDefinition(
                group='Communication',
                parameters=[
                    ]
            ),
        'get_domain_messages' : EventDefinition(
                group='Communication',
                parameters=[
                        EventParameter(0, Type[int], False, 
                                        api_description='Earliest data version to request (optional)', api_type=Type[int], api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Server status
        'get_failing_source_servers' : EventDefinition(
                group='Server status',
                parameters=[
                    ]
            ),
        'get_server_time' : EventDefinition(
                group='Server status',
                parameters=[
                    ]
            ),


    # Unavailable
        'check_waiting_bucket' : None,
        'get_continuable_sessions' : None,
        'get_waiting_clients' : None,
        'put_waiting_client_in_session' : None,
    }

event_set = EventSet(definitions, domain='io')