import json

class Response():
    def __init__( self, 
                http_status_code = None,
                http_status_message = None,
                response_headers = None,
                response_encoding = None,
                response_body = None
            ):
        self._http_status_code = http_status_code
        self._http_status_message = http_status_message
        self._response_headers = response_headers
        self._response_encoding = response_encoding
        self._response_body = response_body

    @staticmethod
    def from_request_result( result ):
        return Response(
                http_status_code=getattr(result, 'status',None),
                http_status_message=getattr(result, 'reason',None),
                response_headers=getattr(result, 'headers',[]),
                response_encoding=result.headers.get_content_charset( 'utf-8' ),
                response_body=result.read()
            )
        
    def get_http_status_code( self ):
        return self._http_status_code
        
    def get_http_status_message( self ):
        return self._http_status_message
    
    def get_response_headers( self ):
        return self._response_headers
    def get_response_encoding( self ):
        return self._response_encoding
    
    
    
    def get_response_body( self ):
        if ( self.get_response_encoding() ):
            try:
                return self._response_body.decode( self.get_response_encoding() );
            except UnicodeDecodeError:
                pass
        return self._response_body;
    def get_response_body_json( self ):
        return json.loads( self.get_response_body() )
    
    
    def is_success( self ):
        return (self.get_http_status_code() >=200 and self.get_http_status_code() < 300)
    
    def __str__( self ):
        return '%s (%s) : %s' % (
                self.get_http_status_code(), 
                self.get_http_status_message(), 
                self.get_response_body(), 
            )
            
    def __len__( self ):
        try:
            return getattr( self.get_response_headers(), 'Content-Length' )
        except Exception as e:
            raise e