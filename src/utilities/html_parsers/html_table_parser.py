from html.parser import HTMLParser

class HtmlTableParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.output = []
        self.row = None
        self.cell = None
        
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