from ..... import utilities

class UsageData:
    
    def __init__( self, data = {}, **kwargs ):
        if ( isinstance(data,list) ):
            data = {
                'new_projects_today': int(data[0]),
                'total_projects_saved': int(data[1]),
                'domain_total_area': int(data[2]),
                'subdomain_total_area': int(data[3]),
                'geoshare_usage': int(data[4])
            }
        self._data = { **data, **kwargs }
    
    def __str__(self):
        return '{new_project_count} new project(s), {total_domain_area} km2 across all projects, {geoshare_usage} MB used on geoshare'.format(
                new_project_count=self.new_projects_today,
                total_domain_area=self.domain_total_area,
                geoshare_usage=self.geoshare_usage
            )
            
    @property
    def new_projects_today(self):
        return self._data.get('new_projects_today')

    @property
    def total_projects_saved(self):
        return self._data.get('total_projects_saved')
        
    @property
    def domain_total_area(self):
        return self._data.get('domain_total_area')
        
    @property
    def subdomain_total_area(self):
        return self._data.get('subdomain_total_area')
        
    @property
    def geoshare_usage(self):
        return self._data.get('geoshare_usage')