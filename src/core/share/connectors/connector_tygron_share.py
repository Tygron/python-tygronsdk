from ...core.connectors.connector_tygron import ConnectorTygron

class ConnectorTygronShare(ConnectorTygron):

    def __init__( self, settings = {}  ):
        super().__init__(settings);
        self.set_base( 'share' );
        return;