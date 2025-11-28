from ......core.events import EventSet

from ......core.data.events import EventDefinition
from ......core.data.events import EventParameter

from typing import Type

definitions = {


    # Session
        'scenario_set_active' : EventDefinition(
                group='Session',
                parameters=[
                        EventParameter('scenario_id', Type[int], 
                                        api_description='Level ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'session_release' : EventDefinition(
                group='Session',
                parameters=[
                        EventParameter('client_token', Type[str], 
                                        api_description='ClientToken', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'stakeholder_release' : EventDefinition(
                group='Session',
                parameters=[
                        EventParameter('stakeholder_id', Type[int], 
                                        api_description='Stakeholder ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'stakeholder_select' : EventDefinition(
                group='Session',
                parameters=[
                        EventParameter('stakeholder_id', Type[int], 
                                        api_description='Preferred Stakeholder ID or empty', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('client_token', Type[str], 
                                        api_description='Client Token (from Join Session event)', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Information
        'action_log_export' : EventDefinition(
                group='Information',
                parameters=[
                    ]
            ),
        'dismiss_error' : EventDefinition(
                group='Information',
                parameters=[
                        EventParameter('error_log_id', Type[int], aggregation=1, 
                                        api_description='ErrorLog ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'search' : EventDefinition(
                group='Information',
                parameters=[
                        EventParameter('maptype', ['CURRENT', 'MAQUETTE'], 
                                        api_description='Map;{"default": null, "values": ["CURRENT", "MAQUETTE"]}', api_type=['CURRENT', 'MAQUETTE'], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('name', Type[str], 
                                        api_description='Query', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Visualization
        'set_traffic_multiplier' : EventDefinition(
                group='Visualization',
                parameters=[
                        EventParameter('traffic_factor', Type[float], 
                                        api_description='Factor, default 4.0', api_type=Type[float], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'special_effect_set_active' : EventDefinition(
                group='Visualization',
                parameters=[
                        EventParameter('special_effect_id', Type[int], 
                                        api_description='Special Effect ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('active', Type[bool], 
                                        api_description='Activated;{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'unit_type_set_active' : EventDefinition(
                group='Visualization',
                parameters=[
                        EventParameter('unit_data_id', Type[int], 
                                        api_description='UnitDataOverride ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('active', Type[bool], 
                                        api_description='Activated;{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Cinematic
        'cinematic_reached_point' : EventDefinition(
                group='Cinematic',
                parameters=[
                        EventParameter('stakeholder_id', Type[int], 
                                        api_description='Stakeholder ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('cinematic_id', Type[int], 
                                        api_description='Cinematic ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('cinematic_keypoint_id', Type[int], 
                                        api_description='ID of point in cinematic reached', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'cinematic_stakeholder_start' : EventDefinition(
                group='Cinematic',
                parameters=[
                        EventParameter('stakeholder_id', Type[int], 
                                        api_description='Stakeholder ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('cinematic_id', Type[int], 
                                        api_description='Cinematic ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('animate_to_start', Type[bool], True, True, 
                                        api_description='Animate to cinematic starting point;{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'cinematic_stakeholder_stop' : EventDefinition(
                group='Cinematic',
                parameters=[
                        EventParameter('stakeholder_id', Type[int], 
                                        api_description='Stakeholder ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Transaction
        'map_direct_sell_land' : EventDefinition(
                group='Transaction',
                parameters=[
                        EventParameter('stakeholder_id_seller', Type[int], 
                                        api_description='Selling Stakeholder ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('stakeholder_id_buyer', Type[int], 
                                        api_description='Buying Stakeholder ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('transaction_area', 'MultiPolygon', 
                                        api_description='Area of land being sold', api_type='MultiPolygon', api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('price_per_m2', Type[float], 
                                        api_description='Price per square meter', api_type=Type[float], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'money_transfer_add' : EventDefinition(
                group='Transaction',
                parameters=[
                        EventParameter('stakeholder_id_sender', Type[int], 
                                        api_description='Stakeholder From ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('stakeholder_id_receiver', Type[int], 
                                        api_description='Stakeholder To ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('money_transfer_type', ['LAND', 'SUBSIDY', 'TRANSFER'], 
                                        api_description='Money transfer Type;{"default": null, "values": ["LAND", "SUBSIDY", "TRANSFER"]}', api_type=['LAND', 'SUBSIDY', 'TRANSFER'], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('description', Type[str], 
                                        api_description='Provided motivation', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('amount', Type[float], 
                                        api_description='Transfer amount', api_type=Type[float], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'money_transfers_set_approved' : EventDefinition(
                group='Transaction',
                parameters=[
                        EventParameter('money_transfer_id', Type[int], 
                                        api_description='Money transfer ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('approved', Type[bool], True, True, 
                                        api_description='Approved;{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'undo_last_building_action' : EventDefinition(
                group='Transaction',
                parameters=[
                        EventParameter('stakeholder_id', Type[int], 
                                        api_description='Stakeholder ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Measurement
        'measurement_item_add' : EventDefinition(
                group='Measurement',
                parameters=[
                        EventParameter('overlay_id', Type[int], 
                                        api_description='Overlay ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('maplink', ['ACTION_LOGS', 'ACTION_MENUS', 'ADDRESSES', 'AREAS', 'ATTRIBUTE_ACTIONS', 'BUILDINGS', 'CHAT_MESSAGES', 'CINEMATIC_DATAS', 'CLIENT_WORDS', 'COSTS', 'CUSTOM_GEOMETRIES', 'DEFAULT_WORDS', 'ERROR_LOGS', 'EVENT_BUNDLES', 'EXCEL_SHEETS', 'FUNCTION_OVERRIDES', 'FUNCTIONS', 'GEO_LINKS', 'GEO_OPTIONS', 'GEO_PLUGINS', 'GEO_TIFFS', 'GLOBALS', 'HEIGHTS', 'INCOMES', 'INDICATORS', 'LEVEES', 'MEASUREMENTS', 'MEASURES', 'MODEL_DATAS', 'MODEL_SETS', 'MONEY_TRANSFERS', 'NEIGHBORHOODS', 'NET_CLUSTERS', 'NET_FUNCTIONS', 'NET_LINES', 'NET_LOADS', 'NET_NODES', 'NET_SETTINGS', 'OVERLAYS', 'PANELS', 'PARAMETRIC_DESIGNS', 'PARAMETRIC_EXAMPLES', 'PARTICLE_EMITTERS', 'PLOTS', 'POPUPS', 'PROGRESS', 'PROJECT_ASSETS', 'RECORDINGS', 'SCENARIOS', 'SERVER_WORDS', 'SETTINGS', 'SOUNDS', 'SOURCES', 'SPECIAL_EFFECTS', 'SPECIAL_OPTIONS', 'STAKEHOLDERS', 'TERRAIN_TYPE_OVERRIDES', 'TERRAIN_TYPES', 'TERRAINS', 'TEXTURES', 'TIMES', 'TRIGGERS', 'UNIT_DATA_OVERRIDES', 'UNIT_DATAS', 'UPGRADE_TYPES', 'WATER_VALUES', 'WEATHERS', 'ZIP_CODES', 'ZONES'], 
                                        api_description='MapLink ID;{"default": null, "values": ["ACTION_LOGS", "ACTION_MENUS", "ADDRESSES", "AREAS", "ATTRIBUTE_ACTIONS", "BUILDINGS", "CHAT_MESSAGES", "CINEMATIC_DATAS", "CLIENT_WORDS", "COSTS", "CUSTOM_GEOMETRIES", "DEFAULT_WORDS", "ERROR_LOGS", "EVENT_BUNDLES", "EXCEL_SHEETS", "FUNCTION_OVERRIDES", "FUNCTIONS", "GEO_LINKS", "GEO_OPTIONS", "GEO_PLUGINS", "GEO_TIFFS", "GLOBALS", "HEIGHTS", "INCOMES", "INDICATORS", "LEVEES", "MEASUREMENTS", "MEASURES", "MODEL_DATAS", "MODEL_SETS", "MONEY_TRANSFERS", "NEIGHBORHOODS", "NET_CLUSTERS", "NET_FUNCTIONS", "NET_LINES", "NET_LOADS", "NET_NODES", "NET_SETTINGS", "OVERLAYS", "PANELS", "PARAMETRIC_DESIGNS", "PARAMETRIC_EXAMPLES", "PARTICLE_EMITTERS", "PLOTS", "POPUPS", "PROGRESS", "PROJECT_ASSETS", "RECORDINGS", "SCENARIOS", "SERVER_WORDS", "SETTINGS", "SOUNDS", "SOURCES", "SPECIAL_EFFECTS", "SPECIAL_OPTIONS", "STAKEHOLDERS", "TERRAIN_TYPE_OVERRIDES", "TERRAIN_TYPES", "TERRAINS", "TEXTURES", "TIMES", "TRIGGERS", "UNIT_DATA_OVERRIDES", "UNIT_DATAS", "UPGRADE_TYPES", "WATER_VALUES", "WEATHERS", "ZIP_CODES", "ZONES"]}', api_type=['ACTION_LOGS', 'ACTION_MENUS', 'ADDRESSES', 'AREAS', 'ATTRIBUTE_ACTIONS', 'BUILDINGS', 'CHAT_MESSAGES', 'CINEMATIC_DATAS', 'CLIENT_WORDS', 'COSTS', 'CUSTOM_GEOMETRIES', 'DEFAULT_WORDS', 'ERROR_LOGS', 'EVENT_BUNDLES', 'EXCEL_SHEETS', 'FUNCTION_OVERRIDES', 'FUNCTIONS', 'GEO_LINKS', 'GEO_OPTIONS', 'GEO_PLUGINS', 'GEO_TIFFS', 'GLOBALS', 'HEIGHTS', 'INCOMES', 'INDICATORS', 'LEVEES', 'MEASUREMENTS', 'MEASURES', 'MODEL_DATAS', 'MODEL_SETS', 'MONEY_TRANSFERS', 'NEIGHBORHOODS', 'NET_CLUSTERS', 'NET_FUNCTIONS', 'NET_LINES', 'NET_LOADS', 'NET_NODES', 'NET_SETTINGS', 'OVERLAYS', 'PANELS', 'PARAMETRIC_DESIGNS', 'PARAMETRIC_EXAMPLES', 'PARTICLE_EMITTERS', 'PLOTS', 'POPUPS', 'PROGRESS', 'PROJECT_ASSETS', 'RECORDINGS', 'SCENARIOS', 'SERVER_WORDS', 'SETTINGS', 'SOUNDS', 'SOURCES', 'SPECIAL_EFFECTS', 'SPECIAL_OPTIONS', 'STAKEHOLDERS', 'TERRAIN_TYPE_OVERRIDES', 'TERRAIN_TYPES', 'TERRAINS', 'TEXTURES', 'TIMES', 'TRIGGERS', 'UNIT_DATA_OVERRIDES', 'UNIT_DATAS', 'UPGRADE_TYPES', 'WATER_VALUES', 'WEATHERS', 'ZIP_CODES', 'ZONES'], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('item_id', Type[int], 
                                        api_description='Item ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('attribute_key', Type[str], 
                                        api_description='Identifying Key', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('measurement_name', Type[str], 
                                        api_description='Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('save', Type[bool], True, True, 
                                        api_description='Save Measurement;{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'measurement_line_add' : EventDefinition(
                group='Measurement',
                parameters=[
                        EventParameter('overlay_id', Type[int], aggregation=1, 
                                        api_description='Overlay IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('point_start', 'Unknown: (point with crs: epsg:3857)', 
                                        api_description='Point start', api_type='Unknown: (point with crs: epsg:3857)', api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('point_end', 'Unknown: (point with crs: epsg:3857)', 
                                        api_description='Point end', api_type='Unknown: (point with crs: epsg:3857)', api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('measurement_name', Type[str], 
                                        api_description='Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('timeframe', Type[int], True, -1, 
                                        api_description='Timeframe (-1 for automatic last)', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('save', Type[bool], True, True, 
                                        api_description='Save Measurement;{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('sum', Type[bool], True, False, 
                                        api_description='Sum;{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'measurement_point_add' : EventDefinition(
                group='Measurement',
                parameters=[
                        EventParameter('overlay_id', Type[int], aggregation=1, 
                                        api_description='Overlay IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('point', 'Unknown: (point with crs: epsg:3857)', 
                                        api_description='Point', api_type='Unknown: (point with crs: epsg:3857)', api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('measurement_name', Type[str], 
                                        api_description='Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('save', Type[bool], 
                                        api_description='Save Measurement;{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('sum', Type[bool], True, False, 
                                        api_description='Sum;{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'measurement_remove' : EventDefinition(
                group='Measurement',
                parameters=[
                        EventParameter('measurement_id', Type[int], aggregation=1, 
                                        api_description='Measurement ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'measurement_save' : EventDefinition(
                group='Measurement',
                parameters=[
                        EventParameter('measurement_id', Type[int], 
                                        api_description='Measurement ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'measurement_set_overlays' : EventDefinition(
                group='Measurement',
                parameters=[
                        EventParameter('measurement_id', Type[int], 
                                        api_description='Measurement ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('overlay_id', Type[int], aggregation=1, 
                                        api_description='Overlay ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'measurement_set_sum' : EventDefinition(
                group='Measurement',
                parameters=[
                        EventParameter('measurement_id', Type[int], 
                                        api_description='Measurement ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('sum', Type[bool], True, True, 
                                        api_description='Add base Overlays;{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Action menu
        'action_menu_set_function_available' : EventDefinition(
                group='Action menu',
                parameters=[
                        EventParameter('action_menu_id', Type[int], 
                                        api_description='Action Menu ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('function_id', Type[int], 
                                        api_description='Function ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('available', Type[bool], 
                                        api_description='Available;{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'action_menu_set_measure_available' : EventDefinition(
                group='Action menu',
                parameters=[
                        EventParameter('action_menu_id', Type[int], 
                                        api_description='Action Menu ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('measure_id', Type[int], 
                                        api_description='Measure ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('available', Type[bool], 
                                        api_description='Available;{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'action_menu_set_upgrade_available' : EventDefinition(
                group='Action menu',
                parameters=[
                        EventParameter('action_menu_id', Type[int], 
                                        api_description='Action Menu ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('upgrade_id', Type[int], 
                                        api_description='Upgrade ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('available', Type[bool], 
                                        api_description='Available;{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Area
        'area_set_active' : EventDefinition(
                group='Area',
                parameters=[
                        EventParameter('area_id', Type[int], aggregation=1, 
                                        api_description='Area ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('active', Type[bool], aggregation=1, 
                                        api_description='Activated', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'area_set_attribute' : EventDefinition(
                group='Area',
                parameters=[
                        EventParameter('area_id', Type[int], 
                                        api_description='Area ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('attribute_name', Type[str], 
                                        api_description='Attribute Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('attribute_value', Type[float], 
                                        api_description='Value', api_type=Type[float], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'areas_set_attributes' : EventDefinition(
                group='Area',
                parameters=[
                        EventParameter('area_id', Type[int], aggregation=1, 
                                        api_description='Array of Area IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_name', Type[str], aggregation=1, 
                                        api_description='Array of Attributes', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_value', Type[float], aggregation=1, 
                                        api_description='Array of Values', api_type=Type[float], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),


    # Building
        'building_set_attribute' : EventDefinition(
                group='Building',
                parameters=[
                        EventParameter('building_id', Type[int], 
                                        api_description='Building ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('attribute_name', Type[str], 
                                        api_description='Attribute Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('attribute_value', Type[float], 
                                        api_description='Value', api_type=Type[float], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'building_set_attributes' : EventDefinition(
                group='Building',
                parameters=[
                        EventParameter('building_id', Type[int], aggregation=1, 
                                        api_description='Array of Building IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_name', Type[str], aggregation=1, 
                                        api_description='Attribute Names', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_value', Type[float], aggregation=2, 
                                        api_description='Array of values', api_type=Type[float], api_required=True, api_default=None, api_aggregation=2,  ),
                    ]
            ),


    # Global
        'global_set_value' : EventDefinition(
                group='Global',
                parameters=[
                        EventParameter('global_id', Type[int], aggregation=1, 
                                        api_description='Global ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('value', Type[float], aggregation=1, 
                                        api_description='Value', api_type=Type[float], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'global_set_values' : EventDefinition(
                group='Global',
                parameters=[
                        EventParameter('global_id', Type[int], aggregation=1, 
                                        api_description='Global ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('value', Type[float], aggregation=2, 
                                        api_description='Values', api_type=Type[float], api_required=True, api_default=None, api_aggregation=2,  ),
                    ]
            ),


    # Neighborhood
        'neighborhood_set_attribute' : EventDefinition(
                group='Neighborhood',
                parameters=[
                        EventParameter('neighborhood_id', Type[int], 
                                        api_description='Neighborhood ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('attribute_name', Type[str], 
                                        api_description='Valid attribute name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('attribute_value', Type[float], 
                                        api_description='Attribute value', api_type=Type[float], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Network
        'net_cluster_set_fraction_connected' : EventDefinition(
                group='Network',
                parameters=[
                        EventParameter('net_cluster_id', Type[int], 
                                        api_description='NetCluster ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('fraction_connected', Type[float], 
                                        api_description='Fraction connected, between 0 and 1', api_type=Type[float], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'net_cluster_set_load_attribute' : EventDefinition(
                group='Network',
                parameters=[
                        EventParameter('net_cluster_id', Type[int], 
                                        api_description='NetCluster ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('attribute_name', Type[str], 
                                        api_description='Attribute name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('attribute_value', Type[float], 
                                        api_description='Value', api_type=Type[float], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'net_cluster_set_load_attributes' : EventDefinition(
                group='Network',
                parameters=[
                        EventParameter('net_cluster_id', Type[int], 
                                        api_description='NetCluster ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('attribute_name', Type[str], aggregation=1, 
                                        api_description='Array with attribute names', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_value', Type[float], aggregation=1, 
                                        api_description='Array with values', api_type=Type[float], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'net_clusters_set_default_fraction_connected' : EventDefinition(
                group='Network',
                parameters=[
                        EventParameter('fraction_connected', Type[float], 
                                        api_description='Fraction connected, between 0 and 1', api_type=Type[float], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'net_clusters_set_load_attributes' : EventDefinition(
                group='Network',
                parameters=[
                        EventParameter('net_cluster_id', Type[int], aggregation=1, 
                                        api_description='NetCluster IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_name', Type[str], aggregation=1, 
                                        api_description='Array with attribute names', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_value', Type[float], aggregation=2, 
                                        api_description='Array with values', api_type=Type[float], api_required=True, api_default=None, api_aggregation=2,  ),
                    ]
            ),
        'net_clusters_set_state' : EventDefinition(
                group='Network',
                parameters=[
                        EventParameter('net_cluster_id', Type[int], aggregation=1, 
                                        api_description='NetCluster IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('net_type', ['HEAT', 'INTERNET', 'SEWER', 'GAS', 'ELECTRICITY'], aggregation=1, 
                                        api_description='NetType of loads to be changed.', api_type=['HEAT', 'INTERNET', 'SEWER', 'GAS', 'ELECTRICITY'], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('state', 'Unknown: (timestate or multiple values in array [a, b, c])', aggregation=1, 
                                        api_description='Time State (NOTHING, REQUEST_CONSTRUCTION_APPROVAL, REQUEST_ZONING_APPROVAL, READY)', api_type='Unknown: (timestate or multiple values in array [a, b, c])', api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'net_line_set_attribute' : EventDefinition(
                group='Network',
                parameters=[
                        EventParameter('net_line_id', Type[int], 
                                        api_description='NetLine ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('attribute_name', Type[str], 
                                        api_description='Attribute', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('attribute_value', Type[float], 
                                        api_description='Value', api_type=Type[float], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'net_lines_set_attribute' : EventDefinition(
                group='Network',
                parameters=[
                        EventParameter('net_line_id', Type[int], aggregation=1, 
                                        api_description='Array of NetLine IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_name', Type[str], 
                                        api_description='Attribute', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('attribute_value', Type[float], 
                                        api_description='Value', api_type=Type[float], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'net_lines_set_attributes' : EventDefinition(
                group='Network',
                parameters=[
                        EventParameter('net_line_id', Type[int], aggregation=1, 
                                        api_description='Array of NetLine IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_name', Type[str], aggregation=1, 
                                        api_description='Array of Attributes', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_value', Type[float], aggregation=1, 
                                        api_description='Array of Values', api_type=Type[float], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'set_net_setting_boolean' : EventDefinition(
                group='Network',
                parameters=[
                        EventParameter('net_type', 'Unknown: (type or multiple values in array [a, b, c])', aggregation=1, 
                                        api_description='NetSetting Type', api_type='Unknown: (type or multiple values in array [a, b, c])', api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('active', Type[bool], aggregation=1, 
                                        api_description='True or false', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),


    # Zoning
        'zone_set_attribute' : EventDefinition(
                group='Zoning',
                parameters=[
                        EventParameter('zone_id', Type[int], 
                                        api_description='Zone ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('attribute_name', Type[str], 
                                        api_description='Valid attribute name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('attribute_value', Type[float], 
                                        api_description='Attribute value', api_type=Type[float], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'zones_set_attributes' : EventDefinition(
                group='Zoning',
                parameters=[
                        EventParameter('zone_id', Type[int], aggregation=1, 
                                        api_description='Zone IDs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_name', Type[str], aggregation=1, 
                                        api_description='Valid attribute names', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_value', Type[float], aggregation=2, 
                                        api_description='Attribute values', api_type=Type[float], api_required=True, api_default=None, api_aggregation=2,  ),
                    ]
            ),
    }

event_set = EventSet(definitions, domain='logic')