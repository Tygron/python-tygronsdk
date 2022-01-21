import json

class Response():
    def __init__( self, http_status_code = None, http_status_message = None, response_headers = None, response_body = None ):
        self.http_status_code = http_status_code;
        self.http_status_message = http_status_message;
        self.response_headers = response_headers;
        self.response_body = response_body;
        
    def get_http_status_code( self ):
        return self.http_status_code;
        
    def get_http_status_message( self ):
        return self.http_status_message;
    
    def get_response_headers( self ):
        return self.response_headers;
        
    def get_response_body( self ):
        return self.response_body;
    def get_response_body_json( self ):
        return json.loads( self.get_response_body() );
    
    
    def is_success( self ):
        return (self.get_http_status_code() >=200 and self.get_http_status_code() < 300)
    
    def __str__( self ):
        return '%s (%s) : %s' % (
                self.get_http_status_code(), 
                self.get_http_status_message(), 
                self.get_response_body(), 
            );