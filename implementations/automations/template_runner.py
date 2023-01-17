from ... import sdk as tygron
from ... import items as items

from ... import utilities as utilities

import json
from typing import List, Callable

class TemplateRunner:
    
    def __init__( self, settings: dict = {}, **kwargs ):
        self.default_run_export_key =  '{run_collection_name}-{run_name}-'
        self.default_data_export_key =  '{item_type}-{item_name}-{item_id}{extention}'
        
        self.settings = {
            'run_collection_name' : 'automated',
            'run_name' : utilities.strings.generate_random_token(10),
        
            'template_name' : None,
            'new_project_name' : utilities.strings.generate_random_token(10),
            'attempts' : None,
            'session_language' : None,
            'keep_alive' : False,
            
            'generate' : False,
            'location_x' : 480108.02047298977,
            'location_y' : 6815252.010235827,
            'size_x' : 1000,
            'size_y' : 1000,
            
            'area_geojsons' : [],
            'area_geojson_buffers' : [],
            'area_geojson_names' : [],
            
            'timeout_in_seconds' : None,
            'recalculate_reset_sequence' : [True],
            'recalculate_scheduled_sequence' : False,
            
            'exports' : { 
                'indicator' : {
                    'ids' : [],
                    'formats' : [],
                    'export_key' : None
                },
                'panel' : {
                    'ids' : [],
                    'formats' : [],
                    'export_key' : None
                },
                'overlay' : {
                    'ids' : {},
                    'formats' : [],
                    'export_key' : None
                },
            },
            'export_files' : False,
            'export_location': '',
            
            'log_api_token' : False,
            'keep_session_active' : False,
            'keep_project' : False,
        }
        
        self.settings = { **self.settings, **settings, **kwargs }
        
        self.short_logging_function = None
        self.long_logging_function = None
        self.exports = {}
        self.logs = []
 
    def set_sdk( self, sdk:tygron = None, **kwargs ):
        if ( sdk == None ):
            sdk = tygron.sdk( kwargs )
        self.sdk = sdk
    
    def set_run_name( self, run_name:str ):
        self.setting['run_name'] = run_name
    def set_run_collection_name( self, run_collection_name:str ):
        self.setting['run_collection_name'] = run_collection_name
        
    def get_run_name( self ):
        return self.setting['run_name']
    def get_run_collection_name( self ):
        return self.setting['run_collection_name']
    def get_full_run_name( self ):
        return '{collection}-{run}'.format(
                collection=self.settings['run_collection_name'],
                run=self.settings['run_name'],
            )
        
    def set_logging_functions( self, short_log_function:Callable = None, long_log_function:Callable = None ):
        self.short_logging_function = short_log_function
        self.long_logging_function = long_log_function
            
    def set_log_api_token( self, token_in_log:bool = True ):
        self.settings['log_api_token'] = token_in_log
    
    
    
    def check_sdk_ready( self, authentication:dict = {} ):
        if ( getattr(self, 'sdk', None ) == None ):
            self.set_sdk()
        self.sdk.base.authenticate(authentication)  

    def check_settings_ready( self ):
        if ( self.settings['template_name'] == None ):
            raise Exception('A template project must be provided')
    
        
        
    def set_template_name( self, template_name:str ):
        if ( not utilities.tygron_strings.is_allowed_project_name( template_name) ):
            raise Exception('The name of the template must be valid')
        self.settings['template_name'] = template_name
    def set_new_project_name( self, new_project_name:str ):
        if ( not utilities.tygron_strings.is_allowed_project_name( new_project_name) ):
            raise Exception('The name of a new project must be valid')
        self.settings['new_project_name'] = new_project_name
        
    def set_project_generation_attempts( self, attempts:int ):
        if ( attempts < 1 ):
            raise Exception('If an amount of project creation attempts is specified, it must be more than 0')
        self.settings['attempts'] = attempts
    def set_new_project_generation( self, size_x:int = None, size_y:int = None, location_x_epsg3857:float = None, location_y_epsg3857:float = None ):
        if ( size_x == None and size_y == None and location_x_epsg3857 == None and location_y_epsg3857 == None ):
            self.settings['generate'] = False
            return
        if ( size_x == None or size_y == None or location_x_epsg3857 == None or location_y_epsg3857 == None ):
            raise Exception('If a new project must be generated, both the size and the location of the new project must be provided.')
        self.settings['generate'] = True
        self.settings['size_x'] = size_x
        self.settings['size_y'] = size_x
        self.settings['location_x_epsg3857'] = location_x_epsg3857
        self.settings['location_y_epsg3857'] = location_y_epsg3857
    def set_new_project_generation_errors_allowed( self, allow_errors:bool = True ):
        self.settings['allow_errors'] = allow_errors
    
    
    
    def set_recalculation_sequence( self, recalculation_sequence:List[bool] = [] ):
        sequence = []
        for entry in recalculation_sequence:
            sequence.append( bool(entry) )
        self.settings['recalculate_reset_sequence'] = sequence
        
        
        
    def set_use_keep_alive( self, keep_alive:bool = False):
        self.settings['keep_alive'] = keep_alive
    def set_keep_resulting_project( self, keep:bool = True ):
        self.settings['keep_project'] = keep
    def set_keep_session_active( self, keep:bool = True ):
        self.settings['keep_session_active'] = keep
    def set_operation_timeout( self, timeout_in_seconds:int ):
        if ( timeout_in_seconds <=0 ):
            raise Exception('Timeout in seconds must be greater than 0')
        self.settings['timeout_in_seconds'] = timeout_in_seconds
    
    
    
    
    def set_export_indicators( self, ids = [], formats = [], export_key:str = None ):
        self.settings['exports']['indicator']['ids'] = ids
        self.settings['exports']['indicator']['formats'] = utilities.lists.coerce(formats)
        if ( not export_key is None ):
            self.settings['exports']['indicator']['export_key'] = export_key
    def set_export_panels( self, ids = [], formats = [], export_key:str = None ):
        self.settings['exports']['panel']['ids'] = ids
        self.settings['exports']['panel']['formats'] = utilities.lists.coerce(formats)
        if ( not export_key is None ):
            self.settings['exports']['panel']['export_key'] = export_key
    def set_export_overlays( self, ids = {}, formats = [], export_key:str = None ):
        self.settings['exports']['overlay']['ids'] = ids
        self.settings['exports']['overlay']['formats'] = utilities.lists.coerce(formats)
        if ( not export_key is None ):
            self.settings['exports']['overlay']['export_key'] = export_key



    def set_write_export_files( self, export:bool = True ):
        self.settings['export_files'] = export
    def set_export_location( self, directory:str = '' ):
        self.settings['export_location'] = directory

    
            
    def add_importable_areas_geojson( self, areas_geojson, areas_buffer:float = None, areas_name_attribute:str = None ):
        areas_geojson_string = None
        if ( isinstance(areas_geojson, dict) ):
            areas_geojson_string = json.dumps(areas_geojson)
        elif ( isinstance(areas_geojson, str) ):
            areas_geojson_string = areas_geojson
        else:
            raise Exception('Areas geojson must be a valid json string, or an appropriate dict')
        
        try:
            json.loads(areas_geojson_string)
        except:
            raise Exception('Areas geojson must be a valid json string')
            
        if ( not (areas_buffer == None) and (areas_buffer <= 0) ):
            raise Exception('When provided, a buffer for geojson areas must be greater than 0')
                
        self.settings['area_geojsons'].append( areas_geojson_string )
        self.settings['area_geojson_buffers'].append( areas_buffer )
        self.settings['area_geojson_names'].append( areas_name_attribute )



    def run( self, authentication:dict = {} ):
    
        self.check_sdk_ready( authentication )
        self.check_settings_ready( )
        self.log( 'Template runner is ready. Starting process.' )
    
        exceptions = []
        
        try:
            self._create_and_join()
            self._keep_alive()
            self._generate()
            self._add_data()
            self._recalculate()
            self._export()
        except Exception as err:
            self.log( 'An unexpected exception has occured, so stopping the process.')
            exceptions.append(err)
            
        try:
            self._cleanup()
        except Exception as err:
            self.log( 'An unexpected exception occured while stopping the sdk.' )
            exceptions.append(err)
            
        try:
            self._write_export_files()
        except Exception as err:
            self.log( 'An unexpected exception occured while exporting files.' )
            exceptions.append(err)
        
        
        if ( len(exceptions) > 0 ):
            raise Exception( 'One or more exceptions occured while running the Template Runner', *exceptions)

        self.log('Template runner process succesfully completed')
    
    def get_exports( self ):
        return self.exports
    
    
    
    def log( self, message = None ):
    
        if ( isinstance(message, Exception) ):
            message = tygron_utilities.exceptions.stringify(message)
        else:
            message = str(message)
    
        self.logs.append(message)
    
        if ( isinstance(self.short_logging_function, Callable) ):
            self.short_logging_function( message )
        if ( isinstance(self.long_logging_function, Callable) ):
            self.long_logging_function( self.get_full_run_name() + ': ' + message )
            
    def get_logs( self ):
        return self.logs
        
        
        
        
        
        
        
    def _create_and_join( self ):
        sdk = self.sdk
        
        self.log( 'Starting template and creating a new project with it.' )
        creation_response = sdk.base.sessions.create_new_project_from_template( **self.settings )
        
        self.log( 'Created a new project named: ' +str(creation_response['project']) )
        self.log( 'Session is running with session id: '+str(creation_response['session_id']) )
        
        sdk.settings = creation_response
        
        sdk.session.authenticate( creation_response )
        self.log( 'Authenticated with the session succesfully.')
        
        if ( self.settings['log_api_token'] ):
            self.log( 'Connected to session at: ' + sdk.session.connector.get_url_full() )
        
            
    def _keep_alive( self ):
        sdk = self.sdk
        
        if ( not self.settings['keep_alive'] ):
            return
            
        sdk.base.sessions.set_session_keep_alive( **self.settings )
        self.log( 'Running session in Keep Alive mode.')
            
    def _generate( self ):
        sdk = self.sdk
        
        if ( not self.settings['generate'] ):
            self.log( 'Skipped generation of new project area.' )
            return
            
        self.log( 'Initiating the map generation process.' )
        result = sdk.session.creation.generate_map( **self.settings )
        
        if ( result == 0 ):
            self.log( 'Map generated succesfully and without errors.' )
        else:
            self.log( 'Map generated with this many errors: ' + str(result) )
            
            
    def _add_data( self ):
        sdk = self.sdk
        
        self.log( 'Adding additional Areas from provided geojsons.' )
        result = sdk.session.data_import.geojsons_areas( **self.settings )
        self.log( 'Geojson Areas import completed, adding this many areas: ' + str(result) )
            
            
    def _recalculate( self ):
        sdk = self.sdk

        self.log( 'Starting recalculation cycles. This may take a while.' )
        
        for index, reset in enumerate(self.settings['recalculate_reset_sequence']):
            scheduled = utilities.lists.get( self.settings['recalculate_scheduled_sequence'], index, False )
            
            self.log( 'Recalculation '+str(index+1)+' starting'+(' (reset)' if reset else '')+(' (scheduled)' if scheduled else '') )
            result = sdk.session.calculation.recalculate( 
                    reset = reset, 
                    scheduled = scheduled, 
                    timeout_in_seconds = self.settings['timeout_in_seconds']
                )
            
        self.log( 'Completed cycle of recalculations.' )
         
    
    def _partially_format_data_export_key( self, export_key:str = None ):
        if ( export_key is None ):
            export_key = self.default_data_export_key
            
        run_key = self.default_run_export_key.format(
            run_collection_name = self.settings['run_collection_name'],
            run_name = self.settings['run_name']
        )
        
        return run_key + export_key
    
    def _export( self ):
        sdk = self.sdk
        self.log( 'Starting export of data' )

        results = {}

        for item_type, export_config in self.settings['exports'].items():
            ids = export_config['ids']
            if ( isinstance(ids, dict) ):
                ids = list(ids.keys())
            
            item_results = {}
            
            if ( item_type == 'overlay' ):
                item_results.update( self._export_overlays(
                        item_ids = ids,
                        timeframes = export_config['ids'],
                        export_formats = export_config['formats'],
                        export_key = export_config['export_key']
                    ) )
            else:
                item_results.update( self._export_items(
                        item_ids = ids,
                        item_type = item_type,
                        export_formats = export_config['formats'],
                        export_key = export_config['export_key']
                    ) )
            results[item_type] = item_results
            
        self.exports = results
        return self.exports
            
    def _export_overlays( self, item_ids:list = [], timeframes:dict = {}, export_formats = [], export_key:str = None ):
        sdk = self.sdk
        export_key = self._partially_format_data_export_key( export_key )
        
        all_item_results = {}
        all_matched_items = sdk.session.items.get_matching( item_type=items.Overlay, matchables=item_ids )
        self.log( 'Exporting '+str(all_matched_items.count())+' of item type '+'overlay' )
        
        for overlay_id in item_ids:
            for overlay in sdk.session.items.get_matching( item_type=items.Overlay, matchables=overlay_id ):
                for export_format in export_formats:
                    try:
                        single_item_results = sdk.session.data_export.export(
                                item_type =     items.Overlay,
                                item_id =       overlay.id,
                                export_type =   export_format,
                                indexes =       timeframes[overlay_id],
                                identifier =    export_key
                            )
                        all_item_results.update(single_item_results)
                    except Exception as err:
                        try:
                            used_url = err.args[0].get_response_url()
                            self.log( 'Could not obtain data from url: '+used_url )
                            self.log( str(err.args[0]) )
                        except Exception as response_err:
                            pass
                        raise err
        return all_item_results
        
    def _export_items(  self, item_ids, item_type, export_formats = [], export_key:str = None ):
        sdk = self.sdk
        export_key = self._partially_format_data_export_key( export_key )
        
        all_item_results = {}
        all_matched_items = sdk.session.items.get_matching( item_type=item_type, matchables=item_ids )
        self.log( 'Exporting '+str(all_matched_items.count())+' of item type '+item_type )
        
        for item in all_matched_items:
            for export_format in export_formats:
                try:
                    single_item_results = sdk.session.data_export.export(
                            item_type =     item_type,
                            item_id =       item.id,
                            export_type =   export_format,
                            identifier =    export_key
                        )
                    all_item_results.update(single_item_results)
                except Exception as err:
                    try:
                        used_url = err.args[0].get_response_url()
                        self.log( 'Could not obtain data from url: '+used_url )
                        self.log( str(err.args[0]) )
                    except Exception as response_err:
                        pass
                    raise err
        
        return all_item_results
    
    def _write_export_files( self ):
        if ( not self.settings['export_files']):
            return
            
        location = self.settings['export_location']
        if ( location is None ):
            location = ''
        
        if (len(self.exports.items()) == 0):
            self.log( 'No exports available, so not writing any files' )
            return
        
        self.log( 'Writing files to location: '+location )
        
        for item_type, results in self.exports.items():
            self.log( 'Writing '+str(len(results))+' file(s) of '+item_type+' results' )
            for name, result in results.items():
                utilities.files.write_file(
                        directory=location, 
                        file=name, 
                        content=result, 
                        append=True
                    )
        self.log( 'Files written' )
    
    def _cleanup( self ):
        sdk = self.sdk
        
        sdk.exit( {
                'save_project': False,
                'save_created_project': self.settings['keep_project'],
                'close_session': (not self.settings['keep_session_active']),
                'kill_session': (not self.settings['keep_session_active']),
                'delete_created_project': (not self.settings['keep_project'])
            } )
        self.log('Template runner\'s sdk has shut down succesfully')
    
    
    
    
    
    
        