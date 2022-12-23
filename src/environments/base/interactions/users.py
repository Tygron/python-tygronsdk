from ..connectors import Connector
from ..data.objects import User
from ..data.objects import Domain
import json

class Users:

    @staticmethod
    def get_my_user( conn: Connector ):
        response = conn.request(
            method='GET',
            url='myuser'
        )
        return User( response.get_response_body_json() )
        
    @staticmethod
    def get_my_domain( conn: Connector ):
        response = conn.request(
            method='GET',
            url='myuser/domain'
        )
        return Domain( response.get_response_body_json() )
        
    @staticmethod
    def get_my_domain_name( conn: Connector ):
        my_user = Users.get_my_user(conn)
        domain = my_user.domain
        
        return domain
        
    @staticmethod
    def get_my_sub_domain_name( conn: Connector, noneIfRoot:bool = True ):
        my_user = Users.get_my_user(conn)
        if ( NoneIfRoot and my_user.has_root_domain_access() ):
            return None
        return my_user.sub_domain