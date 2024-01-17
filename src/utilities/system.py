import sys
import json as jsonlib

from .exceptions import Exceptions
from .files import Files

class System:
    
    @staticmethod
    def get_args( input_args:list = None, simple=False, all_types:bool = True, file:bool = True, json:bool = False, keyvalues:bool = False, parse_bool:bool = True ):
        if ( input_args is None ):
            input_args = sys.argv[1:]
            
        if ( simple ):
            return [*input_args]
        
        result = {}
        if ( len(input_args)==0 ):
            return result
            
        for arg in input_args:
            arg_errors = []
            arg_result = {}  
            
            if ( all_types or json ):
                if (file):
                    try:
                        arg_result = Files.read_file_as_json(arg)
                        result.update(arg_result)
                        continue
                    except Exception as err:
                        arg_errors.append(err)
            
                try:
                    arg_result = jsonlib.loads(arg)
                    result.update(arg_result)
                    continue
                except Exception as err:
                    arg_errors.append(err)
                    
            if ( all_types or keyvalues ):
                if (file):
                    try:
                        arg_result = Files.read_file_as_key_values(arg)
                        result.update(arg_result)
                        continue
                    except Exception as err:
                        arg_errors.append(err)
                try:
                    sep = ';'
                    for entry in arg.split(sep):
                        key, value = entry.partition('=')[::2]
                        arg_result[key] = value
                    result.update(arg_result)
                    continue
                except Exception as err:
                    arg_errors.append(err)

            Exceptions.raise_multiple_exceptions( arg_errors )

        if (parse_bool):
            result.update( 
                    (k, True if result[k] in ['true', 'True'] else False if result[k] in ['false', 'False'] else result[k]) 
                    for k in result.keys()
                )

        return result