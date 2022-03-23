from ..core.connectors import ConnectorTygronSession
from ..utilities.geometries import Geometries

import json

class DataImport:

    @staticmethod
    def geojson_areas( conn_session: ConnectorTygronSession, area_data_content: str, buffer: int = 1 ):
        feature_collection = json.load( area_data_content )
        
        geometry_collection = { 
                "type": "GeometryCollection",
                "geometries": []
            }
        names = []
        attributes_keys = []
        attributes = []
        values = []
        
        
        for  feature in feature_collection['features'] :
            geometry_collection['geometries'].append(feature['geometry'])
            names.append( feature['properties'].get('NAME', 'Unnamed Area') )
            for  prop, value in feature['properties'].items() :
                if (prop.upper() not in attributes):
                    attributes_keys.append( prop ) 
                    attributes.append( prop.upper() ) 
        
        for  feature in feature_collection['features'] :
            for  attribute in attributes_keys :
                value = feature['properties'].get(attribute, None)
                try:
                    float(value)
                except (ValueError, TypeError):
                    if ( not isinstance(value, list) ):
                        value = None
                values.append( value )
        
        query_params = {}
        crs = Geometries.feature_collection_get_crs_code( feature_collection )
        if (crs):
            query_params['CRS'] = crs
        
        response = conn_session.request(
                method='POST',
                url='event/editorarea/import', 
                query_params=query_params,
                data=[ geometry_collection, names, attributes, values, buffer, None ],
            )   