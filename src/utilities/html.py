from html.parser import HTMLParser
from .lists import Lists

class Html:
    
    @staticmethod
    def parse_html_table_to_list( html:str, vertical_first:bool=False, fill_up:bool = True ):
        html = html if (not (html is None)) else ''
    
        output = []
        
        class MyHTMLParser(HTMLParser):
            output = []
            row = None
            cell = None
            def handle_starttag(self, tag, attrs):
                if ( tag == 'tr' ):
                    # Catch for unclosed row
                    self.handle_endtag('td')
                    self.handle_endtag('tr')
                    self.row = []
                if ( tag == 'td' or tag == 'th' ):
                    self.handle_endtag('td')
                    self.cell = ''

            def handle_endtag(self, tag):
                if ( tag == 'td' or tag == 'th'):
                    if ( isinstance(self.row,list) and ( not (self.cell is None) ) ):
                        self.row.append(self.cell)
                    self.cell=None
                if ( tag == 'tr' ):
                    if ( isinstance(self.row,list) ):
                        self.output.append(self.row)
                    self.row = None

            def handle_data(self, data):
                if ( not (self.cell is None) ):
                    self.cell += str(data)

        parser = MyHTMLParser()
        parser.feed(html)
        output = parser.output
        
        if ( fill_up ):
            output = Lists.list_of_lists_fill_up( output )
            
        if ( vertical_first ):
            output = [ list(el) for el in zip( *output, strict=True ) ]
        return output
        
        
    @staticmethod
    def parse_html_table_to_dict( html:str, vertical_first:bool=False, key_mapping:dict = {} ):
        result_dict = {}
        parsed_list = Html.parse_html_table_to_list(
                html=html,
                vertical_first=vertical_first,
                fill_up=True
            )
        headers = None
        for row in parsed_list:
            if ( len(row)==0 ):
                continue
                
            if (headers is None):
                headers = []
                for head in row:
                    headers.append( key_mapping.get(head.lower(), head) )
                continue
            row_key = str(row[0])
            row_key = key_mapping.get(row_key.lower(), row_key)
            result_dict[row_key] = {}
            for index, value in enumerate(row):
                if ( index >= len(headers) ):
                    break
                result_dict[row_key][headers[index]] = value
                
        return result_dict
                
            
            