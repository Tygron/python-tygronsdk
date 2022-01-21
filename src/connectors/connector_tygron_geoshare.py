from .connector_tygron import ConnectorTygron

class ConnectorTygronGeoshare(ConnectorTygron):

    def __init__( self ):
        super().__init__();
        self.set_base( 'geoshare' );
        return;