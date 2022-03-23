



class Geometries:

    @staticmethod
    def feature_get_centre( feature ):
        queue = json.loads(json.dumps( feature.get('geometry', {}).get('coordinates', [] ) ))
        minX = None
        maxX = None
        minY = None
        maxY = None
        while queue:
            elem = queue.pop()
            try:
                minX = ( float(elem[0]) if minX == None else min(minX, float(elem[0])) )
                maxX = ( float(elem[0]) if maxX == None else max(maxX, float(elem[0])) )
                minY = ( float(elem[1]) if minY == None else min(minY, float(elem[1])) )
                maxY = ( float(elem[1]) if maxY == None else max(maxY, float(elem[1])) )
            except (ValueError, TypeError, IndexError) as err:
                if ( isinstance(elem, list) ):
                    queue += elem
                else:
                    raise err
        return [ ((minX+maxX)/2), ((minY+maxY)/2) ]
        
    @staticmethod
    def feature_collection_get_crs_code( self, feature_collection = {} ):
        if ( feature_collection.get('crs', False) ):
            if ( feature_collection['crs'].get('properties', False) ):
                if ( feature_collection['crs']['properties'].get('name', False) ):
                    crs_parts = feature_collection['crs']['properties']['name'].split(':')
                    if ( len(crs_parts)==2 and str(crs_parts[1]).isnumeric() ):
                        return crs_parts[1]
        return None