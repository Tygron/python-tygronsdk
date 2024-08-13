from ..connectors import ConnectorTygron








class InteractionSet():
        
    @staticmethod
    def versioned( conn: ConnectorTygron, module ):
        return module._get_platform_version( conn.get_platform_version() )
    
    