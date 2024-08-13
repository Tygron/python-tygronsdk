from ......core.events import EventSet

from ......core.data.events import EventDefinition
from ......core.data.events import EventParameter

from typing import Type

definitions = {


    # General
        'add' : EventDefinition(
                group='General',
                parameters=[
                        EventParameter('type', ['AREA', 'BUILDING', 'ROAD', 'TERRAIN_HEIGHT', 'WATER_BOTTOM'], 
                                        api_description='GeoLinkType;{"default": null, "values": ["AREA", "BUILDING", "ROAD", "TERRAIN_HEIGHT", "WATER_BOTTOM"]}', api_type=['AREA', 'BUILDING', 'ROAD', 'TERRAIN_HEIGHT', 'WATER_BOTTOM'], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'duplicate' : EventDefinition(
                group='General',
                parameters=[
                        EventParameter('geoplugin_id', Type[int], aggregation=1, 
                                        api_description='Geo Plugins', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'remove' : EventDefinition(
                group='General',
                parameters=[
                        EventParameter('geoplugin_id', Type[int], aggregation=1, 
                                        api_description='Geo Plugins', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),


    # Link
        'add_link' : EventDefinition(
                group='Link',
                parameters=[
                        EventParameter('geoplugin_id', Type[int], aggregation=1, 
                                        api_description='Geo Plugins', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('geolink_id', Type[int], aggregation=1, 
                                        api_description='Geo Links', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'add_new_links' : EventDefinition(
                group='Link',
                parameters=[
                        EventParameter('geoplugin_id', Type[int], aggregation=1, 
                                        api_description='Geo Plugins', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('name', Type[str], aggregation=1, 
                                        api_description='String[]', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'remove_link' : EventDefinition(
                group='Link',
                parameters=[
                        EventParameter('geoplugin_id', Type[int], aggregation=1, 
                                        api_description='Geo Plugins', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('geolink_id', Type[int], aggregation=1, 
                                        api_description='Geo Links', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),


    # Datasource
        'remove_source' : EventDefinition(
                group='Datasource',
                parameters=[
                        EventParameter('geoplugin_id', Type[int], aggregation=1, 
                                        api_description='Geo Plugins', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('source_id', Type[int], aggregation=1, 
                                        api_description='Sources', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'set_crs' : EventDefinition(
                group='Datasource',
                parameters=[
                        EventParameter('geoplugin_id', Type[int], aggregation=1, 
                                        api_description='Geo Plugins', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('crs', Type[str], aggregation=1, 
                                        api_description='String[]', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'set_force_xy' : EventDefinition(
                group='Datasource',
                parameters=[
                        EventParameter('geoplugin_id', Type[int], aggregation=1, 
                                        api_description='Geo Plugins', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('force_xy', Type[bool], aggregation=1, 
                                        api_description='Boolean[]', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'set_id_attribute' : EventDefinition(
                group='Datasource',
                parameters=[
                        EventParameter('geoplugin_id', Type[int], aggregation=1, 
                                        api_description='Geo Plugins', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('id_attribute', Type[str], aggregation=1, 
                                        api_description='String[]', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'set_layer_name' : EventDefinition(
                group='Datasource',
                parameters=[
                        EventParameter('geoplugin_id', Type[int], aggregation=1, 
                                        api_description='Geo Plugins', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('layer_name', Type[str], aggregation=1, 
                                        api_description='String[]', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'set_name_attribute' : EventDefinition(
                group='Datasource',
                parameters=[
                        EventParameter('geoplugin_id', Type[int], aggregation=1, 
                                        api_description='Geo Plugins', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('name_attribute', Type[str], aggregation=1, 
                                        api_description='String[]', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'set_source' : EventDefinition(
                group='Datasource',
                parameters=[
                        EventParameter('geoplugin_id', Type[int], aggregation=1, 
                                        api_description='Geo Plugins', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('source_id', Type[int], aggregation=1, 
                                        api_description='Sources', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),


    # Information
        'set_image' : EventDefinition(
                group='Information',
                parameters=[
                        EventParameter('geoplugin_id', Type[int], aggregation=1, 
                                        api_description='Geo Plugins', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('image_name', Type[str], aggregation=1, 
                                        api_description='String[]', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'set_name' : EventDefinition(
                group='Information',
                parameters=[
                        EventParameter('geoplugin_id', Type[int], aggregation=1, 
                                        api_description='Geo Plugins', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('name', Type[str], aggregation=1, 
                                        api_description='String[]', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),


    # Templating
        'set_new_project' : EventDefinition(
                group='Templating',
                parameters=[
                        EventParameter('geoplugin_id', Type[int], aggregation=1, 
                                        api_description='Geo Plugins', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('new_project', Type[bool], aggregation=1, 
                                        api_description='Boolean[]', api_type=Type[bool], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
    }

event_set = EventSet(definitions, domain='editorgeoplugin')