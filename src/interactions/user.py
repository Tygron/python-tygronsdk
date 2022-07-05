from ..core.connectors import ConnectorTygronApi

import json

class User:

    @staticmethod
    def get_my_user( conn_api: ConnectorTygronApi ):
        response = conn_api.request(
            method='GET',
            url='myuser'
        )
        return response.get_response_body_json()