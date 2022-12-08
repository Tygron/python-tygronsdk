from .response import Response

import json

class ResponseStream(Response):
    def __init__( self, 
                http_status_code = None,
                http_status_message = None,
                response_headers = None,
                response_encoding = None,
                response_body = None,
                response = None,
            ):
        super().__init__(
                http_status_code = http_status_code,
                http_status_message = http_status_message,
                response_headers = response_headers,
                response_encoding = response_encoding,
                response_body = None
            )
        self._response = response
        
        self.set_chunk_size( 1026 * 16 )

    @staticmethod
    def from_request_result( result ):
        return ResponseStream(
                http_status_code=result.status,
                http_status_message=str(result.reason) if result.reason else None,
                response_headers=result.headers,
                response_encoding=result.headers.get_content_charset( None ),
                response=result
            )
    
    def set_chunk_size( self, chunk_size:int ):
        if ( chunk_size < 1 ):
            raise ValueError('Chunk size must be at least 1')
        self._chunk_size = chunk_size;
    def get_chunk_size( self ):
        return self._chunk_size
    
    
    def get_response_body( self ):
        if ( self._response_body == None ):
            self._response_body = self._response.read()
        return super().get_response_body()
    
    
    def __iter__( self ):
        return ResponseStreamIterator( self )
            
class ResponseStreamIterator:
    def __init__( self, response_stream ):
        self._response = response_stream._response
        self._chunk_size = response_stream._chunk_size
        self._index = 0
    
    def __iter__( self ):
        return self
    
    def __next__( self ):
        while True:
            chunk = self._response.read( self._chunk_size )
            if not chunk:
                break
            return chunk
        #close stream?
        raise StopIteration