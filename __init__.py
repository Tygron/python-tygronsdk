import sys
min_version = (3,10)
if (sys.version_info < min_version):
    raise Exception('Minimum python version required is Python ' + '.'.join(map(str,min_version)))

from .src import sdk as sdk
from .src import core as core
from .src import environments as environments

from .src import interfaces as interfaces
from .src import utilities as utilities

from .src.environments.session.data import items as items


def platform_module_name( platform:str = 'engine', module:str = '' ):
    return str(module+'_'+platform).replace('_engine','')

events = core.events.EventSetMultiCollection()
for platform in ['engine', 'preview']:
    module=platform_module_name(platform, 'events')
    
    events.add_event_sets(platform, **{
        **utilities.modules.get_content_from_module(getattr(environments.base.data,module,[]), core.events.EventSet),
        **utilities.modules.get_content_from_module(getattr(environments.session.data,module,[]), core.events.EventSet),
        **utilities.modules.get_content_from_module(getattr(environments.share.data,module,[]), core.events.EventSet),
    })


def load_data_from_file( file:str = None, files:list=['./data.txt','./data.json','./config.txt','./config.json',], fail_if_missing:bool=False ):
    files_to_try = [ f for f in utilities.lists.coerce(files)+utilities.lists.coerce(file) if f is not None ]
    for f in ( files_to_try ):
        try :
            return utilities.data.DataStore( file=f )
        except FileNotFoundError:
            pass
    if ( fail_if_missing ):
        raise FileNotFoundError( files_to_try )
    return utilities.data.DataStore()
    
def load_credentials_from_file( file:str = None, files:list=['./credentials.txt','./credentials.json'], create_if_missing:bool = False ):
    files_to_try = [ f for f in utilities.lists.coerce(files)+utilities.lists.coerce(file) if f is not None ]
    for f in ( files_to_try ):
        try :
            return utilities.data.CredentialsStore( file=f )
        except FileNotFoundError:
            pass
    if ( create_if_missing ):
        create_default_credentials_file()
        return load_credentials_from_file( files=files_to_try, create_if_missing=False )
    raise FileNotFoundError( files_to_try )


def create_default_credentials_file( file:str = 'credentials.json' ):
    print('Creating a credentials file named '+file+'. SECURITY WARNING that this stores credentials in plaintext, albeit base64 encoded!')
    import base64
    credentials = {
        'base64_username': base64.b64encode(input('Enter username: ').encode('ASCII')).decode('ASCII'),
        'base64_password': base64.b64encode(input('Enter password: ').encode('ASCII')).decode('ASCII')
    }
    if ( utilities.files.get_extention(file) == '.json' ):
        content = utilities.strings.create_json_string(credentials)
        utilities.files.write_file( directory = './', file = file, content=content )
    else:
        content = utilities.strings.create_keys_values_string(credentials)
        utilities.files.write_file( directory = './', file = file, content=content )