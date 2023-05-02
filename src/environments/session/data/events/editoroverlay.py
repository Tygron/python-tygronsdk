from .....core.events import EventSet

from .....core.data.events import EventDefinition
from .....core.data.events import EventParameter

from typing import Type

definitions = {


    # General
        'add' : EventDefinition(
                group='General',
                parameters=[
                        EventParameter('overlay_type', ['AERIUS', 'AREAS', 'ATTRIBUTE', 'AVG', 'COMBO', 'DISTANCE_SIGHT', 'DISTANCE_ZONE', 'DISTURBANCE_DISTANCE', 'FLOODING', 'FUNCTION_HIGHLIGHT', 'GEO_TIFF', 'GROUNDWATER', 'HEAT_STRESS', 'HEIGHTMAP', 'IMAGE', 'LIVABILITY', 'MUNICIPALITIES', 'NEIGHBORHOODS', 'NETWORK_DISTANCE', 'NETWORK_OVERVIEW', 'NETWORK_OWNERSHIP', 'OWNERSHIP', 'OWNERSHIP_GRID', 'RAINFALL', 'RESULT_CHILD', 'SAFETY_DISTANCE', 'SOURCE', 'SUBSIDENCE', 'TEST', 'TRAFFIC_DENSITY', 'TRAFFIC_NO2', 'TRAFFIC_NOISE', 'TRAVEL_DISTANCE', 'UNDERGROUND', 'VACANCY', 'WATERSHED', 'WATERWIJZER', 'WCS', 'WMS', 'ZIP_CODES', 'ZONING'], 
                                        api_description='OverlayType;{"default": null, "values": ["AERIUS", "AREAS", "ATTRIBUTE", "AVG", "COMBO", "DISTANCE_SIGHT", "DISTANCE_ZONE", "DISTURBANCE_DISTANCE", "FLOODING", "FUNCTION_HIGHLIGHT", "GEO_TIFF", "GROUNDWATER", "HEAT_STRESS", "HEIGHTMAP", "IMAGE", "LIVABILITY", "MUNICIPALITIES", "NEIGHBORHOODS", "NETWORK_DISTANCE", "NETWORK_OVERVIEW", "NETWORK_OWNERSHIP", "OWNERSHIP", "OWNERSHIP_GRID", "RAINFALL", "RESULT_CHILD", "SAFETY_DISTANCE", "SOURCE", "SUBSIDENCE", "TEST", "TRAFFIC_DENSITY", "TRAFFIC_NO2", "TRAFFIC_NOISE", "TRAVEL_DISTANCE", "UNDERGROUND", "VACANCY", "WATERSHED", "WATERWIJZER", "WCS", "WMS", "ZIP_CODES", "ZONING"]}', api_type=['AERIUS', 'AREAS', 'ATTRIBUTE', 'AVG', 'COMBO', 'DISTANCE_SIGHT', 'DISTANCE_ZONE', 'DISTURBANCE_DISTANCE', 'FLOODING', 'FUNCTION_HIGHLIGHT', 'GEO_TIFF', 'GROUNDWATER', 'HEAT_STRESS', 'HEIGHTMAP', 'IMAGE', 'LIVABILITY', 'MUNICIPALITIES', 'NEIGHBORHOODS', 'NETWORK_DISTANCE', 'NETWORK_OVERVIEW', 'NETWORK_OWNERSHIP', 'OWNERSHIP', 'OWNERSHIP_GRID', 'RAINFALL', 'RESULT_CHILD', 'SAFETY_DISTANCE', 'SOURCE', 'SUBSIDENCE', 'TEST', 'TRAFFIC_DENSITY', 'TRAFFIC_NO2', 'TRAFFIC_NOISE', 'TRAVEL_DISTANCE', 'UNDERGROUND', 'VACANCY', 'WATERSHED', 'WATERWIJZER', 'WCS', 'WMS', 'ZIP_CODES', 'ZONING'], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'add_type' : EventDefinition(
                group='General',
                parameters=[
                        EventParameter('overlay_type', 'TYPE?', aggregation=1, 
                                        api_description='Array of OverlayTypes', api_type='TYPE?', api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'add_result_child_overlay' : EventDefinition(
                group='General',
                parameters=[
                        EventParameter('overlay_id', Type[int], 
                                        api_description='Overlay ID (must relate to a grid Overlay with result types)', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('overlay_type', Type[str], 
                                        api_description='Result type for new child Overlay (must be a valid result for the parent Overlay type)', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'duplicate' : EventDefinition(
                group='General',
                parameters=[
                        EventParameter('overlay_id', Type[int], aggregation=1, 
                                        api_description='Overlays', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'remove' : EventDefinition(
                group='General',
                parameters=[
                        EventParameter('overlay_id', Type[int], aggregation=1, 
                                        api_description='Overlay IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),


    # Information
        'set_name' : EventDefinition(
                group='Information',
                parameters=[
                        EventParameter('overlay_id', Type[int], aggregation=1, 
                                        api_description='Overlay ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('overlay_name', Type[str], aggregation=1, 
                                        api_description='Name for the Overlay', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'set_visible' : EventDefinition(
                group='Information',
                parameters=[
                        EventParameter('overlay_id', Type[int], aggregation=1, 
                                        api_description='Overlay ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('visibility', Type[bool], aggregation=1, 
                                        api_description='Visualized', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'set_parent' : EventDefinition(
                group='Information',
                parameters=[
                        EventParameter('overlay_id', Type[int], 
                                        api_description='Overlay ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('parent_id', Type[int], 
                                        api_description='Overlay ID of parent (overlays without a parent should have their parent Overlay ID set to -1)', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_icon' : EventDefinition(
                group='Information',
                parameters=[
                        EventParameter('overlay_id', Type[int], aggregation=1, 
                                        api_description='Overlay ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('asset_path', Type[str], aggregation=1, 
                                        api_description='Project asset name, omitting the directory', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),


    # Attribute
        'set_attribute' : EventDefinition(
                group='Attribute',
                parameters=[
                        EventParameter('overlay_id', Type[int], aggregation=1, 
                                        api_description='Overlays', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_name', Type[str], 
                                        api_description='Attribute Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('attribute_values', Type[float], aggregation=1, 
                                        api_description='Attribute Values', api_type=Type[float], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('source_id', Type[int], False, 
                                        api_description='Source (optional)', api_type=Type[int], api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_attributes' : EventDefinition(
                group='Attribute',
                parameters=[
                        EventParameter('overlay_id', Type[int], aggregation=1, 
                                        api_description='Overlays', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_name', Type[str], aggregation=1, 
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
                        EventParameter('overlay_id', Type[int], aggregation=1, 
                                        api_description='Overlay ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_name', Type[str], aggregation=1, 
                                        api_description='Attributes to remove', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),


    # Calculation Model
        'set_prequel' : EventDefinition(
                group='Calculation Model',
                parameters=[
                        EventParameter('overlay_id', Type[int], 
                                        api_description='Overlay ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('prequel_id', Type[int], 
                                        api_description='Prequel Overlay ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('prequel_type', Type[str], 
                                        api_description='Prequel Type Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('prequel_timeframe', Type[int], False, 
                                        api_description='Prequel Timeframe ID (optional)', api_type=Type[int], api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'remove_prequel' : EventDefinition(
                group='Calculation Model',
                parameters=[
                        EventParameter('overlay_id', Type[int], 
                                        api_description='Grid Overlay ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('prequel_type', Type[str], 
                                        api_description='Prequel Type Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_grid_active' : EventDefinition(
                group='Calculation Model',
                parameters=[
                        EventParameter('overlay_id', Type[int], 
                                        api_description='Overlay ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('active', Type[bool], 
                                        api_description='Activated;{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_result_type' : EventDefinition(
                group='Calculation Model',
                parameters=[
                        EventParameter('overlay_id', Type[int], 
                                        api_description='Overlay ID (must relate to a grid Overlay with result types)', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('result_type', Type[str], 
                                        api_description='Result type for the Overlay (must be a valid result type of the Overlay type)', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_show_difference' : EventDefinition(
                group='Calculation Model',
                parameters=[
                        EventParameter('overlay_id', Type[int], 
                                        api_description='Overlay ID (must relate to a grid Overlay)', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('difference', Type[bool], 
                                        api_description='Has a difference option (false means there is no difference option for this Overlay);{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_key_value' : EventDefinition(
                group='Calculation Model',
                parameters=[
                        EventParameter('overlay_id', Type[int], 
                                        api_description='Overlay ID (must relate to a grid Overlay)', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('key_name', Type[str], 
                                        api_description='Key name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('attribute_name', Type[str], 
                                        api_description='Attribute to look for', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Export
        'save_grid' : EventDefinition(
                group='Export',
                parameters=[
                        EventParameter('overlay_id', Type[int], 
                                        api_description='Overlay ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Calculation
        'refresh_grid' : EventDefinition(
                group='Calculation',
                parameters=[
                    ]
            ),


    # Legend
        'set_custom_legend' : EventDefinition(
                group='Legend',
                parameters=[
                        EventParameter('overlay_id', Type[int], 
                                        api_description='Overlay ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('custom_legend', Type[bool], 
                                        api_description='Has a custom legend (false sets the Overlay to use the default legend);{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'add_legend_entry' : EventDefinition(
                group='Legend',
                parameters=[
                        EventParameter('overlay_id', Type[int], aggregation=1, 
                                        api_description='Overlay ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('difference_legend', Type[bool], True, False, aggregation=1, 
                                        api_description='Add to custom difference legend (false adds the entry to the normal custom legend)', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('entry_name', Type[str], False, aggregation=1, 
                                        api_description='Name (optional)', api_type=Type[str], api_required=False, api_default=None, api_aggregation=1,  ),
                        EventParameter('entry_color', 'Unknown: (tcolor or multiple values in array [a, b, c])', False, aggregation=1, 
                                        api_description='Color (optional)', api_type='Unknown: (tcolor or multiple values in array [a, b, c])', api_required=False, api_default=None, api_aggregation=1,  ),
                        EventParameter('entry_color', Type[float], False, aggregation=1, 
                                        api_description='Value (optional)', api_type=Type[float], api_required=False, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'remove_legend_entry' : EventDefinition(
                group='Legend',
                parameters=[
                        EventParameter('overlay_id', Type[int], 
                                        api_description='Overlay ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('difference_legend', Type[bool], True, False, 
                                        api_description='Remove from custom difference legend (false removes the entry from the normal custom legend);{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('entry_id', Type[int], aggregation=1, 
                                        api_description='Ids of entries which should be removed', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'set_legend_entry_name' : EventDefinition(
                group='Legend',
                parameters=[
                        EventParameter('overlay_id', Type[int], 
                                        api_description='Overlay ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('difference_legend', Type[bool], True, False, 
                                        api_description='Affect the custom difference legend (false means affect the normal custom legend);{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('entry_id', Type[int], 
                                        api_description='ID of entry which should be changed', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('entry_name', Type[str], 
                                        api_description='New name for the entry', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_legend_entry_value' : EventDefinition(
                group='Legend',
                parameters=[
                        EventParameter('overlay_id', Type[int], 
                                        api_description='Overlay ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('difference_legend', Type[bool], True, False, 
                                        api_description='Affect the custom difference legend (false means affect the normal custom legend);{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('entry_id', Type[int], 
                                        api_description='ID of entry which should be changed', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('entry_value', Type[float], 
                                        api_description='New value for the entry', api_type=Type[float], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_legend_entry_color' : EventDefinition(
                group='Legend',
                parameters=[
                        EventParameter('overlay_id', Type[int], 
                                        api_description='Overlay ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('difference_legend', Type[bool], True, False, 
                                        api_description='Affect the custom difference legend (false means affect the normal custom legend);{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('entry_id', Type[int], 
                                        api_description='ID of entry which should be changed', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('entry_color', 'Unknown: (tcolor)', 
                                        api_description='Color', api_type='Unknown: (tcolor)', api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Overlay: Areas
        'set_overlay_area' : EventDefinition(
                group='Overlay: Areas',
                parameters=[
                        EventParameter('overlay_id', Type[int], 
                                        api_description='Overlay ID (must relate to an AREAS Overlay)', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('area_id', Type[int], aggregation=1, 
                                        api_description='Array of area IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('add', Type[bool], 
                                        api_description='Should be added to the Overlay (false removes the areas from the Overlay);{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Overlay: Functions
        'set_overlay_primary_color' : EventDefinition(
                group='Overlay: Functions',
                parameters=[
                        EventParameter('overlay_id', Type[int], 
                                        api_description='Overlay ID (must relate to a FUNCTION or ATTRIBUTE Overlay)', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('legend_entry_color', 'Unknown: (tcolor)', 
                                        api_description='Color', api_type='Unknown: (tcolor)', api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_overlay_rest_color' : EventDefinition(
                group='Overlay: Functions',
                parameters=[
                        EventParameter('overlay_id', Type[int], 
                                        api_description='Overlay ID (must relate to a FUNCTION or ATTRIBUTE Overlay)', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('legend_entry_color', 'Unknown: (tcolor)', False, 
                                        api_description='Color', api_type='Unknown: (tcolor)', api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'add_overlay_function' : EventDefinition(
                group='Overlay: Functions',
                parameters=[
                        EventParameter('overlay_id', Type[int], 
                                        api_description='Overlay ID (must relate to a FUNCTION_HIGHLIGHT Overlay)', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('function_id', Type[int], aggregation=1, 
                                        api_description='Function IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'remove_overlay_function' : EventDefinition(
                group='Overlay: Functions',
                parameters=[
                        EventParameter('overlay_id', Type[int], 
                                        api_description='Overlay ID (must relate to a FUNCTION_HIGHLIGHT Overlay)', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('function_id', Type[int], aggregation=1, 
                                        api_description='Function IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),


    # Overlay: Attribute
        'set_attribute_overlay_color_attribute' : EventDefinition(
                group='Overlay: Attribute',
                parameters=[
                        EventParameter('overlay_id', Type[int], 
                                        api_description='Overlay ID (must relate to an ATTRIBUTE Overlay)', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('attribute_name', Type[str], 
                                        api_description='Attribute to use to color a found item', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_attribute_overlay_values' : EventDefinition(
                group='Overlay: Attribute',
                parameters=[
                        EventParameter('overlay_id', Type[int], 
                                        api_description='Overlay ID (must relate to an ATTRIBUTE Overlay)', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('maplink', ['ACTION_LOGS', 'ACTION_MENUS', 'ADDRESSES', 'AREAS', 'ATTRIBUTE_ACTIONS', 'BUILDINGS', 'CHAT_MESSAGES', 'CINEMATIC_DATAS', 'CLIENT_WORDS', 'COSTS', 'CUSTOM_GEOMETRIES', 'DEFAULT_WORDS', 'ERROR_LOGS', 'EVENT_BUNDLES', 'EXCEL_SHEETS', 'FUNCTION_OVERRIDES', 'FUNCTIONS', 'GEO_LINKS', 'GEO_OPTIONS', 'GEO_PLUGINS', 'GEO_TIFFS', 'GLOBALS', 'HEIGHTS', 'INCOMES', 'INDICATORS', 'LEVEES', 'MEASUREMENTS', 'MEASURES', 'MODEL_DATAS', 'MODEL_SETS', 'MONEY_TRANSFERS', 'NEIGHBORHOODS', 'NET_CLUSTERS', 'NET_FUNCTIONS', 'NET_LINES', 'NET_LOADS', 'NET_NODES', 'NET_SETTINGS', 'OVERLAYS', 'PANELS', 'PARAMETRIC_DESIGNS', 'PARAMETRIC_EXAMPLES', 'PARTICLE_EMITTERS', 'PLOTS', 'POPUPS', 'PROGRESS', 'PROJECT_ASSETS', 'RECORDINGS', 'SCENARIOS', 'SERVER_WORDS', 'SETTINGS', 'SOUNDS', 'SOURCES', 'SPECIAL_EFFECTS', 'SPECIAL_OPTIONS', 'STAKEHOLDERS', 'TERRAIN_TYPE_OVERRIDES', 'TERRAIN_TYPES', 'TERRAINS', 'TEXTURES', 'TIMES', 'TRIGGERS', 'UNIT_DATA_OVERRIDES', 'UNIT_DATAS', 'UPGRADE_TYPES', 'WATER_VALUES', 'WEATHERS', 'ZIP_CODES', 'ZONES', 'ZOOMLEVELS'], 
                                        api_description='MapLink: AREAS, BUILDINGS, NEIGHBORHOODS, NET_LOADS, TERRAINS, ZONES;{"default": null, "values": ["ACTION_LOGS", "ACTION_MENUS", "ADDRESSES", "AREAS", "ATTRIBUTE_ACTIONS", "BUILDINGS", "CHAT_MESSAGES", "CINEMATIC_DATAS", "CLIENT_WORDS", "COSTS", "CUSTOM_GEOMETRIES", "DEFAULT_WORDS", "ERROR_LOGS", "EVENT_BUNDLES", "EXCEL_SHEETS", "FUNCTION_OVERRIDES", "FUNCTIONS", "GEO_LINKS", "GEO_OPTIONS", "GEO_PLUGINS", "GEO_TIFFS", "GLOBALS", "HEIGHTS", "INCOMES", "INDICATORS", "LEVEES", "MEASUREMENTS", "MEASURES", "MODEL_DATAS", "MODEL_SETS", "MONEY_TRANSFERS", "NEIGHBORHOODS", "NET_CLUSTERS", "NET_FUNCTIONS", "NET_LINES", "NET_LOADS", "NET_NODES", "NET_SETTINGS", "OVERLAYS", "PANELS", "PARAMETRIC_DESIGNS", "PARAMETRIC_EXAMPLES", "PARTICLE_EMITTERS", "PLOTS", "POPUPS", "PROGRESS", "PROJECT_ASSETS", "RECORDINGS", "SCENARIOS", "SERVER_WORDS", "SETTINGS", "SOUNDS", "SOURCES", "SPECIAL_EFFECTS", "SPECIAL_OPTIONS", "STAKEHOLDERS", "TERRAIN_TYPE_OVERRIDES", "TERRAIN_TYPES", "TERRAINS", "TEXTURES", "TIMES", "TRIGGERS", "UNIT_DATA_OVERRIDES", "UNIT_DATAS", "UPGRADE_TYPES", "WATER_VALUES", "WEATHERS", "ZIP_CODES", "ZONES", "ZOOMLEVELS"]}', api_type=['ACTION_LOGS', 'ACTION_MENUS', 'ADDRESSES', 'AREAS', 'ATTRIBUTE_ACTIONS', 'BUILDINGS', 'CHAT_MESSAGES', 'CINEMATIC_DATAS', 'CLIENT_WORDS', 'COSTS', 'CUSTOM_GEOMETRIES', 'DEFAULT_WORDS', 'ERROR_LOGS', 'EVENT_BUNDLES', 'EXCEL_SHEETS', 'FUNCTION_OVERRIDES', 'FUNCTIONS', 'GEO_LINKS', 'GEO_OPTIONS', 'GEO_PLUGINS', 'GEO_TIFFS', 'GLOBALS', 'HEIGHTS', 'INCOMES', 'INDICATORS', 'LEVEES', 'MEASUREMENTS', 'MEASURES', 'MODEL_DATAS', 'MODEL_SETS', 'MONEY_TRANSFERS', 'NEIGHBORHOODS', 'NET_CLUSTERS', 'NET_FUNCTIONS', 'NET_LINES', 'NET_LOADS', 'NET_NODES', 'NET_SETTINGS', 'OVERLAYS', 'PANELS', 'PARAMETRIC_DESIGNS', 'PARAMETRIC_EXAMPLES', 'PARTICLE_EMITTERS', 'PLOTS', 'POPUPS', 'PROGRESS', 'PROJECT_ASSETS', 'RECORDINGS', 'SCENARIOS', 'SERVER_WORDS', 'SETTINGS', 'SOUNDS', 'SOURCES', 'SPECIAL_EFFECTS', 'SPECIAL_OPTIONS', 'STAKEHOLDERS', 'TERRAIN_TYPE_OVERRIDES', 'TERRAIN_TYPES', 'TERRAINS', 'TEXTURES', 'TIMES', 'TRIGGERS', 'UNIT_DATA_OVERRIDES', 'UNIT_DATAS', 'UPGRADE_TYPES', 'WATER_VALUES', 'WEATHERS', 'ZIP_CODES', 'ZONES', 'ZOOMLEVELS'], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('attribute', Type[str], 
                                        api_description='Attribute to look for', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Overlay: Image
        'set_image' : EventDefinition(
                group='Overlay: Image',
                parameters=[
                        EventParameter('overlay_id', Type[int], aggregation=1, 
                                        api_description='Overlay IDs (must relate to an IMAGE Overlay)', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('asset_name', Type[str], aggregation=2, 
                                        api_description='Array of Project asset names, omitting the directory', api_type=Type[str], api_required=True, api_default=None, api_aggregation=2,  ),
                    ]
            ),


    # Overlay: Network
        'set_net_overlay' : EventDefinition(
                group='Overlay: Network',
                parameters=[
                        EventParameter('overlay_id', Type[int], 
                                        api_description='Overlay ID (must relate to a network Overlay)', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('net_type', ['ELECTRICITY', 'GAS', 'HEAT', 'INTERNET', 'SEWER'], 
                                        api_description='NetType;{"default": null, "values": ["ELECTRICITY", "GAS", "HEAT", "INTERNET", "SEWER"]}', api_type=['ELECTRICITY', 'GAS', 'HEAT', 'INTERNET', 'SEWER'], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('visualize_network', Type[bool], 
                                        api_description='Whether to show the network (false means no lines will be visualized);{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('active_only', Type[bool], 
                                        api_description='Whether only active connections should be visualized (false means both active and inactive connections are visualized);{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Overlay: Source
        'set_overlay_source' : EventDefinition(
                group='Overlay: Source',
                parameters=[
                        EventParameter('overlay_id', Type[int], 
                                        api_description='Overlay ID (must relate to a SOURCES Overlay)', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('source_id', Type[int], aggregation=1, 
                                        api_description='Array of source IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('add', Type[bool], 
                                        api_description='Should be added to the Overlay (false removes the sources from the Overlay);{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Overlay: GeoTiff
        'set_geotiff' : EventDefinition(
                group='Overlay: GeoTiff',
                parameters=[
                        EventParameter('overlay_id', Type[int], 
                                        api_description='Overlay ID (must relate to a GeoTIFF Overlay)', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('geotiff_id', Type[int], aggregation=1, 
                                        api_description='Unique GeoTIFF IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),


    # Overlay: WMS/WCS
        'set_source' : EventDefinition(
                group='Overlay: WMS/WCS',
                parameters=[
                        EventParameter('overlay_id', Type[int], 
                                        api_description='Service Source Overlay ID ', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('source_id', Type[int], 
                                        api_description='Source ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_source_layer' : EventDefinition(
                group='Overlay: WMS/WCS',
                parameters=[
                        EventParameter('overlay_id', Type[int], 
                                        api_description='Service Source Overlay ID ', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('source_layer', Type[str], 
                                        api_description='Layer name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Overlay: Avg
        'set_avg_distance' : EventDefinition(
                group='Overlay: Avg',
                parameters=[
                        EventParameter('overlay_id', Type[int], 
                                        api_description='Overlay ID (must relate to an AVG Overlay)', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('distance', Type[float], 
                                        api_description='Averaging distance', api_type=Type[float], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_avg_type' : EventDefinition(
                group='Overlay: Avg',
                parameters=[
                        EventParameter('overlay_id', Type[int], 
                                        api_description='Overlay ID (must relate to an AVG Overlay)', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('average_type', ['FIRST', 'MAX', 'MIN', 'SINGLE_LAYER', 'GRID'], 
                                        api_description='Averaging type: FIRST, MIN, MAX, SINGLE_LAYER;{"default": null, "values": ["FIRST", "MAX", "MIN", "SINGLE_LAYER", "GRID"]}', api_type=['FIRST', 'MAX', 'MIN', 'SINGLE_LAYER', 'GRID'], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('maplink', None, False, 
                                        api_description='MapLink (will only affect the SINGLE_LAYER averaging type): BUILDINGS, TERRAINS, AREAS, NEIGHBORHOODS', api_type=None, api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Overlay: Combo
        'set_combo_formula' : EventDefinition(
                group='Overlay: Combo',
                parameters=[
                        EventParameter('overlay_id', Type[int], 
                                        api_description='Overlay ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('formula', Type[str], 
                                        api_description='Formula', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Overlay: Heat
        'set_heat_model' : EventDefinition(
                group='Overlay: Heat',
                parameters=[
                        EventParameter('overlay_id', Type[int], 
                                        api_description='Overlays', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('heat_model', ['DPRA', 'UNESCO'], 
                                        api_description='HeatModel;{"default": null, "values": ["DPRA", "UNESCO"]}', api_type=['DPRA', 'UNESCO'], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Overlay: Water
        'set_show_system_visualization' : EventDefinition(
                group='Overlay: Water',
                parameters=[
                        EventParameter('overlay_id', Type[int], 
                                        api_description='Overlay ID (must relate to a water Overlay)', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('visualization_type', ['AREAS', 'OBJECTS'], 
                                        api_description='Visual Type;{"default": null, "values": ["AREAS", "OBJECTS"]}', api_type=['AREAS', 'OBJECTS'], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('visualization_active', Type[bool], 
                                        api_description='Show;{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_water_mode' : EventDefinition(
                group='Overlay: Water',
                parameters=[
                        EventParameter('overlay_id', Type[int], 
                                        api_description='Overlays', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('water_mode', ['ACCURACY', 'AVERAGE', 'SPEED'], 
                                        api_description='Mode;{"default": null, "values": ["ACCURACY", "AVERAGE", "SPEED"]}', api_type=['ACCURACY', 'AVERAGE', 'SPEED'], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_water_weather' : EventDefinition(
                group='Overlay: Water',
                parameters=[
                        EventParameter('overlay_id', Type[int], 
                                        api_description='Water Overlay ID ', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('weather_id', Type[int], 
                                        api_description='Weather ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'remove_water_weather' : EventDefinition(
                group='Overlay: Water',
                parameters=[
                        EventParameter('overlay_id', Type[int], 
                                        api_description='Overlays', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Overlay: Watershed
        'set_discharge_method' : EventDefinition(
                group='Overlay: Watershed',
                parameters=[
                        EventParameter('overlay_id', Type[int], 
                                        api_description='Overlays', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('discharge_method', ['HEIGHT_MINIMA', 'AREAS', 'WATER_TERRAINS'], 
                                        api_description='DischargeMethod;{"default": null, "values": ["HEIGHT_MINIMA", "AREAS", "WATER_TERRAINS"]}', api_type=['HEIGHT_MINIMA', 'AREAS', 'WATER_TERRAINS'], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
    }

event_set = EventSet(definitions, domain='editoroverlay')