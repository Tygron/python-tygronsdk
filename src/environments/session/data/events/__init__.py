from .....utilities import modules
from .....core.events import EventSet

import os
def get_versions():
    this_dir = os.path.dirname(os.path.realpath(__file__))
    return sorted([
                name
                for name in os.listdir(this_dir)
                if name.startswith('version_')]
            )

__all__ = get_versions()
from . import *

versions = {k.replace('version_',''):v for k,v in globals().items() if k.startswith('version_')}

def _set_module_version( version ):
    global versions
    events = versions.get(version,versions.get('events_'+version,None))
    
    event_sets = modules.get_content_from_module(events, EventSet)
    for event_set_name, event_set in event_sets.items():
        globals()[event_set_name] = event_set
    return events

def _get_module_version( version ):
    global versions
    events = versions.get(version,versions.get(version,None))
    return events
    
_set_module_version( next(iter(versions)) )