import sys
min_version = (3,10)
if (sys.version_info < min_version):
    raise Exception('Minimum python version required is Python ' + '.'.join(map(str,min_version)))

from .src import sdk as sdk
from .src import core as core
from .src import environments as environments

from .src import interfaces as interfaces
from .src import utilities as utilities

from .src.utilities import init as init

from .src.environments.session.data import items as items

import re, bisect

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
    return init_data

def get_matching_version( version:str = None, module=None ):
    versions = environments.base.data.events.versions
    if ( not (module is None)):
        versions = module.versions
    if ( not (version is None)):
        version = str(version)
        version_keys = [ tuple(k.split('_')) for k in versions.keys()]
        target_version = tuple(re.split('[\s\-|_.]+', version))
        version_key = version_keys[max(0,bisect.bisect_right(version_keys,target_version)-1)]
        return '_'.join(version_key);
    return next(iter(versions.keys()))

def get_module_version( module, version:str = None ):
    match = get_matching_version( version, module)
    versions = module.versions
    return versions[match]

events = core.events.EventSetCollection()
def set_global_module_version( version = None, force_version:bool = False ):
    global events
    global global_module_version
    if ( version is None or (not force_version) ):
        version = get_matching_version(version)
    version = str(version)
    global_module_version = version
    
    events = core.events.EventSetCollection()
    version_event_sets = {
        **utilities.modules.get_content_from_module(environments.base.data.events._set_module_version(version), core.events.EventSet),
        **utilities.modules.get_content_from_module(environments.session.data.events._set_module_version(version), core.events.EventSet),
        #**utilities.modules.get_content_from_module(environments.share.data.events._set_module_version(version), core.events.EventSet),
    }
    
    events.add_event_sets(**version_event_sets)
    return global_module_version

set_global_module_version()