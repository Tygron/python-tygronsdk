from .....core.events import EventSet

from .....core.data.events import Event
from .....core.data.events import EventParameter
from .....core.data.events import EventParameterListable
from .....core.data.events import EventParameterMatrixable

from typing import Type, Union

class EventDefinitionsCollectionClass():

    _add = [
            EventParameter('geotiff_name', Type[str]),
            EventParameter('geotiff_content_bytes', Type[bytes]),
            EventParameter('uploader_name', Type[str]),
            EventParameter('crs', Type[str], False),
        ]
    _add_ascii = [
            EventParameter('geotiff_name', Type[str]),
            EventParameter('ascii_content_bytes', Type[bytes]),
            EventParameter('uploader_name', Type[str]),
        ]
    _set_geotiff = [
            EventParameter('geotiff_id', Type[int]),
            EventParameter('geotiff_content_bytes', Type[bytes]),
            EventParameter('uploader_name', Type[str]),
            EventParameter('crs', Type[str], False),
        ]
    
    _add_url = [
            EventParameter('geotiff_name', Type[str]),
            EventParameter('geotiff_url', Type[str]),
            EventParameter('uploader_name', Type[str]),
            EventParameter('crs', Type[str], False),
        ]
    _add_ascii_url = [
            EventParameter('geotiff_name', Type[str]),
            EventParameter('ascii_url', Type[str]),
            EventParameter('uploader_name', Type[str]),
        ]
    _set_geotiff_url = [
            EventParameter('geotiff_id', Type[int]),
            EventParameter('geotiff_url', Type[str]),
            EventParameter('uploader_name', Type[str]),
            EventParameter('crs', Type[str], False),
        ]
    
    _export = [
            EventParameter('geotiff_id', Type[int]),
        ]
        
    _remove = [
            EventParameterListable('geotiff_id', Type[int]),
        ]


Instance = EventSet(EventDefinitionsCollectionClass)