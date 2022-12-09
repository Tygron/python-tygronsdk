from ..connectors import Connector

import json

class Users:

    @staticmethod
    def get_my_user( conn: Connector ):
        response = conn.request(
            method='GET',
            url='myuser'
        )
        return response.get_response_body_json()