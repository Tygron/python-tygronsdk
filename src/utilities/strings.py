import os
import math, binascii, re

class Strings:
    
    @staticmethod
    def generate_random_token( length:int = 32 ):
        token = binascii.hexlify( os.urandom( math.ceil(length/2) ) ).decode()
        return token[:length]
        
    @staticmethod
    def is_length( string:str = '', min_length:int=None, max_length:int=None ) -> bool:
        if ( not min_length == None ):
            if ( len(string) < min_length ):
                return False
        if ( not max_length == None ):
            if ( len(string) > max_length ):
                return False
        return True
    
    @staticmethod
    def format( string:str = '', **kwargs ):
        formatted = ''
        to_process = string
        while( True ):
            start_index = to_process.find('{') 
            end_index = to_process.find('}', start_index)
            if ( (start_index < 0) or (end_index < 0) ):
                formatted += to_process
                break
            
            formatted += to_process[:start_index]
            formattable = to_process[start_index:end_index+1]
            to_process = to_process[end_index+1:]
            
            try:
                formatted += formattable.format(**kwargs)
            except:
                formatted+=formattable
        return formatted
            
        """
            Find start of format keys
            Find end of format key
            Substring and attempt to replace it with formatted
            If error, replace with substring itself
        """
    
    @staticmethod
    def strip_to_number( input:str, negative_kept:bool = False, decimal_character:str = None ):
        regex = '^0-9'
        regex = regex + ( '\-' if negative_kept else '' )
        regex = regex + ( decimal_character if ( not decimal_character is None ) else '' )
        regex = '['+regex+']'
        return re.sub(regex,'',str(input))
        
    @staticmethod
    def strip_to_letters( input:str, ):
        regex = '^a-zA-Z'
        regex = '['+regex+']'
        return re.sub(regex,'',str(input))
    
    @staticmethod
    def parse_file_size_string( input:str, output_unit:str = 'MB' ):
        units = {"B": 1, "KB": 2**10, "MB": 2**20, "GB": 2**30, "TB": 2**40}
        number = int(Strings.strip_to_number(str(input)))
        unit = Strings.strip_to_letters(str(input))
        size = number*units[unit]
        
        return size/units.get(output_unit.upper(), 1)
        
    @staticmethod
    def parse_surface_area_from_sizes_string( input:str, negative_kept:bool = False, decimal_character = None ):
        seperator_chars = [' ','x','X', 'by',':']
        split_input = re.split('|'.join(seperator_chars),str(input))
        value = None
        for entry in split_input:
            try:
                number = float( Strings.strip_to_number(entry, negative_kept, decimal_character) )
                value = number if ( value is None ) else value*number
            except Exception as err:
                pass
        if ( not (value is None) ):
            return value
        raise Exception('Could not parse 2 numbers to multiply from "'+str(input)+'"')
    
    @staticmethod
    def create_json_string( obj:dict = {} ):
        return json.dumps(obj)
    
    @staticmethod
    def create_keys_values_string( obj:dict = {} ):
        return os.linesep.join([k+'='+v for k,v in obj.items()])