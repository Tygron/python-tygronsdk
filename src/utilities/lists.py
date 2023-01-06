

from typing import List

class Lists:
    
    @staticmethod
    def coerce( value ):
        return value if isinstance(value,list) else [value]
    
    @staticmethod
    def get( value, index:int, default = None ):
        if ( not isinstance(value, list) ):
            return default
        if ( (len(value) > index) and (not value[index] == None) ):
            return value[index]
        return default
        