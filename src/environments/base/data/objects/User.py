from .....utilities import datetimes

class User:
    
    def __init__( self, data:dict = {}, **kwargs ):
        self._data = { **data, **kwargs }
    
    def __str__(self):
        return '{user} ( {rights} : {domain} )'.format(
                user=self.user_name,
                rights=self.rights,
                domain=self.get_domain_as_string()
            )
    
    @property
    def user_name(self):
        return self._data.get( 'userName', None )
    
    @property
    def active(self):
        return self._data.get( 'active', False )
        
    @property
    def domain(self):
        return self._data.get( 'domain', None )
    @property
    def sub_domain(self):
        return self._data.get( 'subDomain', None )
        
    def is_root_domain_user(self):
        return self.sub_domain == 'All Sub Domains'
    def get_domain_as_string(self):
        if ( self.is_root_domain_user() ):
            return self.domain
        return '{}, {}'.format(self.domain, self.sub_domain)    
    
    
    @property
    def max_option(self):
        return self._data.get( 'maxOption', None )
    @property
    def rights(self):
        return self.max_option
    
    @property
    def first_name(self):
        return self._data.get( 'firstName', None )
    @property
    def last_name(self):
        return self._data.get( 'lastName', None )
    @property
    def nick_name(self):
        return self._data.get( 'nickName', None )
    @property
    def phone(self):
        return self._data.get( 'phone', '' )
    def get_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
    def has_phone(self):
        return not (self.phone == '' or self.phone == 'PLEASE DONT CALL ME')
    
    @property
    def last_login(self):
        return datetimes.timestamp_to_datetime( self._data.get( 'lastLogin', None ) )
    @property
    def macs(self):
        return self._data.get( 'macs', [] )
    @property
    def recent_projects(self):
        return self._data.get( 'recentProjects', [] )
    
    @property
    def invote_token(self):
        return self._data.get( 'inviteToken', None )
    
    
    
    
    
    
    
    