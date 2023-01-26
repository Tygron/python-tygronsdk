import os
import math, binascii


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