from .....core.events import EventSet

from .....core.data.events import EventDefinition
from .....core.data.events import EventParameter

from typing import Type

definitions = {


    # General
        'add' : EventDefinition(
                group='General',
                parameters=[
                    ]
            ),
        'duplicate_indicator' : EventDefinition(
                group='General',
                parameters=[
                        EventParameter('indicator_id', Type[int], 
                                        api_description='Indicators', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('stakeholder_id', Type[int], 
                                        api_description='Integer', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'remove' : EventDefinition(
                group='General',
                parameters=[
                        EventParameter('indicator_id', Type[int], aggregation=1, 
                                        api_description='Indicators', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),


    # Attribute
        'set_attribute' : EventDefinition(
                group='Attribute',
                parameters=[
                        EventParameter('indicator_id', Type[int], aggregation=1, 
                                        api_description='Indicators', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_name', Type[str], 
                                        api_description='Attribute Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('attribute_value', Type[float], aggregation=1, 
                                        api_description='Attribute Values', api_type=Type[float], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('source_id', Type[int], False, 
                                        api_description='Source (optional)', api_type=Type[int], api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'remove_attribute' : EventDefinition(
                group='Attribute',
                parameters=[
                        EventParameter('indicator_id', Type[int], aggregation=1, 
                                        api_description='Indicators', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_name', Type[str], aggregation=1, 
                                        api_description='String[]', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),


    # Information
        'set_name' : EventDefinition(
                group='Information',
                parameters=[
                        EventParameter('indicator_id', Type[int], aggregation=1, 
                                        api_description='Indicators', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('name', Type[str], aggregation=1, 
                                        api_description='String[]', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'set_short_name' : EventDefinition(
                group='Information',
                parameters=[
                        EventParameter('indicator_id', Type[int], 
                                        api_description='Indicators', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('name', Type[str], 
                                        api_description='String', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_stakeholder' : EventDefinition(
                group='Information',
                parameters=[
                        EventParameter('indicator_id', Type[int], 
                                        api_description='Indicators', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('stakeholder_id', Type[int], 
                                        api_description='Stakeholders', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'remove_stakeholder' : EventDefinition(
                group='Information',
                parameters=[
                        EventParameter('indicator_id', Type[int], 
                                        api_description='Indicators', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_color' : EventDefinition(
                group='Information',
                parameters=[
                        EventParameter('indicator_id', Type[int], aggregation=1, 
                                        api_description='Indicators', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('color', 'Unknown: (tcolor or multiple values in array [a, b, c])', aggregation=1, 
                                        api_description='TColor[]', api_type='Unknown: (tcolor or multiple values in array [a, b, c])', api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'set_description' : EventDefinition(
                group='Information',
                parameters=[
                        EventParameter('indicator_id', Type[int], 
                                        api_description='Indicators', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('description', Type[str], 
                                        api_description='String', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_image' : EventDefinition(
                group='Information',
                parameters=[
                        EventParameter('indicator_id', Type[int], aggregation=1, 
                                        api_description='Indicators', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('asset_path', Type[str], aggregation=1, 
                                        api_description='String[]', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'set_show_graph' : EventDefinition(
                group='Information',
                parameters=[
                        EventParameter('indicator_id', Type[int], 
                                        api_description='Indicators', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('graph', Type[bool], 
                                        api_description='Boolean;{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Calculation model
        'set_absolute' : EventDefinition(
                group='Calculation model',
                parameters=[
                        EventParameter('indicator_id', Type[int], 
                                        api_description='Indicators', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('absolute', Type[bool], 
                                        api_description='Boolean;{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_active' : EventDefinition(
                group='Calculation model',
                parameters=[
                        EventParameter('indicator_id', Type[int], aggregation=1, 
                                        api_description='Indicators', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('active', Type[bool], aggregation=1, 
                                        api_description='Boolean[]', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'set_excel' : EventDefinition(
                group='Calculation model',
                parameters=[
                        EventParameter('indicator_id', Type[int], 
                                        api_description='Indicators', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('excel_id', Type[int], 
                                        api_description='Excel Sheets', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_target' : EventDefinition(
                group='Calculation model',
                parameters=[
                        EventParameter('scenario_id', Type[int], 
                                        api_description='Scenarios', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('indicator_id', Type[int], 
                                        api_description='Indicators', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('target_id', Type[int], 
                                        api_description='Integer', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('target_value', Type[float], 
                                        api_description='Double', api_type=Type[float], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Calculation
        'reset_indicators' : EventDefinition(
                group='Calculation',
                parameters=[
                        EventParameter('xqueries', Type[bool], False, 
                                        api_description='Reload all Excel X-Queries (optional)', api_type=Type[bool], api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'reset_indicators_with_id' : EventDefinition(
                group='Calculation',
                parameters=[
                        EventParameter('xqueries', Type[bool], 
                                        api_description='Reload all Excel X-Queries;{"default": null, "values": ["true", "false"]}', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('recalculation_id', Type[int], 
                                        api_description='Unique Update ID to prevent multiple updates', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Export
        'export_debug_excel' : EventDefinition(
                group='Export',
                parameters=[
                        EventParameter('indicator_id', Type[int], 
                                        api_description='Indicators', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'excel_min_log_time' : EventDefinition(
                group='Export',
                parameters=[
                        EventParameter('calc_time_in_millis', Type[int], 
                                        api_description='Long', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'export_excel_call_tree' : EventDefinition(
                group='Export',
                parameters=[
                        EventParameter('indicator_id', Type[int], 
                                        api_description='Indicators', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
    }

event_set = EventSet(definitions, domain='editorindicator')