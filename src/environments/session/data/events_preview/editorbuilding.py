from .....core.events import EventSet

from .....core.data.events import EventDefinition
from .....core.data.events import EventParameter

from typing import Type

definitions = {


    # General
        'add' : EventDefinition(
                group='General',
                parameters=[
                        EventParameter('owner', Type[int], aggregation=1, 
                                        api_description='Stakeholders', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('function_id', Type[int], aggregation=1, 
                                        api_description='Functions', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('name', Type[str], aggregation=1, 
                                        api_description='String[]', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'add_standard' : EventDefinition(
                group='General',
                parameters=[
                        EventParameter('owner', Type[int], 
                                        api_description='Stakeholders', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'add_road' : EventDefinition(
                group='General',
                parameters=[
                        EventParameter('owner', Type[int], 
                                        api_description='Stakeholders', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'add_underground' : EventDefinition(
                group='General',
                parameters=[
                        EventParameter('owner', Type[int], 
                                        api_description='Stakeholders', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'duplicate' : EventDefinition(
                group='General',
                parameters=[
                        EventParameter('building_id', Type[int], aggregation=1, 
                                        api_description='Buildings', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'import' : EventDefinition(
                group='General',
                parameters=[
                        EventParameter('geometry_collection', 'Unknown: (geometrycollection with crs: epsg:3857)', 
                                        api_description='Collection of Building geometries', api_type='Unknown: (geometrycollection with crs: epsg:3857)', api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('names', Type[str], aggregation=1, 
                                        api_description='Building Names', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_names', Type[str], aggregation=1, 
                                        api_description='Attribute Names', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_values', Type[float], aggregation=2, 
                                        api_description='Attribute Values', api_type=Type[float], api_required=True, api_default=None, api_aggregation=2,  ),
                        EventParameter('functions', Type[int], aggregation=1, 
                                        api_description='Functions', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('owners', Type[int], aggregation=1, 
                                        api_description='Owners', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('buffer_m', Type[float], False, 
                                        api_description='Buffer for Points and Lines to make Polygons (optional)', api_type=Type[float], api_required=False, api_default=None, api_aggregation=0,  ),
                        EventParameter('source_id', Type[int], False, 
                                        api_description='Source (optional)', api_type=Type[int], api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'remove' : EventDefinition(
                group='General',
                parameters=[
                        EventParameter('building_id', Type[int], aggregation=1, 
                                        api_description='Buildings', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),


    # Sections
        'add_section' : EventDefinition(
                group='Sections',
                parameters=[
                        EventParameter('building_id', Type[int], aggregation=1, 
                                        api_description='Buildings', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'duplicate_sections' : EventDefinition(
                group='Sections',
                parameters=[
                        EventParameter('building_id', Type[int], aggregation=1, 
                                        api_description='Buildings', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('section_id', Type[int], aggregation=1, 
                                        api_description='Integer[]', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'remove_sections' : EventDefinition(
                group='Sections',
                parameters=[
                        EventParameter('building_id', Type[int], aggregation=1, 
                                        api_description='Buildings', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('section_id', Type[int], aggregation=1, 
                                        api_description='Integer[]', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'set_floors' : EventDefinition(
                group='Sections',
                parameters=[
                        EventParameter('building_id', Type[int], aggregation=1, 
                                        api_description='Building ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('section_id', Type[int], aggregation=1, 
                                        api_description='Section ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('floors', Type[int], aggregation=1, 
                                        api_description='Number of floors', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'reset_slanting_roof_height' : EventDefinition(
                group='Sections',
                parameters=[
                        EventParameter('building_id', Type[int], 
                                        api_description='Building ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('section_id', Type[int], 
                                        api_description='Section ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_slanting_roof_height' : EventDefinition(
                group='Sections',
                parameters=[
                        EventParameter('building_id', Type[int], 
                                        api_description='Building ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('section_id', Type[int], 
                                        api_description='Section ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('slanting_roof_height', Type[float], 
                                        api_description='Slanting roof height', api_type=Type[float], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Polygon
        'add_polygons' : EventDefinition(
                group='Polygon',
                parameters=[
                        EventParameter('building_id', Type[int], aggregation=1, 
                                        api_description='Building ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('section_id', Type[int], aggregation=1, 
                                        api_description='Section ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('polygon', 'Unknown: (multipolygon with crs: epsg:3857 or multiple values in array [a, b, c])', aggregation=1, 
                                        api_description='MultiPolygon', api_type='Unknown: (multipolygon with crs: epsg:3857 or multiple values in array [a, b, c])', api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('largest_owner', Type[bool], 
                                        api_description='Use largest Owner;{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'remove_polygons' : EventDefinition(
                group='Polygon',
                parameters=[
                        EventParameter('building_id', Type[int], aggregation=1, 
                                        api_description='Building ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('section_id', Type[int], aggregation=1, 
                                        api_description='Section ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('polygon', 'Unknown: (multipolygon with crs: epsg:3857)', 
                                        api_description='MultiPolygon', api_type='Unknown: (multipolygon with crs: epsg:3857)', api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'add_geometry' : EventDefinition(
                group='Polygon',
                parameters=[
                        EventParameter('building_id', Type[int], aggregation=1, 
                                        api_description='Building ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('geometry_id', Type[int], aggregation=1, 
                                        api_description='Custom Geometry ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('primary_building', 'Unknown: (boolean or multiple values in array [a, b, c])', aggregation=1, 
                                        api_description='Primary building for geometry', api_type='Unknown: (boolean or multiple values in array [a, b, c])', api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('source_id', Type[int], False, 
                                        api_description='Source (optional)', api_type=Type[int], api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'remove_geometries' : EventDefinition(
                group='Polygon',
                parameters=[
                        EventParameter('building_id', Type[int], aggregation=1, 
                                        api_description='Building ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),


    # Attribute
        'set_attribute' : EventDefinition(
                group='Attribute',
                parameters=[
                        EventParameter('building_id', Type[int], aggregation=1, 
                                        api_description='Buildings', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_name', Type[str], 
                                        api_description='Attribute Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('attribute_value', Type[float], aggregation=1, 
                                        api_description='Attribute Values', api_type=Type[float], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('source_id', Type[int], False, 
                                        api_description='Source (optional)', api_type=Type[int], api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_attributes' : EventDefinition(
                group='Attribute',
                parameters=[
                        EventParameter('building_id', Type[int], aggregation=1, 
                                        api_description='Buildings', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_names', Type[str], aggregation=1, 
                                        api_description='Attribute Names', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_values', Type[float], aggregation=2, 
                                        api_description='Attribute Values', api_type=Type[float], api_required=True, api_default=None, api_aggregation=2,  ),
                        EventParameter('source_id', Type[int], False, 
                                        api_description='Source (optional)', api_type=Type[int], api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'remove_attribute' : EventDefinition(
                group='Attribute',
                parameters=[
                        EventParameter('building_id', Type[int], aggregation=1, 
                                        api_description='Buildings', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_name', Type[str], aggregation=1, 
                                        api_description='String[]', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'generate_rotation_angles' : EventDefinition(
                group='Attribute',
                parameters=[
                        EventParameter('attribute_for_filter', Type[str], 
                                        api_description='Identifying attribute', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('attribute_for_value', Type[str], 
                                        api_description='Rotation attribute', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('building_ids', Type[int], False, aggregation=1, 
                                        api_description='Specific buildingIDs only (optional)', api_type=Type[int], api_required=False, api_default=None, api_aggregation=1,  ),
                    ]
            ),


    # Calculation model
        'set_function' : EventDefinition(
                group='Calculation model',
                parameters=[
                        EventParameter('building_id', Type[int], aggregation=1, 
                                        api_description='Buildings', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('function_id', Type[int], aggregation=1, 
                                        api_description='Functions', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'set_function_value' : EventDefinition(
                group='Calculation model',
                parameters=[
                        EventParameter('building_id', Type[int], 
                                        api_description='Buildings', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('function_value_name', ['ALIGN_ELEVATION', 'BASEMENT_COLOR', 'BASEMENT_HEIGHT_M', 'BOWEN_RATIO', 'CRITICAL_INFRASTRUCTURE', 'DEFAULT_FLOORS', 'DISTANCE_ZONE_M', 'DISTURBANCE_DISTANCE_M', 'DRAINAGE', 'EXTRA_COLOR', 'FLOOR_HEIGHT_M', 'FOLIAGE_CROWN_FACTOR', 'GROUND_COLOR', 'GROUND_INFILTRATION_MD', 'HEAT_EFFECT', 'HEIGHT_OFFSET_M', 'JAM_FACTOR_BUSES', 'JAM_FACTOR_CARS', 'JAM_FACTOR_TRUCKS', 'JAM_FACTOR_VANS', 'LIVABILITY_EFFECT', 'MAX_FLOORS', 'MIN_FLOORS', 'MONUMENTAL', 'NUM_AIRPLANES', 'NUM_BICYCLES', 'NUM_BUSES', 'NUM_CARS', 'NUM_PEDESTRIANS', 'NUM_SHIPS', 'NUM_TRAINS', 'NUM_TRAMS', 'NUM_TRUCKS', 'NUM_VANS', 'PIPES_PERMITTED', 'ROOF_COLOR', 'ROOT_DEPTH_M', 'SAFETY_DISTANCE_M', 'SEWERED', 'SLANTING_ROOF_HEIGHT', 'SOLAR_PANELS', 'SOLID', 'TERRAIN_MIX', 'TOP_COLOR', 'TRAFFIC_LANES', 'TRAFFIC_NOISE_SIGMA', 'TRAFFIC_NOISE_TAU', 'TRAFFIC_SPEED', 'VEGETATION_FRACTION', 'WATER_EVAPORATION_FACTOR', 'WATER_MANNING', 'WATER_MICRORELIEF_M', 'WATER_STORAGE_M2', 'ZONING_PERMIT_REQUIRED'], 
                                        api_description='FunctionValue;{"default": null, "values": ["ALIGN_ELEVATION", "BASEMENT_COLOR", "BASEMENT_HEIGHT_M", "BOWEN_RATIO", "CRITICAL_INFRASTRUCTURE", "DEFAULT_FLOORS", "DISTANCE_ZONE_M", "DISTURBANCE_DISTANCE_M", "DRAINAGE", "EXTRA_COLOR", "FLOOR_HEIGHT_M", "FOLIAGE_CROWN_FACTOR", "GROUND_COLOR", "GROUND_INFILTRATION_MD", "HEAT_EFFECT", "HEIGHT_OFFSET_M", "JAM_FACTOR_BUSES", "JAM_FACTOR_CARS", "JAM_FACTOR_TRUCKS", "JAM_FACTOR_VANS", "LIVABILITY_EFFECT", "MAX_FLOORS", "MIN_FLOORS", "MONUMENTAL", "NUM_AIRPLANES", "NUM_BICYCLES", "NUM_BUSES", "NUM_CARS", "NUM_PEDESTRIANS", "NUM_SHIPS", "NUM_TRAINS", "NUM_TRAMS", "NUM_TRUCKS", "NUM_VANS", "PIPES_PERMITTED", "ROOF_COLOR", "ROOT_DEPTH_M", "SAFETY_DISTANCE_M", "SEWERED", "SLANTING_ROOF_HEIGHT", "SOLAR_PANELS", "SOLID", "TERRAIN_MIX", "TOP_COLOR", "TRAFFIC_LANES", "TRAFFIC_NOISE_SIGMA", "TRAFFIC_NOISE_TAU", "TRAFFIC_SPEED", "VEGETATION_FRACTION", "WATER_EVAPORATION_FACTOR", "WATER_MANNING", "WATER_MICRORELIEF_M", "WATER_STORAGE_M2", "ZONING_PERMIT_REQUIRED"]}', api_type=['ALIGN_ELEVATION', 'BASEMENT_COLOR', 'BASEMENT_HEIGHT_M', 'BOWEN_RATIO', 'CRITICAL_INFRASTRUCTURE', 'DEFAULT_FLOORS', 'DISTANCE_ZONE_M', 'DISTURBANCE_DISTANCE_M', 'DRAINAGE', 'EXTRA_COLOR', 'FLOOR_HEIGHT_M', 'FOLIAGE_CROWN_FACTOR', 'GROUND_COLOR', 'GROUND_INFILTRATION_MD', 'HEAT_EFFECT', 'HEIGHT_OFFSET_M', 'JAM_FACTOR_BUSES', 'JAM_FACTOR_CARS', 'JAM_FACTOR_TRUCKS', 'JAM_FACTOR_VANS', 'LIVABILITY_EFFECT', 'MAX_FLOORS', 'MIN_FLOORS', 'MONUMENTAL', 'NUM_AIRPLANES', 'NUM_BICYCLES', 'NUM_BUSES', 'NUM_CARS', 'NUM_PEDESTRIANS', 'NUM_SHIPS', 'NUM_TRAINS', 'NUM_TRAMS', 'NUM_TRUCKS', 'NUM_VANS', 'PIPES_PERMITTED', 'ROOF_COLOR', 'ROOT_DEPTH_M', 'SAFETY_DISTANCE_M', 'SEWERED', 'SLANTING_ROOF_HEIGHT', 'SOLAR_PANELS', 'SOLID', 'TERRAIN_MIX', 'TOP_COLOR', 'TRAFFIC_LANES', 'TRAFFIC_NOISE_SIGMA', 'TRAFFIC_NOISE_TAU', 'TRAFFIC_SPEED', 'VEGETATION_FRACTION', 'WATER_EVAPORATION_FACTOR', 'WATER_MANNING', 'WATER_MICRORELIEF_M', 'WATER_STORAGE_M2', 'ZONING_PERMIT_REQUIRED'], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('function_value_value', Type[float], aggregation=1, 
                                        api_description='double[]', api_type=Type[float], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'set_category_value' : EventDefinition(
                group='Calculation model',
                parameters=[
                        EventParameter('building_id', Type[int], 
                                        api_description='Buildings', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('category', ['AGRICULTURE', 'BRIDGE', 'EDUCATION', 'GARDEN', 'HEALTHCARE', 'INDUSTRY', 'INTERSECTION', 'LEISURE', 'LUXE', 'NATURE', 'NORMAL', 'OFFICES', 'OTHER', 'PARK', 'PAVED_AREA', 'ROAD', 'SENIOR', 'SHOPPING', 'SOCIAL', 'STUDENT', 'UNDERGROUND'], 
                                        api_description='Category;{"default": null, "values": ["AGRICULTURE", "BRIDGE", "EDUCATION", "GARDEN", "HEALTHCARE", "INDUSTRY", "INTERSECTION", "LEISURE", "LUXE", "NATURE", "NORMAL", "OFFICES", "OTHER", "PARK", "PAVED_AREA", "ROAD", "SENIOR", "SHOPPING", "SOCIAL", "STUDENT", "UNDERGROUND"]}', api_type=['AGRICULTURE', 'BRIDGE', 'EDUCATION', 'GARDEN', 'HEALTHCARE', 'INDUSTRY', 'INTERSECTION', 'LEISURE', 'LUXE', 'NATURE', 'NORMAL', 'OFFICES', 'OTHER', 'PARK', 'PAVED_AREA', 'ROAD', 'SENIOR', 'SHOPPING', 'SOCIAL', 'STUDENT', 'UNDERGROUND'], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('category_value_name', ['BUYOUT_COST_M2', 'CATEGORY_WEIGHT', 'CONSTRUCTION_COST_M2', 'DEMOLISH_COST_M2', 'HEAT_FLOW_M2_CHANGE_PER_YEAR', 'HEAT_FLOW_M2_START_VALUE', 'HEAT_FLOW_M2_START_YEAR', 'HEAT_POWER_TO_FLOW_MULTIPLIER', 'PARKING_LOTS_DEMAND_PER_M2', 'PARKING_LOTS_PER_M2', 'SELL_PRICE_M2', 'UNIT_SIZE_M2'], 
                                        api_description='CategoryValue;{"default": null, "values": ["BUYOUT_COST_M2", "CATEGORY_WEIGHT", "CONSTRUCTION_COST_M2", "DEMOLISH_COST_M2", "HEAT_FLOW_M2_CHANGE_PER_YEAR", "HEAT_FLOW_M2_START_VALUE", "HEAT_FLOW_M2_START_YEAR", "HEAT_POWER_TO_FLOW_MULTIPLIER", "PARKING_LOTS_DEMAND_PER_M2", "PARKING_LOTS_PER_M2", "SELL_PRICE_M2", "UNIT_SIZE_M2"]}', api_type=['BUYOUT_COST_M2', 'CATEGORY_WEIGHT', 'CONSTRUCTION_COST_M2', 'DEMOLISH_COST_M2', 'HEAT_FLOW_M2_CHANGE_PER_YEAR', 'HEAT_FLOW_M2_START_VALUE', 'HEAT_FLOW_M2_START_YEAR', 'HEAT_POWER_TO_FLOW_MULTIPLIER', 'PARKING_LOTS_DEMAND_PER_M2', 'PARKING_LOTS_PER_M2', 'SELL_PRICE_M2', 'UNIT_SIZE_M2'], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('category_value_value', Type[float], aggregation=1, 
                                        api_description='double[]', api_type=Type[float], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'reset_category_values' : EventDefinition(
                group='Calculation model',
                parameters=[
                        EventParameter('building_id', Type[int], 
                                        api_description='Buildings', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('category', ['AGRICULTURE', 'BRIDGE', 'EDUCATION', 'GARDEN', 'HEALTHCARE', 'INDUSTRY', 'INTERSECTION', 'LEISURE', 'LUXE', 'NATURE', 'NORMAL', 'OFFICES', 'OTHER', 'PARK', 'PAVED_AREA', 'ROAD', 'SENIOR', 'SHOPPING', 'SOCIAL', 'STUDENT', 'UNDERGROUND'], 
                                        api_description='Category;{"default": null, "values": ["AGRICULTURE", "BRIDGE", "EDUCATION", "GARDEN", "HEALTHCARE", "INDUSTRY", "INTERSECTION", "LEISURE", "LUXE", "NATURE", "NORMAL", "OFFICES", "OTHER", "PARK", "PAVED_AREA", "ROAD", "SENIOR", "SHOPPING", "SOCIAL", "STUDENT", "UNDERGROUND"]}', api_type=['AGRICULTURE', 'BRIDGE', 'EDUCATION', 'GARDEN', 'HEALTHCARE', 'INDUSTRY', 'INTERSECTION', 'LEISURE', 'LUXE', 'NATURE', 'NORMAL', 'OFFICES', 'OTHER', 'PARK', 'PAVED_AREA', 'ROAD', 'SENIOR', 'SHOPPING', 'SOCIAL', 'STUDENT', 'UNDERGROUND'], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('vategory_value_name', 'Unknown: (categoryvalue or multiple values in array [a, b, c])', aggregation=1, 
                                        api_description='CategoryValue[]', api_type='Unknown: (categoryvalue or multiple values in array [a, b, c])', api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'reset_function_values' : EventDefinition(
                group='Calculation model',
                parameters=[
                        EventParameter('building_id', Type[int], 
                                        api_description='Buildings', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('function_value_name', 'Unknown: (functionvalue or multiple values in array [a, b, c])', aggregation=1, 
                                        api_description='FunctionValue[]', api_type='Unknown: (functionvalue or multiple values in array [a, b, c])', api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),


    # Generate
        'generate_water_connection' : EventDefinition(
                group='Generate',
                parameters=[
                        EventParameter('function_id', Type[int], 
                                        api_description='Function', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('area_to_generate', 'Unknown: (multipolygon with crs: epsg:3857)', 
                                        api_description='Area', api_type='Unknown: (multipolygon with crs: epsg:3857)', api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('min_length', Type[float], 
                                        api_description='Min Length', api_type=Type[float], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('max_length', Type[float], 
                                        api_description='Max Length', api_type=Type[float], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('width', Type[float], 
                                        api_description='Width', api_type=Type[float], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('large_road_area_threshold', Type[float], 
                                        api_description='Large Road Area', api_type=Type[float], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('large_road_straight_distance', Type[float], 
                                        api_description='Straight Distance', api_type=Type[float], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('max_height_different', Type[float], 
                                        api_description='Max Height Difference', api_type=Type[float], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('ignore_upstream', Type[float], 
                                        api_description='Ignore Upstream', api_type=Type[float], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('include_water_bodies', Type[bool], 
                                        api_description='Include Water Bodies;{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # 
        'multi_select' : EventDefinition(
                group='',
                parameters=[
                        EventParameter('function_id', Type[int], 
                                        api_description='Functions', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('floors', Type[int], 
                                        api_description='Integer', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('merge', Type[bool], 
                                        api_description='Boolean;{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('building_id', Type[int], aggregation=1, 
                                        api_description='Buildings', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'query' : EventDefinition(
                group='',
                parameters=[
                        EventParameter('query', Type[str], 
                                        api_description='TQL Query Statement', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('value', Type[float], False, aggregation=1, 
                                        api_description='Value for update queries (optional)', api_type=Type[float], api_required=False, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'append_attribute' : EventDefinition(
                group='',
                parameters=[
                        EventParameter('building_id', Type[int], aggregation=1, 
                                        api_description='Buildings', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_name', Type[str], 
                                        api_description='Attribute Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('attribute_value', Type[float], aggregation=1, 
                                        api_description='Attribute Values appended to existing values', api_type=Type[float], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('source_id', Type[int], False, 
                                        api_description='Source (optional)', api_type=Type[int], api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Information
        'set_name' : EventDefinition(
                group='Information',
                parameters=[
                        EventParameter('building_id', Type[int], aggregation=1, 
                                        api_description='Buildings', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('name', Type[str], aggregation=1, 
                                        api_description='String[]', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'set_owner' : EventDefinition(
                group='Information',
                parameters=[
                        EventParameter('building_id', Type[int], 
                                        api_description='Buildings', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('stakeholder_id', Type[int], 
                                        api_description='Stakeholders', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_vacant' : EventDefinition(
                group='Information',
                parameters=[
                        EventParameter('building_id', Type[int], 
                                        api_description='Buildings', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('vacant', Type[bool], 
                                        api_description='Boolean;{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_decals' : EventDefinition(
                group='Information',
                parameters=[
                        EventParameter('building_id', Type[int], 
                                        api_description='Buildings', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('decal_type', ['BASEMENT', 'EXTRA', 'GROUND', 'ROOF', 'TOP'], 
                                        api_description='FaceType;{"default": null, "values": ["BASEMENT", "EXTRA", "GROUND", "ROOF", "TOP"]}', api_type=['BASEMENT', 'EXTRA', 'GROUND', 'ROOF', 'TOP'], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('decal_values', Type[float], False, aggregation=1, 
                                        api_description='float[]', api_type=Type[float], api_required=False, api_default=None, api_aggregation=1,  ),
                    ]
            ),
    }

event_set = EventSet(definitions, domain='editorbuilding')