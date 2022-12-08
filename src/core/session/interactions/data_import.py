from ..connectors import Connector
from ....utilities import geometries

import json

class DataImport:

    @staticmethod
    def geojson_areas( conn: Connector, area_data_content: str, buffer: int = 1, name_attribute:str = 'NAME' ):
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
            names.append( feature['properties'].get(name_attribute, 'Unnamed Area') )
            for  prop, value in feature['properties'].items() :
                if (prop.upper() not in attributes):
                    attributes_keys.append( prop ) 
                    attributes.append( prop.upper() ) 
        
        for  feature in feature_collection['features'] :
            for  attribute in attributes_keys :
                value = feature['properties'].get(attribute, None)
                try:
                    value = float(value)
                except (ValueError, TypeError):
                    if ( not isinstance(value, list) ):
                        value = None
                    #TODO: test whether each entry in list is float, cast to float
                values.append( value )
        
        query_params = {}
        crs = geometries.feature_collection_get_crs_code( feature_collection )
        if (crs):
            query_params['CRS'] = crs
        
        response = conn.request(
                method='POST',
                url='event/editorarea/import', 
                query_params=query_params,
                data=[ geometry_collection, names, attributes, values, buffer, None ],
            )   