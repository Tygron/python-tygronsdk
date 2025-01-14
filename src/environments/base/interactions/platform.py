from ....core.interactions.interaction_set import InteractionSet

from ..connectors import Connector
from ..data import events, objects

from .... import utilities

import json, re

class Platform(InteractionSet):

    @staticmethod
    def get_maintenance_window( conn: Connector ):
        url = conn.get_url_part_protocol()+conn.get_url_part_host()+'/maintenance'
        
        maintenance_data = conn.request(
            method='GET',
            url = url,
            query_params={}
        ).get_response_body_json()
        
        maintenance_window = objects.MaintenanceWindowData(maintenance_data)
        
        return maintenance_window