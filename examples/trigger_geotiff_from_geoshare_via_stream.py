from .. import interfaces
from .. import items

class TriggerGeotiffFromGeoshareViaStream(interfaces.Trigger):
    
    def run( self ):
        conn_session = self.get_session_connection()
        
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
            print( overlay['name'] )
            for tiff_index, tiff_id in enumerate(overlay['geoTiffIDs']):
                tiff_id = overlay['geoTiffIDs'][tiff_index]
                value = conn_session.run_query( 'SELECT_GRIDVOLUME_WHERE_GRID_IS_'+ str(overlay['id'])+'_AND_TIMEFRAME_IS_'+str(tiff_index) ).get_response_body()
                print( [geotiffs.get(tiff_id)['name'], value] )
                if ( value == 0 or True ):
                    tiff = geotiffs.get(tiff_id)
                    if ( not tiff_id ):
                        continue
                    asset_name = tiff['name']
                    geoshare_path = self.determine_geoshare_path( asset_name, tiff_id )
                    if ( geoshare_path == None ):
                        continue
                    self.import_geotiff_from_geoshare( geoshare_path, tiff_id, asset_name )

                
    def determine_geoshare_path( self, tiff_name, tiff_id ):
        #check whether tiff_id is part of parameters. If not, check whether asset name is part of parameters
        #invalid urls cause ip block, so don't blindly attempt to load in files
        geoshare_path = self.get_parameter( tiff_id, None )
        if ( geoshare_path == None ):
            geoshare_path = self.get_parameter( tiff_name, None )
        return geoshare_path 
        
    
    def import_geotiff_from_geoshare( self, asset_url:str, asset_id:int = None, asset_name:str = None ):
        
        conn_geoshare = self.get_sdk().create_connector_geoshare()
        conn_session = self.get_session_connection()
        
        geotiff_file_response = conn_geoshare.request(
                url=asset_url,
                stream=True
            )
         
        upload_response = conn_session.stream_upload_geotiff(
                asset_name=asset_name,
                asset_id=asset_id,
                file_data=geotiff_file_response
            )
            
        print(upload_response)
        
        return upload_response.get_response_body()
        
        
        