from ....core.interactions.interaction_set import InteractionSet

from ..connectors import Connector
from ..data import objects

from ..interactions.domains import Domains

import json

class Users(InteractionSet):

    @staticmethod
    def get_my_user( conn: Connector ):
        response = conn.request(
            method='GET',
            url='myuser'
        )
        return objects.UserData( response.get_response_body_json() )
        
    @staticmethod
    def get_my_domain( conn: Connector ):
        return Domains.get_domain( conn )
    
    @staticmethod
    def get_my_license( conn: Connector ):
        return Domains.get_domain_license( conn )
    
    
    @staticmethod
    def get_my_domain_name( conn: Connector ):
        my_user = Users.get_my_user(conn)
        domain_name = my_user.domain
        
        return domain_name
        
    @staticmethod
    def get_my_sub_domain_name( conn: Connector, none_if_root:bool = True ):
        my_user = Users.get_my_user(conn)
        if ( none_if_root and my_user.has_root_domain_access() ):
            return None
        return my_user.sub_domain
        
        
    @staticmethod
    def get_my_domain_usage( conn: Connector, subdomain:str = None ):
        return Domains.get_domain_usage( conn, subdomain )
        