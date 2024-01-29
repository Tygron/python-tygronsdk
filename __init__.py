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



def init_data( init_file_data:str = None, init_file_credentials:str = None, use_data:bool = True, use_credentials:bool = True, use_args:bool = True, credentials_create_if_missing:bool = False, **kwargs):
    return init.init_data(
            init_file_data=init_file_data, 
            init_file_credentials=init_file_credentials,
            use_data=use_data,
            use_credentials=use_credentials,
            use_args=use_args,
            credentials_create_if_missing=credentials_create_if_missing,
            **kwargs
        )



def platform_module_name( platform:str = 'engine', module:str = '' ):
    return init.platform_module_name(
            platform=platform,
            module=module
        )
        
events = core.events.EventSetMultiCollection()
for platform in ['engine', 'preview']:
    module=platform_module_name(platform, 'events')
    
    events.add_event_sets(platform, **{
        **utilities.modules.get_content_from_module(getattr(environments.base.data,module,[]), core.events.EventSet),
        **utilities.modules.get_content_from_module(getattr(environments.session.data,module,[]), core.events.EventSet),
        **utilities.modules.get_content_from_module(getattr(environments.share.data,module,[]), core.events.EventSet),
    })