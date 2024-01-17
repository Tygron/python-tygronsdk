import tygronsdk
from tygronsdk import sdk as tygron
from tygronsdk import utilities as utilities

from ..code_generators.event_set_generator import EventSetGenerator

import os

class Script():

    def run( self, *args, **kwargs ):

        settings = {
            'platform' : 'engine',
            'computer_name' : 'dev script',
            
            'credentials' : ['credentials.json'],
            'minimal_rights' : 'DOMAIN_ADMIN',
            'assume_unchanged_parameters' : True,
            'existing_types_only' : True,
            
            'output_directory' : 'dev_output',
            **kwargs
        }

        output_dir = os.path.join( settings['output_directory'], *['src','environments','{env}','data','events'] )
        tygronsdk.utilities.files.write_file( settings['output_directory'], '.gitignore', '/*' )

        credentials = tygronsdk.load_credentials_from_file( files=
                utilities.lists.coerce(settings['credentials'])+[
                        './credentials.txt',
                        './credentials.json'
                    ],
            create_if_missing=False )
        sdk = tygron.sdk( settings )

        sdk.base.authenticate(credentials)

        if ( not (sdk.base.users.get_my_user().rights) == settings['minimal_rights'] ):
            raise Exception(' User ' + str(sdk.base.users.get_my_user()) + ' has insufficient rights. Use "credentials=" to overwrite used credentials file.' )


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
        gen.environment_events = tygronsdk.src.environments.base.data.events
        gen.connector = sdk.base.connector
        generators.append(gen)


        gen = EventSetGenerator()
        gen.gen_name = 'event generator for session environment'
        gen.assume_unchanged_parameters = settings['assume_unchanged_parameters']
        gen.output_directory = output_dir.format( env='session' )
        gen.environment_events = tygronsdk.src.environments.session.data.events
        gen.connector = sdk.session.connector
        generators.append(gen)

        """
        gen = EventSetGenerator()
        gen.gen_name = 'event generator for share environment'
        gen.assume_unchanged_parameters = settings['assume_unchanged_parameters']
        gen.output_directory = output_dir.format( env='share' )
        gen.environment_events = tygronsdk.src.environments.share.data.events
        gen.connector = sdk.share.connector
        generators.append(gen)
        """


        generated_files = []

        try:
            print('Settings: ')
            print('platform: ' +                    str(settings['platform']) )
            print('assume_unchanged_parameters: ' + str(settings['assume_unchanged_parameters']) )
            print('existing_types_only: '+          str(settings['existing_types_only']) )
            print('minimal_rights: ' +              str(settings['minimal_rights']) )

            for gen in generators:
                print( '-----' )
                print( 'Starting '+gen.gen_name )
                api_event_sets = gen.get_api_event_sets()
                print( 'Obtained ' + str(len(api_event_sets.keys())) + ' event sets from API' )
                sdk_event_sets = gen.get_sdk_event_sets()
                print( 'Obtained ' + str(len(sdk_event_sets.keys())) + ' event sets from SDK' )
                merged_event_sets = gen.get_merged_event_sets(sdk_event_sets, api_event_sets)
                print( 'Obtained ' + str(len(merged_event_sets.keys())) + ' merged sets' )
                
                if ( settings['existing_types_only'] ):
                    merged_event_sets = {key: merged_event_sets[key] for key in list(sdk_event_sets.keys())}
                    print('Filtered to ' + str(len(merged_event_sets.keys())) + ' merged sets' )
                
                result = gen.write_event_set_files(merged_event_sets)
                generated_files.extend( result )
                
                print( 'Written merged event sets to '+str(gen.output_directory) )
                print( 'Finished '+gen.gen_name )
                print( '-----' )
        except Exception as err:
            print( utilities.exceptions.stringify(err) )
            pass
        sdk.exit()
        
        return generated_files


if __name__ == '__main__':
    Script().run( **utilities.system.get_args() )
