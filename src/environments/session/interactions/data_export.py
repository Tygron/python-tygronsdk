from ..connectors import Connector
from ..data.items import Item, ItemMap
from ..data.items import Indicator, Panel, Overlay
from .items import Items
from .... import utilities

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
    def get_overlay_geotiff( conn: Connector, overlay_id:int, timeframe: int = None ):
        #raise Exception('Deprecated')
        return conn.request(
                method  ='GET',
                url     = 'overlay.geotiff',
                query_params  = {'id':overlay_id, 'timeframe':timeframe}
            ).get_response_body()
            
    @staticmethod
    def get_overlay_geotiff_url( conn: Connector, overlay_id:int, timeframe: int = None ):
        #raise Exception('Deprecated')
        return conn.get_url_full(
                path    = 'overlay.geotiff',
                params  = {'id':overlay_id, 'timeframe':timeframe}
            )
    
    
    
    
    
    
    
    @staticmethod
    def export( conn: Connector, item_type, item_id:int, export_type:str, indexes = -1, 
                identifier:str = '{item_type}-{item_name}-{item_id}{extention}'
            ):
        item_type = item_type if isinstance(item_type, str) else item_type.get_item_type()
        item_type = item_type.lower()
        
        item = Items.get(
                conn=conn,
                item_type=item_type, 
                item_id=item_id
            )
        
        export_type = export_type.lower()
        multiple_indexes = False
        
        export_results = {}
        export_result = None
        if ( export_type == 'png' ):
            multiple_indexes = True
            export_result = DataExport.export_overlay_as_png( conn, item_id, timeframes=indexes )
            extention = 'png'
        elif ( export_type == 'geotiff' ):
            multiple_indexes = True
            export_result = DataExport.export_overlay( conn, item_id, timeframes=indexes, format=export_type)
            extention = 'tiff'
            
        elif ( export_type == 'json' ):
            export_result = DataExport.export_as_json( conn, item_type, item_id )
            extention = 'json'
        elif ( export_type == 'content' ):
            export_result = DataExport.export_as_content( conn, item_type, item_id )
            extention = 'txt'
        elif ( export_type == 'html' ):
            export_result = DataExport.export_as_html( conn, item_type, item_id )
            extention = 'html'
        elif ( export_type == 'body' ):
            export_result = DataExport.export_as_body( conn, item_type, item_id )
            extention = 'html'
        elif ( export_type == 'excel' ):
            export_result = DataExport.export_as_excel( conn, item_type, item_id )
            extention = 'xlsx'
        else:
            raise Exception( 'Unknown export format: '+export_type )
        
        extention = '.'+extention if (not extention is None) else ''
        
        if ( identifier is None ):
            return export_result
        
        if ( not multiple_indexes ):
            export_result = { 0:export_result }
        for index, result in export_result.items():
            formatted_identifier = DataExport.generate_export_key(
                    string_format=identifier,
                    item_type = item_type,
                    item_id   = item_id,
                    item_name = item.name,
                    item_index = index if multiple_indexes else None,
                    extention = extention
                )
            export_results[formatted_identifier] = result
        return export_results
        
    @staticmethod
    def generate_export_key( string_format=None, **kwargs ):
        item_id = kwargs.get('item_id')
        item_index = kwargs.get('item_index')
        if ( not item_index is None ):
            item_id = str(item_id)+' ('+str(item_index)+')'
        if ( string_format == None ):
            string_format = '{item_type}-{item_id}{extention}'
        terms = {**kwargs, 'item_id':item_id}
        return utilities.strings.format( string_format, **terms )
    
    @staticmethod
    def export_as_json( conn: Connector, item_type:str, item_id:int ):
        maplink = Item.maplink_from( item_type )
        
        result = conn.request(
                url = '/items/'+maplink+'/'+str(item_id)
            ).get_response_body()
        return result
        
        
    @staticmethod
    def export_as_content( conn: Connector, item_type:str, item_id:int ):
        if ( not (item_type.lower() in ['indicator', 'panel']) ):
            raise Exception( 'Cannot export content from '+item_type )
            
        maplink = Item.maplink_from( item_type )
            
        property = {
                'indicator' : 'explanation',
                'panel' : 'text',
            }[item_type]
        
        return conn.request(
                url = '/items/'+maplink+'/'+str(item_id)+'/'+property
            ).get_response_body_json()
        
        
    @staticmethod
    def export_as_html( conn: Connector, item_type:str, item_id:int ):        
        if ( not (item_type in ['indicator', 'panel']) ):
            raise Exception( 'Cannot export html from '+item_type )
            
        url = conn.get_url_part_protocol()+conn.get_url_part_host()
        url += '/web/'+item_type.lower()+'.html'
        query_params = conn.get_url_part_query_params( '', {
                'id': str(item_id)
            })
        url+='?'+query_params
        return conn.request( url = url ).get_response_body()
        
        
    @staticmethod
    def export_as_body( conn: Connector, item_type:str, item_id:int ):
        if ( not (item_type in ['indicator', 'panel']) ):
            raise Exception( 'Cannot export body from '+item_type )
            
        url = conn.get_url_part_protocol()+conn.get_url_part_host()
        url += '/web/'+item_type.lower()+'.body'
        query_params = conn.get_url_part_query_params( '', {
                'id': str(item_id)
            })
        url+='?'+query_params
        return conn.request( url = url ).get_response_body()
        
        
    @staticmethod
    def export_as_excel( conn: Connector, item_type:str, item_id:int ):
        if ( not (item_type in ['indicator', 'panel']) ):
            raise Exception( 'Cannot export excel from '+item_type )
            
        return conn.request(
            method='POST',
            url='/events/editor'+item_type+'/debug_excel_file',
            data=[item_id]
        ).get_response_body()
        
    
    @staticmethod
    def export_overlay_as_png( conn: Connector, item_id:int = None, timeframes = -1, export_params:dict = {}  ):
        item = Items.get(
                conn=conn,
                item_type=Overlay, 
                item_id=item_id
            )
        timeframes = item.get_timeframes_range(timeframes)
 
        base_url = conn.get_url_part_protocol()+conn.get_url_part_host()
        base_url += '/web/'+Overlay.get_item_type().lower()+'.png'
 
        results = {}
        for  timeframe in timeframes:
            query_params = conn.get_url_part_query_params( '', {
                    'id': item_id,
                    'timeframe':timeframe
                })
            url= base_url+'?'+query_params
            results[timeframe] = conn.request( url = url ).get_response_body()

        return results
    
    
    @staticmethod
    def export_overlay( conn: Connector, item_id:int = None, timeframes = -1, format:str = 'geotiff', export_params:dict = {}  ):
        item = Items.get(
                conn=conn,
                item_type=Overlay, 
                item_id=item_id
            )
        timeframes = item.get_timeframes_range(timeframes)
        
        results = {}
        for  timeframe in timeframes:
            results[timeframe] =  conn.request(
                    url     = 'overlay.'+format,
                    query_params  = {'id':item_id, 'timeframe':timeframe, **export_params}
                ).get_response_body()
        return results