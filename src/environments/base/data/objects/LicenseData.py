from ..... import utilities

class LicenseData:
    
    def __init__( self, data:dict = {}, variables:dict={}, **kwargs ):
        lowercase_data = {k.lower(): v for k, v in { **data, **kwargs }.items()}
        uppercase_variables = {k.upper(): v for k, v in variables.items()}
        self._data = lowercase_data
        self._variables = uppercase_variables
        
        self.key_mapping = {
                'license': [None, 'type lts license'],
                'new_projects_per_day': ['MAX_NEW_PROJECTS', 'new projects per day'],
                'max_project_area': ['MAX_PROJECT_DIM_M', 'max project area (km2)'],
                'max_total_area': ['MAX_AREA_KM2', 'total area (km2)'],
                'max_geoshare_storage': ['MAX_SHARE_MB','geoshare storage'],
                'price': ['PRICE_EUR', 'price per year (ex. vat)'],
                'users': ['MAX_USERS', 'users'],
                
                'min_cell_size': ['MIN,CELL,CM','min cell size (cm)'],
                'min_project_cells': ['MIN_PROJECT_CELLS', 'min project cells'],
                'max_project_cells': ['MAX_PROJECT_CELLS', 'max project cells'],
                'max_project_versions': ['MAX_PROJECT_VERSIONS', 'max project versions'],
                
                'allow_basic': ['ALLOW_BASIC','basic mode'],
                'allow_long_keepalive': ['ALLOW_LONG_KEEPALIVE','long keep-alive'],
                'allow_preview': ['ALLOW_PREVIEW','access to preview'],
                'allow_subdomains': ['ALLOW_SUBDOMAINS','subdomains'],
                
                'support': ['SUPPORT','support']
            }
        self.support_mapping = ['community', 'premium', 'advanced']
    
    def create_custom_license( self, variables:dict={} ):
        license = LicenseData( self._data, {**self._variables, **variables} )
        return license
    
    def __str__(self):
        return '{license} ( {new_projects} new projects, at most {max_size} km2, totalling {total_size} km2 )'.format(
                license=self.license,
                new_projects=self.max_projects_per_day,
                max_size=self.max_project_area,
                total_size=self.max_total_area
            )
    
    def get_license_value(self, key:str = '', base_only:bool = False, override_only = False):
        variable_term = 0
        table_term = 1
        value = None
        if ( not base_only ):
            value = self._variables.get( self.key_mapping[key][variable_term], None )
        if ( value is None and (not override_only) ):
            value = self._data.get( self.key_mapping[key][table_term], None )
        return value
          
    @property
    def license_variables(self):
        return self._variables
        
    @property
    def license(self):
        return self.get_license_value( 'license' )
    @property
    def license_enum(self):
      return utilities.tygron_strings.make_enum_term( self.license )
    
    @property
    def new_projects_per_day(self):
        value = self.get_license_value('new_projects_per_day')
        return int(utilities.strings.strip_to_number(value))
    @property
    def max_projects_per_day(self):
        return self.new_projects_per_day
    
    @property
    def max_project_area(self):
        value = self.get_max_project_area_extent()
        return int( utilities.strings.parse_surface_area_from_sizes_string(value) )
    def get_max_project_area_extent(self):
        term = 'max_project_area'
        value = self.get_license_value(term, override_only=True)
        if ( not (value is None) ):
            return '{} x {}'.format(value/1000,value/1000)
        return self.get_license_value(term, base_only=True)
    
    @property
    def max_total_area(self):
        value = self.get_license_value('max_total_area')
        return int( utilities.strings.strip_to_number(value) )
        
    @property
    def max_users(self):
        value = self.get_license_value('users')
        return int( utilities.strings.strip_to_number(value) )
    
    @property
    def max_geoshare_storage(self):
        value = self.get_max_geoshare_storage_string()
        return int( utilities.strings.parse_file_size_string(value) )
    def get_max_geoshare_storage_string(self):
        term = 'max_geoshare_storage'
        value = self.get_license_value(term, override_only=True)
        if ( (value is None) ):
            value = self.get_license_value(term, base_only=True)
        else:
            value = str(value) + ' MB'
        return value
    
    @property
    def price(self):
        value = utilities.strings.strip_to_number( self.get_price_string() )
        return 0 if ( value == '' ) else int(value)
    def get_price_string(self):
        term = 'price'
        value = self.get_license_value(term, override_only=True)
        if ( (value is None) ):
            value = self.get_license_value(term, base_only=True)
        else:
            value = '€ '+str(value)+',-'
        return value
    def get_price_in_euro_or_free(self):
        value = self.price
        return 'free' if (value == 0) else value
    def get_price_conditions_apply(self):
        return self.get_price_string.lower().find('conditions apply')>=0
    
    @property
    def min_cell_size(self):
        value = self.get_license_value('min_cell_size')
        return int(value)
    @property
    def min_project_cells(self):
        value = self.get_license_value('min_project_cells')
        return int(utilities.strings.strip_to_number(value))
    @property
    def max_project_cells(self):
        value = self.get_license_value('max_project_cells')
        return int(utilities.strings.strip_to_number(value))
    @property
    def max_project_versions(self):
        value = self.get_license_value('max_project_versions')
        return int(value)

    @property
    def allow_basic(self):
        value = self.get_license_value('allow_basic')
        return (value == 1) or (value.lower() == 'yes')
    @property
    def allow_long_keepalive(self):
        value = self.get_license_value('allow_long_keepalive')
        return (value == 1) or (value.lower() == 'yes')
    @property
    def allow_preview(self):
        value = self.get_license_value('allow_preview')
        return (value == 1) or (value.lower() == 'yes')
    @property
    def allow_subdomains(self):
        value = self.get_license_value('allow_subdomains')
        return (value == 1) or (value.lower() == 'yes')
    def get_allows_string(self):
        values = []
        if (self.allow_basic): values.append('basic mode')
        if (self.allow_long_keepalive): values.append('long keepalive')
        if (self.allow_preview): values.append('preview')
        if (self.allow_subdomains): values.append('subdomains')
        return '' if len(values) == 0 else ', '.join(values)
    
    @property
    def support_level(self):
        value = self.get_license_value('support')
        if ( value in self.support_mapping ):
            value = self.support_mapping.index(value)
        return value
    def get_support_string(self):
        value = self.get_license_value('support')
        try:
            value = self.support_mapping[value]
        except:
            pass
        return value
    def premium_support(self):
        return self.support_level > self.support_mapping.index('premium')
    def advanced_support(self):
        return self.support_level > self.support_mapping.index('advanced')