from ....core.interactions.interaction_set import InteractionSet

from ..connectors import Connector
from ..data import events, objects

from ..interactions.licenses import Licenses

import json

class Domains(InteractionSet):

    @staticmethod
    def get_domain( conn: Connector ):
        response = conn.request(
            method='GET',
            url='myuser/domain'
        )
        return objects.DomainData( response.get_response_body_json() )

    @staticmethod 
    def get_domain_license( conn: Connector ):
        domain = Domains.get_domain(conn)
        license =  Licenses.get_license(conn, domain.license)
        license = license.create_custom_license(domain.license_variables)
        return license


    @staticmethod
    # If subdomain does not exist, it will report 0. If no subdomain is provided, it will report 0.
    def get_domain_usage( conn: Connector, subdomain: str = None ):
        versioned_events = InteractionSet.versioned(conn, events)
        
        domain_name = Domains.get_domain(conn).name
        
        response = conn.fire_event( versioned_events.io.get_domain_usage(domain_name, subdomain ) )
        
        usage = objects.UsageData(response.get_response_body_json())
        
        return usage
    
    
    @staticmethod
    def get_domain_allowance( conn: Connector, subdomain: str = None, license: objects.LicenseData = None, usage: objects.UsageData = None ):
        if ( license is None ):
            license = Domains.get_domain_license( conn )
        if ( usage is None ):
            if ( subdomain is None):
                usage = Domains.get_domain_usage( conn )
            else:
                usage = Domains.get_domain_usage( conn, subdomain )

        return objects.AllowanceData( license=license, usage=usage )