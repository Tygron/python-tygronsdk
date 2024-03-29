from ... import interfaces
from ... import items

import json
import re

class TriggerGeotiffFromGeoshare(interfaces.Trigger):
    
    def is_only_mode_editor( self ):
        return True
    
    def get_supported_types( self ):
        return 'EVENT'
    
    def get_description( self ):
        return '''<p>Checks whether specific GeoTiff files in a Project are empty (have no data), and if so instructs the Tygron Platform to update them with indicated data from the GeoShare.</p>
        
        <p>This allows for GeoTiff files in Projects created from Templates to be populated with data from the GeoShare automatically. In the original Template Project the GeoTiff may have appropriate data, but in a new Project based on that Project Template the GeoTiff will not have any data. By providing GeoShare urls of where to find data for specific GeoTiffs, this trigger will repopulate data to the GeoTiffs automatically.</p>
        
        <p>Note that the GeoShare host accessed is the same host the Session is active on. When the originating Session is the LTS Platform, the GeoShare accessed is the LTS Platform.</p>'''
    
    def get_documented_results( self ):
        return 'All indicated GeoTiffs are updated with the latest version as available on the GeoShare.'
    
    def get_documented_parameters( self ):
        return '''Add parameters of the form "&[GEOTIFF]=[URL]" to the task url, where:<ol>
            <li>[GEOTIFF] is either the ID of the GeoTiff or the name of the GeoTiff</li>
            <li>[URL] is the location of the file on the GeoShare</li>
            As many can be added as desired.'''
    
    def get_instructions_usage( self ):
        return '''<p>Ensure the data for the GeoTiff is present on the GeoShare, and that the url for the GeoTiff file on the GeoShare is known.</p>
        <p>Ensure that there is a GeoTiff present in the Project, and that that GeoTiff is used in a GeoTiff Overlay.</p>
        <p>Add Add parameters of the form "&[GEOTIFF]=[URL]" to the task url.</p>
        <p>Recalculate the project. All indicated GeoTiffs which are part of a GeoTiff Overlay, and have no discernable data (their volume value amounts to 0) will be updated from their respectively indicated urls.</p>
        '''
    
    def get_usage_examples( self ):
        return {
            '&bbp-value=tygron/foo/bbp-information.tiff' : 'Will check whether a GeoTiff named "bbp-value has any discernable data. If not, will instruct the Tygron Platform to update the GeoTiff with data on the GeoShare. Specifically, the file accessible by the url "https://engine.tygron.com/share/tygron/foo/bbp-information.tiff".'
        }
    
    def run( self ):
        result_ids = []
        result_urls = []
        result_uploaders = []
	
        sdk = self.get_sdk()
        
        overlays = sdk.session.items.load( items.Overlay )
        geotiffs = sdk.session.items.load( items.GeoTiff )
        
        overlay_skip_check = self.get_parameter( 'overlaySkipCheck' )
        timeframe_skip_check = self.get_parameter( 'timeframeSkipCheck' )
        if ( not(overlay_skip_check is None) ):
            value = self.check_overlay_has_data( overlay_skip_check, timeframe_skip_check )
            print(value)
            if ( float(value) != 0 ):
                return

        for overlay in overlays:
            if overlay.get('type') != 'GEO_TIFF':
                continue
            for tiff_index, tiff_id in enumerate(overlay.get('geoTiffIDs')):      

                value = self.check_overlay_has_data( overlay.id, tiff_index )

                if ( float(value) != 0 ):
                    print( 'Geotiff has value '+value+', skip' )
                    continue;

                tiff = geotiffs.get(tiff_id)
                if ( not tiff ):
                    continue
                url = self.get_geoshare_url_for_geotiff( tiff.id, tiff.name )
                if ( url == None):
                    continue;
                result_ids.append( tiff.id)
                if ( re.match('^([^.]*)://', url) ):
                    result_urls.append( url )
                else:
                    result_urls.append( sdk.share.connector.get_url_full(url) )
                result_uploaders.append( self.get_trigger_name() )
        
        if ( len(result_ids) == 0 ):
            return

        self.add_result( 'editorgeotiff/set_geotiff_url', [
                result_ids,
                result_urls, #json.dumps(result_urls) if len(result_urls) != 1 else result_urls[0],
                result_uploaders #json.dumps(result_uploaders) if len(result_uploaders) != 1 else result_uploaders[0],
            ])

    def check_overlay_has_data( self, overlay_id:int, timeframe_index:int = None ):
        query = 'SELECT_GRIDVOLUME_WHERE_GRID_IS_' + str(overlay_id)
        if ( not(timeframe_index is None) ):
            query = query + '_AND_TIMEFRAME_IS_'+str(timeframe_index)

        sdk = self.get_sdk()
        value = sdk.session.connector.run_query( query ).get_response_body()

        return value
    
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


