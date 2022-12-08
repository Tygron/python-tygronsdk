from ...core.connectors.connector_tygron import ConnectorTygron

class ConnectorTygronApi(ConnectorTygron):

    def __init__( self, settings = {} ):
        super().__init__(settings)
        self.set_base( 'api' )
        return;
        
    def authenticate( self ):
    
        try:
            response = self.request(
                method='GET',
                url='event/user/get_my_login_key'
            )
            if ( response.is_success() ):
                return True
        except Exception as err:
            pass
            
        try:
            response = self.request(
                method='GET',
                url='event/user/get_my_hash_key'
            )
            if ( response.is_success() ):
                return True
        except Exception as err:
            pass
            
        return False