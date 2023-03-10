from .items import Items

from ..connectors import Connector
from ....utilities import geometries

import json
from typing import List

class DataImport:


    @staticmethod
    def geojsons_areas( conn: Connector, area_geojson_strings:List[str] = [], area_buffers = [], area_name_attributes = [] ):

        start_areas = Items.size( conn, 'areas' )
        results = []

        for index, entry in enumerate(area_geojson_strings):
            area_geojson_string = entry
            
            buffer = area_buffers
            if ( isinstance(buffer, list) and len(buffer)>index ):
                buffer = buffer[index]
            if ( not (isinstance(buffer, int) or isinstance(buffer, float)) ):
                buffer = 1
                
            name_attribute = area_name_attributes
            if ( isinstance(name_attribute, list) and len(name_attribute)>index ):
                name_attribute = name_attribute[index]
            if ( not isinstance(name_attribute, str) ):
                name_attribute = 'NAME'
                
            result = DataImport.geojson_areas( conn, area_geojson_string, buffer, name_attribute )
            results.append(result)
            
        return Items.size( conn, 'areas' ) - start_areas


    @staticmethod
    def geojson_areas( conn: Connector, area_geojson_string: str, buffer: int = 1, name_attribute:str = 'NAME' ):
        feature_collection = json.loads( area_geojson_string )
        
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
        
        start_areas = Items.size( conn, 'areas' )
        
        response = conn.request(
                method='POST',
                url='event/editorarea/import', 
                query_params=query_params,
                data=[ geometry_collection, names, attributes, values, buffer, None ],
            )
            
        return Items.size( conn, 'areas' ) - start_areas
            