from .. import interfaces
from .. import items
import base64

class TriggerGeotiffFromGeoshare(interfaces.Trigger):
    
    def run( self ):
        conn_session = self.get_session_connection()
        conn_geoshare = self.get_sdk().create_connector_geoshare()
        
        geotiff_id = self.get_parameter('id')
        geoshare_path = self.get_parameter('geoshare_path')
        
        geotiff_file = None
        
        
        
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
                if ( not tiff_id == geotiff_id ):
                    continue
                    
                value = conn_session.run_query( 'SELECT_GRIDVOLUME_WHERE_GRID_IS_'+ str(overlay['id'])+'_AND_TIMEFRAME_IS_'+str(tiff_index) ).get_response_body()
                if ( value == 0 or True ):
                    tiff = geotiffs.get(tiff_id)
                    if ( not tiff ):
                        continue
                    geotiff_file = conn_geoshare.request(
                            url=geoshare_path
                        ).get_response_body()
                    break
        
        if ( geotiff_file == None ):
            return
        geotiff_file = base64.b64encode(geotiff_file).decode('utf-8')
        self.add_result( 'editorgeotiff/set_geotiff', [
                        geotiff_id,
                        geotiff_file,
                        self.get_trigger_name(),
            ] )