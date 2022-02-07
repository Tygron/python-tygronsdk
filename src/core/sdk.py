from . import connectors
from .. import automation

class sdk():

    def __init__( self, settings = {}, **kwargs ):
        self.settings = {};
        self.set_sdk_settings( {**settings,  **kwargs} );
        return;
    
    def set_sdk_settings( self, settings = {} ):
        self.settings = {**self.settings, **settings}
    
    def get_sdk_settings( self ):
        return self.settings;
    
    def create_connector_api( self ):
        conn = connectors.ConnectorTygronApi();
        conn.apply_settings( self.get_sdk_settings() );
        return conn;
    
    def create_connector_geoshare( self ):
        conn = connectors.ConnectorTygronGeoshare();
        conn.apply_settings( self.get_sdk_settings() );
        return conn;
    
    def create_connector_session( self, session_connection = None ):
        conn = connectors.ConnectorTygronSession();
        conn.apply_settings( self.get_sdk_settings() );
        
        if ( session_connection != None ):
            conn.apply_session_connection(session_connection)
            
        return conn;
        
    def create_automation_templating( self ):
        return 