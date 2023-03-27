from .html_table_parser import HtmlTableParser

import json

class HtmlTableWithOptionsParser(HtmlTableParser):
    def __init__(self, options_format=';{json}'):
        super().__init__()
        self.output = []
        self.row = None
        self.cell = None
        
        self.options_format = options_format
        
        self.values  = None
        self.default = None
        self.curr_value = None
        
    def handle_starttag(self, tag, attrs):
        if ( tag == 'input' ):
            #print('input '+str(attrs))
            #self.default = 'something from input'
            pass
        elif ( tag == 'select' ):
            print('select '+str(attrs))
            self.values = []
        elif ( tag == 'option' ):
            print('option '+str(attrs))
            self.curr_value = ''
        else:
            super().handle_starttag(tag, attrs)

    def handle_endtag(self, tag):
        if ( tag == 'select' ):
            self.handle_input_data( self.default, self.values )
            self.default = None
            self.values = None
            pass
        elif ( tag == 'option' ):
            self.values.append(self.curr_value)
            self.curr_value = None
            pass
        else:
            super().handle_endtag(tag)
    
    
    def handle_data(self, data):
        if ( not(self.curr_value is None) ):
            self.curr_value += str(data)
        else:
            super().handle_data(data)
   
    def handle_input_data(self, default=None, values=None):
        super().handle_data(self.options_format.format(
                default = default,
                values = values,
                
                json = json.dumps({'default':default, 'values':values})
            ))