from ..... import utilities

class LicenseData:
    
    def __init__( self, data:dict = {}, **kwargs ):
        lowercase_data = {k.lower(): v for k, v in { **data, **kwargs }.items()}
        self._data = lowercase_data
        
        self.key_mapping = {
                'license': 'type lts license',
                'new_projects_per_day': 'new projects per day',
                'max_project_area': 'max project area (km2)',
                'max_total_area': 'total area (km2)',
                'max_geoshare_storage': 'geoshare storage',
                'price': 'price per year (ex. vat)'
            }
    
    def __str__(self):
        return '{license} ( {new_projects} new projects, at most {max_size} km2, totalling {total_size} km2 )'.format(
                license=self.license,
                new_projects=self.max_projects_per_day,
                max_size=self.max_project_area,
                total_size=self.max_total_area
            )
    
    @property
    def license(self):
        return self._data.get( self.key_mapping['license'] , None )
    @property
    def license_enum(self):
        return utilities.tygron_strings.make_enum_term( self.license )
    
    @property
    def new_projects_per_day(self):
        value = self._data.get( self.key_mapping['new_projects_per_day'], None )
        return int(utilities.strings.strip_to_number(value))
    @property
    def max_projects_per_day(self):
        return self.new_projects_per_day
    
    @property
    def max_project_area(self):
        value = self.get_max_project_area_extent()
        return int( utilities.strings.parse_surface_area_from_sizes_string(value) )
    def get_max_project_area_extent(self):
        return self._data.get( self.key_mapping['max_project_area'], None )
    
    @property
    def max_total_area(self):
        value = self._data.get( self.key_mapping['max_total_area'], None )
        return int( utilities.strings.strip_to_number(value) )
    
    @property
    def max_geoshare_storage(self):
        value = self.get_max_geoshare_storage_string()
        return int( utilities.strings.parse_file_size_string(value) )
    def get_max_geoshare_storage_string(self):
        return self._data.get( self.key_mapping['max_geoshare_storage'], None )
    
    @property
    def price(self):
        return self._data.get( self.key_mapping['price'], None )
    def get_price_in_euro(self):
        value = utilities.strings.strip_to_number(self.price )
        return 0 if ( value == '' ) else int(value)
    def get_price_in_euro_or_free(self):
        value = self.get_price_in_euro()
        return 'free' if (value == 0) else value
    def get_price_conditions_apply(self):
        return self.price.lower().find('conditions apply')>=0
    
    
