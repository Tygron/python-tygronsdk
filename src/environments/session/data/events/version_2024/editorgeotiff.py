from ......core.events import EventSet

from ......core.data.events import EventDefinition
from ......core.data.events import EventParameter

from typing import Type

definitions = {


    # Add
        'add' : EventDefinition(
                group='Add',
                parameters=[
                        EventParameter('geotiff_name', Type[str], 
                                        api_description='GeoTIFF Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('geotiff_content_bytes', Type[bytes], aggregation=1, 
                                        api_description='File bytes (< 2GB)', api_type=Type[bytes], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('uploader_name', Type[str], 
                                        api_description='Uploader', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('crs', Type[str], False, 
                                        api_description='CRS Override (optional) ', api_type=Type[str], api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'add_ascii' : EventDefinition(
                group='Add',
                parameters=[
                        EventParameter('geotiff_name', Type[str], 
                                        api_description='GeoTIFF Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('ascii_content_bytes', Type[bytes], aggregation=1, 
                                        api_description='ASCII File bytes (< 2GB)', api_type=Type[bytes], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('uploader_name', Type[str], 
                                        api_description='Uploader', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('crs', Type[str], 
                                        api_description='CRS', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'add_url' : EventDefinition(
                group='Add',
                parameters=[
                        EventParameter('geotiff_name', Type[str], aggregation=1, 
                                        api_description='GeoTIFF Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('geotiff_url', Type[str], aggregation=1, 
                                        api_description='Web URL', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('uploader_name', Type[str], aggregation=1, 
                                        api_description='Uploader', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('crs', Type[str], False, aggregation=1, 
                                        api_description='CRS Override (optional)', api_type=Type[str], api_required=False, api_default=None, api_aggregation=1,  ),
                    ]
            ),
        'add_ascii_url' : EventDefinition(
                group='Add',
                parameters=[
                        EventParameter('geotiff_name', Type[str], aggregation=1, 
                                        api_description='GeoTIFF Name', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('ascii_url', Type[str], aggregation=1, 
                                        api_description='Web ASCII URL', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('uploader_name', Type[str], aggregation=1, 
                                        api_description='Uploader', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('crs', Type[str], aggregation=1, 
                                        api_description='CRS', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),


    # Set
        'set_geotiff' : EventDefinition(
                group='Set',
                parameters=[
                        EventParameter('geotiff_id', Type[int], 
                                        api_description='GeoTIFF ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('geotiff_content_bytes', Type[bytes], aggregation=1, 
                                        api_description='File bytes (< 2GB)', api_type=Type[bytes], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('uploader_name', Type[str], 
                                        api_description='Uploader', api_type=Type[str], api_required=True, api_default=None, api_aggregation=0,  ),
                        EventParameter('crs', Type[str], False, 
                                        api_description='CRS Override (optional)', api_type=Type[str], api_required=False, api_default=None, api_aggregation=0,  ),
                    ]
            ),
        'set_geotiff_url' : EventDefinition(
                group='Set',
                parameters=[
                        EventParameter('geotiff_id', Type[int], aggregation=1, 
                                        api_description='GeoTIFF ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('geotiff_url', Type[str], aggregation=1, 
                                        api_description='Web URL', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('uploader_name', Type[str], aggregation=1, 
                                        api_description='Uploader', api_type=Type[str], api_required=True, api_default=None, api_aggregation=1,  ),
                        EventParameter('crs', Type[str], False, aggregation=1, 
                                        api_description='CRS Override (optional)', api_type=Type[str], api_required=False, api_default=None, api_aggregation=1,  ),
                    ]
            ),


    # Export
        'export' : EventDefinition(
                group='Export',
                parameters=[
                        EventParameter('geotiff_id', Type[int], 
                                        api_description='GeoTIFF ID', api_type=Type[int], api_required=True, api_default=None, api_aggregation=0,  ),
                    ]
            ),


    # Remove
        'remove' : EventDefinition(
                group='Remove',
                parameters=[
                        EventParameter('geotiff_id', Type[int], aggregation=1, 
                                        api_description='Geo Tiffs', api_type=Type[int], api_required=True, api_default=None, api_aggregation=1,  ),
                    ]
            ),
    }

event_set = EventSet(definitions, domain='editorgeotiff')