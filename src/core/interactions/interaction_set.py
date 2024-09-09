from ..connectors import ConnectorTygron








class InteractionSet():
        
    @staticmethod
    def versioned( conn: ConnectorTygron, module ):
        from .... import get_module_version
        versioned_module = get_module_version( module=module, version=conn.get_platform_version() )
        return versioned_module
    
    