from ..connectors import Connector
from ..data import events

from ..interactions.users import Users

import json

class Domains:

    @staticmethod
    # If subdomain does not exist, it will report 0. If no subdomain is provided, it will report 0.
    def get_domain_usage( conn: Connector, subdomain: str = None ):
        domain = Users.get_my_domain_name(conn)
            
        response = conn.request(
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