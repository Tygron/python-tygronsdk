from ......core.events import EventSet

from ......core.data.events import EventDefinition
from ......core.data.events import EventParameter

from typing import Type

definitions = {


    # General
        'add' : EventDefinition(
                group='General',
                parameters=[
                        EventParameter('stakeholder_id', Type[int], 
                                        api_description='Stakeholder ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'duplicate' : EventDefinition(
                group='General',
                parameters=[
                        EventParameter('measure_id', Type[int], aggregation=1, 
                                        api_description='Measure IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'remove' : EventDefinition(
                group='General',
                parameters=[
                        EventParameter('measure_id', Type[int], aggregation=1, 
                                        api_description='Measure IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),


    # Imports
        'import_buildings' : EventDefinition(
                group='Imports',
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
                        EventParameter('owners', Type[int], False, aggregation=1, 
                                        api_description='Owners (optional)', api_type=Type[int], api_required=False, api_default=None, api_aggregation=1,  ),
                        EventParameter('measure_id', Type[int], False, 
                                        api_description='Set for existing Measure ID (optional)', api_type=Type[int], api_required=False, api_default=None, api_aggregation=0,  ),
                        EventParameter('buffer_m', Type[float], False, 
                                        api_description='Buffer for Points and Lines to make Polygons (optional)', api_type=Type[float], api_required=False, api_default=None, api_aggregation=0,  ),
                        EventParameter('source_id', Type[int], False, 
                                        api_description='Source (optional)', api_type=Type[int], api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'import_geotiffs' : EventDefinition(
                group='Imports',
                parameters=[
                        EventParameter(0, 'Unknown: (geometrycollection with crs: epsg:3857)', 
                                        api_description='Collection of GeoTIFF Geometries where the GeoTIFF will be applied', api_type='Unknown: (geometrycollection with crs: epsg:3857)', api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter(1, Type[int], aggregation=1, 
                                        api_description='Terrain Type IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter(2, Type[int], aggregation=1, 
                                        api_description='GeoTIFF ID arrays', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter(3, Type[int], False, 
                                        api_description='Set for existing Measure ID (optional)', api_type=Type[int], api_required=False, api_default=None, api_aggregation=0,  ),
                        EventParameter(4, Type[float], False, 
                                        api_description='Buffer for Points and Lines to make Polygons (optional)', api_type=Type[float], api_required=False, api_default=None, api_aggregation=0,  ),
                        EventParameter(5, Type[int], False, 
                                        api_description='Source (optional)', api_type=Type[int], api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'import_grids' : EventDefinition(
                group='Imports',
                parameters=[
                        EventParameter(0, 'Unknown: (geometrycollection with crs: epsg:3857)', 
                                        api_description='Collection of Grid Geometries where the Grid will be applied', api_type='Unknown: (geometrycollection with crs: epsg:3857)', api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter(1, Type[int], aggregation=1, 
                                        api_description='Terrain Type IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter(2, Type[int], aggregation=1, 
                                        api_description='Grid ID arrays', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter(3, Type[int], False, 
                                        api_description='Set for existing Measure ID (optional)', api_type=Type[int], api_required=False, api_default=None, api_aggregation=0,  ),
                        EventParameter(4, Type[float], False, 
                                        api_description='Buffer for Points and Lines to make Polygons (optional)', api_type=Type[float], api_required=False, api_default=None, api_aggregation=0,  ),
                        EventParameter(5, Type[int], False, 
                                        api_description='Source (optional)', api_type=Type[int], api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'import_levees' : EventDefinition(
                group='Imports',
                parameters=[
                        EventParameter(0, 'Unknown: (geometrycollection with crs: epsg:3857)', 
                                        api_description='Collection of Levee Geometries', api_type='Unknown: (geometrycollection with crs: epsg:3857)', api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter(1, Type[int], aggregation=1, 
                                        api_description='Levee IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter(2, Type[float], aggregation=1, 
                                        api_description='Override Angles', api_type=Type[float], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter(3, Type[float], aggregation=1, 
                                        api_description='Override Heights', api_type=Type[float], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter(4, Type[bool], aggregation=1, 
                                        api_description='Override relative height', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter(5, Type[int], False, 
                                        api_description='Set for existing Measure ID (optional)', api_type=Type[int], api_required=False, api_default=None, api_aggregation=0,  ),
                        EventParameter(6, Type[float], False, 
                                        api_description='Buffer for Points and Lines to make Polygons (optional)', api_type=Type[float], api_required=False, api_default=None, api_aggregation=0,  ),
                        EventParameter(7, Type[int], False, 
                                        api_description='Source (optional)', api_type=Type[int], api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'import_terrains' : EventDefinition(
                group='Imports',
                parameters=[
                        EventParameter(0, 'Unknown: (geometrycollection with crs: epsg:3857)', 
                                        api_description='Collection of Terrain Geometries', api_type='Unknown: (geometrycollection with crs: epsg:3857)', api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter(1, ['BUILDING', 'FLATTEN', 'GEOTIFF', 'GRID', 'LEVEE', 'RAISE', 'UPGRADE', 'WATER'], 
                                        api_description='Measure Edit Type;{"default": null, "values": ["BUILDING", "FLATTEN", "GEOTIFF", "GRID", "LEVEE", "RAISE", "UPGRADE", "WATER"]}', api_type=['BUILDING', 'FLATTEN', 'GEOTIFF', 'GRID', 'LEVEE', 'RAISE', 'UPGRADE', 'WATER'], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter(2, Type[bool], aggregation=1, 
                                        api_description='Is Inner', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter(3, Type[int], aggregation=1, 
                                        api_description='Terrain Type IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter(4, Type[float], aggregation=1, 
                                        api_description='Override Inner Heights', api_type=Type[float], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter(5, Type[bool], aggregation=1, 
                                        api_description='Height Relative', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter(6, Type[int], False, 
                                        api_description='Set for existing Measure ID (optional)', api_type=Type[int], api_required=False, api_default=None, api_aggregation=0,  ),
                        EventParameter(7, Type[float], False, 
                                        api_description='Buffer for Points and Lines to make Polygons (optional)', api_type=Type[float], api_required=False, api_default=None, api_aggregation=0,  ),
                        EventParameter(8, Type[int], False, 
                                        api_description='Source (optional)', api_type=Type[int], api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'import_upgrades' : EventDefinition(
                group='Imports',
                parameters=[
                        EventParameter(0, 'Unknown: (geometrycollection with crs: epsg:3857)', 
                                        api_description='Collection of Upgrade Geometries', api_type='Unknown: (geometrycollection with crs: epsg:3857)', api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter(1, Type[int], aggregation=1, 
                                        api_description='Upgrade Types', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter(2, Type[int], False, 
                                        api_description='Set for existing Measure ID (optional)', api_type=Type[int], api_required=False, api_default=None, api_aggregation=0,  ),
                        EventParameter(3, Type[float], False, 
                                        api_description='Buffer for Points and Lines to make Polygons (optional)', api_type=Type[float], api_required=False, api_default=None, api_aggregation=0,  ),
                        EventParameter(4, Type[int], False, 
                                        api_description='Source (optional)', api_type=Type[int], api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Information
        'set_name' : EventDefinition(
                group='Information',
                parameters=[
                        EventParameter('measure_id', Type[int], aggregation=1, 
                                        api_description='Measure IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('name', Type[str], aggregation=1, 
                                        api_description='Names', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'set_description' : EventDefinition(
                group='Information',
                parameters=[
                        EventParameter('measure_id', Type[int], 
                                        api_description='Measure ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('description', Type[str], 
                                        api_description='Description', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_owner' : EventDefinition(
                group='Information',
                parameters=[
                        EventParameter('measure_id', Type[int], 
                                        api_description='Measure IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('stakeholder_id', Type[int], 
                                        api_description='Stakeholder ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_image' : EventDefinition(
                group='Information',
                parameters=[
                        EventParameter('measure_id', Type[int], aggregation=1, 
                                        api_description='Measure IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('image_name', Type[str], aggregation=1, 
                                        api_description='Image names', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),


    # Calculation
        'set_cost' : EventDefinition(
                group='Calculation',
                parameters=[
                        EventParameter('measure_id', Type[int], 
                                        api_description='Measure ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('measure_action', ['CONSTRUCTION'], True, 'Construction', 
                                        api_description='Cost Type;{"default": null, "values": ["CONSTRUCTION"]}', api_type=['CONSTRUCTION'], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('cost', Type[float], 
                                        api_description='Cost in valuata', api_type=Type[float], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('fixed_cost', Type[bool], 
                                        api_description='Fixed (if false, cost per cubic meter);{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_requires_confirmation' : EventDefinition(
                group='Calculation',
                parameters=[
                        EventParameter('measure_id', Type[int], 
                                        api_description='Measure ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('confirmation_required', Type[bool], 
                                        api_description='Confirmation Required Boolean ;{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Buildings
        'add_building' : EventDefinition(
                group='Buildings',
                parameters=[
                        EventParameter('measure_id', Type[int], aggregation=1, 
                                        api_description='Measure IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'duplicate_building' : EventDefinition(
                group='Buildings',
                parameters=[
                        EventParameter('building_id', Type[int], aggregation=1, 
                                        api_description='Building IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),


    # Events
        'add_event' : EventDefinition(
                group='Events',
                parameters=[
                        EventParameter('measure_id', Type[int], aggregation=1, 
                                        api_description='Measure ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('event_server_side', Type[bool], True, True, aggregation=1, 
                                        api_description='Server Side (false = Client Side)', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('measure_action', ['CONSTRUCTION_PLAN', 'CONSTRUCTION_PLAN_CANCEL'], True, 'CONSTRUCTION_PLAN', aggregation=1, 
                                        api_description='Action Type', api_type=['CONSTRUCTION_PLAN', 'CONSTRUCTION_PLAN_CANCEL'], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'remove_event' : EventDefinition(
                group='Events',
                parameters=[
                        EventParameter('measure_id', Type[int], aggregation=1, 
                                        api_description='Measure ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('event_server_side', Type[bool], True, True, aggregation=1, 
                                        api_description='Server Side (false = Client Side)', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('measure_action', ['CONSTRUCTION_PLAN', 'CONSTRUCTION_PLAN_CANCEL'], True, 'CONSTRUCTION_PLAN', aggregation=1, 
                                        api_description='Action Type', api_type=['CONSTRUCTION_PLAN', 'CONSTRUCTION_PLAN_CANCEL'], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('event_id', Type[int], aggregation=1, 
                                        api_description='Event ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'set_event' : EventDefinition(
                group='Events',
                parameters=[
                        EventParameter('measure_id', Type[int], aggregation=1, 
                                        api_description='Measure ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('event_server_side', Type[bool], True, True, aggregation=1, 
                                        api_description='Server Side (false = Client Side)', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('measure_action', ['CONSTRUCTION_PLAN', 'CONSTRUCTION_PLAN_CANCEL'], True, 'CONSTRUCTION_PLAN', aggregation=1, 
                                        api_description='Action Type', api_type=['CONSTRUCTION_PLAN', 'CONSTRUCTION_PLAN_CANCEL'], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('coded_event', 'Unknown: (codedevent or multiple values in array [a, b, c])', aggregation=1, 
                                        api_description='CodedEvent contents', api_type='Unknown: (codedevent or multiple values in array [a, b, c])', api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),


    # Levees
        'add_levee' : EventDefinition(
                group='Levees',
                parameters=[
                        EventParameter('measure_id', Type[int], 
                                        api_description='Measure ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('levee_type_id', Type[int], 
                                        api_description='Levee ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'remove_levee' : EventDefinition(
                group='Levees',
                parameters=[
                        EventParameter('measure_id', Type[int], 
                                        api_description='Measure IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('levee_spatial_id', Type[int], aggregation=1, 
                                        api_description='Levee Spatial IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'add_levee_polygons' : EventDefinition(
                group='Levees',
                parameters=[
                        EventParameter('measure_id', Type[int], 
                                        api_description='Measure ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('levee_spatial_id', Type[int], 
                                        api_description='Levee Spatial ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('polygon', 'MultiPolygon', 
                                        api_description='Multipolygon', api_type='MultiPolygon', api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'remove_levee_polygons' : EventDefinition(
                group='Levees',
                parameters=[
                        EventParameter('measure_id', Type[int], 
                                        api_description='Measure ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('levee_spatial_id', Type[int], 
                                        api_description='Levee Spatial ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('polygon', 'MultiPolygon', 
                                        api_description='MultiPolygon', api_type='MultiPolygon', api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_levee_type' : EventDefinition(
                group='Levees',
                parameters=[
                        EventParameter('measure_id', Type[int], 
                                        api_description='Measure ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('levee_spatial_id', Type[int], 
                                        api_description='Levee Spatial ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('levee_type_id', Type[int], 
                                        api_description='Levee ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Terrains
        'add_terrain' : EventDefinition(
                group='Terrains',
                parameters=[
                        EventParameter('measure_id', Type[int], 
                                        api_description='Measure ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'remove_terrain' : EventDefinition(
                group='Terrains',
                parameters=[
                        EventParameter('measure_id', Type[int], 
                                        api_description='Measure IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('spatial_id', Type[int], aggregation=1, 
                                        api_description='Terrain Spatial IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'add_terrain_polygons' : EventDefinition(
                group='Terrains',
                parameters=[
                        EventParameter('measure_id', Type[int], 
                                        api_description='Measure ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('spatial_id', Type[int], 
                                        api_description='Levee Spatial ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('outer', Type[bool], 
                                        api_description='Is Outer (false = inner);{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('polygon', 'MultiPolygon', 
                                        api_description='MultiPolygon', api_type='MultiPolygon', api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'remove_terrain_polygons' : EventDefinition(
                group='Terrains',
                parameters=[
                        EventParameter('measure_id', Type[int], 
                                        api_description='Measure ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('spatial_id', Type[int], 
                                        api_description='Terrain Spatial ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('outer', Type[bool], 
                                        api_description='Is Outer (false = inner);{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('polygon', 'MultiPolygon', 
                                        api_description='MultiPolygon', api_type='MultiPolygon', api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_terrain_edit_type' : EventDefinition(
                group='Terrains',
                parameters=[
                        EventParameter('measure_id', Type[int], 
                                        api_description='Measure ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('spatial_id', Type[int], 
                                        api_description='Terrain Spatial ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('spatial_type', ['BUILDING', 'FLATTEN', 'GEOTIFF', 'GRID', 'LEVEE', 'RAISE', 'UPGRADE', 'WATER'], 
                                        api_description='Edit Type;{"default": null, "values": ["BUILDING", "FLATTEN", "GEOTIFF", "GRID", "LEVEE", "RAISE", "UPGRADE", "WATER"]}', api_type=['BUILDING', 'FLATTEN', 'GEOTIFF', 'GRID', 'LEVEE', 'RAISE', 'UPGRADE', 'WATER'], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_terrain_type' : EventDefinition(
                group='Terrains',
                parameters=[
                        EventParameter('measure_id', Type[int], 
                                        api_description='Measure ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('spatial_id', Type[int], 
                                        api_description='Terrain Spatial ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('terrain_type_id', Type[int], 
                                        api_description='Terrain Type ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_terrain_height' : EventDefinition(
                group='Terrains',
                parameters=[
                        EventParameter('measure_id', Type[int], 
                                        api_description='Measure IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('spatial_id', Type[int], 
                                        api_description='Terrain Spatial ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('height_absolute', Type[float], 
                                        api_description='Height value', api_type=Type[float], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Tiffs
        'add_geotiff' : EventDefinition(
                group='Tiffs',
                parameters=[
                        EventParameter('measure_id', Type[int], 
                                        api_description='Measure ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'remove_geotiff_terrain_type' : EventDefinition(
                group='Tiffs',
                parameters=[
                        EventParameter('measure_id', Type[int], 
                                        api_description='Measure ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('tiff_spatial_id', Type[int], 
                                        api_description='GeoTIFF Spatial ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_geotiff' : EventDefinition(
                group='Tiffs',
                parameters=[
                        EventParameter('measure_id', Type[int], 
                                        api_description='Measure ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('tiff_spatial_id', Type[int], 
                                        api_description='GeoTIFF Spatial ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('geotiff_id', Type[int], aggregation=1, 
                                        api_description='GeoTIFF IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'add_geotiff_polygons' : EventDefinition(
                group='Tiffs',
                parameters=[
                        EventParameter('measure_id', Type[int], 
                                        api_description='Measure ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('tiff_spatial_id', Type[int], 
                                        api_description='GeoTIFF Spatial ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('polygon', 'MultiPolygon', 
                                        api_description='MultiPolygon', api_type='MultiPolygon', api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'remove_geotiff_polygons' : EventDefinition(
                group='Tiffs',
                parameters=[
                        EventParameter('measure_id', Type[int], 
                                        api_description='Measure ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('tiff_spatial_id', Type[int], 
                                        api_description='GeoTIFFs Spatial ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('polygon', 'MultiPolygon', 
                                        api_description='MultiPolygon', api_type='MultiPolygon', api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_geotiff_automatic_polygons' : EventDefinition(
                group='Tiffs',
                parameters=[
                        EventParameter('measure_id', Type[int], 
                                        api_description='Measure ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('tiff_spatial_id', Type[int], 
                                        api_description='GeoTIFF Spatial ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('automatic_polygon_calculation', Type[bool], 
                                        api_description='Automatic calculation;{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_geotiff_terrain_type' : EventDefinition(
                group='Tiffs',
                parameters=[
                        EventParameter('measure_id', Type[int], 
                                        api_description='Measure ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('tiff_spatial_id', Type[int], 
                                        api_description='GeoTIFF Spatial ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('terrain_type_id', Type[int], 
                                        api_description='Terrain Type ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'remove_geotiff' : EventDefinition(
                group='Tiffs',
                parameters=[
                        EventParameter('measure_id', Type[int], 
                                        api_description='Measure IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('tiff_spatial_id', Type[int], aggregation=1, 
                                        api_description='GeoTIFF Spatial IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),


    # Upgrades
        'add_upgrade' : EventDefinition(
                group='Upgrades',
                parameters=[
                        EventParameter('measure_id', Type[int], 
                                        api_description='Measure ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'remove_upgrade' : EventDefinition(
                group='Upgrades',
                parameters=[
                        EventParameter('measure_id', Type[int], 
                                        api_description='Measure IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('upgrade_spatial_id', Type[int], aggregation=1, 
                                        api_description='Upgrade Spatial IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'set_upgrade_type' : EventDefinition(
                group='Upgrades',
                parameters=[
                        EventParameter('measure_id', Type[int], 
                                        api_description='Measure ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('upgrade_spatial_id', Type[int], 
                                        api_description='Upgrade Spatial ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('upgrade_type_id', Type[int], 
                                        api_description='Upgrade Type ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'add_upgrade_polygons' : EventDefinition(
                group='Upgrades',
                parameters=[
                        EventParameter('measure_id', Type[int], 
                                        api_description='Measure ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('upgrade_spatial_id', Type[int], 
                                        api_description='Upgrade Spatial ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('polygon', 'MultiPolygon', 
                                        api_description='MultiPolygon', api_type='MultiPolygon', api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'remove_upgrade_polygons' : EventDefinition(
                group='Upgrades',
                parameters=[
                        EventParameter('measure_id', Type[int], 
                                        api_description='Measure ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('upgrade_spatial_id', Type[int], 
                                        api_description='Upgrade Spatial ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('polygon', 'MultiPolygon', 
                                        api_description='MultiPolygon', api_type='MultiPolygon', api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # 
        'add_grid' : EventDefinition(
                group='',
                parameters=[
                        EventParameter(0, Type[int], 
                                        api_description='Measure ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'add_grid_polygons' : EventDefinition(
                group='',
                parameters=[
                        EventParameter(0, Type[int], 
                                        api_description='Measure ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter(1, Type[int], 
                                        api_description='Grid Spatial ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter(2, 'MultiPolygon', 
                                        api_description='MultiPolygon', api_type='MultiPolygon', api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'remove_grid' : EventDefinition(
                group='',
                parameters=[
                        EventParameter(0, Type[int], 
                                        api_description='Measure IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter(1, Type[int], aggregation=1, 
                                        api_description='Grid Spatial IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'remove_grid_polygons' : EventDefinition(
                group='',
                parameters=[
                        EventParameter(0, Type[int], 
                                        api_description='Measure ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter(1, Type[int], 
                                        api_description='Grid Spatial ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter(2, 'MultiPolygon', 
                                        api_description='MultiPolygon', api_type='MultiPolygon', api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'remove_grid_terrain_type' : EventDefinition(
                group='',
                parameters=[
                        EventParameter(0, Type[int], 
                                        api_description='Measure ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter(1, Type[int], 
                                        api_description='Grid Spatial ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_grid' : EventDefinition(
                group='',
                parameters=[
                        EventParameter(0, Type[int], 
                                        api_description='Measure ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter(1, Type[int], 
                                        api_description='Grid Spatial ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter(2, Type[int], aggregation=1, 
                                        api_description='Overlay IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'set_grid_automatic_polygons' : EventDefinition(
                group='',
                parameters=[
                        EventParameter(0, Type[int], 
                                        api_description='Measure ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter(1, Type[int], 
                                        api_description='Grid Spatial ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter(2, Type[bool], 
                                        api_description='Automatic calculation;{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_grid_terrain_type' : EventDefinition(
                group='',
                parameters=[
                        EventParameter(0, Type[int], 
                                        api_description='Measure ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter(1, Type[int], 
                                        api_description='Grid Spatial ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter(2, Type[int], 
                                        api_description='Terrain Type ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_levee_angle' : EventDefinition(
                group='',
                parameters=[
                        EventParameter(0, Type[int], 
                                        api_description='Measure IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter(1, Type[int], 
                                        api_description='Levee Spatial ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter(2, Type[float], False, 
                                        api_description='Angle', api_type=Type[float], api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_levee_height' : EventDefinition(
                group='',
                parameters=[
                        EventParameter(0, Type[int], 
                                        api_description='Measure IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter(1, Type[int], 
                                        api_description='Levee Spatial ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter(2, Type[float], False, 
                                        api_description='Height value', api_type=Type[float], api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_levee_height_relative' : EventDefinition(
                group='',
                parameters=[
                        EventParameter(0, Type[int], 
                                        api_description='Measure IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter(1, Type[int], 
                                        api_description='Levee Spatial ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter(2, Type[bool], False, 
                                        api_description='Boolean', api_type=Type[bool], api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_terrain_height_relative' : EventDefinition(
                group='',
                parameters=[
                        EventParameter(0, Type[int], 
                                        api_description='Measure IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter(1, Type[int], 
                                        api_description='Terrain Spatial ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter(2, Type[bool], 
                                        api_description='Boolean;{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
    }

event_set = EventSet(definitions, domain='editormeasure')