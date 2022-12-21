from .....core.events import EventSet

from .....core.data.events import Event
from .....core.data.events import EventParameter
from .....core.data.events import EventParameterListable
from .....core.data.events import EventParameterMatrixable

from typing import Type, Union

class EventDefinitionsCollectionClass():

    _add = [
            EventParameter('overlay_type', Type[str]),
        ]
    _add_type = [
            EventParameterListable('overlay_type', Type[str]),
        ]
    _add_result_child_overlay = [
            EventParameter('overlay_id', Type[int]),
            EventParameter('overlay_type', Type[str]),
        ]
    _duplicate = [
            EventParameterListable('overlay_id', Type[int]),
        ]
    _remove = [
            EventParameterListable('overlay_id', Type[int]),
        ]
    
    
    
    _set_name = [
            EventParameterListable('overlay_id', Type[int]),
            EventParameterListable('overlay_name', Type[str]),
        ]
    """_set_icon = [
            EventParameterListable('overlay_id', Type[int]),
            EventParameterListable('asset_name', Type[str]),
        ]"""
    _set_visible = [
            EventParameterListable('overlay_id', Type[int]),
            EventParameterListable('visibility', Type[bool]),
        ]
    _set_parent = [
            EventParameter('overlay_id', Type[int]),
            EventParameter('parent_id', Type[int]),
        ]
    
    
    
    _set_attribute = [
            EventParameterListable('overlay_id', Type[int]),
            EventParameter('attribute_name', Type[str]),
            EventParameterListable('attribute_values', Type[float]),
            EventParameter('source_id', Type[int], False),
        ]
    _set_attributes = [
            EventParameterListable('overlay_id', Type[int]),
            EventParameterListable('attribute_name', Type[str]),
            EventParameterMatrixable('attribute_values', Type[float]),
            EventParameter('source_id', Type[int], False),
        ]
    _remove_attribute = [
            EventParameterListable('overlay_id', Type[int]),
            EventParameterListable('attribute_name', Type[str]),
        ]
    
    _set_prequel = [
            EventParameter('overlay_id', Type[int]),
            EventParameter('prequel_id', Type[int]),
            EventParameter('prequel_type', Type[str]),
            EventParameter('prequel_timeframe', Type[int], False),
        ]
    _remove_prequel = [
            EventParameter('overlay_id', Type[int]),
            EventParameter('prequel_type', Type[str]),
        ]
    
    
    
    _set_grid_active = [
            EventParameter('overlay_id', Type[int]),
            EventParameter('active', Type[bool]),
        ]
    _set_result_type = [
            EventParameter('overlay_id', Type[int]),
            EventParameter('result_type', Type[str]),
        ]
    _set_show_difference = [
            EventParameter('overlay_id', Type[int]),
            EventParameter('difference', Type[bool]),
        ]
    _set_key_value = [
            EventParameter('overlay_id', Type[int]),
            EventParameter('key_name', Type[str]),
            EventParameter('attribute_name', Type[str]),
        ]
    _save_grid = [
            EventParameter('overlay_id', Type[int]),
        ]
    
    _refresh_grid = [
        ]
    
    
    
    # Legends
    _set_custom_overlay_legend = [
            EventParameter('overlay_id', Type[int]),
            EventParameter('custom_legend', Type[bool]),
        ]
    """_add_custom_gridoverlay_legend_entry = [
            EventParameterListable('overlay_id', Type[int]),
            EventParameterListable('difference', Type[bool], False, False),
            EventParameterListable('legend_entry_name', Type[str], False, None),
            EventParameterListable('legend_entry_color', Type[float], False, None),
            EventParameterListable('legend_entry_value', Type[float], False, None),
        ]"""
    _remove_custom_overlay_legend_entry = [
            EventParameter('overlay_id', Type[int]),
            EventParameter('difference', Type[bool], False, False),
            EventParameterListable('legend_entry_id', Type[int]),
        ]
    _set_custom_overlay_legend_entry_name = [
            EventParameter('overlay_id', Type[int]),
            EventParameter('difference', Type[bool], False, False),
            EventParameterListable('legend_entry_id', Type[int]),
            EventParameterListable('legend_entry_name', Type[str]),
        ]
    _set_custom_overlay_legend_entry_value = [
            EventParameter('overlay_id', Type[int]),
            EventParameter('difference', Type[bool], False, False),
            EventParameter('legend_entry_id', Type[int]),
            EventParameter('legend_entry_value', Type[float]),
        ]
    """_set_custom_overlay_legend_entry_color = [
            EventParameter('overlay_id', Type[int]),
            EventParameter('difference', Type[bool], False, False),
            EventParameter('legend_entry_id', Type[int]),
            EventParameter('legend_entry_color', Type[float], False, None),
        ]"""
    
    
    # Overlay: Area
    _set_overlay_area = [
            EventParameter('overlay_id', Type[int]),
            EventParameterListable('area_id', Type[int]),
            EventParameter('add', Type[bool], False, True),
        ]
    
    
    """_set_overlay_primary_color = [
            EventParameter('overlay_id', Type[int]),
            EventParameter('legend_entry_color', Type[float]),
        ]
    _set_overlay_rest_color = [
            EventParameter('overlay_id', Type[int]),
            EventParameter('legend_entry_color', Type[float], False, None),
        ]"""
    # Overlay: Attribute
    _set_attribute_overlay_color_attribute = [
            EventParameter('overlay_id', Type[int]),
            EventParameter('attribute_name', Type[str]),
        ]
    _set_attribute_overlay_values = [
            EventParameter('overlay_id', Type[int]),
            EventParameter('maplink', Type[str]),
            EventParameter('attribute', Type[str]),
        ]
    # Overlay: Functions
    _add_overlay_function = [
            EventParameter('overlay_id', Type[int]),
            EventParameterListable('function_id', Type[int]),
        ]
    _remove_overlay_function = [
            EventParameter('overlay_id', Type[int]),
            EventParameterListable('function_id', Type[int]),
        ]


    # Overlay: Image
    _set_image = [
            EventParameterListable('overlay_id', Type[int]),
            EventParameterListable('asset_name', Type[str]),
        ]


    # Overlay: Network
    _set_net_overlay = [
            EventParameter('overlay_id', Type[int]),
            EventParameter('net_type', Type[str]),
            EventParameter('visualize_network', Type[bool]),
            EventParameter('active_only', Type[bool]),
        ]


    # Overlay: Source
    _set_overlay_source = [
            EventParameter('overlay_id', Type[int]),
            EventParameterListable('source_id', Type[int]),
            EventParameter('add', Type[bool], False, True),
        ]


    # Overlay: GeoTiff
    _set_geotiff = [
            EventParameter('overlay_id', Type[int]),
            EventParameterListable('geotiff_id', Type[int]),
        ]


    # Overlay: Service source (WMS, WCS)
    set_source = [
            EventParameter('overlay_id', Type[int]),
            EventParameter('source_id', Type[int]),
        ]
    set_source_layer = [
            EventParameter('overlay_id', Type[int]),
            EventParameter('source_layer', Type[str]),
        ]
    

    # Overlay: Avg
    _set_avg_distance = [
            EventParameter('overlay_id', Type[int]),
            EventParameter('distance', Type[float]),
        ]
    _set_avg_type = [
            EventParameter('overlay_id', Type[int]),
            EventParameter('average_type', Type[str]),
            EventParameter('maplink', Type[str], False),
        ]


    # Overlay: Combo
    _set_combo_formula = [
            EventParameter('overlay_id', Type[int]),
            EventParameter('formula', Type[str]),
        ]


    # Overlay: Heat
    _set_heat_model = [
            EventParameter('overlay_id', Type[int]),
            EventParameter('heat_model', Type[str]),
        ]


    # Overlay: Water
    _set_show_system_visualization = [
            EventParameter('overlay_id', Type[int]),
            EventParameter('visualization_type', Type[str]),
            EventParameter('visualization_active', Type[bool]),
        ]
    _set_water_mode = [
            EventParameter('overlay_id', Type[int]),
            EventParameter('water_mode', Type[str]),
        ]
    _set_water_weather = [
            EventParameter('overlay_id', Type[int]),
            EventParameter('weather_id', Type[int]),
        ]
    _remove_water_weather = [
            EventParameter('overlay_id', Type[int]),
        ]


    # Overlay: Watershed
    _set_discharge_method = [
            EventParameter('overlay_id', Type[int]),
            EventParameter('discharge_method', Type[str]),
        ]
    



Instance = EventSet(EventDefinitionsCollectionClass)