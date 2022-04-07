from ..core.connectors import ConnectorTygronSession
from ..utilities.strings import Strings

import json

class Session:

    @staticmethod
    def ping_session( conn_session: ConnectorTygronSession, timeout_in_seconds:int = 30 ):
        try:
            #Pinging a session with a small, instantly completing, request to appropriate endpoint
            response = conn_session.request(
                    method='POST',
                    url='update',
                    data={'ZOOMLEVELS':0},
                    timeout=timeout_in_seconds
                )
            return response.is_success()
        except Exception as err:
            return False
        return False