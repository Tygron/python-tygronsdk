from .connector_tygron import ConnectorTygron

class ConnectorTygronApi(ConnectorTygron):

    def __init__( self ):
        super().__init__()
        self.set_base( 'api' )
        return;