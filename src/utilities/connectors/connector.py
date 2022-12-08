from .response import Response
from .response_stream import ResponseStream

import os
import base64, json

import http.client 
import urllib.error
import urllib.parse
import urllib.request

class Connector:

    def __init__( self ):
        self.set_protocol( 'https' );
        self.set_host( 'www.example.com' );
        self.set_port( None );
        self.set_base( None );
        self.set_query_params( {} );
        self.set_headers( {} );
        
        return;
   
    def set_protocol( self, protocol ):
        self.protocol = protocol
    def set_host( self, host ):
        self.host = host.rstrip('/')
    def set_port( self, port = None ):
        self.port = port
    def set_headers( self, headers ):
        self.headers = getattr( self, 'headers', {} )
        self.headers = {**self.headers, **headers}
    
    def set_http_basic_authentication( self, username = None, password = None ):
        if ( username == None or password == None ):
            self.http_basic_authentication = None
        self.http_basic_authentication = 'Basic '+base64.b64encode((username+':'+password).encode('ASCII')).decode('ASCII')
    
    def set_base( self, base = '' ):
        self.set_query_params( self.parse_query_params_from_url(base) )
        if ( base == None ):
            self.base = ''
        else:
            base = base.split('?')[0]
            self.base = base.lstrip('/').rstrip('/')
    def set_query_params( self, params ):
        self.query_params = getattr( self, 'query_params', {} )
        self.query_params = {**self.query_params, **params}
        self.query_params = {k: v for k, v in self.query_params.items() if v is not None}
    
    def set_request_format( self, format ):
        self.request_format = format if format else None 
    def set_exception_on_error( self, exception_on_error = True ):
        self.exception_on_error = exception_on_error
    
    
    def get_protocol( self ):
        return self.protocol
    def get_host( self ):
        return self.host
    def get_port( self ):
        return self.port
    def get_headers( self ):
        return self.headers
    
    def has_http_basic_authentication( self ):
        httpba = getattr( self, 'http_basic_authentication', None )
        return ( httpba != None )
    
    def get_base( self ):
        return self.base
    def get_query_params( self ):
        return self.query_params

    def get_request_format( self ):
        return getattr( self, 'request_format', None )
    def get_exception_on_error( self ):
        return getattr( self, 'exception_on_error', None )
    
    def path_is_url( self, path ):
        parts = self.parse_url(path)
        return (not not parts.scheme) and (not not parts.hostname)
    def path_is_file( self, path ):
        return path.rfind('.') > path.rfind('/')
    def path_has_params( self, path ):
        return path.rfind('?') -1
        
    def parse_url( self, path ):
        # 'http://user:pass@NetLoc:80/path;parameters?query=argument#fragment'
        
        #scheme  : http
        #netloc  : user:pass@NetLoc:80
        #path    : /path
        #params  : parameters
        #query   : query=argument
        #fragment: fragment
        #username: user
        #password: pass
        #hostname: netloc (netloc in lower case)
        #port    : 80
        
        return urllib.parse.urlparse(path)
        
    def parse_query_params_from_url( self, path ):
        return dict( urllib.parse.parse_qsl( self.parse_url(path).query ) )
    def create_query_string(self, query_params):
        return urllib.parse.urlencode(query_params)
    
    
    
    def get_url_part_protocol( self ):
        return self.get_protocol()+'://'
    def get_url_part_host( self ):
        return self.get_host()
    def get_url_part_port( self ):
        return ( ':' + str(self.port) ) if self.port != None else ''
    def get_url_part_path( self, path=None ):
        full_path = '/'+self.base
        if ( (not self.path_is_file(full_path)) or (path != None) ):
            full_path = full_path.rstrip('/')+'/'
        if ( path!=None ):
            full_path+=path
            if ( self.path_has_params(full_path) ):
                full_path = full_path.split('?')[0]
            if ( not self.path_is_file(full_path) ):
                full_path = full_path.rstrip('/')+'/'
            
        return full_path;
    def get_url_part_query_params( self, path='', query_params={} ):
        path_params = {}
        if ( self.path_has_params(path) ):
            path_params = self.parse_query_params_from_url( path )
        path_params.update( query_params )
        return self.create_query_string( path_params )
        
    def get_url_full( self, path = '', params = {} ):
        url = self.get_url_part_protocol()
        url+= self.get_url_part_host()
        url+= self.get_url_part_port()
        url+= self.get_url_part_path( path )

        param_string = self.get_url_part_query_params( path, {**self.get_query_params(), **params} )
        url += ('?'+param_string) if (len(param_string) > 0) else ''

        return url;
    
    def get_request_headers( self, headers = {} ):
        request_headers = self.headers.copy()
        if ( self.has_http_basic_authentication() ):
            request_headers.update({'Authorization': self.http_basic_authentication})
        request_headers.update(headers)
        return request_headers
    
    
   
    def is_ready( self ):
        # May be overridden to raise an exception instead
        return True;
    
    def request( self, method='GET', url='', headers={}, query_params={}, data=None, stream=False, timeout=None ):
        self.is_ready()

        if (query_params == None):
            query_params = {};
                
        if (method == 'GET'):
            if (data == None):
                data = {};
                
            query_params = {**query_params, **data}
            data = None
        
        if ( not self.path_is_url(url) ):
            url = self.get_url_full( url, query_params );

        headers = self.get_request_headers(headers);

        if data:
            if (stream):
                data = data
            else:
                if (self.get_request_format() == 'JSON'):
                    data = json.dumps(data);
                    headers['Content-Type'] = 'application/json; charset=UTF-8'
                else:
                    data = urllib.parse.urlencode(data).encode()
                data = data.encode('utf-8');
            
        request = urllib.request.Request(
            url, data=data, headers=headers, method=method
        );
        
        response = None
        try:
            httpresponse = None
            error = False
            try:
                httpresponse = urllib.request.urlopen(request, timeout=timeout) #what if timeout (TimeoutError)?
            except (urllib.error.HTTPError, http.client.RemoteDisconnected) as e:
                httpresponse = e
                error = True
            finally:
                response = self.create_request_response( httpresponse, stream )
                if ( not stream ):
                    if ( httpresponse != None ):
                        try:
                            httpresponse.close()
                        except AttributeError as e:
                            pass #Tried to close an exception. No problem
                else:
                    pass
        except Exception as e:
            raise e
        if ( error and self.get_exception_on_error() ):
            raise Exception( response )
        return response
        
    def create_request_response( self, response_from_request = None, stream:bool = False ):
        if ( response_from_request == None ):
            return None
        if ( isinstance(response_from_request, Exception) and not isinstance(response_from_request, urllib.error.HTTPError) ):
            response = Response(
                    http_status_code = 'TIMEOUT',
                    http_status_message = 'An exception occurred, and there was no response',
                    response_body = response_from_request
                )
        elif stream:
            response = ResponseStream.from_request_result(response_from_request)
        else:
            response = Response.from_request_result(response_from_request)
        return response
        
