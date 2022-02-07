from .connector_tygron import ConnectorTygron

class ConnectorTygronSession(ConnectorTygron):

    def __init__( self ):
        super().__init__();
        self.set_base( 'api/session' );
        return;


        
    def is_ready( self ):
        if ( not self.get_api_token() ):
            raise Exception( 'An API token must be set to communicate with a session.' )



    def set_api_token( self, api_token ):
        self.api_token=api_token
        self.set_query_params({'token': api_token})
    def set_client_token( self, client_token):
        self.client_token=client_token
        
    def set_client_data( self, client_data = {} ):
        self.client_data = client_data
        self.set_client_token(None);
        
    def get_api_token( self ):
        return self.api_token
    def get_client_token( self ):
        return getattr( self, 'client_token', 
                getattr( self.get_client_data(), 'clientToken', None)
            )
    
    def get_client_data( self ):
        return getattr( self, 'client_data', {} )



    def apply_session_connection( self, session_connection = {} ):
        self.set_api_token( session_connection.get( 'apiToken', None ) )
        self.set_client_data( session_connection.get( 'client', None ) )
        self.set_client_token( self.get_client_data().get( 'clientToken', None ) )
    
    
    
    def run_query( self, query:str, value = None ):
        return self.request(
                method='GET',
                url='query/'+query, 
                query_params=None if value is None else {'value': value}
            )
    
    
    
    def stream_upload_geotiff( self, file_data, asset_name:str = None, asset_id:int = None ):
        return self.stream_upload(
                map_link='GEO_TIFFS',
                asset_name=asset_name,
                asset_id=asset_id,
                file_data = file_data
            )      
    def stream_upload( self, file_data, map_link:str='GEO_TIIFS', asset_name:str = None, asset_id:int = None, ):
        if ( not (asset_id or asset_name) ):
            #raise Exception('A streamed asset requires either an asset_name (new assets) or an asset_id (updating assets)')
            pass
            
        query_params = {
            'mapLink' : map_link
        }
        
        if ( asset_id ):
            query_params['id'] = asset_id
        if ( asset_name ):
            query_params['name'] = asset_name
            
        return self.request(
            method='POST',
            url='stream/import',
            query_params=query_params,
            data=file_data,
            stream=True
        )
        