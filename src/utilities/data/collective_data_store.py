from . import DataStore
from . import CredentialsStore

from ..tygron_strings import TygronStrings

import json, base64

class CollectiveDataStore(DataStore):

    def __init__( self, data:dict = None, file:str = None ):
        self._credentials_store = CredentialsStore.create()
        self._data_store = DataStore.create()
        self._source = None
        self.update( 
                data=data,
                file=file
            )
    
    @staticmethod
    def create( file:str = None ):
        return CollectiveDataStore( file=file )
    
    def update( self, data:dict = {}, clear:bool = False, file:str = None, **kwargs ):
        if ( len(kwargs) > 0 ):
            data = { **kwargs } if data is None else { **data, **kwargs }
        
        if ( not (isinstance(data, dict) or isinstance(file,str) ) ):
            return
            
        from_file = False
        if ( data is None ):
            data = self.load_from_file(file)
            from_file = True
        if ( not isinstance(data, dict) ):
            raise Exception('File read succesfully, but did not contain valid data. Must be either a JSON, or key value pairs')    
        
        data = self.parse_keys(data)
        
        credentials_data= {}
        misc_data = {}
        
        for key in data:
            if ( key in self._credentials_store._credential_keys ):
                credentials_data[key] = data[key]
            else:
                misc_data[key] = data[key]
        if ( len(credentials_data)>0 ):
            self._credentials_store.update(credentials_data, clear=clear)
                    
            if (from_file):
                self._credentials_store._source = file
                
        if ( len(misc_data)>0 ):
            self._data_store.update(misc_data, clear=clear)
            if (from_file):
                self._data_store._source = file
        
    def get_data_store(self):
        return self._data_store
        
    def get_credentials_store(self):
        return self._credentials_store
     
    def keys(self):
        return self.get_data_store().keys()
    def __getitem__(self, key):
        return self._data[key]
    def __setitem__(self, key, value):
        self._data[key] = value
    def __len__(self):
        return len(self._data)
    def __iter__(self):
        return iter(self._data)   
        
    def __str__(self):
        output = []
        output.append(self._data_store)
        output.append(self._credentials_store)
        return 'Collective Data Store with '+ (', '.join(output))