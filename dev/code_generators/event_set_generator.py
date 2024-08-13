import tygronsdk
from tygronsdk import sdk as tygron
from tygronsdk import utilities as utilities

from tygronsdk.src.core.data.events import EventDefinition, EventParameter
from tygronsdk.src.core.events import EventSet

from ..api_readers.api_reader_event_set import ApiReaderEventSet
from ..mergers.event_set_merger import EventSetMerger

import os
from typing import Union

class EventSetGenerator:
    
    def __init__( self, sdk_settings:dict = {} ):
        self.connector = None
        self.sdk_environment = None
        
        self.output_directory = 'dev_output'
        self.output_file = '{domain}.py'
        
        self.linesep = '\n'
        
        self.assume_unchanged_parameters = False
    
    def get_connector( self, sdk:tygronsdk.sdk.sdk = None ):
        if ( not (self.connector is None) ):
            return self.connector
        raise Exception( ' A "get_connector" implementation must be defined, returning a ready-to-use connector' )
    def get_environment_events( self ):
        if ( not (self.environment_events is None) ):
            return self.environment_events
        raise Exception( ' A "get_environment_events" implementation must be defined, returning a list of events of the environment' )
    
    
    
    def get_api_event_sets( self ):
        api_reader = ApiReaderEventSet()
        return api_reader.generate_event_sets_from_api( self.get_connector() )
    
    def get_sdk_event_sets( self ):
        environment_events = self.get_environment_events()
        event_set_collection = utilities.modules.get_content_from_module(environment_events, EventSet)
        return event_set_collection
    
    def get_merged_event_sets( self, sdk_event_sets:dict = None, api_event_sets:dict = None ):
        api_event_sets = api_event_sets if ( not (api_event_sets is None)) else self.get_api_event_sets()
        sdk_event_sets = sdk_event_sets if ( not (sdk_event_sets is None)) else self.get_sdk_event_sets()
        
        event_set_merger = EventSetMerger()
        event_set_merger.assume_unchanged_parameters = True
        merged_event_sets = event_set_merger.get_merged_sets( sdk_event_sets, api_event_sets )
        
        return merged_event_sets
        
    
    
    
    def print_difference_between_event_sets ( self, *event_sets_dicts ):
        
        domains = { domain for event_sets in event_sets_dicts for domain in event_sets.keys() }
        events_per_domain = {}            
    
        event_names = {}
        for event_sets in event_sets_dicts:
            for event_set in event_sets.values():
                event_names[event_set.domain] = list( event_names.get(event_set.domain, []) ) + list( event_set.definitions.keys() )
                
            print(event_sets)
                
        for domain, names in event_names.items():
            for name in names:
                print( ' --- ' + domain + '/' + name + ' --- ' )
                for event_sets in event_sets_dicts:
                    known = event_sets.get(domain, None)
                    if ( not ( known is None) ):
                        known = known.definitions.get(name, None)
                    print( str(known) )
    
    
    
    
    def write_event_set_files( self, event_sets:dict ):
        files = []
        for domain, event_set in event_sets.items():

            generated_code = self.generate_event_set_code( event_set )
            
            file_name = utilities.strings.format( self.output_file, domain=domain )
            files.append( os.path.join( self.output_directory, file_name ) )
            
            utilities.files.write_file(
                directory=  self.output_directory,
                file=       file_name,
                content=    self.generate_event_set_file( event_set )
            )
        return files
    
    def generate_event_set_file( self, event_set:EventSet, lines_as_list=True ):
            code = self.generate_event_set_code( event_set )
            file_content = self.linesep.join([
                    'from ......core.events import EventSet',
                    '',
                    'from ......core.data.events import EventDefinition',
                    'from ......core.data.events import EventParameter',
                    '',
                    'from typing import Type',
                    '',
                    '{code}',
                ])
            
            code = self.linesep.join(code)
            return utilities.strings.format( file_content, code=code )
    
    def generate_event_set_code( self, event_set:EventSet, lines_as_list=True ):
        data = {
                'domain':event_set.domain
            }
        data = self.primitives_in_dict_to_string( data )
    
        code=[ 
                'definitions = {'
            ] 
        
        group = None
        for event_definition_name in event_set.get_definition_names_as_grouped_list( include_empty=True ):
            event_definition = event_set.get_definition( event_definition_name )
            
            ed_group = 'Unavailable'
            if ( event_definition is None ):
                event_definition = event_definition_name
            else:
                ed_group = event_definition.group
                
            if ( not (ed_group is group) ):
                group = ed_group
                code = code + [ '', '', '    # '+group]
                
            code = code + ['        '+l for l in self.generate_event_definition_code(event_definition)]
            code[-1] = code[-1]+','
        
        code = code + [
                '    }',
                '',
                'event_set = EventSet(definitions, domain={domain})',
        ]
        
        code = [ utilities.strings.format(l, **data) for l in code ]
        return code if lines_as_list else self.linesep.join(code)
        
    def generate_event_definition_code( self, event_definition:Union[EventDefinition,str], lines_as_list=True ):
        data = {}
        
        if ( type(event_definition) is str ):
            data['name'] = event_definition
            data = self.primitives_in_dict_to_string( data )
            code = ['{name} : None']
        else:
            data = event_definition.data
            data = self.primitives_in_dict_to_string( data )
        
            code = [
                '{name} : EventDefinition(',
                '        group={group},',
                '        parameters=[',
                ]
        
            for event_parameter in event_definition.parameters:
                code = code + ['                '+l for l in self.generate_event_parameter_code(event_parameter)]
                code[-1] = code[-1]+','
        
            code = code + [
                '            ]',
                '    )',
                ]
        
        code = [ utilities.strings.format(l, **data) for l in code ]
        return code if lines_as_list else self.linesep.join(code)
    
    def generate_event_parameter_code( self, event_parameter:EventParameter, lines_as_list=True ):
        data = event_parameter.data
        data = self.primitives_in_dict_to_string( event_parameter.data )
        
        codeline = 'EventParameter({arg_name}, {arg_type}, '
        if ( (not event_parameter.required) ):
            codeline = codeline + '{required}, '
        elif ( (not event_parameter.arg_default is None) ):
            codeline = codeline + '{required}, {arg_default}, '
        if ( not (event_parameter.aggregation == 0) ):
            codeline = codeline + 'aggregation={aggregation}, '
        
        apiline = ''
        apiline = apiline + 'api_description={api_description}, '
        apiline = apiline + 'api_type={api_type}, '
        apiline = apiline + 'api_required={api_required}, '
        apiline = apiline + 'api_default={api_default}, '
        apiline = apiline + 'api_aggregation={api_aggregation}, '
        
        code = [
            codeline,
            '                '+apiline + ' )',
        ]
        
        code = [ utilities.strings.format(l, **data) for l in code ]
        return code if lines_as_list else self.linesep.join(code)
        
        
    def primitives_in_dict_to_string( self, prim_dict:dict ):
        prim_dict = { k: self.primitive_to_string(v) for k,v in prim_dict.items() }
        return prim_dict
    
    def primitive_to_string( self, prim ):
        if ( type(prim) is str ):
            return '\''+str(prim)+'\''
        if ( str(prim).startswith('typing.Type') ):
            return str(prim).removeprefix('typing.')
        return str(prim)