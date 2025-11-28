from ......core.events import EventSet

from ......core.data.events import EventDefinition
from ......core.data.events import EventParameter

from typing import Type

definitions = {


    # General
        'add' : EventDefinition(
                group='General',
                parameters=[
                    ]
            ),
        'duplicate' : EventDefinition(
                group='General',
                parameters=[
                        EventParameter('indicator_id', Type[int], aggregation=1, 
                                        api_description='Indicators', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
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
        'append_attribute' : EventDefinition(
                group='Attribute',
                parameters=[
                        EventParameter('indicator_id', Type[int], aggregation=1, 
                                        api_description='Indicators', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_name', Type[str], 
                                        api_description='Attribute Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('attribute_value', Type[float], aggregation=1, 
                                        api_description='Attribute Values appended to existing values', api_type=Type[float], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('source', Type[int], False, 
                                        api_description='Source (optional)', api_type=Type[int], api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),
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
        'set_attributes' : EventDefinition(
                group='Attribute',
                parameters=[
                        EventParameter('indicator_id', Type[int], aggregation=1, 
                                        api_description='Indicators', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_name', Type[str], aggregation=1, 
                                        api_description='Attribute Names', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_value', Type[float], aggregation=2, 
                                        api_description='Attribute Values', api_type=Type[float], api_required=True, api_default=None, api_aggregation=2,  ),
                        EventParameter('source', Type[int], False, 
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
        'set_parent' : EventDefinition(
                group='Information',
                parameters=[
                        EventParameter('indicator_id', Type[int], 
                                        api_description='Indicator ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('indicator_parent_id', Type[int], 
                                        api_description='Indicator ID of parent (indicators without a parent should have their parent Indicator ID set to -1)', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_short_name' : EventDefinition(
                group='Information',
                parameters=[
                        EventParameter('indicator_id', Type[int], aggregation=1, 
                                        api_description='Indicators', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('name', Type[str], aggregation=1, 
                                        api_description='String[]', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
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
        'swap_order' : EventDefinition(
                group='Information',
                parameters=[
                        EventParameter('indicator_id', Type[int], aggregation=1, 
                                        api_description='Indicators', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('indicator_target_id', Type[int], aggregation=1, 
                                        api_description='Indicators', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
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


    # Calculation model
        'set_absolute' : EventDefinition(
                group='Calculation model',
                parameters=[
                        EventParameter('indicator_id', Type[int], aggregation=1, 
                                        api_description='Indicators', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('absolute', Type[bool], aggregation=1, 
                                        api_description='Boolean[]', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=1,  ),
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
        'set_update_timing' : EventDefinition(
                group='Calculation model',
                parameters=[
                        EventParameter('indicator_id', Type[int], aggregation=1, 
                                        api_description='Indicators', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('timing', ['BEFORE', 'AFTER'], aggregation=1, 
                                        api_description='Timing[]', api_type=['BEFORE', 'AFTER'], api_required=True, api_default=None, api_aggregation=1,  ),
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