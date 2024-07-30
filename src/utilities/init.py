import base64

from .lists import Lists
from .files import Files
from .strings import Strings
from .system import System
from .data import CollectiveDataStore, DataStore, CredentialsStore

class Init:
    
    def init_data( init_file_data:str = None, init_file_credentials:str = None, use_data:bool = True, use_credentials:bool = True, use_sys_args:bool = True, use_provided_args:bool = True, credentials_create_if_missing:bool = False, **kwargs):
        args = {}
        data = {}
        cred = {}
        
        if (use_sys_args):
            args.update( **System.get_args() )
        
        if (use_provided_args):
            args.update( **kwargs )
            
        if (use_data):
            data = Init.load_data_from_file( file=args.get('init_file_data', init_file_data ) )
        data.update( **args ) 
        
        if (use_credentials):
            cred = Init.load_credentials_from_file( file=data.get('init_file_credentials', init_file_credentials ), create_if_missing=credentials_create_if_missing )
        cred.update( **args )

        data_store = CollectiveDataStore( data_store=data, credentials_store=cred )
        data_store.update( **args )
        
        return data_store
        
    
    def platform_module_name( platform:str = 'engine', module:str = '' ):
        return str(module+'_'+platform).replace('_engine','')
    
    def load_data_from_file( file:str = None, files:list=['./data.txt','./data.json','./config.txt','./config.json',], fail_if_missing:bool=False ):
        files_to_try = [ f for f in Lists.coerce(file)+Lists.coerce(files) if f is not None ]
        for f in ( files_to_try ):
            try :
                return DataStore( file=f )
            except FileNotFoundError:
                pass
        if ( fail_if_missing ):
            raise FileNotFoundError( files_to_try )
        return DataStore()
        
    def load_credentials_from_file( file:str = None, files:list=['./credentials.txt','./credentials.json'], require:bool = False, create_if_missing:bool = False ):
        files_to_try = [ f for f in Lists.coerce(file)+Lists.coerce(files) if f is not None ]
        for f in ( files_to_try ):
            try :
                return CredentialsStore( data=None, file=f )
            except FileNotFoundError:
                pass
        if ( create_if_missing ):
            Init.create_default_credentials_file()
            return Init.load_credentials_from_file( files=files_to_try, create_if_missing=False )
        if (require):
            raise FileNotFoundError( files_to_try )
        return CredentialsStore()
            
    def create_default_credentials_file( file:str = 'credentials.json' ):
        print('Creating a credentials file named '+file+'. SECURITY WARNING that this stores credentials in plaintext, albeit base64 encoded!')

        credentials = {
            'base64_username': base64.b64encode(input('Enter username: ').encode('ASCII')).decode('ASCII'),
            'base64_password': base64.b64encode(input('Enter password: ').encode('ASCII')).decode('ASCII')
        }
        if ( Files.get_extention(file) == '.json' ):
            content = Strings.create_json_string(credentials)
            Files.write_file( directory = './', file = file, content=content )
        else:
            content = Strings.create_keys_values_string(credentials)
            Files.write_file( directory = './', file = file, content=content )