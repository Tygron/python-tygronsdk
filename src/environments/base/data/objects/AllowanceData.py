from ..... import utilities
from .LicenseData import LicenseData
from .UsageData import UsageData

from typing import Union

class AllowanceData:
    
    def __init__( self, license:Union[dict,LicenseData], usage:Union[list,UsageData], **kwargs ):
        license = license if isinstance(license, LicenseData) else LicenseData(license)
        usage = usage if isinstance(usage, UsageData) else UsageData(usage)
        
        self._data = {
            license: None,
            usage: None,
            **kwargs
        }
        self._license = license
        self._usage = usage
    
    def __str__(self):
        return 'New projects: {used_new}/{max_new} ({fraction_new}%) used, Area: {used_area}/{max_area} km2 ({fraction_area}%) used, Geoshare: {used_geoshare}/{max_geoshare} ({fraction_geoshare}%) used. Max project size: {max_project_size} km2'.format(
 
                used_new=self._usage.new_projects_today,
                max_new=self._license.new_projects_per_day,
                fraction_new=round(self.usage_fraction_projects_today*100,0),
                
                used_area=self._usage.domain_total_area,
                max_area=self._license.max_total_area,
                fraction_area=round(self.usage_fraction_total_area*100,0),
                
                used_geoshare=self._usage.geoshare_usage,
                max_geoshare=self._license.max_geoshare_storage,
                fraction_geoshare=round(self.usage_fraction_geoshare_data*100,0),
                
                max_project_size=round(self.get_max_project_area_available(),0)
            )
            
    @property
    def license(self):
        return self._license
    @property
    def usage(self):
        return self._usage

    
    @property
    def remaining_projects_today(self):
        return self._license.new_projects_per_day- self._usage.new_projects_today
        
    @property
    def usage_fraction_projects_today(self):
        if ( self._license.new_projects_per_day == 0 ):
            return 1
        return self._usage.new_projects_today / self._license.new_projects_per_day
    
    
    @property
    def remaining_total_area(self):
        #TODO: add subdomain calculation
        return self._license.max_total_area - self._usage.domain_total_area
    
    @property
    def usage_fraction_total_area(self):
        if ( self._license.max_total_area == 0 ):
            return 1
        return self._usage.domain_total_area / self._license.max_total_area
    
    
    @property
    def remaining_geoshare_data(self):
        return self._license.max_geoshare_storage - self._usage.geoshare_usage
    
    @property
    def usage_fraction_geoshare_data(self):
        if ( self._license.max_geoshare_storage == 0 ):
            return 1
        return self._usage.geoshare_usage / self._license.max_geoshare_storage
    
    
    
    def get_max_project_area_available(self):
        domain_total_remaining = self.remaining_total_area
        subdomain_total_remaining = domain_total_remaining #TODO: Subdomain check
        domain_allowed_project_size = self._license.max_project_area
        subdomain_allowed_project_size = domain_allowed_project_size #TODO: Subdomain check
        
        return min(
                domain_total_remaining,
                subdomain_total_remaining,
                domain_allowed_project_size,
                subdomain_allowed_project_size
            )
    
    def get_fraction_max_project_area_available(self):
        domain_allowed_project_size = self._license.max_project_area
        domain_or_subdomain_allowed_project_size = domain_allowed_project_size #TODO: Subdomain check
        if ( domain_or_subdomain_allowed_project_size == 0 ):
            return 0
        return self.max_project_area_available / domain_or_subdomain_allowed_project_size
        