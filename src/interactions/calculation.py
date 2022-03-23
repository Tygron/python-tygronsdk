from ..core.connectors import ConnectorTygronSession
from ..utilities.timing import Timing

import json

class Calculation:

    @staticmethod
    def recalculate( conn_session: ConnectorTygronSession, reset: bool = True ):
        response = conn_session.request(
                method='POST',
                url='event/editorindicator/reset_indicators',
                data=[ reset ]
            )
        return Calculation.wait_for_recalculate( conn_session )
     
    def wait_for_recalculate( conn_session: ConnectorTygronSession ):
        def wait_function():
            try:
                response = conn_session.request(
                        method='POST',
                        url='update',
                        data={"SETTINGS":0}
                    )
                return response.is_success()
            except Exception as err:
                if (err.args[0].get_http_status_code == 504):
                    return None
                raise err
            
        return Timing.wait_for( wait_function )