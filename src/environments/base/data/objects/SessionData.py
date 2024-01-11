class SessionData:
    
    def __init__( self, data:dict = {}, **kwargs ):
        self._data = { **data, **kwargs }
    
    def __str__(self):
        return '{id} : {project_name} ({session_type} {language})'.format(
                id              = self.id,
                project_name    = self.project_name,
                session_type    = self.session_type,
                language        = self.language
            )
    
    @property
    def id(self):
        return self._data.get( 'id', None )
    @property
    def session_id(self):
        return self.id
    @property
    def name(self):
        return self._data.get( 'name', None )
    @property
    def project_name(self):
        return self.name
    @property
    def session_type(self):
        return self._data.get( 'sessionType', None )
    @property
    def language(self):
        return self._data.get( 'language', None )
    @property
    def map_size(self):
        return self._data.get( 'mapSizeM', None )
    
    @property
    def detailed(self):
        return self._data.get( 'detailed', True )
    @property
    def wizard_finished(self):
        return self._data.get( 'wizardFinished', False )
    @property
    def app_type(self):
        return self._data.get( 'appType', None )
    
    @property
    def group_token(self):
        return self._data.get( 'groupToken', None )
    @property
    def token_pair(self):
        return self._data.get( 'tokenPair', None )
        
    @property
    def timeout_ms(self):
        return self._data.get( 'timeoutMS', None )