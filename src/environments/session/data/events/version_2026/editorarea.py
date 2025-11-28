from ......core.events import EventSet

from ......core.data.events import EventDefinition
from ......core.data.events import EventParameter

from typing import Type

definitions = {


    # General
        'add' : EventDefinition(
                group='General',
                parameters=[
                        EventParameter('amount', Type[int], False, 
                                        api_description='Amount (optional)', api_type=Type[int], api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'add_with_attribute' : EventDefinition(
                group='General',
                parameters=[
                        EventParameter('attribute_name', Type[str], 
                                        api_description='String', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('attribute_values', Type[float], 
                                        api_description='Double', api_type=Type[float], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'duplicate' : EventDefinition(
                group='General',
                parameters=[
                        EventParameter('area_id', Type[int], aggregation=1, 
                                        api_description='Areas', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'remove' : EventDefinition(
                group='General',
                parameters=[
                        EventParameter('area_id', Type[int], aggregation=1, 
                                        api_description='Areas', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'import' : EventDefinition(
                group='General',
                parameters=[
                        EventParameter('geometry_collection', 'Unknown: (geometrycollection with crs: epsg:3857)', 
                                        api_description='Collection of Area geometries', api_type='Unknown: (geometrycollection with crs: epsg:3857)', api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('names', Type[str], aggregation=1, 
                                        api_description='Area Names', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_names', Type[str], aggregation=1, 
                                        api_description='Attribute Names', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_values', Type[float], aggregation=2, 
                                        api_description='Attribute Values', api_type=Type[float], api_required=True, api_default=None, api_aggregation=2,  ),
                        EventParameter('buffer', Type[float], False, 
                                        api_description='Buffer for Points and Lines to make Polygons (optional)', api_type=Type[float], api_required=False, api_default=None, api_aggregation=0,  ),
                        EventParameter('source_id', Type[int], False, 
                                        api_description='Source (optional)', api_type=Type[int], api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Information
        'set_name' : EventDefinition(
                group='Information',
                parameters=[
                        EventParameter('area_id', Type[int], aggregation=1, 
                                        api_description='Areas', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('name', Type[str], aggregation=1, 
                                        api_description='String[]', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'set_color' : EventDefinition(
                group='Information',
                parameters=[
                        EventParameter('area_id', Type[int], aggregation=1, 
                                        api_description='Areas', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('color', 'Unknown: (tcolor or multiple values in array [a, b, c])', aggregation=1, 
                                        api_description='TColor[]', api_type='Unknown: (tcolor or multiple values in array [a, b, c])', api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),


    # Calculation model
        'set_active' : EventDefinition(
                group='Calculation model',
                parameters=[
                        EventParameter('area_id', Type[int], aggregation=1, 
                                        api_description='Areas', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('active', Type[bool], aggregation=1, 
                                        api_description='Boolean[]', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'add_relation' : EventDefinition(
                group='Calculation model',
                parameters=[
                        EventParameter(0, Type[int], 
                                        api_description='Areas', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter(1, ['BORDER_A', 'BORDER_B', 'BUILDING', 'CONSTRUCTOR', 'DEMOLISHER', 'NETOWNER', 'OWNER', 'PARENT', 'PERMITTER', 'RECEIVER', 'RESULT_PARENT', 'SENDER', 'WEATHER'], 
                                        api_description='Relation;{"default": null, "values": ["BORDER_A", "BORDER_B", "BUILDING", "CONSTRUCTOR", "DEMOLISHER", "NETOWNER", "OWNER", "PARENT", "PERMITTER", "RECEIVER", "RESULT_PARENT", "SENDER", "WEATHER"]}', api_type=['BORDER_A', 'BORDER_B', 'BUILDING', 'CONSTRUCTOR', 'DEMOLISHER', 'NETOWNER', 'OWNER', 'PARENT', 'PERMITTER', 'RECEIVER', 'RESULT_PARENT', 'SENDER', 'WEATHER'], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_relation' : EventDefinition(
                group='Calculation model',
                parameters=[
                        EventParameter(0, Type[int], 
                                        api_description='Areas', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter(1, ['BORDER_A', 'BORDER_B', 'BUILDING', 'CONSTRUCTOR', 'DEMOLISHER', 'NETOWNER', 'OWNER', 'PARENT', 'PERMITTER', 'RECEIVER', 'RESULT_PARENT', 'SENDER', 'WEATHER'], 
                                        api_description='Relation;{"default": null, "values": ["BORDER_A", "BORDER_B", "BUILDING", "CONSTRUCTOR", "DEMOLISHER", "NETOWNER", "OWNER", "PARENT", "PERMITTER", "RECEIVER", "RESULT_PARENT", "SENDER", "WEATHER"]}', api_type=['BORDER_A', 'BORDER_B', 'BUILDING', 'CONSTRUCTOR', 'DEMOLISHER', 'NETOWNER', 'OWNER', 'PARENT', 'PERMITTER', 'RECEIVER', 'RESULT_PARENT', 'SENDER', 'WEATHER'], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter(2, Type[int], 
                                        api_description='Integer', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'remove_relations' : EventDefinition(
                group='Calculation model',
                parameters=[
                        EventParameter(0, Type[int], 
                                        api_description='Areas', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter(1, 'Unknown: (relation or multiple values in array [a, b, c])', aggregation=1, 
                                        api_description='Relation[]', api_type='Unknown: (relation or multiple values in array [a, b, c])', api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),


    # Polygon
        'add_polygons' : EventDefinition(
                group='Polygon',
                parameters=[
                        EventParameter('area_id', Type[int], aggregation=1, 
                                        api_description='Areas', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('geometry', 'Unknown: (multipolygon with crs: epsg:3857 or multiple values in array [a, b, c])', aggregation=1, 
                                        api_description='MultiPolygon[]', api_type='Unknown: (multipolygon with crs: epsg:3857 or multiple values in array [a, b, c])', api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'remove_polygons' : EventDefinition(
                group='Polygon',
                parameters=[
                        EventParameter('area_id', Type[int], aggregation=1, 
                                        api_description='Areas', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('geometry', 'Unknown: (multipolygon with crs: epsg:3857 or multiple values in array [a, b, c])', aggregation=1, 
                                        api_description='MultiPolygon[]', api_type='Unknown: (multipolygon with crs: epsg:3857 or multiple values in array [a, b, c])', api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),


    # Attribute
        'set_attributes' : EventDefinition(
                group='Attribute',
                parameters=[
                        EventParameter('area_id', Type[int], aggregation=1, 
                                        api_description='Areas', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_name', Type[str], aggregation=1, 
                                        api_description='Attribute Names', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_value', Type[float], aggregation=2, 
                                        api_description='Attribute Values', api_type=Type[float], api_required=True, api_default=None, api_aggregation=2,  ),
                        EventParameter('source_id', Type[int], False, 
                                        api_description='Source (optional)', api_type=Type[int], api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'remove_attribute' : EventDefinition(
                group='Attribute',
                parameters=[
                        EventParameter('area_id', Type[int], aggregation=1, 
                                        api_description='Areas', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_name', Type[str], aggregation=1, 
                                        api_description='String[]', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'add_group' : EventDefinition(
                group='Attribute',
                parameters=[
                        EventParameter(0, Type[str], 
                                        api_description='Attribute name to group Areas by', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'remove_all_attributes' : EventDefinition(
                group='Attribute',
                parameters=[
                        EventParameter(0, Type[int], aggregation=1, 
                                        api_description='Areas', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'remove_group' : EventDefinition(
                group='Attribute',
                parameters=[
                        EventParameter(0, Type[str], aggregation=1, 
                                        api_description='String[]', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'set_attribute' : EventDefinition(
                group='Attribute',
                parameters=[
                        EventParameter(0, Type[int], aggregation=1, 
                                        api_description='Areas', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter(1, Type[str], 
                                        api_description='Attribute Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter(2, Type[float], aggregation=1, 
                                        api_description='Attribute Values', api_type=Type[float], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter(3, Type[int], False, 
                                        api_description='Source (optional)', api_type=Type[int], api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Generate
        'generate_border_areas' : EventDefinition(
                group='Generate',
                parameters=[
                        EventParameter('attribute_to_generate_for', Type[str], 
                                        api_description='String', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('attribute_to_add', Type[str], 
                                        api_description='String', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('width', Type[float], 
                                        api_description='Double', api_type=Type[float], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'generate_inundation_areas' : EventDefinition(
                group='Generate',
                parameters=[
                        EventParameter('inundation_level_datum', Type[float], 
                                        api_description='Double', api_type=Type[float], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'generate_sewer_areas' : EventDefinition(
                group='Generate',
                parameters=[
                        EventParameter('urbanization', Type[int], 
                                        api_description='Integer', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('storage_before_1965', Type[float], 
                                        api_description='Double', api_type=Type[float], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('storage', Type[float], 
                                        api_description='Double', api_type=Type[float], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('pump_capacity', Type[float], 
                                        api_description='Double', api_type=Type[float], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('water_area_attribute', Type[str], 
                                        api_description='String', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'generate_water_areas' : EventDefinition(
                group='Generate',
                parameters=[
                        EventParameter('inundation_level_datum', Type[float], 
                                        api_description='Double', api_type=Type[float], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # 
        'append_attribute' : EventDefinition(
                group='',
                parameters=[
                        EventParameter('area_id', Type[int], aggregation=1, 
                                        api_description='Areas', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_name', Type[str], 
                                        api_description='Attribute Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('attribute_value', Type[float], aggregation=1, 
                                        api_description='Attribute Values appended to existing values', api_type=Type[float], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('source_id', Type[int], False, 
                                        api_description='Source (optional)', api_type=Type[int], api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),
    }

event_set = EventSet(definitions, domain='editorarea')