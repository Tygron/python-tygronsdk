from .....utilities import datetimes

class ProjectData:
    
    def __init__( self, data:dict = {}, **kwargs ):
        self._data = { **data, **kwargs }
    
    def __str__(self):
        return '{file_name} ({universal}{template}Available languages: {languages})'.format(
                file_name       = self.file_name,
                universal       = 'Universal, ' if self.universal else '',
                template        = 'Template, ' if self.template else '',
                languages       = str(self.languages)
            )
    
    
    @property
    def active_version(self):
        return self._data.get( 'activeVersion', None )
        
    @property
    def delete_date(self):
        return self._data.get( 'deleteDate', None )
        
    @property
    def description(self):
        return self._data.get( 'description', None )
        
    @property
    def detailed(self):
        return self._data.get( 'detailed', True )
        
    @property
    def disclaimer(self):
        return self._data.get( 'disclaimer', None )
        
    @property
    def domain(self):
        return self._data.get( 'domain', None )
        
    @property
    def editing(self):
        return self._data.get( 'editing', False )
        
    @property
    def file_name(self):
        return self._data.get( 'fileName', None )
        
    @property
    def languages(self):
        return self._data.get( 'languages', [] )
        
    @property
    def last_activity(self):
        return datetimes.timestamp_to_datetime( self._data.get( 'lastActivity', None ) )
        
    @property
    def last_user(self):
        return self._data.get( 'lastUser', None )
        
    @property
    def owner(self):
        return self._data.get( 'owner', None )
        
    @property
    def permissions(self):
        return self._data.get( 'permissions', ['NONE','NONE','NONE'] )
        
    @property
    def restore_date(self):
        return datetimes.timestamp_to_datetime( self._data.get( 'restoreDate', None ) )
        
    @property
    def size(self):
        return self._data.get( 'size', None )
        
    @property
    def sub_domain(self):
        return self._data.get( 'subDomain', 'All Sub Domains' )
        
    @property
    def template(self):
        return self._data.get( 'template', False )
        
    @property
    def universal(self):
        return self._data.get( 'universal', False )
        
    @property
    def version_map(self):
        return self._data.get( 'versionMap', {} )
        
    @property
    def versions(self):
        return self._data.get( 'versions', [] )
    