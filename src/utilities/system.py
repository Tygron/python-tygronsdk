import sys
import json as jsonlib
from shlex import shlex

from .exceptions import Exceptions
from .files import Files

class System:
    
    @staticmethod
    def get_args( input_args:list = None, simple=False, all_types:bool = True, file:bool = False, json:bool = False, keyvalues:bool = False ):
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
            
            if ( all_types and json ):
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
                    print('Processed as json')
                    continue
                except Exception as err:
                    arg_errors.append(err)
                    
            if ( all_types and keyvalues ):
                if (file):
                    try:
                        arg_result = Files.read_file_as_key_values(arg)
                        result.update(arg_result)
                        continue
                    except Exception as err:
                        arg_errors.append(err)
                try:
                    lexer = shlex(arg, posix=True)
                    lexer.whitespace = ';'
                    lexer.wordchars += '='
                    arg_result = dict( word.split('=', maxsplit=1) for word in lexer )
                    result.update(arg_result)
                    continue
                except Exception as err:
                    arg_errors.append(err)

            Exceptions.raise_multiple_exceptions( arg_errors )

        return result