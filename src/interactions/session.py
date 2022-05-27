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

    @staticmethod        
    def get_session_data( conn_session: ConnectorTygronSession ):
        response = conn_session.request(
                method='GET',
                url='info'
            ).get_response_body_json()
        return response

    @staticmethod    
    def is_session_state_editing( conn_session: ConnectorTygronSession ):
        session_data = Session.get_session_data( conn_session )
        return ( (session_data['type'] == 'EDITOR') and (session_data['state'] == 'NORMAL') )
        
    @staticmethod
    def is_session_state_map_selection( conn_session: ConnectorTygronSession ):
        session_data = Session.get_session_data( conn_session )
        return ( (session_data['type'] == 'EDITOR') and (session_data['state'] == 'GEO_WIZARD') )
        
    @staticmethod
    def is_session_state_testrun( conn_session: ConnectorTygronSession ):
        session_data = Session.get_session_data( conn_session )
        return ( (session_data['type'] == 'EDITOR') and (session_data['state'] == 'TESTRUN') )
        
    @staticmethod
    def is_session_state_session( conn_session: ConnectorTygronSession ):
    
        session_data = Session.get_session_data( conn_session )
        if ( (session_data['type'] == 'EDITOR') and (session_data['state'] == 'TESTRUN') ):
            return True
        if ( (session_data['type'] == 'SINGLE') and (session_data['state'] == 'NORMAL') ):
            return True
        if ( (session_data['type'] == 'MULTI') and (session_data['state'] == 'NORMAL') ):
            return True
        
        