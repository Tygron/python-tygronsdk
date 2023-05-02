from .....core.events import EventSet

from .....core.data.events import EventDefinition
from .....core.data.events import EventParameter

from typing import Type

definitions = {


    # User
        'get_my_domain' : EventDefinition(
                group='User',
                parameters=[
                    ]
            ),
        'get_my_login_key' : EventDefinition(
                group='User',
                parameters=[
                    ]
            ),
        'get_my_user' : EventDefinition(
                group='User',
                parameters=[
                    ]
            ),
        'set_user_passwd' : EventDefinition(
                group='User',
                parameters=[
                        EventParameter('username', Type[str], 
                                        api_description='Username', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('password', Type[str], 
                                        api_description='Password', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Domain info
        'get_domain' : EventDefinition(
                group='Domain info',
                parameters=[
                        EventParameter('domain', Type[str], 
                                        api_description='Domain Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'get_domain_user_names' : EventDefinition(
                group='Domain info',
                parameters=[
                        EventParameter('domain', Type[str], 
                                        api_description='Domain Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'get_domain_users' : EventDefinition(
                group='Domain info',
                parameters=[
                        EventParameter('domain', Type[str], 
                                        api_description='Domain Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Management
        'add_user' : EventDefinition(
                group='Management',
                parameters=[
                        EventParameter('domain', Type[str], 
                                        api_description='Domain Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('username', Type[str], 
                                        api_description='Username', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'remove_user' : EventDefinition(
                group='Management',
                parameters=[
                        EventParameter('username', Type[str], 
                                        api_description='Username', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_user_active' : EventDefinition(
                group='Management',
                parameters=[
                        EventParameter('domain', Type[str], 
                                        api_description='Domain Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('username', Type[str], 
                                        api_description='Username', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('active', Type[bool], 
                                        api_description='Whether account should be active;{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_user_data' : EventDefinition(
                group='Management',
                parameters=[
                        EventParameter('domain', Type[str], 
                                        api_description='Domain Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('username', Type[str], 
                                        api_description='Username', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('forum_name', Type[str], 
                                        api_description='Forum nickname', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('first_name', Type[str], 
                                        api_description='First name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('last_name', Type[str], 
                                        api_description='Last name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('phone_number', Type[str], 
                                        api_description='Phone number', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('rights', ['DOMAIN_ADMIN', 'EDITOR', 'HOST_SESSION', 'JOIN_ONLY', 'NONE', 'SUPER_USER'], 
                                        api_description='User access level;{"default": null, "values": ["DOMAIN_ADMIN", "EDITOR", "HOST_SESSION", "JOIN_ONLY", "NONE", "SUPER_USER"]}', api_type=['DOMAIN_ADMIN', 'EDITOR', 'HOST_SESSION', 'JOIN_ONLY', 'NONE', 'SUPER_USER'], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_user_sub_domain' : EventDefinition(
                group='Management',
                parameters=[
                        EventParameter('domain', Type[str], 
                                        api_description='Domain Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('username', Type[str], 
                                        api_description='Username', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('subdomain', Type[str], 
                                        api_description='Subdomain name (empty means access to the root of the domain)', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'add_sub_domain' : EventDefinition(
                group='Management',
                parameters=[
                        EventParameter('domain', Type[str], 
                                        api_description='Domain Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('subdomain', Type[str], 
                                        api_description='Subdomain name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('max_project_area_total', Type[int], 
                                        api_description='Total savable area (km2)', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('max_project_area_single', Type[int], 
                                        api_description='Max project area (m2)', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'reset_passwd' : EventDefinition(
                group='Management',
                parameters=[
                        EventParameter('username', Type[str], 
                                        api_description='Username', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Usage
        'get_domain_new_projects_for_license_year' : EventDefinition(
                group='Usage',
                parameters=[
                        EventParameter('domain', Type[str], 
                                        api_description='Domain Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Logging
        'get_log' : EventDefinition(
                group='Logging',
                parameters=[
                        EventParameter('domain', Type[str], 
                                        api_description='String', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('log_type', ['SECURITY', 'SESSIONS', 'USERS'], 
                                        api_description='Type;{"default": null, "values": ["SECURITY", "SESSIONS", "USERS"]}', api_type=['SECURITY', 'SESSIONS', 'USERS'], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('log_id_token', Type[str], 
                                        api_description='String', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'get_logs' : EventDefinition(
                group='Logging',
                parameters=[
                        EventParameter('domain', Type[str], 
                                        api_description='Domain Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('log_type', ['SECURITY', 'SESSIONS', 'USERS'], 
                                        api_description='Type;{"default": null, "values": ["SECURITY", "SESSIONS", "USERS"]}', api_type=['SECURITY', 'SESSIONS', 'USERS'], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('start_time_in_millis', Type[int], 
                                        api_description='Date in millis', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Identity
        'get_domain_logo' : EventDefinition(
                group='Identity',
                parameters=[
                        EventParameter('domain', Type[str], 
                                        api_description='Domain Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_domain_logo' : EventDefinition(
                group='Identity',
                parameters=[
                        EventParameter('domain', Type[str], 
                                        api_description='Domain Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('file_data', Type[bytes], aggregation=1, 
                                        api_description='.png file', api_type=Type[bytes], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),


    # Unavailable
        'activate_trial_account' : None,
        'add_trial_account' : None,
        'get_esri_client_id' : None,
        'get_esri_portal' : None,
        'get_esri_refresh_token' : None,
        'set_domain_adress_info' : None,
        'set_domain_license' : None,
        'set_domain_security_policy' : None,
        'set_esri_auth_parameters' : None,
        'set_esri_refresh_token' : None,
        'set_hardware_info' : None,
    }

event_set = EventSet(definitions, domain='user')