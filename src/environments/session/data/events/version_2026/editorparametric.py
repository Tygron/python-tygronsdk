from ......core.events import EventSet

from ......core.data.events import EventDefinition
from ......core.data.events import EventParameter

from typing import Type

definitions = {


    # General
        'add' : EventDefinition(
                group='General',
                parameters=[
                        EventParameter('alignment', ['ROAD', 'SPACED'], 
                                        api_description='Alignment;{"default": null, "values": ["ROAD", "SPACED"]}', api_type=['ROAD', 'SPACED'], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'duplicate' : EventDefinition(
                group='General',
                parameters=[
                        EventParameter('design_id', Type[int], aggregation=1, 
                                        api_description='Parametric Designs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'remove' : EventDefinition(
                group='General',
                parameters=[
                        EventParameter('design_id', Type[int], aggregation=1, 
                                        api_description='Parametric Designs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'set_name' : EventDefinition(
                group='General',
                parameters=[
                        EventParameter('design_id', Type[int], aggregation=1, 
                                        api_description='Parametric Designs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('name', Type[str], aggregation=1, 
                                        api_description='String[]', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'add_example' : EventDefinition(
                group='General',
                parameters=[
                        EventParameter('example_type', ['CITY_NEIGHBORHOOD', 'SUBURBAN_NEIGHBORHOOD', 'URBAN_NEIGHBORHOOD', 'WINDMILL_AREA'], 
                                        api_description='Example;{"default": null, "values": ["CITY_NEIGHBORHOOD", "SUBURBAN_NEIGHBORHOOD", "URBAN_NEIGHBORHOOD", "WINDMILL_AREA"]}', api_type=['CITY_NEIGHBORHOOD', 'SUBURBAN_NEIGHBORHOOD', 'URBAN_NEIGHBORHOOD', 'WINDMILL_AREA'], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Attribute
        'append_attribute' : EventDefinition(
                group='Attribute',
                parameters=[
                        EventParameter('design_id', Type[int], aggregation=1, 
                                        api_description='Parametric Designs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_name', Type[str], 
                                        api_description='String', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('attribute_value', Type[float], aggregation=1, 
                                        api_description='double[]', api_type=Type[float], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('source_id', Type[int], False, 
                                        api_description='Sources', api_type=Type[int], api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'remove_attribute' : EventDefinition(
                group='Attribute',
                parameters=[
                        EventParameter('design_id', Type[int], aggregation=1, 
                                        api_description='Parametric Designs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_name', Type[str], aggregation=1, 
                                        api_description='String[]', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'set_attribute' : EventDefinition(
                group='Attribute',
                parameters=[
                        EventParameter('design_id', Type[int], aggregation=1, 
                                        api_description='Parametric Designs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_name', Type[str], 
                                        api_description='String', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('attribute_value', Type[float], aggregation=1, 
                                        api_description='double[]', api_type=Type[float], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('source_id', Type[int], False, 
                                        api_description='Sources', api_type=Type[int], api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_attributes' : EventDefinition(
                group='Attribute',
                parameters=[
                        EventParameter('design_id', Type[int], aggregation=1, 
                                        api_description='Parametric Designs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_name', Type[str], aggregation=1, 
                                        api_description='String[]', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_value', Type[float], aggregation=2, 
                                        api_description='double[][]', api_type=Type[float], api_required=True, api_default=None, api_aggregation=2,  ),
                        EventParameter('source_id', Type[int], False, 
                                        api_description='Sources', api_type=Type[int], api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Parameters
        'add_plot' : EventDefinition(
                group='Parameters',
                parameters=[
                        EventParameter('design_id', Type[int], aggregation=1, 
                                        api_description='Parametric Designs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('function_id', Type[int], aggregation=1, 
                                        api_description='Functions', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'remove_plot' : EventDefinition(
                group='Parameters',
                parameters=[
                        EventParameter('design_id', Type[int], aggregation=1, 
                                        api_description='Parametric Designs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('plot_id', Type[int], aggregation=1, 
                                        api_description='Integer[]', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'remove_plot_attributes' : EventDefinition(
                group='Parameters',
                parameters=[
                        EventParameter('design_id', Type[int], aggregation=1, 
                                        api_description='Parametric Designs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('plot_id', Type[int], aggregation=1, 
                                        api_description='Integer[]', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_name', Type[str], aggregation=1, 
                                        api_description='String[]', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'set_alignment' : EventDefinition(
                group='Parameters',
                parameters=[
                        EventParameter('design_id', Type[int], aggregation=1, 
                                        api_description='Parametric Designs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('alignment', ['ROAD', 'SPACED'], aggregation=1, 
                                        api_description='Alignment[]', api_type=['ROAD', 'SPACED'], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'set_function' : EventDefinition(
                group='Parameters',
                parameters=[
                        EventParameter('design_id', Type[int], aggregation=1, 
                                        api_description='Parametric Designs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('functiontype', ['ROAD', 'BUILDING', 'REMAINDER', 'WATER', 'PARKING', 'PUBLIC_GREEN', 'SIDEWALK', 'GARDEN'], aggregation=1, 
                                        api_description='FunctionType[]', api_type=['ROAD', 'BUILDING', 'REMAINDER', 'WATER', 'PARKING', 'PUBLIC_GREEN', 'SIDEWALK', 'GARDEN'], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('function_id', Type[int], aggregation=1, 
                                        api_description='Integer[]', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'set_plot_attributes' : EventDefinition(
                group='Parameters',
                parameters=[
                        EventParameter('design_id', Type[int], aggregation=1, 
                                        api_description='Parametric Designs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('plot_id', Type[int], aggregation=1, 
                                        api_description='Integer[]', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_name', Type[str], aggregation=1, 
                                        api_description='String[]', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('attribute_value', Type[float], aggregation=2, 
                                        api_description='double[][]', api_type=Type[float], api_required=True, api_default=None, api_aggregation=2,  ),
                        EventParameter(4, Type[int], False, 
                                        api_description='Integer', api_type=Type[int], api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_plot_function' : EventDefinition(
                group='Parameters',
                parameters=[
                        EventParameter('design_id', Type[int], aggregation=1, 
                                        api_description='Parametric Designs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('plot_id', Type[int], aggregation=1, 
                                        api_description='Integer[]', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('function_id', Type[int], aggregation=1, 
                                        api_description='Functions', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),


    # Generation
        'generate' : EventDefinition(
                group='Generation',
                parameters=[
                        EventParameter('design_id', Type[int], 
                                        api_description='Parametric Designs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_polygons' : EventDefinition(
                group='Generation',
                parameters=[
                        EventParameter('design_id', Type[int], aggregation=1, 
                                        api_description='Parametric Designs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('multipolygon', 'MultiPolygon', aggregation=1, 
                                        api_description='MultiPolygon[]', api_type='MultiPolygon', api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),


    # Usage
        'apply' : EventDefinition(
                group='Usage',
                parameters=[
                        EventParameter('design_id', Type[int], 
                                        api_description='Parametric Designs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('stakeholder_id', Type[int], 
                                        api_description='Stakeholders', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('functiontype', ['ROAD', 'BUILDING', 'REMAINDER', 'WATER', 'PARKING', 'PUBLIC_GREEN', 'SIDEWALK', 'GARDEN'], aggregation=1, 
                                        api_description='FunctionType[]', api_type=['ROAD', 'BUILDING', 'REMAINDER', 'WATER', 'PARKING', 'PUBLIC_GREEN', 'SIDEWALK', 'GARDEN'], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('plot_id', Type[int], aggregation=1, 
                                        api_description='Integer[]', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('multipolygon', 'MultiPolygon', aggregation=1, 
                                        api_description='MultiPolygon[][]', api_type='MultiPolygon', api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'save_as_measure' : EventDefinition(
                group='Usage',
                parameters=[
                        EventParameter('design_id', Type[int], 
                                        api_description='Parametric Designs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('stakeholder_id', Type[int], 
                                        api_description='Stakeholders', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('functiontype', ['ROAD', 'BUILDING', 'REMAINDER', 'WATER', 'PARKING', 'PUBLIC_GREEN', 'SIDEWALK', 'GARDEN'], aggregation=1, 
                                        api_description='FunctionType[]', api_type=['ROAD', 'BUILDING', 'REMAINDER', 'WATER', 'PARKING', 'PUBLIC_GREEN', 'SIDEWALK', 'GARDEN'], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('plot_id', Type[int], aggregation=1, 
                                        api_description='Integer[]', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('multipolygon', 'MultiPolygon', aggregation=1, 
                                        api_description='MultiPolygon[][]', api_type='MultiPolygon', api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
    }

event_set = EventSet(definitions, domain='editorparametric')