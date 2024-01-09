from .....utilities import datetimes

class DomainData:
    
    def __init__( self, data:dict = {}, **kwargs ):
        self._data = { **data, **kwargs }
    
    def __str__(self):
        return '{domain} ( {license} )'.format(
                domain=self.name,
                license=self.get_license_as_string()
            )
        pass
    
    
    @property
    def id(self):
        return self._data.get( 'id', None )
    @property
    def name(self):
        return self._data.get( 'name', None )
        
        
    @property
    def license(self):
        return self._data.get( 'license', None )
    @property
    def license_variables(self):
        return self._data.get( 'licenseVariables', None )
    @property
    def partnership(self):
        return self._data.get( 'partnership', None )
    def is_partner(self):
        return self.partnership not in [None, "NONE"]
    def get_license_as_string(self):
        if ( not self.is_partner() ):
            return self.license
        return '{}, {}'.format(self.license, self.partnership)
    
    
    @property
    def save_areas(self):
        return self._data.get( 'saveAreas', {} )
        
    def get_save_areas_total(self):
        return 
    @property
    def saves(self):
        return self._data.get( 'saves', {} )
    @property
    def share_storages(self):
        return self._data.get( 'shareStorages', {} )
    
    
    @property
    def sub_domain_map(self):
        return self._data.get( 'subDomainMap', {} )
    
    
    
    
    @property
    def login_key_expiration(self):
        return self._data.get( 'loginKeyExpiration', None )
    @property
    def min_password_length(self):
        return self._data.get( 'minPasswdLength', None )
    @property
    def min_password_length(self):
        return self._data.get( 'twoFactorLevel', None )
    
    
    
    
    @property
    def address(self):
        return self._data.get( 'address', None )
    @property
    def city(self):
        return self._data.get( 'city', None )
    @property
    def zip_code(self):
        return self._data.get( 'zipCode', None )
    @property
    def country(self):
        return self._data.get( 'country', None )
    
    
    @property
    def organisation(self):
        return self._data.get( 'organisation', None )
    @property
    def industry(self):
        return self._data.get( 'industry', None )
    
    
    
    
    @property
    def contact_email(self):
        return self._data.get( 'contactEmail', None )
    @property
    def contact_first_name(self):
        return self._data.get( 'contactFirstname', None )
    @property
    def contact_last_name(self):
        return self._data.get( 'contactLastname', None )
    @property
    def contact_phone(self):
        return self._data.get( 'contactPhone', None )
    def get_contact_name(self):
        return '{} {}'.format(self.contact_first_name, self.contact_last_name)
    
    
    
    
    @property
    def license_number(self):
        return self._data.get( 'licenseNumber', None )
    
    
    
    
    @property
    def creation_date(self):
        return datetimes.timestamp_to_datetime( self._data.get( 'creationDate', None ) )
    @property
    def expire_date(self):
        return datetimes.timestamp_to_datetime( self._data.get( 'expireDate', None ) )
    
    
    
    
    @property
    def activation_code(self):
        return self._data.get( 'activationCode', None )
    @property
    def state(self):
        return self._data.get( 'state', None )
    @property
    def routing_map(self):
        return self._data.get( 'routingMap', {} )
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    