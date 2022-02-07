from ..core.connectors import ConnectorTygronSession

import json

class FileImport:

    def __init__( self ):
        #super().__init__();
        return;

    def import_areas( self, conn_session: ConnectorTygronSession, area_data_content: str, buffer: int = 1 ):
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
        crs = self.get_crs_code_from_feature_collection( feature_collection )
        if (crs):
            query_params['CRS'] = crs
        
        response = conn_session.request(
                method='POST',
                url='event/editorarea/import', 
                query_params=query_params,
                data=[ geometry_collection, names, attributes, values, buffer, None ],
            )
    



    
    def get_crs_code_from_feature_collection( self, feature_collection = {} ):
        if ( feature_collection.get('crs', False) ):
            if ( feature_collection['crs'].get('properties', False) ):
                if ( feature_collection['crs']['properties'].get('name', False) ):
                    crs_parts = feature_collection['crs']['properties']['name'].split(':')
                    if ( len(crs_parts)==2 and str(crs_parts[1]).isnumeric() ):
                        return crs_parts[1]
        return None
