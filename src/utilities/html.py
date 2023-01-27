from html.parser import HTMLParser

class Html:
    
    @staticmethod
    def parse_html_table_to_list( html:str, vertical_first:bool=False ):
        output = []
        
        class MyHTMLParser(HTMLParser):
            output = []
            row = None
            cell = None
            def handle_starttag(self, tag, attrs):
                if ( tag == 'tr' ):
                    self.row = []
                if ( tag == 'td' or tag == 'th' ):
                    self.cell = ''

            def handle_endtag(self, tag):
                if ( tag == 'td' or tag == 'th'):
                    if ( isinstance(self.row,list) ):
                        self.row.append(self.cell)
                    self.cell=None
                if ( tag == 'tr' ):
                    self.output.append(self.row)
                    self.row = None

            def handle_data(self, data):
                if ( not (self.cell is None) ):
                    self.cell += str(data)

        parser = MyHTMLParser()
        parser.feed(html)
        output = parser.output
        
        if ( vertical_first ):
            output = list( zip( *output ) )
        
        return output
        
        
    @staticmethod
    def parse_html_table_to_dict( html:str, vertical_first:bool=False, key_mapping:dict = {} ):
        result_dict = {}
        parsed_list = Html.parse_html_table_to_list(
                html=html,
                vertical_first=vertical_first
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
                
            
            