from ..connectors import Connector

from typing import List
import json

class DataExport:

    #Standardized forms of export are:
    # html      decorated output
    # body      pure output
    # excel     debug excel which generated output
    # png       image
    # geotiff   grid geodata
    # geojson   vector geodata
    # json      dump
    
    def __init__( self ):
        #super().__init__();
        return;
 
    @staticmethod   
    def export_indicators( conn: Connector, location: str, forms: List[str] ):
        response = conn.request(
                method='GET',
                url='items/indicators'
            ).get_response_body()
        if 'html'.lower() in (form.lower() for form in forms):
            return
        
    @staticmethod
    def get_overlay_geotiff( conn: Connector, overlay_id:int, timeframe: int = None ):
        return conn.request(
                method  ='GET',
                url     = 'overlay.geotiff',
                query_params  = {'id':overlay_id, 'timeframe':timeframe}
            ).get_response_body()
            
    @staticmethod
    def get_overlay_geotiff_url( conn: Connector, overlay_id:int, timeframe: int = None ):
        return conn.get_url_full(
                path    = 'overlay.geotiff',
                params  = {'id':overlay_id, 'timeframe':timeframe}
            )