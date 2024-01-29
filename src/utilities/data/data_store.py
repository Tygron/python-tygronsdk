from ..files import Files

import json, base64

class DataStore():

    def __init__( self, data:dict = None, file:str = None ):
        self._data = {}
        self._source = None
        self.update( 
                data=data,
                file=file
            )
    
    @staticmethod
    def create( file:str = None ):
        return DataStore( file=file )
        
    @property
    def source(self):
        return self._source
    
    def clear( self ):
        self._data = {}
        self._source = None
    
    def update( self, data:dict = None, clear:bool = False, file:str = None, **kwargs ):
        if ( clear ):
            self.clear()
        
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
 
        self._data.update( self.parse_keys(data) )
        
        if ( from_file ):
            self._source = file
            
    def parse_keys( self, data ):
        return self.decode_keys(data)
    
    def decode_keys( self, data ):
        new_data = {}
        for key, value in data.items():
            decoded_data = self.decode_base64_key(key, value)
            if ( len(decoded_data) > 0 ):
                new_data.update( decoded_data )
            else:
                new_data[key] = value
        return new_data
    
    def decode_base64_key( self, key, value ):
        b64term = 'base64'  if ( key.find('base64') >=0 )  else None
        b64term = 'b64'     if ( key.find('b64')    >=0 )  else b64term
        
        if ( b64term is None ):
            return {}
        try:
            decoded_value = base64.b64decode(value.encode('ASCII')).decode('ASCII')
        except UnicodeDecodeError:
            return {}
            
        b64_removable_term = '_'+b64term+'_' if ( key.find('_'+b64term+'_') >=0 ) else None
        replacement_term = '' if b64_removable_term is None else '_'
        if ( (b64_removable_term is None) and (key.find('_'+b64term) >=0) ):
            b64_removable_term = '_'+b64term
        if ( (b64_removable_term is None) and (key.find(b64term+'_') >=0) ):
            b64_removable_term = b64term+'_'
        
        proper_key = key.replace( b64_removable_term, replacement_term )
        
        return { proper_key : decoded_value}
        
    def load_from_file( self, file:str = None ):
        if ( file is None ):
            return None
        try:
            data = Files.read_file_as_json( file )
        except json.decoder.JSONDecodeError:
            data = Files.read_file_as_key_values( file )
        return data
    
    def get(self, key, default=None):
        return self._data.get(key,default)
        
    def data(self):
        return self._data
        
    def keys(self):
        return self.data()
    def __getitem__(self, key):
        return self._data[key]
    def __setitem__(self, key, value):
        self._data[key] = value
    def __len__(self):
        return len(self._data)
    def __iter__(self):
        return iter(self._data)
        
    def __str__(self):
        return 'DataStore with: ' + str( len(self._data) ) + ' entries'