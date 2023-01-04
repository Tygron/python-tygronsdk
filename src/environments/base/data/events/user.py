from .....core.events import EventSet

from .....core.data.events import Event
from .....core.data.events import EventParameter

from typing import Type

class EventDefinitionsCollectionClass():


    _add_sub_domain = [
            EventParameter('domain', Type[str]),
            EventParameter('sub_domain', Type[str]),
            EventParameter('max_project_area_total', Type[str]), #km2
            EventParameter('max_project_area_single', Type[str]), #m2
        ]
    _add_user = [
            EventParameter('domain', Type[str]),
            EventParameter('username', Type[str]),
        ]
    _get_domain = [
            EventParameter('domain', Type[str]),
        ]
    _get_domain_logo = [
        ]
    _get_domain_new_projects_for_license_year = [
            EventParameter('domain', Type[str]),
        ]
    _get_domain_user_names = [
            EventParameter('domain', Type[str]),
        ]
    _get_domain_users = [
            EventParameter('domain', Type[str]),
        ]




Instance = EventSet(EventDefinitionsCollectionClass)