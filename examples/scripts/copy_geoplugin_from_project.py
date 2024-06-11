import tygronsdk
from tygronsdk import sdk as tygron
from tygronsdk import items as items
from tygronsdk import utilities as utilities
from tygronsdk import interfaces as interfaces




class Script(interfaces.Script):

    def run( self, *args, **kwargs ):
        stored_err = None

        settings = {
            'origin_project_name' : 'tygron_dxf_template',
            'origin_session_id' : None,
            'origin_session_token' : None,
            'origin_geoplugin_name' : 'Basis NLCS interpretatie',
            
            'target_session_id' : None,
            'target_session_token' : None,
            'target_geoplugin_name' : None,
            
            'fill_custom_functions' : False,
            
            'platform' : 'engine',
            **kwargs
        }

        settings['origin_platform'] = settings.get('origin_platform',settings.get('platform'))
        settings['target_platform'] = settings.get('target_platform',settings.get('platform'))
            
        sdk = tygron.sdk( settings )
        auth_result = sdk.authenticate()['base']
        if ( not auth_result ):
            raise Exception('Credentials must be provided, defining "username" and "password". Can either be a json object in "credentials.json", or key-value pairs in "credentials.txt".')


        self.log('This script will copy a GeoPlugin from one Project to another running session.')


        sdk_origin = tygron.sdk( {
                'computer_name' : 'Python SDK Script - Copy Geoplugin from Project (Origin)',
                **settings,
                'platform' : settings['origin_platform']
            } )
        sdk_origin.configure_exit( {
                'save_project': False,
                'save_created_project': False,
                'close_session': True,
                'kill_session': False,
                'delete_created_project': False
            } )
            
            
        sdk_target = tygron.sdk( {
                'computer_name' : 'Python SDK Script - Copy Geoplugin from Project (Target)',
                **settings,
                'platform' : settings['target_platform']
            } )
        sdk_target.configure_exit( {
                'save_project': False,
                'save_created_project': False,
                'close_session': False,
                'kill_session': False,
                'delete_created_project': False
            } )

        self.log( 'Authenticating origin base API environment using '+str(sdk_origin.data) )
        self.log( 'Authenticating target base API environment using '+str(sdk_target.data) )
        auth_result = sdk_origin.authenticate()['base'] and sdk_target.authenticate()['base']
        if ( auth_result is False ):
            raise Exception('Could not authenticate origin, target, or both, with provided credentials')
        
        if ( (settings['target_session_token'] is None) ):
            sessions = sdk_target.base.sessions.get_joinable_sessions()
        if ( (settings['origin_session_token'] is None) ):
            projects = sdk_origin.base.projects.get_startable_projects()
        

        if ( not (settings['target_session_token'] is None) and len(str(settings['target_session_token']))>=8 ):
            settings['target_session_id'] = settings['target_session_token'][0:8]
        if ( settings['target_session_id'] is None or settings['target_session_id'] == '' ):
            self.log( 'Missing parameter. Add target_session_id=X as argument, where X is one of the following numerical ids:' )
            for session in sessions:
                self.log ( session )
            raise Exception('Missing parameter target_session_id')
        
        if ( not (settings['origin_session_token'] is None) and len(str(settings['origin_session_token']))>=8 ):
            settings['origin_session_id'] = settings['origin_session_token'][0:8]
        elif ( settings['origin_project_name'] is None or settings['origin_project_name'] == '' ):
            self.log( 'Missing parameter. Add origin_project_name=X as argument, where X is one of the following:' )
            for project in projects:
                self.log ( project )
            raise Exception('Missing parameter origin_project_name')
        
        if ( settings['origin_geoplugin_name'] is None or settings['origin_geoplugin_name'] == '' ):
            self.log( 'Missing parameter. Add origin_geoplugin_name=X as argument' )
            raise Exception('Missing parameter origin_geoplugin_name')
        elif ( settings['target_geoplugin_name'] is None ):
            settings['target_geoplugin_name'] = settings['origin_geoplugin_name']
        
        try:
            if ( settings['target_session_token'] is None ):
                target_session = 'session: '+str(next(session for session in sessions if str(session.id) == str(settings['target_session_id'])))
            else:
                target_session = 'session: '+str(settings['target_session_id']) + ' (identified by api token)'
        except StopIteration as err:
            raise Exception('Target session with id '+str( settings['target_session_id'] )+' not found')
        try:
            if ( settings['origin_session_token'] is None ):
                origin_project = 'project: '+str(next(project for project in projects if str(project.file_name) == settings['origin_project_name']))
            else:
                origin_project = 'session: '+str(settings['origin_session_id'])+' (identified by api token)'
        except StopIteration as err:
            raise Exception('Origin project name '+str( settings['origin_project_name'] )+' not found')
        
        
        
        self.log()
        self.log('Copying GeoPlugin ("'+str(settings['origin_geoplugin_name'])+'") from '+str(origin_project))
        self.log('Copying GeoPlugin (renamed to "'+str(settings['target_geoplugin_name'])+'") to '+str(target_session))
        self.log()
        
        
        
        try:
        
            if ( settings['origin_session_token'] is None ):
                if ( settings['origin_session_id'] is None ):
                    origin_session_id = sdk_origin.base.sessions.start_project_session(origin_project.file_name)
                else:
                    origin_session_id=settings['origin_session_id']
                origin_session_data = sdk_origin.base.sessions.join_project_session(origin_session_id)
            else:
                origin_session_data = { 'api_token' : settings['origin_session_token'] }
                sdk_origin.configure_exit( {
                'save_project': False,
                'save_created_project': False,
                'close_session': False,
                'kill_session': False,
                'delete_created_project': False
            } )
            
            auth_result = sdk_origin.session.authenticate(origin_session_data)
            if ( auth_result is False ):
                raise Exception('Could not authenticate to origin session')
                    
                    
                    
            sdk_origin.data = origin_session_data
            
            if ( settings['target_session_token'] is None ):
                target_session_data = sdk_target.base.sessions.join_project_session(settings['target_session_id'])
            else:
                target_session_data = { 'api_token': settings['target_session_token'] }
            auth_result = sdk_target.session.authenticate(target_session_data)
            if ( auth_result is False ):
                raise Exception('Could not authenticate to target session')
                
            self.log('Authenticated to both origin and target')
            
            
            
            origin_geoplugin = sdk_origin.session.items.get_matching(items.Geoplugin, settings['origin_geoplugin_name'])
            if ( not (origin_geoplugin.count() == 1) ):
                raise Exception('Unable to find desired GeoPlugin in origin')
            origin_geoplugin = next(item for item in origin_geoplugin)
            self.log(origin_geoplugin.get_data())
        
            #origin_geolinks = sdk_origin.session.items.get_matching('geolinks', origin_geoplugin.geo_link_ids)
            origin_geolinks = sdk_origin.session.items.get_matching(items.Geolink, origin_geoplugin.geolink_ids)
            for geolink in origin_geolinks:
                self.log(geolink.get_data())
        
            origin_geolink_names     =[link.name          for link in origin_geolinks]
            origin_geolink_functions =[link.function_id   for link in origin_geolinks]
            origin_geolink_geo_modes =[link.geo_mode      for link in origin_geolinks]
        
            response_plugin_id = sdk_target.session.connector.fire_event(
                    tygronsdk.events.editorgeoplugin.add(
                        type=origin_geoplugin.link_type 
                    )
                )
            target_plugin_id = response_plugin_id.get_response_body_json()
            self.log( 'New plugin id: ' + str(target_plugin_id) )
        
            sdk_target.session.connector.fire_event(
                    tygronsdk.events.editorgeoplugin.set_name(
                        geoplugin_id=target_plugin_id,
                        name=settings['target_geoplugin_name']                    
                    )
                )
            sdk_target.session.connector.fire_event(
                    tygronsdk.events.editorgeoplugin.set_new_project(
                        geoplugin_id=target_plugin_id,
                        new_project=origin_geoplugin.new_project                    
                    )
                )
                
                
                
                
            sdk_target.session.connector.fire_event(
                    tygronsdk.events.editorgeoplugin.add_new_links(
                        geoplugin_id=[target_plugin_id] * len(origin_geoplugin.geolink_ids),
                        name=['placeholder']            * len(origin_geoplugin.geolink_ids)
                    )
                )
                
            target_geoplugin = sdk_target.session.items.get_matching(items.Geoplugin, target_plugin_id)
            if ( not (target_geoplugin.count() == 1) ):
                raise Exception('Unable to find created GeoPlugin in target')
            target_geoplugin = next(item for item in target_geoplugin)
            target_geolink_ids = target_geoplugin.geolink_ids
            self.log( 'New link ids: ' + str(target_geolink_ids) )
        
        
        
            sdk_target.session.connector.fire_event(
                    tygronsdk.events.editorgeolink.set_name(
                        geolink_id=target_geolink_ids,
                        name=origin_geolink_names                   
                    )
                )
                
                
            sdk_target.session.connector.fire_event(
                    tygronsdk.events.editorgeolink.set_geometry_mode(
                        geolink_id      = target_geolink_ids,
                        geometry_mode   = [link.geo_mode for link in origin_geolinks]
                    )
                )
                
            attribute_ids=[]
            attribute_names=[]
            attribute_values=[]
            
            mapping_ids=[]
            mapping_names=[]
            mapping_values=[]
            
            filtered_geolink_ids_points=[]
            filtered_buffers_points=[]
            
            filtered_geolink_ids_lines=[]
            filtered_buffers_lines=[]
            
            filtered_geolink_ids_functions = []
            filtered_function_ids = []
            
            for index, link in enumerate(origin_geolinks):
                link_id = target_geolink_ids[index]
                  
                for attr_name, attr_val in link.attributes.items():
                    attribute_ids.append( link_id )
                    attribute_names.append( attr_name )
                    attribute_values.append( attr_val )
                  
                for attr_name, attr_val in link.mapping.items():
                    mapping_ids.append( link_id )
                    mapping_names.append( attr_name )
                    mapping_values.append( attr_val )
                    
                if ( not (link.point_buffer is None) ):
                    filtered_geolink_ids_points.append( link_id )
                    filtered_buffers_points.append( link.point_buffer )
                if ( not (link.line_buffer is None) ):
                    filtered_geolink_ids_lines.append( link_id )
                    filtered_buffers_lines.append( link.point_buffer )
                    
                if ( link.function_id == items.Item.NONE ):
                    continue
                if ( not(settings['fill_custom_functions'] or ( link.function_id < items.Item.CUSTOM_ID_START )) ):
                    continue
                filtered_geolink_ids_functions.append( link_id )
                filtered_function_ids.append( link.function_id )

            sdk_target.session.connector.fire_event(
                    tygronsdk.events.editorgeolink.set_line_buffer(
                        geolink_id      = filtered_geolink_ids_points,
                        buffer          = filtered_buffers_points
                    )
                )
            sdk_target.session.connector.fire_event(
                    tygronsdk.events.editorgeolink.set_point_buffer(
                        geolink_id      = filtered_geolink_ids_lines,
                        buffer          = filtered_buffers_lines
                    )
                )
              
            sdk_target.session.connector.fire_event(
                    tygronsdk.events.editorgeolink.set_attributes(
                        geolink_id      = attribute_ids,
                        attribute       = attribute_names,
                        attribute_value = attribute_values
                    )
                )
                
            sdk_target.session.connector.fire_event(
                    tygronsdk.events.editorgeolink.set_mapping(
                        geolink_id      = mapping_ids,
                        attribute       = mapping_names,
                        new_attribute   = mapping_values
                    )
                )
            
            sdk_target.session.connector.fire_event(
                    tygronsdk.events.editorgeolink.set_function(
                        geolink_id      = filtered_geolink_ids_functions,
                        function_id     = filtered_function_ids
                    )
                )
            
            target_geolinks = sdk_target.session.items.get_matching(items.Geolink, target_geoplugin.geolink_ids)
            for index, geolink in enumerate(target_geolinks):
                origin_link=origin_geolinks.get(origin_geoplugin.geolink_ids[index])
                target_link=geolink
                self.log('-----')
                self.log(origin_link.get_data())
                self.log(target_link.get_data())        
        
        
        
        except Exception as err:
            self.log('An error has occured')
            stored_err = err
                    
        finally:
            self.log('Closing connections')
            sdk_origin.exit()
            sdk_target.exit()
            self.log('Connections closed')
            
        if ( not (stored_err is None) ):
            raise stored_err
        

if __name__ == '__main__':
    Script().start()

