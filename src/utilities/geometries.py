import json



class Geometries:

    @staticmethod
    def feature_get_center( feature ):
        envelope  = Geometries.feature_get_envelope( feature )
        
        if (envelope == None):
            return envelope
            
        return [ ((envelope['minX']+envelope['maxX'])/2), ((envelope['minY']+envelope['maxY'])/2) ]
        
    @staticmethod
    def feature_get_envelope( feature ):
        queue = [json.loads(json.dumps( feature.get('geometry', {}).get('coordinates', [] ) ))]
        min_x = None
        max_x = None
        min_y = None
        max_y = None
        while queue:
            elem = queue.pop()
            try:
                min_x = ( float(elem[0]) if min_x == None else min(min_x, float(elem[0])) )
                max_x = ( float(elem[0]) if max_x == None else max(max_x, float(elem[0])) )
                min_y = ( float(elem[1]) if min_y == None else min(min_y, float(elem[1])) )
                max_y = ( float(elem[1]) if max_y == None else max(max_y, float(elem[1])) )
            except (ValueError, TypeError, IndexError) as err:
                if ( isinstance(elem, list) ):
                    queue += elem
                else:
                    raise err
                    
        if ( min_x == None ):
            return None
            
        envelope = {
                'minX' : min_x,
                'maxX' : max_x,
                'minY' : min_y,
                'maxY' : max_y
            }
        envelope['xmin'] = envelope['minX']
        envelope['xmax'] = envelope['maxX']
        envelope['ymin'] = envelope['minY']
        envelope['ymax'] = envelope['maxY']
        return envelope
        
    @staticmethod
    def feature_collection_get_crs_code( self, feature_collection = {} ):
        if ( feature_collection.get('crs', False) ):
            if ( feature_collection['crs'].get('properties', False) ):
                if ( feature_collection['crs']['properties'].get('name', False) ):
                    crs_parts = feature_collection['crs']['properties']['name'].split(':')
                    if ( len(crs_parts)==2 and str(crs_parts[1]).isnumeric() ):
                        return crs_parts[1]
        return None