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
    
    @staticmethod
    def make_enum_term( string:str = '' ) -> str:
        term = string.upper()
        term = term.replace( ' ', '_' )
        term = re.sub( '[^_0-9a-zA-Z]', '', term )
        return term
        
    @staticmethod
    def parse_session_id_from_api_token( api_token:str, as_string:bool=False ):
        session_id_length = 8
        session_id = api_token[:session_id_length]
        if ( len(session_id) < session_id_length ):
            raise Exception('Extracted substring was of insufficient length')
        try:
            int(session_id)
        except:
            raise Exception('Session id "'+str(session_id)+'" could not parse to a valid session id. Not numeric.')
        return int(session_id) if ( not as_string ) else session_id