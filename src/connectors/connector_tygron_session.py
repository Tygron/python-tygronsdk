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