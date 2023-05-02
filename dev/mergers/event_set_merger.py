import tygronsdk
from tygronsdk import utilities

from tygronsdk.src.core.data.events import EventDefinition, EventParameter
from tygronsdk.src.core.events import EventSet

class EventSetMerger:

    def __init__( self ):
        self.assume_unchanged_parameters = False
            
    def get_merged_sets( self, base:dict, new:dict ):
        merged_sets = {}
        for domain, new_set in new.items():
            base_set = base.get( domain, None )
            merged_sets[domain] = self.get_merged_set( base_set, new_set )
        for domain, old_set in base.items():
            merged_sets[domain] = merged_sets.get( domain, None )
        return merged_sets
    
    def get_merged_set( self, base:EventSet, new:EventSet ):
        if ( new is None ):
            return None
        
        merged_definitions = self.get_merged_ordered_definitions( base, new )
            
        merged_set = EventSet( merged_definitions, new.domain )
        
        return merged_set
    
    def get_merged_ordered_definitions( self, base:EventSet, new:EventSet ):
        if ( new is None ):
            return {}
        
        base_definitions = [] if base is None else [ k for k in base.get_definition_names_as_grouped_list() ]
        new_definitions =  [] if  new is None else [ k for k in  new.get_definition_names_as_grouped_list() ]

        merged_definitions = {}

        for def_name in base_definitions + new_definitions:
            if ( not (merged_definitions.get(def_name, False) is False) ):
                continue
                
            base_def = None if base is None else base.definitions.get(def_name, None)
            new_def =  None if  new is None else  new.definitions.get(def_name, None)
            merged_def = None
            
            if ( new_def is None ):
                continue
            
            base_def_is_none = False
            if ( not (base is None) ):
                base_def_is_none = (base.definitions.get(def_name, False) is None)
            
            if ( not base_def_is_none ):
                merged_def = self.get_merged_definition( base_def, new_def )

            merged_definitions[def_name] = merged_def
        
        return merged_definitions
    
    def get_merged_definition( self, base:EventDefinition, new:EventDefinition ):
        if ( new is None ):
            return None

        merged_params = []
        param_mismatch = ( base is None or (not (len(base.parameters) == len(new.parameters)) ) )
        change = param_mismatch
        
        for index, new_param in enumerate(new.parameters):
            base_param = None
            base_param = None if param_mismatch else utilities.lists.get( base.parameters, index, None )
            merged_param = self.get_merged_parameter( base_param, new_param )
            merged_params.append( merged_param )
            change = change or merged_param.changed
            
        definition = EventDefinition(
                name=new.name,
                domain=new.domain,
                parameters=merged_params,
                group=None if base is None else base.group
            )
        definition.changed = change
        return definition
    
    def get_merged_parameter( self, base:EventParameter, new:EventParameter ):
        change = False
        if ( new is None ):
            return None
        
        ignore_old = False
        if ( base is None ):
            ignore_old = True
        elif ( not self.assume_unchanged_parameters and (not new.api_description == base.api_description) ):
            ignore_old = True
        
        if ( ignore_old ):
            merged_param = EventParameter( **new.data )
            merged_param.changed = True
            return merged_param
                    
        merged_data = {}
        merged_data['arg_name'] = base.arg_name
        merged_data['arg_default'] = None
        if ( (base.api_required is new.api_required) and (base.api_default is new.api_default) ):
            merged_data['arg_default'] = base.arg_default
        elif( new.api_required is False and not (new.arg_default is None) ):
            merged_data['arg_default'] = new.arg_default
        #merged_data['required'] = ( (not new.api_required) or (not merged_data['arg_default'] is None) )
        
        merged_param = EventParameter( **{**new.data, **merged_data} )
        merged_param.changed = change
        return merged_param