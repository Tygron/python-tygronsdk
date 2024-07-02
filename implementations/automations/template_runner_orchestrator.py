import tygronsdk
from tygronsdk import sdk as tygron
from tygronsdk import utilities
from tygronsdk import interfaces


import os, sys, json
import importlib, inspect

from pathlib import Path
from typing import Callable

class TemplateRunnerOrchestrator:

    def __init__( self, settings: dict = {}, **kwargs ):
    
        self.settings = {
                'task_file' : None, 
                
                'base_directory' : 'automations',
        
                'input_directory' : 'input',
                'output_directory' : 'output',
                'error_directory' : 'error',
                'running_directory' : 'running',
                'data_directory' : 'data',
                'credentials_directory' : 'credentials',
                
                'default_credentials_file' : ['credentials.json','credentials.txt'],
                
                
                'parallel_tasks' : 2,
                'domain_projects_limit' : 80,
                'domain_projects_limit_fraction' : 0.75,
                'license_allowance_retry_time_in_seconds' : 3600,
                
                
                'single_task' : False,
                'on_start_clean_running_tasks' : True,
                'on_start_reset_completed_tasks' : False,
                'on_start_clean_output' : False,
                'on_done_stop_orchestration' : True,
                
                'path_to_orchestrator' : None,
                'debug_on_completion_reset_output_tasks' : False
            }
        
        self.logging_function = None
        
        self.logs = []
        
        self.paused = False
        
        self.settings = { **self.settings, **settings, **kwargs }
        
    def set_logging_function( self, logging_function:Callable = None ):
        self.logging_function = logging_function
    
    def get_input_dir_or_file( self, file:str = '' ):
        return os.path.join(
                self.settings['base_directory'], self.settings['input_directory'], file
            )
    def get_running_dir_or_file( self, file:str = '' ):
        return os.path.join(
                self.settings['base_directory'], self.settings['running_directory'], file
            )
    def get_output_dir_or_file( self, file:str = '' ):
        return os.path.join(
                self.settings['base_directory'], self.settings['output_directory'], file
            )
    def get_error_dir_or_file( self, file:str = '' ):
        return os.path.join(
                self.settings['base_directory'], self.settings['output_directory'], self.settings['error_directory'], file
            )
    def get_data_dir_or_file( self, file:str = '' ):
        return os.path.join(
                self.settings['base_directory'], self.settings['data_directory'], file
            )
    def get_credentials_dir_or_file( self, file:str = '' ):
        return os.path.join(
                self.settings['base_directory'], self.settings['credentials_directory'], file
            )
    
    
    def get_files( self, directory:str, tasks_only:bool = False ):
        regex = None if not tasks_only else '.json$'
        return utilities.files.get_content_of_directory( directory=directory, regex=regex )
    
    def get_input_files( self, tasks_only:bool = True ):
        return self.get_files( self.get_input_dir_or_file(), tasks_only )
    def get_running_files( self, tasks_only:bool = True ):
        return self.get_files( self.get_running_dir_or_file(), tasks_only )
    def get_output_files( self, tasks_only:bool = True ):
        return self.get_files( self.get_output_dir_or_file(), tasks_only )
    def get_error_files( self, tasks_only:bool = True ):
        return self.get_files( self.get_error_dir_or_file(), tasks_only )
        
        
    def get_credentials( self, credentials_file:str = None ):
        if ( credentials_file is None ):
            target_file = self.settings['default_credentials_file']
        else:
            target_file = self.get_credentials_dir_or_file(credentials_file)
        
        credentials = tygronsdk.init.load_credentials_from_file( files=target_file, require=True )
        
        if ( not getattr(credentials, 'username', False) and getattr(credentials, 'password', False) ):
            raise Exception( 'Credentials file must define both a "username" and a "password"' )
        return credentials
    
    
    def move_task_file( self, task_file:str, task_from:str, task_to:str ):
        utilities.files.move_file(
                file=task_file,
                source_location=task_from,
                target_location=task_to
            )
    def move_task_file_input_running( self, task_file:str ):
        self.move_task_file( task_file=task_file,
                task_from=self.get_input_dir_or_file(),
                task_to=self.get_running_dir_or_file()
            )
    def move_task_file_running_output( self, task_file:str ):
        self.move_task_file( task_file=task_file,
                task_from=self.get_running_dir_or_file(),
                task_to=self.get_output_dir_or_file()
            )
    def move_task_file_running_error( self, task_file:str ):
        self.move_task_file( task_file=task_file,
                task_from=self.get_running_dir_or_file(),
                task_to=self.get_error_dir_or_file()
            )
    def move_task_file_running_input( self, task_file:str ):
        self.move_task_file( task_file=task_file,
                task_from=self.get_running_dir_or_file(),
                task_to=self.get_input_dir_or_file()
            )
    def move_task_file_output_input( self, task_file:str ):
        self.move_task_file( task_file=task_file,
                task_from=self.get_output_dir_or_file(),
                task_to=self.get_input_dir_or_file()
            )
    def move_task_file_error_input( self, task_file:str ):
        self.move_task_file( task_file=task_file,
                task_from=self.get_error_dir_or_file(),
                task_to=self.get_input_dir_or_file()
            )
    
    
    def get_module_path_to_orchestrator( self ):
        if ( not (self.settings['path_to_orchestrator'] is None) ):
            return self.settings['path_to_orchestrator']
        
        if __name__ == '__main__':
            from .template_runner_orchestrator import TemplateRunnerOrchestrator as self_module
            return inspect.getmodule(self_module).__name__
        return __name__
    
    
    
    def run( self ):
        if ( not self.settings['task_file'] is None ):
            try:
                self.run_task( )
            except Exception as err:
                self.log_orchestrator( 'An error occured while running task file '+self.settings['task_file'] )
                self.log_orchestrator( utilities.exceptions.stringify(err) )

        else:
            try:
                self.run_orchestration( )
            except Exception as err:
                self.log_orchestrator( 'An error occured while orchestrating' )
                self.log_orchestrator( utilities.exceptions.stringify(err) )
            finally:
                self.output_log_of_orchestrator()

            
    
    def run_orchestration( self ):
        self.start_orchestration()
        
        loop = not bool(self.settings['single_task'])
        while( True ):
            next_task = self.get_next_task_available()
            if ( next_task and self.additional_parallel_task_allowed() ):
                self.paused = False
                self.run_task_in_separate_process(next_task)
        
            if ( self.should_break_orchestration_loop() ):
                loop = False
            elif ( next_task is None and not self.paused ):
                self.paused = True
                self.log_orchestrator( 'Orchestrator has no further tasks to run, but will accept new tasks while running tasks complete' )
                if (self.settings['on_done_stop_orchestration']):
                    self.log_orchestrator( 'When all tasks complete and no new tasks are added, the orchestrator will finish and stop' )
            if (not loop):
                break

            utilities.timing.wait_for( timeout_in_seconds=5 )                
                
        self.log_orchestrator( 'Orchestrator has completed its orchestration' )
            
    
    def start_orchestration( self ):
        self.log_orchestrator( 'Starting orchestrator' )
        
        self.log_configuration()
    
        utilities.files.ensure_directory( self.get_input_dir_or_file() )
        utilities.files.ensure_directory( self.get_running_dir_or_file() )
        utilities.files.ensure_directory( self.get_output_dir_or_file() )
        utilities.files.ensure_directory( self.get_data_dir_or_file() )
        utilities.files.ensure_directory( self.get_credentials_dir_or_file() )
    
        if ( self.settings['single_task'] ):
            return
        
        if ( self.settings['on_start_clean_running_tasks'] ):
            self.clean_running_tasks()
            
        if ( self.settings['on_start_reset_completed_tasks'] ):
            self.reset_completed_tasks()
        
        if ( self.settings['on_start_clean_output'] ):
            self.clean_output()
    
    def log_configuration( self ):
        configuration_for_log = [
                '',
                '',
                '---- Orchestrator configuration ----',
                '',
                'Directories:',
                'Data: '+self.get_data_dir_or_file(),
                'Input: '+self.get_input_dir_or_file(),
                'Running: '+self.get_running_dir_or_file(),
                'Output: '+self.get_output_dir_or_file(),
                'Credentials: '+self.get_credentials_dir_or_file(),
                '',
                'On start:',
                'Clean running tasks to input: '+str(self.settings['on_start_clean_running_tasks']),
                'Reset completed tasks to input: '+str(self.settings['on_start_reset_completed_tasks']),
                'Delete contents of output directory: '+str(self.settings['on_start_clean_output']),
                '',
                'Running tasks:',
                'Amount of tasks in parallel: '+str(self.settings['parallel_tasks']),
                'Maximum allowed amount of new projects. Runs are paused if exceeded: '+str(self.settings['domain_projects_limit']),
                'Maximum allowed percentage of new projects. Runs are paused if exceeded: '+str(self.settings['domain_projects_limit_fraction']),
                'Paused runs are paused for this many seconds: '+str(self.settings['license_allowance_retry_time_in_seconds']),
                '',
                'On finish:',
                'Stop orchestration when input and running directories are empty: '+str(self.settings['on_done_stop_orchestration']),
            ]
        
        configuration_for_log.extend(['','---- ----',''])
        self.log_orchestrator( '\r\n'.join(configuration_for_log) )
    
    def clean_running_tasks( self ):
        running_tasks = self.get_running_files()
        if (len(running_tasks)==0 ):
            return
            
        self.log_orchestrator( 'Cleaning '+str(len(running_tasks))+' task(s) which were still running, moving them back to input: ' + ', '.join(running_tasks) )

        for task in running_tasks :
            self.move_task_file_running_input(task)
    
    def reset_completed_tasks( self ):
        completed_tasks = self.get_output_files()
        errored_tasks = self.get_error_files()
        total_amount_of_tasks = (len(completed_tasks) + len(errored_tasks))
        if ( total_amount_of_tasks == 0):
            return
            
        completed=str(len(completed_tasks))
        errored=str(len(errored_tasks))
        totalled=str(total_amount_of_tasks)
        self.log_orchestrator( 'Resetting '+totalled+' task(s) which were already completed ('+completed+' successful, '+errored+' with error'+')' )
        
        for task in completed_tasks:
            self.move_task_file_output_input(task)
        for task in errored_tasks:
            self.move_task_file_error_input(task)
    
    def clean_output( self ):
        output_files = self.get_output_files( tasks_only = False )
        
        if ( len(output_files) == 0 ):
            return
            
        self.log_orchestrator( 'Cleaning '+str(len(output_files))+' file(s) and folder(s) from the output location' )
        
        for output_file in output_files:
            file = self.get_output_dir_or_file(output_file)
            utilities.files.delete_file(file=file, also_directories=True )
        
        
    
    def get_next_task_available( self ):
        tasks = self.get_input_files( tasks_only=True )
        return None if len(tasks)==0 else tasks[0]
        
    def additional_parallel_task_allowed( self ):
        return len(self.get_running_files( tasks_only=True )) < self.settings['parallel_tasks']
        
    def should_break_orchestration_loop( self ):
        if ( len(self.get_running_files( tasks_only=True )) > 0 ):
            return False
        if ( len(self.get_input_files( tasks_only=True )) > 0 ):
            return False
        return self.settings['on_done_stop_orchestration']
    
    
    
    
    
    def run_task_in_separate_process( self, task_file ):
        self.log_orchestrator( 'Starting a new task in a seperate process for file: '+task_file )
        task_settings = {**self.settings}
        task_settings['task_file'] = task_file
        task_settings['path_to_orchestrator'] = self.get_module_path_to_orchestrator()
        
        module_path = task_settings['path_to_orchestrator']
        cmd = ' '.join( [ os.path.basename(sys.executable),' -m ', module_path, json.dumps(json.dumps(task_settings)) ] )
        process = utilities.processes.run_subprocess( cmd, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True )
        pass
    
    def run_task( self ):
        runner = interfaces.TemplateRunner()
        runner.set_formatted_logging_function( self.log_runner, '{log_run_name} : {message}' )
        
        critical_error = None
        
        task_in_input = True
        credentials = None
        
        try:
            task_file = self.get_input_dir_or_file( self.settings['task_file'] )
            task_parameters = utilities.files.read_file_as_json( task_file )
            runner.set_settings( task_parameters )
            self.log_orchestrator( 'Read out task file and configured runner with settings.' )
            
            geojson_definitions_count = self.add_geojson_definitions_to_runner( runner, task_parameters.get('geojson_files', None) )
            self.log_orchestrator( 'Orchestrator read out task file and configured runner with settings' )
            
            self.move_task_file_input_running( self.settings['task_file'] )
            self.log_orchestrator( 'Moved task file into running directory.' )
            task_in_input = False
            
        except Exception as err:
            self.log_orchestrator( 'Encountered an error while interpreting task file data' )
            critical_error = err
            
        
        if ( not critical_error ):
            try:
                credentials = self.get_credentials( task_parameters.get('credentials_file', None) )
                self.log_orchestrator( 'Read out credentials file from '+str(credentials.source) )
            except Exception as err:
                self.log_orchestrator( 'Encountered an error while establishing credentials for run' )
                critical_error = err
        
        
        if ( not critical_error ):
            try:
                self.log_orchestrator( 'Checking runner can authenticate with obtained credentials' )
                runner.check_sdk_ready( credentials )
                
                self.log_orchestrator( 'Checking license allowance for new projects today' )
                self.wait_license_allowance_new_projects( runner.sdk )        
            except Exception as err:
                self.log_orchestrator( 'Encountered an error while checking authorization and license' )
                critical_error = err
        
        if ( not critical_error ):
            try:
                self.log_orchestrator( 'Starting the template runner as user: '+str(credentials.username) )
                runner.run(credentials)        
            except Exception as err:
                self.log_orchestrator( 'Encountered an error while the task was running' )
                critical_error = err

        
        if (task_in_input):
            self.move_task_file_input_running( self.settings['task_file'] )
        
        self.output_log_of_runner( self.settings['task_file'], runner, critical_error )
        self.output_task_file( self.settings['task_file'], critical_error )
        
        if ( not critical_error is None ):
            self.log_orchestrator(critical_error)
    
    
    
    def wait_license_allowance_new_projects( self, sdk:tygron.sdk ):
        result = False
        previous_result = False
        
        while ( not result is True):
            if ( not (previous_result == result) ):
                if ( previous_result is False ):
                    self.log_orchestrator( 'Task is not allowed to start due to license allowance: '+str(result) )
                    self.log_orchestrator( 'Waiting until license allows creation of further projects' )
                else:
                    self.log_orchestrator( 'Task is still not allowed to start due to license allowance: '+str(result) )
                previous_result = result
                utilities.timing.wait_for( timeout_in_seconds=self.settings['license_allowance_retry_time_in_seconds'] )       
            result = self.check_license_allows_new_projects( sdk )
            
        return True
    
    def check_license_allows_new_projects( self, sdk:tygron.sdk ):
        allowance_data = sdk.base.domains.get_domain_allowance()
        
        if ( allowance_data.usage.new_projects_today >= self.settings['domain_projects_limit'] ):
            return 'The configured amount of projects allowed to create per day has been reached.'
        elif (allowance_data.usage_fraction_projects_today >= self.settings['domain_projects_limit_fraction'] ):
            return 'The configured amount of projects allowed to create per day has been reached.'
        elif ( allowance_data.remaining_projects_today <= 0 ):
            return 'The license allows no further project creations today.'
        else:
            return True
            
    
    
    def add_geojson_definitions_to_runner( self, runner:interfaces.TemplateRunner, geojson_file_definitions:list ):
        definitions_count = 0
            
        if ( not isinstance(geojson_file_definitions,list) ):
            geojson_file_definitions = utilities.lists.coerce(geojson_file_definitions)
            
        for entry in geojson_file_definitions:
            if ( not isinstance(entry, dict) ):
                continue
            geojson = utilities.files.read_file_as_json( self.get_data_dir_or_file(entry['file_name']) )
            runner.add_importable_areas_geojson(
                areas_geojson=geojson,
                areas_buffer=entry['buffer'],
                areas_name_attribute=entry['name_attribute']
            )
            definitions_count+=1
        return definitions_count
    
    def output_log_of_runner( self, task_file, runner, error:Exception = None ):
        target_dir = self.get_output_dir_or_file()
        
        if ( error ):
            runner.log( 'Writing log and error file' )
        else:
            runner.log( 'Writing log file' )
            
        if ( error ):
            target_dir = self.get_error_dir_or_file()
            
            error_string = utilities.exceptions.stringify(error)
            exception_file = task_file+'.exception.log'
            utilities.files.write_file( directory=target_dir, file=exception_file, content=error_string )
        
        log_file_name = task_file+'.log'
        utilities.files.write_file( directory=target_dir, file=log_file_name, content='\r\n'.join(runner.get_logs()) )
    
            
    def output_task_file( self, file, err:Exception = None ):
            
        if ( self.settings['debug_on_completion_reset_output_tasks'] ):
            self.move_task_file_running_input( self.settings['task_file'] )
        elif (not err is None):
            self.move_task_file_running_error( self.settings['task_file'] )
        else:
            self.move_task_file_running_output( self.settings['task_file'] )
        
        
    
    
    def log_orchestrator( self, message ):
        orchestrator_name = 'orchestration' if self.settings['task_file'] is None else self.settings['task_file']
        message = utilities.exceptions.stringify(message)
        self.log_formatted('Orchestrator ('+orchestrator_name+') : ' + str(message) )
    
    def log_runner( self, message ):
        message = utilities.exceptions.stringify(message)
        self.log_formatted('Runner : ' + str(message) )
        
    def log_formatted( self, message ):
        message = utilities.exceptions.stringify(message)
        current_time = utilities.timing.get_timestamp_seconds()
        readable_time = utilities.datetimes.datetime_to_string_datetime(current_time)
        self.log( str(readable_time) + ' : '+ str(message) )
        
    def log (self, message ):
        message = utilities.exceptions.stringify(message)
        self.logs.append( str(message) )
        if ( isinstance(self.logging_function, Callable) ):
            self.logging_function( message )
        
    def get_logs( self ):
        return self.logs
    
    def output_log_of_orchestrator( self ):
        current_time = utilities.timing.get_timestamp_seconds()
        readable_time = utilities.datetimes.datetime_to_string_datetime(current_time)
        
        target_dir = self.get_output_dir_or_file()
        log_file_name = 'orchestration '+readable_time+'.log'
        log_file_name = utilities.files.remove_invalid_chars_from_filename(log_file_name,'-')

        self.log_orchestrator( 'Writing orchestrator log to '+self.get_output_dir_or_file(log_file_name) )
        
        utilities.files.write_file( directory=target_dir, file=log_file_name, content='\r\n'.join(self.get_logs()) )



def main():
    settings = {}
    
    if ( len(sys.argv)>1 ):
        settings = None
        input_args = sys.argv[1]
        try:
            settings = utilities.files.read_file_as_data(input_args)
        except Exception as err:
            settings = json.loads(input_args)
        
    if ( settings is None ):
        print('Failed to read settings.')
        exit()
    orchestrator = TemplateRunnerOrchestrator( settings )
    orchestrator.set_logging_function(print)
    orchestrator.run()

if __name__ == '__main__':
    main()       