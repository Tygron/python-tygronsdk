from ..core.connectors import ConnectorTygronApi
from ..interactions.user import User

import json

class Domain:

    @staticmethod
    # If subdomain does not exist, it will report 0. If no subdomain is provided, it will report 0.
    def get_domain_usage( conn_api: ConnectorTygronApi, domain: str = None, subdomain: str = None ):
        if (not domain == None ):
            my_user = User.get_my_user(conn_api)
            domain = my_user['domain']
            
        response = conn_api.request(
            method='POST',
            url='event/io/get_domain_usage',
            data=[ domain, subdomain ]
        )
        
        usage = response.get_response_body_json()
        return {
            'new_project_count': usage[0],
            'project_count': usage[1],
            'domain_area': usage[2],
            'subdomain_area': usage[3],
            'geoshare_usage': usage[4]
        }