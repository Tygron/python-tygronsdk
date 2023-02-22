from .....core.events import EventSet

from .....core.data.events import EventDefinition
from .....core.data.events import EventParameter
from .....core.data.events import EventParameterListable
from .....core.data.events import EventParameterMatrixable

from typing import Type, Union

definitions = {
        'add' : EventDefinition(
                parameters=[
                        EventParameter('amount', Type[int], False),
                    ]
            ),
        'duplicate' : EventDefinition(
                parameters=[
                        EventParameterListable('area_id', Type[int]),
                    ]
            ),
        'remove' : EventDefinition(
                parameters=[
                        EventParameterListable('area_id', Type[int]),
                    ]
            ),
        'import' : EventDefinition(
                parameters=[
                        EventParameter('geometry_collection', Type[str]),
                        EventParameterListable('names', Type[str]),
                        EventParameterListable('attribute_names', Type[str]),
                        EventParameterMatrixable('attribute_values', Type[float]),
                        EventParameter('buffer', Type[float], False),
                        EventParameter('source_id', Type[int], False),
                    ]
            
            ),
            
            
            
        'set_name' : EventDefinition(
                parameters=[
                        EventParameterListable('area_id', Type[int]),
                        EventParameterListable('name', Type[str]),
                    ]
            ),
        'set_active' : EventDefinition(
                parameters=[
                        EventParameterListable('area_id', Type[int]),
                        EventParameterListable('active', Type[bool]),
                    ]
            ),
        'set_attributes' : EventDefinition(
                parameters=[
                        EventParameterListable('area_id', Type[int]),
                        EventParameterListable('attribute_name', Type[str]),
                        EventParameterMatrixable('attribute_value', Type[float]),
                        EventParameter('source_id', Type[int], False),
                    ]
            ),
        'add_polygons' : EventDefinition(
                parameters=[
                        EventParameterListable('area_id', Type[int]),
                        EventParameterListable('geometry', Type[str]),
                    ]
            ),
            
            
         
        'remove_attribute' : EventDefinition(
                parameters=[
                        EventParameterListable('area_id', Type[int]),
                        EventParameterListable('attribute_name', Type[str]),
                    ]
            ),
        'remove_polygons' : EventDefinition(
                parameters=[
                        EventParameterListable('area_id', Type[int]),
                        EventParameterListable('geometry', Type[str]),
                    ]
            ),
            
            
          
        'generate_border_areas' : EventDefinition(
                parameters=[
                        EventParameter('attribute_to_generate_for', Type[str]),
                        EventParameter('attribute_to_add', Type[str]),
                        EventParameter('width', Type[float], False),
                    ]
            ),
        'generate_inundation_areas' : EventDefinition(
                parameters=[
                        EventParameter('inundation_level_datum', Type[float]),
                    ]
            ),
        'generate_sewer_areas' : EventDefinition(
                parameters=[
                        EventParameter('urbanization', Type[int], False, 3),
                        EventParameter('storage_before_1965', Type[float], False, 0.7*0.001),
                        EventParameter('storage', Type[float], False, 4*0.001),
                        EventParameter('pump_capacity', Type[float], False, 0.7*0.001),
                        EventParameter('water_area_attribute', Type[str], False, ''),
                    ]
            ),
        'generate_water_areas' : EventDefinition(
                parameters=[
                        EventParameter('inundation_level_datum', Type[float]),
                    ]
            )
    }
    
event_set = EventSet(definitions)