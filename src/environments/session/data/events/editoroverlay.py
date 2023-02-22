from .....core.events import EventSet

from .....core.data.events import EventDefinition
from .....core.data.events import EventParameter
from .....core.data.events import EventParameterListable
from .....core.data.events import EventParameterMatrixable

from typing import Type, Union

definitions = {
        'add' : EventDefinition(
                    parameters=[
                            EventParameter('overlay_type', Type[str]),
                        ]
            ),
        'add_type' : EventDefinition(
                    parameters=[
                            EventParameterListable('overlay_type', Type[str]),
                        ]
            ),
        'add_result_child_overlay' : EventDefinition(
                    parameters=[
                            EventParameter('overlay_id', Type[int]),
                            EventParameter('overlay_type', Type[str]),
                        ]
            ),
        'duplicate' : EventDefinition(
                    parameters=[
                            EventParameterListable('overlay_id', Type[int]),
                        ]
            ),
        'remove' : EventDefinition(
                    parameters=[
                            EventParameterListable('overlay_id', Type[int]),
                        ]
            ),
    
    
    
        'set_name' : EventDefinition(
                    parameters=[
                            EventParameterListable('overlay_id', Type[int]),
                            EventParameterListable('overlay_name', Type[str]),
                        ]
            ),
    """_set_icon' : EventDefinition(
                    parameters=[
                            EventParameterListable('overlay_id', Type[int]),
                            EventParameterListable('asset_name', Type[str]),
                        ]
            ),"""
        'set_visible' : EventDefinition(
                    parameters=[
                            EventParameterListable('overlay_id', Type[int]),
                            EventParameterListable('visibility', Type[bool]),
                        ]
            ),
        'set_parent' : EventDefinition(
                    parameters=[
                            EventParameter('overlay_id', Type[int]),
                            EventParameter('parent_id', Type[int]),
                        ]
            ),
    
    
    
        'set_attribute' : EventDefinition(
                    parameters=[
                            EventParameterListable('overlay_id', Type[int]),
                            EventParameter('attribute_name', Type[str]),
                            EventParameterListable('attribute_values', Type[float]),
                            EventParameter('source_id', Type[int], False),
                        ]
            ),
        'set_attributes' : EventDefinition(
                    parameters=[
                            EventParameterListable('overlay_id', Type[int]),
                            EventParameterListable('attribute_name', Type[str]),
                            EventParameterMatrixable('attribute_values', Type[float]),
                            EventParameter('source_id', Type[int], False),
                        ]
            ),
        'remove_attribute' : EventDefinition(
                    parameters=[
                            EventParameterListable('overlay_id', Type[int]),
                            EventParameterListable('attribute_name', Type[str]),
                        ]
            ),
    
        'set_prequel' : EventDefinition(
                    parameters=[
                            EventParameter('overlay_id', Type[int]),
                            EventParameter('prequel_id', Type[int]),
                            EventParameter('prequel_type', Type[str]),
                            EventParameter('prequel_timeframe', Type[int], False),
                        ]
            ),
        'remove_prequel' : EventDefinition(
                    parameters=[
                            EventParameter('overlay_id', Type[int]),
                            EventParameter('prequel_type', Type[str]),
                        ]
            ),
    
    
    
        'set_grid_active' : EventDefinition(
                    parameters=[
                            EventParameter('overlay_id', Type[int]),
                            EventParameter('active', Type[bool]),
                        ]
            ),
        'set_result_type' : EventDefinition(
                    parameters=[
                            EventParameter('overlay_id', Type[int]),
                            EventParameter('result_type', Type[str]),
                        ]
            ),
        'set_show_difference' : EventDefinition(
                    parameters=[
                            EventParameter('overlay_id', Type[int]),
                            EventParameter('difference', Type[bool]),
                        ]
            ),
        'set_key_value' : EventDefinition(
                    parameters=[
                            EventParameter('overlay_id', Type[int]),
                            EventParameter('key_name', Type[str]),
                            EventParameter('attribute_name', Type[str]),
                        ]
            ),
        'save_grid' : EventDefinition(
                    parameters=[
                            EventParameter('overlay_id', Type[int]),
                        ]
            ),
    
        'refresh_grid' : EventDefinition(
                    parameters=[
                        ]
            ),
    
    
    
    # Legends
        'set_custom_overlay_legend' : EventDefinition(
                    parameters=[
                            EventParameter('overlay_id', Type[int]),
                            EventParameter('custom_legend', Type[bool]),
                        ]
            ),
    """_add_custom_gridoverlay_legend_entry' : EventDefinition(
                    parameters=[
                            EventParameterListable('overlay_id', Type[int]),
                            EventParameterListable('difference', Type[bool], False, False),
                            EventParameterListable('legend_entry_name', Type[str], False, None),
                            EventParameterListable('legend_entry_color', Type[float], False, None),
                            EventParameterListable('legend_entry_value', Type[float], False, None),
                        ]
            ),"""
        'remove_custom_overlay_legend_entry' : EventDefinition(
                    parameters=[
                            EventParameter('overlay_id', Type[int]),
                            EventParameter('difference', Type[bool], False, False),
                            EventParameterListable('legend_entry_id', Type[int]),
                        ]
            ),
        'set_custom_overlay_legend_entry_name' : EventDefinition(
                    parameters=[
                            EventParameter('overlay_id', Type[int]),
                            EventParameter('difference', Type[bool], False, False),
                            EventParameterListable('legend_entry_id', Type[int]),
                            EventParameterListable('legend_entry_name', Type[str]),
                        ]
            ),
        'set_custom_overlay_legend_entry_value' : EventDefinition(
                    parameters=[
                            EventParameter('overlay_id', Type[int]),
                            EventParameter('difference', Type[bool], False, False),
                            EventParameter('legend_entry_id', Type[int]),
                            EventParameter('legend_entry_value', Type[float]),
                        ]
            ),
    """ 'set_custom_overlay_legend_entry_color' : EventDefinition(
                    parameters=[
                            EventParameter('overlay_id', Type[int]),
                            EventParameter('difference', Type[bool], False, False),
                            EventParameter('legend_entry_id', Type[int]),
                            EventParameter('legend_entry_color', Type[float], False, None),
                        ]
            ),"""
    
    
    # Overlay: Area
        'set_overlay_area' : EventDefinition(
                    parameters=[
                            EventParameter('overlay_id', Type[int]),
                            EventParameterListable('area_id', Type[int]),
                            EventParameter('add', Type[bool], False, True),
                        ]
            ),
    
    
    """ 'set_overlay_primary_color' : EventDefinition(
                    parameters=[
                            EventParameter('overlay_id', Type[int]),
                            EventParameter('legend_entry_color', Type[float]),
                        ]
            ),
        'set_overlay_rest_color' : EventDefinition(
                    parameters=[
                            EventParameter('overlay_id', Type[int]),
                            EventParameter('legend_entry_color', Type[float], False, None),
                        ]
            ),"""
    # Overlay: Attribute
        'set_attribute_overlay_color_attribute' : EventDefinition(
                    parameters=[
                            EventParameter('overlay_id', Type[int]),
                            EventParameter('attribute_name', Type[str]),
                        ]
            ),
        'set_attribute_overlay_values' : EventDefinition(
                    parameters=[
                            EventParameter('overlay_id', Type[int]),
                            EventParameter('maplink', Type[str]),
                            EventParameter('attribute', Type[str]),
                        ]
            ),
    # Overlay: Functions
        'add_overlay_function' : EventDefinition(
                    parameters=[
                            EventParameter('overlay_id', Type[int]),
                            EventParameterListable('function_id', Type[int]),
                        ]
            ),
        'remove_overlay_function' : EventDefinition(
                    parameters=[
                            EventParameter('overlay_id', Type[int]),
                            EventParameterListable('function_id', Type[int]),
                        ]
            ),


    # Overlay: Image
        'set_image' : EventDefinition(
                    parameters=[
                            EventParameterListable('overlay_id', Type[int]),
                            EventParameterListable('asset_name', Type[str]),
                        ]
            ),


    # Overlay: Network
        'set_net_overlay' : EventDefinition(
                    parameters=[
                            EventParameter('overlay_id', Type[int]),
                            EventParameter('net_type', Type[str]),
                            EventParameter('visualize_network', Type[bool]),
                            EventParameter('active_only', Type[bool]),
                        ]
            ),


    # Overlay: Source
        'set_overlay_source' : EventDefinition(
                    parameters=[
                            EventParameter('overlay_id', Type[int]),
                            EventParameterListable('source_id', Type[int]),
                            EventParameter('add', Type[bool], False, True),
                        ]
            ),


    # Overlay: GeoTiff
        'set_geotiff' : EventDefinition(
                    parameters=[
                            EventParameter('overlay_id', Type[int]),
                            EventParameterListable('geotiff_id', Type[int]),
                        ]
            ),


    # Overlay: Service source (WMS, WCS)
        'set_source' : EventDefinition(
                    parameters=[
                            EventParameter('overlay_id', Type[int]),
                            EventParameter('source_id', Type[int]),
                        ]
            ),
        'set_source_layer' : EventDefinition(
                    parameters=[
                            EventParameter('overlay_id', Type[int]),
                            EventParameter('source_layer', Type[str]),
                        ]
            ),
    

    # Overlay: Avg
        'set_avg_distance' : EventDefinition(
                    parameters=[
                            EventParameter('overlay_id', Type[int]),
                            EventParameter('distance', Type[float]),
                        ]
            ),
        'set_avg_type' : EventDefinition(
                    parameters=[
                            EventParameter('overlay_id', Type[int]),
                            EventParameter('average_type', Type[str]),
                            EventParameter('maplink', Type[str], False),
                        ]
            ),


    # Overlay: Combo
        'set_combo_formula' : EventDefinition(
                    parameters=[
                            EventParameter('overlay_id', Type[int]),
                            EventParameter('formula', Type[str]),
                        ]
            ),


    # Overlay: Heat
        'set_heat_model' : EventDefinition(
                    parameters=[
                            EventParameter('overlay_id', Type[int]),
                            EventParameter('heat_model', Type[str]),
                        ]
            ),


    # Overlay: Water
        'set_show_system_visualization' : EventDefinition(
                    parameters=[
                            EventParameter('overlay_id', Type[int]),
                            EventParameter('visualization_type', Type[str]),
                            EventParameter('visualization_active', Type[bool]),
                        ]
            ),
        'set_water_mode' : EventDefinition(
                    parameters=[
                            EventParameter('overlay_id', Type[int]),
                            EventParameter('water_mode', Type[str]),
                        ]
            ),
        'set_water_weather' : EventDefinition(
                    parameters=[
                            EventParameter('overlay_id', Type[int]),
                            EventParameter('weather_id', Type[int]),
                        ]
            ),
        'remove_water_weather' : EventDefinition(
                    parameters=[
                            EventParameter('overlay_id', Type[int]),
                        ]
            ),


    # Overlay: Watershed
        'set_discharge_method' : EventDefinition(
                    parameters=[
                            EventParameter('overlay_id', Type[int]),
                            EventParameter('discharge_method', Type[str]),
                        ]
            ),
    }    

event_set = EventSet(definitions)