import unittest

import tygronsdk
from tygronsdk import sdk as tygron
from tygronsdk import items as items
from tygronsdk import utilities as utilities

class TygronTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TygronTest, self).__init__(*args, **kwargs)    
    
        self.new_project_name = 'py_unittest'
        self.existing_project_name = 'demo_heat_stress'
    
    def load_settings(self, *args, **kwargs):
        self.data = tygronsdk.init.init_data(*args, **kwargs)
        return self.data
    
    def setUp(self):
        self.data = self.load_settings()
        self.sdk = tygron.sdk( self.data )

        auth_result = self.sdk.authenticate()['base']
        self.assertTrue(auth_result)
    
    def setUpExistingProject(self, project_name:str = None):
        project_name = project_name or self.existing_project_name
        TygronTest.setUp(self);
        session_id = self.sdk.base.sessions.start_project_session(
                project_name=project_name,
            )
        join_session_data = self.sdk.base.sessions.join_project_session(
                session_id=session_id,
            )
        self.sdk.data = join_session_data
        auth_result = self.sdk.authenticate()['session']
        self.assertTrue(auth_result)
    
    def setUpNewProject(self, project_name:str = None):
        TygronTest.setUp(self);
        join_session_data = None;
        if ( project_name is None):
            join_session_data = self.sdk.base.sessions.create_new_project(
                new_project_name=self.new_project_name
            )
        else:
            join_session_data = self.sdk.base.sessions.create_new_project_from_template(
                project_name,
                self.new_project_name,
                attempts=1000
            )
            
        self.sdk.data = join_session_data
        
        auth_result = self.sdk.authenticate()['session']
        self.assertTrue(auth_result)
    
    def tearDown(self):
        self.sdk.configure_exit( {
                'save_project': False,
                'save_created_project': False,
                'close_session': False,
                'kill_session': True,
                'delete_created_project': True
            } )
        try:
            self.sdk.exit()
        except Exception as err:
            raise Exception(utilities.exceptions.stringify(err))