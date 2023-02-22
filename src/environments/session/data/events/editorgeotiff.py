from .....core.events import EventSet

from .....core.data.events import EventDefinition
from .....core.data.events import EventParameter
from .....core.data.events import EventParameterListable
from .....core.data.events import EventParameterMatrixable

from typing import Type, Union

definitions = {
        'add' : EventDefinition(
                    parameters=[
                            EventParameter('geotiff_name', Type[str]),
                            EventParameter('geotiff_content_bytes', Type[bytes]),
                            EventParameter('uploader_name', Type[str]),
                            EventParameter('crs', Type[str], False),
                        ]
            ),
        'add_ascii' : EventDefinition(
                    parameters=[
                            EventParameter('geotiff_name', Type[str]),
                            EventParameter('ascii_content_bytes', Type[bytes]),
                            EventParameter('uploader_name', Type[str]),
                        ]
            ),
        'set_geotiff' : EventDefinition(
                    parameters=[
                            EventParameter('geotiff_id', Type[int]),
                            EventParameter('geotiff_content_bytes', Type[bytes]),
                            EventParameter('uploader_name', Type[str]),
                            EventParameter('crs', Type[str], False),
                        ]
            ),
    
        'add_url' : EventDefinition(
                    parameters=[
                            EventParameter('geotiff_name', Type[str]),
                            EventParameter('geotiff_url', Type[str]),
                            EventParameter('uploader_name', Type[str]),
                            EventParameter('crs', Type[str], False),
                        ]
            ),
        'add_ascii_url' : EventDefinition(
                    parameters=[
                            EventParameter('geotiff_name', Type[str]),
                            EventParameter('ascii_url', Type[str]),
                            EventParameter('uploader_name', Type[str]),
                        ]
            ),
        'set_geotiff_url' : EventDefinition(
                    parameters=[
                            EventParameter('geotiff_id', Type[int]),
                            EventParameter('geotiff_url', Type[str]),
                            EventParameter('uploader_name', Type[str]),
                            EventParameter('crs', Type[str], False),
                        ]
            ),
    
        'export' : EventDefinition(
                    parameters=[
                            EventParameter('geotiff_id', Type[int]),
                        ]
            ),
        
        'remove' : EventDefinition(
                    parameters=[
                            EventParameterListable('geotiff_id', Type[int]),
                        ]
            ),
    }

event_set = EventSet(definitions)