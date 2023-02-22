from .....core.events import EventSet

from .....core.data.events import EventDefinition
from .....core.data.events import EventParameter

from typing import Type

definitions = {
        'add_sub_domain' : EventDefinition(
                    parameters=[
                            EventParameter('domain', Type[str]),
                            EventParameter('sub_domain', Type[str]),
                            EventParameter('max_project_area_total', Type[str]), #km2
                            EventParameter('max_project_area_single', Type[str]), #m2
                        ]
            ),
        'add_user' : EventDefinition(
                    parameters=[
                            EventParameter('domain', Type[str]),
                            EventParameter('username', Type[str]),
                        ]
            ),
        'get_domain' : EventDefinition(
                    parameters=[
                            EventParameter('domain', Type[str]),
                        ]
            ),
        'get_domain_logo' : EventDefinition(
                    parameters=[
                        ]
            ),
        'get_domain_new_projects_for_license_year' : EventDefinition(
                    parameters=[
                            EventParameter('domain', Type[str]),
                        ]
            ),
        'get_domain_user_names' : EventDefinition(
                    parameters=[
                            EventParameter('domain', Type[str]),
                        ]
            ),
        'get_domain_users' : EventDefinition(
                    parameters=[
                            EventParameter('domain', Type[str]),
                        ]
            )
    }
    
event_set = EventSet(definitions)