from .....core.events import EventSet

from .....core.data.events import EventDefinition
from .....core.data.events import EventParameter

from typing import Type

definitions = {


    # General
        'add' : EventDefinition(
                group='General',
                parameters=[
                        EventParameter('type', ['AREA', 'BUILDING', 'ROAD', 'TERRAIN_HEIGHT', 'WATER_BOTTOM'], aggregation=1, 
                                        api_description='GeoLinkType[]', api_type=['AREA', 'BUILDING', 'ROAD', 'TERRAIN_HEIGHT', 'WATER_BOTTOM'], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('name', Type[str], aggregation=1, 
                                        api_description='String[]', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'duplicate' : EventDefinition(
                group='General',
                parameters=[
                        EventParameter('geolink_id', Type[int], aggregation=1, 
                                        api_description='Geo Links', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'remove' : EventDefinition(
                group='General',
                parameters=[
                        EventParameter('geolink_id', Type[int], aggregation=1, 
                                        api_description='Geo Links', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),


    # Information
        'set_name' : EventDefinition(
                group='Information',
                parameters=[
                        EventParameter('geolink_id', Type[int], aggregation=1, 
                                        api_description='Geo Links', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('name', Type[str], aggregation=1, 
                                        api_description='String[]', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),


    # Feature
        'remove_function' : EventDefinition(
                group='Feature',
                parameters=[
                        EventParameter('geolink_id', Type[int], aggregation=1, 
                                        api_description='Geo Links', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'set_function' : EventDefinition(
                group='Feature',
                parameters=[
                        EventParameter('geolink_id', Type[int], aggregation=1, 
                                        api_description='Geo Links', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('function_id', Type[int], aggregation=1, 
                                        api_description='Functions', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),


    # Geometry
        'set_geometry_mode' : EventDefinition(
                group='Geometry',
                parameters=[
                        EventParameter('geolink_id', Type[int], aggregation=1, 
                                        api_description='Geo Links', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('geometry_mode', ['RADIUS_CENTERPOINT', 'NORMAL'], aggregation=1, 
                                        api_description='GeometryMode[]', api_type=['RADIUS_CENTERPOINT', 'NORMAL'], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'set_line_buffer' : EventDefinition(
                group='Geometry',
                parameters=[
                        EventParameter('geolink_id', Type[int], aggregation=1, 
                                        api_description='Geo Links', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('buffer', Type[float], aggregation=1, 
                                        api_description='double[]', api_type=Type[float], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'set_point_buffer' : EventDefinition(
                group='Geometry',
                parameters=[
                        EventParameter('geolink_id', Type[int], aggregation=1, 
                                        api_description='Geo Links', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('buffer', Type[float], aggregation=1, 
                                        api_description='double[]', api_type=Type[float], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),


    # Mapping
        'remove_mapping' : EventDefinition(
                group='Mapping',
                parameters=[
                        EventParameter('geolink_id', Type[int], aggregation=1, 
                                        api_description='Geo Links', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute', Type[str], aggregation=1, 
                                        api_description='String[]', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'set_mapping' : EventDefinition(
                group='Mapping',
                parameters=[
                        EventParameter('geolink_id', Type[int], aggregation=1, 
                                        api_description='Geo Links', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute', Type[str], aggregation=1, 
                                        api_description='String[]', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('new_attribute', Type[str], aggregation=1, 
                                        api_description='String[]', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'set_priority' : EventDefinition(
                group='Mapping',
                parameters=[
                        EventParameter('geolink_id', Type[int], aggregation=1, 
                                        api_description='Geo Links', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('priority', Type[int], aggregation=1, 
                                        api_description='Integer[]', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),


    # Attribute
        'remove_attribute' : EventDefinition(
                group='Attribute',
                parameters=[
                        EventParameter('geolink_id', Type[int], aggregation=1, 
                                        api_description='Geo Links', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute', Type[str], aggregation=1, 
                                        api_description='String[]', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'remove_attribute_values' : EventDefinition(
                group='Attribute',
                parameters=[
                        EventParameter('geolink_id', Type[int], aggregation=1, 
                                        api_description='Geo Links', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute', Type[str], aggregation=1, 
                                        api_description='String[]', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_value', Type[str], aggregation=2, 
                                        api_description='String[][]', api_type=Type[str], api_required=True, api_default=None, api_aggregation=2,  ),
                    ]
            ),
        'set_attributes' : EventDefinition(
                group='Attribute',
                parameters=[
                        EventParameter('geolink_id', Type[int], aggregation=1, 
                                        api_description='GeoLinks', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute', Type[str], aggregation=1, 
                                        api_description='Attribute Names', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_value', Type[str], aggregation=2, 
                                        api_description='Attribute Values', api_type=Type[str], api_required=True, api_default=None, api_aggregation=2,  ),
                        EventParameter('source_id', Type[int], False, 
                                        api_description='Source (optional)', api_type=Type[int], api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),
    }

event_set = EventSet(definitions, domain='editorgeolink')