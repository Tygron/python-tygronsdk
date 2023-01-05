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