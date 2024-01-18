from ...utilities.connectors import Connector

import base64

class ConnectorTygron(Connector):

    def __init__( self, settings = {}  ):
        super().__init__()
        
        self.settings = {
            'platform' : 'engine',
            'query_params' : {'f':'JSON'},
            'request_format' : 'JSON'
        }
        self.settings = settings
        
        self.set_exception_on_error(True)
        return

    @property
    def settings(self):
        raise NotImplementedError()

    @settings.setter
    def settings(self, value: dict):
        if ( 'host' in value ):
            self.set_host(value['host'])
        elif ( 'server' in value ):
            self.set_host(value['server'])
        elif ( 'platform' in value ):
            self.set_platform(value['platform'])
        
        if ( 'query_params' in value ):
            self.set_query_params(value['query_params'])
        if ( 'request_format' in value ):
            self.set_request_format(value['request_format'])
    
    def authenticate():
        return False
    
    def set_platform( self, platform ):
        self.set_host( platform + '.tygron.com' )
        
    def get_platform( self ):
        if ( '.tygron.com' in self.get_host() ):
            return self.get_host().replace('.tygron.com', '')
    
    def fire_event( self, event, **kwargs ):
        response =  self.request(
            method='POST',
            url='event/'+event.get_path(),
            data=event.get_arguments(),
                **kwargs
            )
        return response