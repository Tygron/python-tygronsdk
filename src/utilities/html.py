from .html_parsers.html_table_parser import HtmlTableParser
from .lists import Lists

import inspect

class Html:
    
    @staticmethod
    def parse_html_table_to_list( html:str, vertical_first:bool=False, fill_up:bool = True, parser=HtmlTableParser ):
        html = html if (not (html is None)) else ''
    
        output = []

        if ( inspect.isclass(parser) ):
            parser = parser()

        parser.feed(html)
        output = parser.output
        
        if ( fill_up ):
            output = Lists.list_of_lists_fill_up( output )
            
        if ( vertical_first ):
            output = [ list(el) for el in zip( *output, strict=True ) ]
        return output


   
    @staticmethod
    def parse_html_table_to_dict( html:str, vertical_first:bool=False, key_mapping:dict = {}, parser=HtmlTableParser ):
        result_dict = {}
        parsed_list = Html.parse_html_table_to_list(
                html=html,
                vertical_first=vertical_first,
                fill_up=True,
                parser=parser
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
