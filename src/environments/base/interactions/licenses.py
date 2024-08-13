from ....core.interactions.interaction_set import InteractionSet

from ..connectors import Connector
from ..data import events, objects

from .... import utilities

import json, re

class Licenses(InteractionSet):

    @staticmethod
    def get_all_licenses( conn: Connector ):
        url = conn.get_url_part_protocol()+conn.get_url_part_host()+'/licensetable.html'
        
        html_table = conn.request(
            method='GET',
            url = url,
            query_params={'all': 'true'}
        ).get_response_body()
        
        licenses_data_table = utilities.html.parse_html_table_to_dict( html= html_table )
        licenses = {}
        for key, license_data in licenses_data_table.items():
            licenses[utilities.tygron_strings.make_enum_term(key)] = objects.LicenseData(license_data)
        return licenses
    
    @staticmethod
    def get_license( conn: Connector, license:str = None ):
        return Licenses.get_all_licenses(conn).get(license)