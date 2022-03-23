from ..core.connectors import ConnectorTygronSession

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
    def export_indicators( conn_session: ConnectorTygronSession, location: str, forms: List[str] ):
        response = conn_session.request(
                method='GET',
                url='items/indicators'
            ).get_response_body();
        if 'html'.lower() in (form.lower() for form in forms):
            return