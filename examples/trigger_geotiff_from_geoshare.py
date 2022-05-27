from .. import interfaces
from .. import items

import json
import base64
import re

class TriggerGeotiffFromGeoshare(interfaces.Trigger):
    
    def is_only_mode_editor( self ):
        return True
    
    def run( self ):
        conn_session = self.get_session_connection()
        conn_geoshare = self.get_sdk().create_connector_geoshare()

        result_ids = []
        result_urls = []
        result_uploaders = []
	
        print( conn_session.get_url_full() )
        overlays = conn_session.request(
                url='items/overlays'
            ).get_response_body_json()
        overlays = items.ItemMap( overlays, False )
        geotiffs = conn_session.request(
                url='items/geotiffs'
            ).get_response_body_json()
        geotiffs = items.ItemMap( geotiffs, False )
        
        for overlay in overlays:
            if overlay['type'] != 'GEO_TIFF':
                continue
            for tiff_index, tiff_id in enumerate(overlay['geoTiffIDs']):      

                value = conn_session.run_query( 'SELECT_GRIDVOLUME_WHERE_GRID_IS_'+ str(overlay['id'])+'_AND_TIMEFRAME_IS_'+str(tiff_index) ).get_response_body()          
                if ( float(value) != 0 ):
                    print( 'Geotiff has value '+value+', skip' )
                    continue;

                tiff = geotiffs.get(tiff_id)
                if ( not tiff ):
                    continue
                url = self.get_geoshare_url_for_geotiff( tiff['id'], tiff['name'] )
                if ( url == None):
                    continue;
                result_ids.append( tiff['id'])
                if ( re.match('^([^.]*)://', url) ):
                    result_urls.append( url )
                else:
                    result_urls.append( conn_geoshare.get_url_full(url) )
                result_uploaders.append( self.get_trigger_name() )
        
        if ( len(result_ids) == 0 ):
            return

        self.add_result( 'editorgeotiff/set_geotiff_url', [
                result_ids,
                result_urls, #json.dumps(result_urls) if len(result_urls) != 1 else result_urls[0],
                result_uploaders #json.dumps(result_uploaders) if len(result_uploaders) != 1 else result_uploaders[0],
            ])
    
    def get_geoshare_url_for_geotiff( self, tiff_id:int = None, tiff_name:str = None):
        print( 'Looking for: ' + tiff_name )
        url = None
        if ( url == None ):
            url = self.get_parameter( str(tiff_id) )
        if ( url == None ):
            url = self.get_parameter( tiff_name )
        if ( url == None ):
            #additional check, accounting for the fact that if this parameter is provided by a php script, the dot may be replaced by an underscore
            url = self.get_parameter( str(tiff_name + '.tiff').replace( '.', '_' ) )

        print( 'Result for: ' + str(tiff_name) + ' (' + str(tiff_id) + ')' +' is ' + str(url) )
        return url


