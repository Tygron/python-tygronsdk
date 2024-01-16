import tygronsdk
from tygronsdk import sdk as tygron
from tygronsdk import utilities as utilities
from tygronsdk import interfaces as interfaces
from tygronsdk.implementations import automations
from tygronsdk.implementations.automations.template_runner_input_generator import TemplateRunnerInputGenerator
from tygronsdk.implementations.automations.template_runner_orchestrator import TemplateRunnerOrchestrator






import os
from pathlib import Path

def main():

    try:
        credentials = tygronsdk.load_credentials_from_file( create_if_missing=True )
    except:
        print('Credentials must be provided, defining "username" and "password". Can either be a json object in "credentials.json", or key-value pairs in "credentials.txt".')
        return
    
    #   More data can be loaded in through configuration or data files. By default, the files sought are data.txt, data.json, config.txt, config.json
    data = tygronsdk.load_data_from_file()
    
    print( 'This example will demonstrate how the TemplateRunnerOrchestrator can be used to automatically perform repeated calculations.' )
    
    print( os.linesep, 'Preface' )
    print( 'This script will create a workspace with example files.' )
    print( 'When such a workspace already exists, the desired operations can also be manually run directly from the terminal: ' )
    print( '    python -m {module}'.format(module=utilities.modules.get_module_dot_notation_string( TemplateRunnerInputGenerator )) )
    print( '    python -m {module}'.format(module=utilities.modules.get_module_dot_notation_string( TemplateRunnerOrchestrator   )) )
    print( 'Each command can be provided an argument of settings. The argument can either be a json object, or a json file containing a json object.')
    
    
    
    print( os.linesep, 'Step 1 : Creation of workspace' )
    
    print( 'For the example, an example workspace will be created with a folder to store template data.')

    base_directory = 'tygron_example_outputs/automations_workspace/'
    utilities.files.delete_file( base_directory, also_directories=True )
    print( 'This base directory will be: '+base_directory)
    

    print( 'At this time, it is important to know about the directories this tooling uses:' )
    
    template_dir =  os.path.join(base_directory,    'template' )
    data_dir =      os.path.join(base_directory,    'data'     )
    input_dir =     os.path.join(base_directory,    'input'    )
    running_dir =   os.path.join(base_directory,    'running'  )
    output_dir =    os.path.join(base_directory,    'output'   )
    error_dir =     os.path.join(output_dir    ,    'error'    )
    
    print( '    Template: '+template_dir+' , which holds the templates for task files, out of the way from actual automations.' )
    print( '    Data    : '+data_dir+' , which holds additional data, such as geojsons for individual task files, so it can be accessed during runs but is otherwise out of the way from actual automations.' )
    print( '    Input   : '+input_dir+' , which hold the individual task files which have not yet run.' )
    print( '    Running : '+running_dir+' , which are associated with an active TemplateRunner and are being processed at that time.' )
    print( '    Output  : '+output_dir+', which holds both the completed tasks as well as (by default) the exported results and logs.' )
    print( '    Error   : '+error_dir+', which is a subdirectory of output and will hold the tasks and logs of any runs that encountered an error, and should be investigated and/or rerun.' )

    
    print( 'In the template folder 2 template files are required: A geojson file indicating locations, and a json file defining the template for all tasks' )
    current_dir = os.path.dirname(os.path.realpath(__file__))
    example_files_dir = os.path.join( current_dir, 'example_files' )
    
    utilities.files.copy_file( 'template_input.json'    , example_files_dir, template_dir, overwrite=True )
    utilities.files.copy_file( 'locations.geojson'      , example_files_dir, template_dir, overwrite=True )

    print( 'Note that each of these directories and files can be renamed through settings provided to the tooling, if neccesary.')   
    
    
    
    print( os.linesep, 'Step 2 : Input generator' )
    
    print( 'The template.json file serves as a template based on which to create multiple individual task files. The locations.geojson file defines the amount of task files, and the locations of the projects.' )
    print(' The TemplateRunnerInputGenerator will take the files as input, and generate the required output files.')
    
    input_generator = TemplateRunnerInputGenerator({
            'input_file' : 'template_input.json',
            'geojson_file' : 'locations.geojson',
            'base_directory' : base_directory
        }) # InputGenerator allows more settings, and can run without any settings as well.
    
    print('After setting the TemplateRunnerInputGenerator up, it can be run')
    input_generator.run(overwrite_data=data)
    
    for directory in [ template_dir, input_dir, data_dir ]:
        print( 'The following files now exist in {dir}: {list}'.format(
                dir=directory,
                list=( (os.linesep+' - ').join(['']+utilities.files.get_content_of_directory(directory)) )
            ))
    
    
    
    print( os.linesep, 'Step 3 : Orchestrator' )
    
    print( 'Each individual task file is intended to compatible with the TemplateRunner.' )
    print( 'The TemplateRunnerOrchestrator will manage creating TemplateRunners based on the task files at an appropriate rate.' )
    
    orchestrator = TemplateRunnerOrchestrator({
            'on_start_clean_output' : True,
            'domain_projects_limit_fraction' : 0.5,
            'base_directory' : base_directory,
            'default_credentials_file' : credentials.source
        }) # Orchestrator allows more settings, and can run without any settings as well.
    
    print('As an additional config when running as part of a program, explicitly set it to log its output by printing them to the terminal')
    orchestrator.set_logging_function(print)
    
    print('After setting the TemplateRunnerOrchestrator up, it can be run')
    
    orchestrator.run()

    print( 'After the orchestrator has completed all tasks, all logging from the orchestrator can be found on the terminal output.' )
    print( 'In addition, logs are also output to the output directory found at :'+input_dir )

    for directory in [ input_dir, output_dir, error_dir ]:
        print( 'The following files now exist in {dir}: {list}'.format(
                dir=directory,
                list=( (os.linesep+' - ').join(['']+utilities.files.get_content_of_directory(directory)) )
            ))
            
    print( 'This example has now fully run.')
            
main()