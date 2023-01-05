from .strings import Strings

import re

class TygronStrings:
    
    @staticmethod
    def is_simple_characters( string:str = '' ) -> bool:        
        return bool( re.match(r'^[a-zA-Z0-9\-\_]+$', string) )
        
    @staticmethod
    def is_allowed_project_name( string:str = '' ) -> bool:
        if ( string == None ):
            return False
        return (
                Strings.is_length( string, min_length=3, max_length=20 )
                and TygronStrings.is_simple_characters( string )
            )