import tygronsdk
from tygronsdk import sdk as tygron
from tygronsdk import utilities as utilities
from tygronsdk import interfaces as interfaces








from pathlib import Path

def main():

    template_project_name = 'demo_heat_stress'
    print('This example will use the TemplateRunner automation to automatically create, calculate, save results of, close and discard a project based on the following template: "' + template_project_name + '".')

    #First, data should be loaded. This will include command-line arguments, a data file with settings/configurations, and a credentials file
    print('The "init_data" call will load arguments from the command line, data from a data.json or data.txt file, and credentials from a credentials.json or credentials.txt file.')
    data = tygronsdk.init_data( credentials_create_if_missing=True )
    print('Created a '+str(data))
    
    
    
    #   The core of the SDK is an SDK object. Settings can be provided to configure it.
    sdk = tygron.sdk( data, computer_name='Python SDK Example' );
        
    runner = interfaces.TemplateRunner()
    
    runner.set_sdk(sdk)
    
    #   Because the TemplateRunner is meant to be run as part of larger batches, logging is important.
    #   Depending on the encompassing application, a normal or a formatted logging function (or both) can be provided which the TemplateRunner will call.
    runner.set_formatted_logging_function( print )
    
    #   Whether to, as the process runs, a log entry should be included which includes the api token
    runner.set_log_api_token( True )
    
    
    #   The configuration of what template to run:
    runner.set_template_name( template_name = template_project_name )
    #   The configuration of where to apply the template anew
    runner.set_new_project_generation(
            size_x = 2000,
            size_y = 2000,
            location_x_epsg3857 = 480108.02047298977,
            location_y_epsg3857 = 6815252.010235827,
        )
    
    #   The configuration of recalculations. Depending on the Template used, multiple recalculations can be run. "True" also does reset-X-Queries.
    runner.set_recalculation_sequence( [True, False] )
    
    #   Additional configurations to tweak how the TenplateRunner deals with timing and errors.
    runner.set_new_project_generation_errors_allowed( True )
    runner.set_operation_timeout( 1200 )
    runner.set_use_keep_alive( True )
    
    #   After the runner completes, the output is available through get_exports. However, the runner can also write the results to files.
    runner.set_write_export_files( True )
    runner.set_export_location( './tygron_example_outputs' )
    
    #   Which data to export from the Project
    #       For each item type, an id, a name, or an Attribute, or a list of any combination of them, can be provided.
    #           Each match will result in an output.
    #           "True" means all items of that type will be exported
    #       A format or list of formats should be provided to indicate how to export the data.
    #           Allowed values include JSON (for any), HTML, BODY, CONTENT (for Indicators and Panels) and GEOTIFF, PNG (for Overlays)
    runner.set_export_indicators( 
            ids=True, 
            formats='HTML'
        )
    runner.set_export_panels( 
            ids=False,
            formats='HTML'
        )
    #   For Overlays, not a list but a dict should be provided.
    #       The key is an identifier for the Overlay (id, name, attribute).
    #       The value indicates which timeframes to export
    #           A single number is the timeframe index. -1 is the last one. -2 second-to-last, etc. A list of timeframes is allowed. True means all.
    runner.set_export_overlays(
            ids={ 
                    'HOURLY_TEMPERATURE' : True, 
                },
            formats=['PNG', 'GEOTIFF']    #Function which takes the item and the timeframe as input, and returns 
        )
    
    username = str(data.get_credentials_store().username)
    password = str(data.get_credentials_store().password)
    
    #   After all configurations are made, the runner can be started by using .run(), providing the credentials to authenticate
    runner.log( 'Starting the template runner with credentials for '+username )
    try:
        runner.run( data.get_credentials_store() )
    except Exception as err:
        print( 'An unexpected error occured while running the example' )
        print( utilities.exceptions.stringify(err) )
        
main()