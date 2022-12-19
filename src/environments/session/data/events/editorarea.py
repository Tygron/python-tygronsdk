from .....core.events import EventSet

from .....core.data.events import Event
from .....core.data.events import EventParameter
from .....core.data.events import EventParameterListable
from .....core.data.events import EventParameterMatrixable

from typing import Type, Union

class EventDefinitionsCollectionClass():

    _add = [
            EventParameter('amount', Type[int], False),
        ]
    _duplicate = [
            EventParameterListable('area_id', Type[int]),
        ]
    _remove = [
            EventParameterListable('area_id', Type[int]),
        ]
    _import = [
            EventParameter('geometry_collection', Type[str]),
            EventParameterListable('names', Type[str]),
            EventParameterListable('attribute_names', Type[str]),
            EventParameterMatrixable('attribute_values', Type[float]),
            EventParameter('buffer', Type[float], False),
            EventParameter('source_id', Type[int], False),
        ]
        
        
        
    _set_name = [
            EventParameterListable('area_id', Type[int]),
            EventParameterListable('name', Type[str]),
        ]
    _set_active = [
            EventParameterListable('area_id', Type[int]),
            EventParameterListable('active', Type[bool]),
        ]
    _set_attributes = [
            EventParameterListable('area_id', Type[int]),
            EventParameterListable('attribute_name', Type[str]),
            EventParameterMatrixable('attribute_value', Type[float]),
            EventParameter('source_id', Type[int], False),
        ]
    _add_polygons = [
            EventParameterListable('area_id', Type[int]),
            EventParameterListable('geometry', Type[str]),
        ]
        
        
        
    _remove_attribute = [
            EventParameterListable('area_id', Type[int]),
            EventParameterListable('attribute_name', Type[str]),
        ]
    _remove_polygons = [
            EventParameterListable('area_id', Type[int]),
            EventParameterListable('geometry', Type[str]),
        ]
        
        
        
    _generate_border_areas = [
            EventParameter('attribute_to_generate_for', Type[str]),
            EventParameter('attribute_to_add', Type[str]),
            EventParameter('width', Type[float], False),
        ]
    _generate_inundation_areas = [
            EventParameter('inundation_level_datum', Type[float]),
        ]
    _generate_sewer_areas = [
            EventParameter('urbanization', Type[int], False, 3),
            EventParameter('storage_before_1965', Type[float], False, 0.7*0.001),
            EventParameter('storage', Type[float], False, 4*0.001),
            EventParameter('pump_capacity', Type[float], False, 0.7*0.001),
            EventParameter('water_area_attribute', Type[str], False, ''),
        ]
    _generate_water_areas = [
            EventParameter('inundation_level_datum', Type[float]),
        ]


Instance = EventSet(EventDefinitionsCollectionClass)