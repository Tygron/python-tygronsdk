import tygronsdk
from tygronsdk.src.core.data import events as event_structure
from tygronsdk.src.core.events import EventSet
from tygronsdk.src.utilities.html_parsers.html_table_with_options_parser import HtmlTableWithOptionsParser

import json, re
from typing import Type, Union

class ApiReaderEventSet:
    
    DEPRECATED_NOTICE = 'Event is deprecated, do not use it anymore'
    
    def __init__( self,  ):
        pass
    
    def generate_event_sets_from_api( self, connector:tygronsdk.core.Connector, base_url:str = None ):
        self.connector = connector
        base_url = 'event' if base_url is None else base_url
        
        api_events_data = self.get_event_data_from_api( base_url=base_url )  
        
       # print(json.dumps(api_events_data,indent=4))
        
        event_sets = self.generate_event_sets_from_api_data( api_events_data )
        self.connector = None
        return event_sets
    
    def get_event_data_from_api( self, base_url ):
        
        events_data = self.get_event_types_from_base_url( base_url )
        for event_type_name, event_type in events_data.items():
        
            events = self.get_events_from_event_type_url( base_url, event_type['name'] )
            event_type['events'] = events
            for event_name, event in events.items():
                event_data = self.get_event_data_from_event_url( base_url, event_type['name'], event['name'] )
                event['parameters'] = event_data
        
        return events_data
    
    def get_event_types_from_base_url( self, url:str ):
        event_types_url = url
        
        try:
            page = self.get_page(event_types_url)
        except Exception as err:
            raise Exception( 'Could not obtain from "'+str(event_types_url)+'"' ) from err
            
        try:
            page_content = tygronsdk.utilities.html.parse_html_table_to_list( html = page )
            data = tygronsdk.utilities.lists.list_of_lists_to_dict(page_content, keys=['name','description'])
        except Exception as err:
            raise Exception( 'Could not obtain or parse event types from "'+str(event_types_url)
                    +'", the content of which was '+str(page) ) from err
            
        return data
    
    def get_events_from_event_type_url( self, url:str, event_type:str ):
        events_url = url+'/'+event_type
        
        try:
            page = self.get_page(events_url)
        except Exception as err:
            raise Exception( 'Could not obtain from "'+str(events_url)+'"' ) from err
            
        try:
            page_content = tygronsdk.utilities.html.parse_html_table_to_list( html = page )
            data = tygronsdk.utilities.lists.list_of_lists_to_dict(page_content, keys=['name','description'])
        except Exception as err:
            raise Exception( 'Could not obtain or parse event type events from "'+str(events_url)
                    +'", the content of which was '+str(page) ) from err
            
        return data
        
    def get_event_data_from_event_url( self, url:str, event_type:str, event:str ):
        event_data_url = url+'/'+event_type+'/'+event
        
        try:
            page = self.get_page(event_data_url)
        except Exception as err:
            raise Exception( 'Could not obtain from "'+str(event_data_url)+'"' ) from err
          
        if ( self.DEPRECATED_NOTICE in page ):
            return ''
                
        try:
            page_content = tygronsdk.utilities.html.parse_html_table_to_list( html = page, vertical_first=True, parser=HtmlTableWithOptionsParser() )
            data = self.parse_event_data_from_page_table_lists(page_content)
        except Exception as err:
            raise Exception( 'Could not obtain or parse event data from "'+str(event_data_url)
                    +'", the content of which was '+str(page) ) from err
            
        return data
    
    
    
    def get_page( self, url:str ):
        try:
            url = str(url)
            response = self.connector.request( url=url, query_params={'f':'HTML'} )
            return response.get_response_body()
        except Exception as err:
            response = err.args[0]
            raise Exception( 'Invalid response from "' + str(response.get_response_url()) + '" : '+ str(response) )
        
    def parse_event_data_from_page_table_lists( self, page_table ):
        parameters = []
        
        name_list = page_table[0]
        descr_list = page_table[1]
    
        # One header line
        range_start = 1
        # Four end lines for: submit button, response codes header, success response code, failure response code
        # Additional -1 to adjust from length to 0-indexed index
        range_end = len(name_list) - 1 - 4
        index = range_start
        
        while( index <= range_end ):
        
            found_index = int(re.search(r'\d+', name_list[index]).group(0))
                
            if ( not ( len(parameters) is found_index ) ):
                raise Exception( 'Expected index '+str(len(parameters))+' does not match found index '+str(found_index) )
                
            parameters.append({
                    'index':        found_index,
                    'required':     'required' in str(name_list[index]).lower(),
                    'description':   descr_list[index+1],
                    'type':         name_list[index+1],
                    'default':      None
                })
            
            index = index+2
        return parameters
    
    
    
    
    def generate_event_sets_from_api_data( self, api_data:dict = {} ):
        generated_definitions = {}
        for event_type_name, event_type_data in api_data.items():
            definition_name = str(event_type_name).lower()
            try:
                definition_content = self.generate_event_set_from_api_data(event_type_data)
            except Exception as err:
                raise Exception( 'Could not parse event type definition of '+str(event_type_name) ) from err
            generated_definitions[definition_name] = definition_content
        return generated_definitions
                
    def generate_event_set_from_api_data( self, event_type_data ):
        event_definitions = {}
        for event_name, event_data in event_type_data['events'].items():
            if ( not (event_data is None) ):
                event_definition = self.generate_event_definition_from_api_data( event_data )
                event_definitions[event_name] = event_definition
        event_set = EventSet(event_definitions, event_type_data['name'])
        return event_set
            
    def generate_event_definition_from_api_data( self, event_data, domain=None ):
        parameters = []
        if ( event_data['parameters'] is None ):
            return None
        if ( event_data['parameters'] == '' ):
            return ''
        
        for event_parameter_data in event_data['parameters']:
            new_parameter = self.generate_event_parameter_definition_from_api_data( event_parameter_data )
            parameters.append(new_parameter)
        event_definition = event_structure.EventDefinition(name=None, domain=domain, parameters=parameters)
        return event_definition
        
    
    def generate_event_parameter_definition_from_api_data( self, event_parameter_data ):
        parameter_class = event_structure.EventParameter
        parameter_aggregation = self.parameter_term_to_aggregation( event_parameter_data['type'] )
        
        parameter_options = self.description_to_options( event_parameter_data['description'] )
        
        parameter_default = parameter_options.get( 'default',event_parameter_data['default'] )
        parameter_type = self.parameter_term_to_parameter_type(
                event_parameter_data['type'],
                parameter_default,
                parameter_options.get('values', None)
            )
        
        parameter_definition = parameter_class(
                arg_name = event_parameter_data['index'],
                arg_type = parameter_type,
                required = event_parameter_data['required'],
                arg_default = event_parameter_data['default'],
                aggregation = parameter_aggregation,
                
                api_description = event_parameter_data['description'],
                api_type = parameter_type,
                api_required = event_parameter_data['required'],
                api_default = parameter_default,
                api_aggregation = parameter_aggregation,
            )
        return parameter_definition
        
    def description_to_options( self, description ):
        # Crude way to find the enum data
        enum_index = description.find(';{"')
        if ( enum_index == -1 ):
            return {}
            
        # Offset of 1 to clear the semicolon
        enum_data_str = description[enum_index+1:]
        enum_data = json.loads(enum_data_str)
            
        return enum_data
    
    def parameter_term_to_aggregation( self, term ):
        param_class = None
        term = term.lower()
        
        if ( 'matrix' in term ):
            return 2
        elif ( 'multiple values in array' in term ):
            return 1
        else:
            return 0
        
        return param_class
    
    def parameter_term_to_parameter_type( self, term, default = None, options = None ):
        term = term.lower()
        
        found_type = 'Unknown: '+str(term)
        
        match=0
        types = {
                'id' : Type[int],
                'string' : Type[str],
                'integer' : Type[int],
                'true, false' : Type[bool],
                'false = ' : Type[bool],
                'floating point' : Type[float],
                'byte' : Type[bytes],
                #'type' : 'TYPE?',
                'enumeration': 'ENUM',
                'multipolygon': 'MultiPolygon',
                
                'geolinktype': ['AREA', 'BUILDING', 'ROAD', 'TERRAIN_HEIGHT', 'WATER_BOTTOM'],
                'geometrymode': ['RADIUS_CENTERPOINT', 'NORMAL'],
                
                'actiontype' : ['CONSTRUCTION_PLAN', 'CONSTRUCTION_PLAN_CANCEL'],
                
                'nettype': ['HEAT', 'INTERNET', 'SEWER', 'GAS', 'ELECTRICITY'],
                'netsetting' : ['INTERNET_ACTIVE', ' SEWER_NETWORK_OWNER_ID', ' ELECTRICITY_NETWORK_OWNER_ID', ' REQUIRE_UTILITY_CORPORATION_APPROVAL', ' INTERNET_FLOW_ATTRIBUTE', ' FIRST_CONNECT_ACCEPT', ' RESTRICT_TO_NET_OVERLAY', ' LOAD_TO_NODE_LINES_ENABLED', ' CLUSTER_MODELS_ENABLED', ' SEWER_ACTIVE', ' ELECTRICITY_ACTIVE', ' HEAT_ACTIVE', ' INTERNET_NETWORK_OWNER_ID', ' SEWER_FLOW_ATTRIBUTE', ' ELECTRICITY_FLOW_ATTRIBUTE', ' HEAT_FLOW_ATTRIBUTE', ' GAS_NETWORK_OWNER_ID', ' HEAT_NETWORK_OWNER_ID', ' GAS_ACTIVE', ' CLUSTER_FRACTION_CONNECTED', ' GAS_FLOW_ATTRIBUTE'],
 
                'overlaytype' : ['AREAS', 'ATTRIBUTE', 'AVG', 'COMBO', 'DISTANCE_SIGHT', 'DISTANCE_ZONE', 'DISTURBANCE_DISTANCE', 'FLOODING', 'FUNCTION_HIGHLIGHT', 'GEO_TIFF', 'GROUNDWATER', 'HEAT_STRESS', 'HEIGHTMAP', 'IMAGE', 'LIVABILITY', 'MUNICIPALITIES', 'NEIGHBORHOODS', 'NETWORK_DISTANCE', 'NETWORK_OVERVIEW', 'NETWORK_OWNERSHIP', 'OWNERSHIP', 'OWNERSHIP_GRID', 'RAINFALL', 'RESULT_CHILD', 'SAFETY_DISTANCE', 'SOURCE', 'SUBSIDENCE', 'TEST', 'TRAFFIC_DENSITY', 'TRAFFIC_NO2', 'TRAFFIC_NOISE', 'TRAVEL_DISTANCE', 'UNDERGROUND', 'VACANCY', 'WATERSHED', 'WCS', 'WMS', 'ZIP_CODES', 'ZONING'],

                'alignment' : ['ROAD', 'SPACED'],
                'functiontype' : ['ROAD', 'BUILDING', 'REMAINDER', 'WATER', 'PARKING', 'PUBLIC_GREEN', 'SIDEWALK', 'GARDEN'],
            }
        
        for string, ptype in types.items():
            if ( string in term and len(string)>match ):
                found_type = ptype
                    
        if ( found_type == 'ENUM' ):
            found_type = options
                    
        return found_type   
