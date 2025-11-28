from ......core.events import EventSet

from ......core.data.events import EventDefinition
from ......core.data.events import EventParameter

from typing import Type

definitions = {


    # Creation
        'set_initial_map_size' : EventDefinition(
                group='Creation',
                parameters=[
                        EventParameter('map_width', Type[int], 
                                        api_description='Width of the map', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('map_height', Type[int], 
                                        api_description='Height of the map', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'start_map_creation' : EventDefinition(
                group='Creation',
                parameters=[
                        EventParameter('center_point_x', Type[float], 
                                        api_description='Center point (Longitude or X coordinate)', api_type=Type[float], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('center_point_y', Type[float], 
                                        api_description='Center point (Latitude or Y coordinate)', api_type=Type[float], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('area_to_generate', 'Unknown: (multipolygon with crs: epsg:3857)', False, 
                                        api_description='Optional: Limit data loading to this Polygon', api_type='Unknown: (multipolygon with crs: epsg:3857)', api_required=False, api_default=None, api_aggregation=0,  ),
                        EventParameter('area_of_interest', 'Unknown: (multipolygon with crs: epsg:3857 or multiple values in array [a, b, c])', False, aggregation=1, 
                                        api_description='Optional: Area of Interest Polygons', api_type='Unknown: (multipolygon with crs: epsg:3857 or multiple values in array [a, b, c])', api_required=False, api_default=None, api_aggregation=1,  ),
                    ]
            ),


    # Editor
        'activate_testrun' : EventDefinition(
                group='Editor',
                parameters=[
                        EventParameter('active', Type[bool], 
                                        api_description='Start the Scenario Testrun (false means stop);{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'clear_map' : EventDefinition(
                group='Editor',
                parameters=[
                        EventParameter('clear_georeference', Type[bool], 
                                        api_description='Delete the map size and georeference too (false means deleting only the geodata);{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Calculation
        'update' : EventDefinition(
                group='Calculation',
                parameters=[
                        EventParameter('xqueries', Type[bool], False, 
                                        api_description='Reset all X-Queries (optional)', api_type=Type[bool], api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'update_with_id' : EventDefinition(
                group='Calculation',
                parameters=[
                        EventParameter('xqueries', Type[bool], 
                                        api_description='Reset all X-Queries;{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('recalculation_id', Type[int], 
                                        api_description='Unique Update ID to prevent multiple updates', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_scheduled_update' : EventDefinition(
                group='Calculation',
                parameters=[
                        EventParameter('scheduled_time', Type[int], False, 
                                        api_description='Scheduled time in milliseconds since epoch 1970. Note: use 0 for direct execution or -1 to cancel', api_type=Type[int], api_required=False, api_default=None, api_aggregation=0,  ),
                        EventParameter('email', Type[str], False, 
                                        api_description='Send Email to this address when finished (optional)', api_type=Type[str], api_required=False, api_default=None, api_aggregation=0,  ),
                        EventParameter('sms', Type[str], False, 
                                        api_description='Send SMS to this number when finished (optional)', api_type=Type[str], api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),
    }

event_set = EventSet(definitions, domain='editor')