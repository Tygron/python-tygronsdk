from ..connectors import Connector
from ..interactions.users import Users

from ....utilities.strings import Strings

import json

class Projects:

    def get_startable_projects( conn: Connector, domain: str ):
        if (domain == None ):
            my_user = Users.get_my_user(conn)
            domain = my_user['domain']
        response = conn.request(
                method='POST',
                url='event/io/get_domain_startable_projects',
                data=[ domain ]
            )
        return response.get_response_body_json()
    
    def get_startable_templates( conn: Connector, domain: str ):
        if (domain == None ):
            my_user = Users.get_my_user(conn)
            domain = my_user['domain']
        response = conn.request(
                method='POST',
                url='event/io/get_domain_startable_templates',
                data=[ domain ]
            )
        return response.get_response_body_json()
    



    @staticmethod
    def get_project( conn: Connector, project_name: str ):
        response = conn.request(
                method='POST',
                url='event/io/get_project_data',
                data=[ project_name ]
            )
        return response.get_response_body_json()
 
    @staticmethod           
    def delete_project( conn: Connector, project_name: str ):
        response = conn.request(
                method='POST',
                url='event/io/trash_project', 
                data=[ project_name, True ]
            );
        if response.is_success():
            return True
        else:
            raise Exception( response );
    @staticmethod           
    def undelete_project( conn: Connector, project_name: str ):
        response = conn.request(
                method='POST',
                url='event/io/trash_project', 
                data=[ project_name, False ]
            );
        if response.is_success():
            return True
        else:
            raise Exception( response );