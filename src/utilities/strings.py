import os
import math, binascii


class Strings:
    
    @staticmethod
    def generate_random_token( length:int = 32 ):
        token = binascii.hexlify( os.urandom( math.ceil(length/2) ) ).decode()
        return token[:length]