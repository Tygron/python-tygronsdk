import sys
min_version = (3,10)
if (sys.version_info < min_version):
    raise Exception('Minimum python version required is Python ' + '.'.join(map(str,min_version)))

_platform_versions = {
    'preview':'2025'
}

from .src import sdk as sdk
from .src import core as core
from .src import environments as environments

from .src import interfaces as interfaces
from .src import utilities as utilities

from .src.utilities import init as init

from .src.environments.session.data import items as items



def init_data( init_file_data:str = None, init_file_credentials:str = None, use_data:bool = True, use_credentials:bool = True, use_sys_args:bool = True, use_provided_args:bool = True, credentials_create_if_missing:bool = False, **kwargs):
    init_data = init.init_data(
            init_file_data=init_file_data, 
            init_file_credentials=init_file_credentials,
            use_data=use_data,
            use_credentials=use_credentials,
            use_sys_args=use_sys_args,
            use_provided_args=use_provided_args,
            credentials_create_if_missing=credentials_create_if_missing,
            **kwargs
        )
    set_platform_version(**init.platform_version_map_from_data(init_data))
    return init_data

def platform_module_name( platform:str = 'engine', module:str = '' ):
    return init.platform_module_name(
            platform=platform,
            module=module
        )

def set_platform_version( **platform_versions ):
    global _platform_versions
    _platform_versions.update( platform_versions )
def get_platform_version( platform:str = None ):
    global global_platform_version, _platform_versions
    default_version = global_platform_version
    return _platform_versions.get(platform, default_version)

events = core.events.EventSetCollection()
def set_global_platform_version( version ):
    global events
    global global_platform_version
    
    version = str(version)
    global_platform_version = version
    
    events = core.events.EventSetCollection()
    version_event_sets = {
        **utilities.modules.get_content_from_module(environments.base.data.events._set_platform_version(version), core.events.EventSet),
        **utilities.modules.get_content_from_module(environments.session.data.events._set_platform_version(version), core.events.EventSet),
        #**utilities.modules.get_content_from_module(environments.share.data.events._set_platform_version(version), core.events.EventSet),
    }
    
    events.add_event_sets(**version_event_sets)

global_platform_version = next(iter(environments.base.data.events.versions))
set_global_platform_version( get_platform_version() )