import tygronsdk
from tygronsdk import sdk as tygron
from tygronsdk import utilities as utilities
from tygronsdk import interfaces as interfaces

from ..code_generators.event_set_generator import EventSetGenerator

import os

class Script(interfaces.Script):

    def run( self, *args, **kwargs ):

        settings = {
            'platform' : 'engine',
            'computer_name' : 'dev script',
            
            'credentials' : ['credentials.json'],
            'minimal_rights' : 'DOMAIN_ADMIN',
            'assume_unchanged_parameters' : False,
            'existing_types_only' : True,
            
            'output_directory' : 'dev_output',
            'platform_postfix' : None,
            **kwargs
        }
            
            
        sdk = tygron.sdk( settings )
        sdk.authenticate()



        if ( not (sdk.base.users.get_my_user().rights) == settings['minimal_rights'] ):    
             raise Exception(' User ' + str(sdk.base.users.get_my_user()) + ' has insufficient rights. Use "credentials=" to overwrite used credentials file.' )



        events_module = 'events'
        if ( settings['platform_postfix'] is None ):
            events_module = sdk.platform_module_name(settings['platform'], events_module)
        elif ( settings['platform_postfix'] == ''):
            events_module = events_module
        else:
            events_module = events_module+'_'+str(settings['platform_postfix'])
            
        output_dir = os.path.join( settings['output_directory'], *['src','environments','{env}','data' ], events_module )
        tygronsdk.utilities.files.write_file( settings['output_directory'], '.gitignore', '/*' )
        
        
        
        session_id = sdk.base.sessions.start_project_session( 'demo_heat_stress' )
        join_session_data = sdk.base.sessions.join_project_session( session_id )

        auth_result = sdk.session.authenticate( {
                'api_token' :join_session_data['apiToken'],
            } )
        sdk.on_exit_settings = {
                    'close_session' : True,
                }



        generators = []
        gen = EventSetGenerator()
        gen.gen_name = 'event generator for base environment'
        gen.assume_unchanged_parameters = settings['assume_unchanged_parameters']
        gen.output_directory = output_dir.format( env='base' )
        gen.environment_events = getattr(tygronsdk.src.environments.base.data, events_module, None)
        gen.connector = sdk.base.connector
        generators.append(gen)


        gen = EventSetGenerator()
        gen.gen_name = 'event generator for session environment'
        gen.assume_unchanged_parameters = settings['assume_unchanged_parameters']
        gen.output_directory = output_dir.format( env='session' )
        gen.environment_events = getattr(tygronsdk.src.environments.session.data, events_module, None)
        gen.connector = sdk.session.connector
        generators.append(gen)

        """
        gen = EventSetGenerator()
        gen.gen_name = 'event generator for share environment'
        gen.assume_unchanged_parameters = settings['assume_unchanged_parameters']
        gen.output_directory = output_dir.format( env='share' )
        gen.environment_events = tygronsdk.src.environments.share.data.events
        gen.environment_events = getattr(tygronsdk.src.environments.share.data, events_module, None)
        gen.connector = sdk.share.connector
        generators.append(gen)
        """


        generated_files = []

        try:
            self.log('Settings: ')
            self.log('platform: ' +                    str(settings['platform']) )
            self.log('events_module: ' +               str(events_module) )
            self.log('assume_unchanged_parameters: ' + str(settings['assume_unchanged_parameters']) )
            self.log('existing_types_only: '+          str(settings['existing_types_only']) )
            self.log('minimal_rights: ' +              str(settings['minimal_rights']) )

            for gen in generators:
                api_event_sets = {}
                sdk_event_sets = {}
                merged_event_sets = {}
            
                self.log( '-----' )
                self.log( 'Starting '+gen.gen_name )
                
                try:
                    api_event_sets = gen.get_api_event_sets()
                    self.log( 'Obtained ' + str(len(api_event_sets.keys())) + ' event sets from API' )
                except:
                    self.log ('No event sets obtained from API. Continuing without.')
                    
                try:
                    sdk_event_sets = gen.get_sdk_event_sets()
                    self.log( 'Obtained ' + str(len(sdk_event_sets.keys())) + ' event sets from SDK' )
                except:
                    self.log ('No event sets obtained from SDK. Continuing without.')
                  
                try:  
                    merged_event_sets = gen.get_merged_event_sets(sdk_event_sets, api_event_sets)
                    self.log( 'Obtained ' + str(len(merged_event_sets.keys())) + ' merged sets' )
                except:
                    self.log ('No event sets merged. Continuing without.')
                
                if ( settings['existing_types_only'] ):
                    merged_event_sets = {key: merged_event_sets[key] for key in list(sdk_event_sets.keys())}
                    self.log('Filtered to ' + str(len(merged_event_sets.keys())) + ' merged sets' )
                
                result = gen.write_event_set_files(merged_event_sets)
                generated_files.extend( result )
                
                self.log( 'Written merged event sets to '+str(gen.output_directory) )
                self.log( 'Finished '+gen.gen_name )
                self.log( '-----' )
        except Exception as err:
            self.log( utilities.exceptions.stringify(err) )
            pass
        sdk.exit()
        
        return generated_files


if __name__ == '__main__':
    Script().start()
