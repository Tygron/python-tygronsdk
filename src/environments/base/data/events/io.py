from .....core.events import EventSet

from .....core.data.events import Event
from .....core.data.events import EventParameter

from typing import Type

class EventDefinitionsCollectionClass():

    _start = [
            EventParameter('client_type', Type[str], True, 'EDITOR'),
            EventParameter('project_name', Type[str]),
            EventParameter('language', Type[str], False),
            EventParameter('session_id', Type[int], False),
            EventParameter('group_token', Type[str], False)
        ]
    _join = [
            EventParameter('session_id', Type[int], True),
            EventParameter('client_type', Type[str], True, 'EDITOR'),
            EventParameter('computer_name', Type[str], False),
            EventParameter('client_token', Type[str], False),
        ]
    _close = [
            EventParameter('session_id', Type[int], True),
            EventParameter('client_token', Type[str], False),
            EventParameter('keep_open', Type[bool], False, False),
        ]
    _kill = [
            EventParameter('session_id', Type[int], True),
        ]
        
        
        
    _save_project = [
            EventParameter('session_id', Type[int], True),
        ]
    _save_project_as = [
            EventParameter('session_id', Type[int], True),
            EventParameter('domain', Type[str], True),
            EventParameter('new_project_name', Type[str], True),
            EventParameter('clear_map', Type[bool], True, False),
        ]
            
            
            
    _get_domain_startable_projects = [
            EventParameter('domain', Type[str])
        ]
    _get_domain_startable_templates = [
            EventParameter('domain', Type[str])
        ]
    _get_project_data = [
            EventParameter('project_name', Type[str])
        ]
        
        
        
    _trash_project = [
            EventParameter('project_name', Type[str]),
            EventParameter('delete', Type[bool], False, True)
        ]



Instance = EventSet(EventDefinitionsCollectionClass)