import unittest

import tygronsdk
from tygronsdk import sdk as tygron
from tygronsdk import items as items
from tygronsdk import utilities as utilities
from tygronsdk.src.environments.base.data import objects as objects

class test(unittest.TestCase):

    def setUp(self):
        self.credentials = tygronsdk.load_credentials_from_file( files=[
                './credentials.txt',
                './credentials.json'
            ], create_if_missing=False )
        self.sdk = tygron.sdk( self.credentials.keys() );
        auth_result = self.sdk.base.authenticate( {
            'username' : self.credentials.username,
            'password' : self.credentials.password,
        } )
        self.assertTrue(auth_result)
    
    def tearDown(self):
        self.sdk.configure_exit( {
                'save_project': False,
                'save_created_project': False,
                'close_session': True,
                'kill_session': True,
                'delete_created_project': True
            } )
        self.sdk.exit()
    
    def test_000_project(self):
        projects = self.sdk.base.projects.get_startable_projects()
        self.assertTrue( len(projects) > 0)
        
        project = projects[0]
        self.assertTrue( isinstance(project, objects.ProjectData) )
        self.assertEqual( project._data, self.sdk.base.projects.get_project( project_name=project.file_name)._data )
        
        self.assertIsNotNone( project.active_version )
        self.assertIsNotNone( project.description )
        self.assertIsNotNone( project.detailed )
        self.assertIsNotNone( project.disclaimer )
        self.assertIsNotNone( project.domain )
        self.assertIsNotNone( project.file_name )
        self.assertTrue( len(project.languages)>0 )
        self.assertIsNotNone( project.last_activity )
        self.assertIsNotNone( project.last_user )
        self.assertIsNotNone( project.owner )
        self.assertIsNotNone( project.permissions )
        self.assertNotEqual( project.permissions, ['NONE','NONE','NONE'] )
        self.assertIsNotNone( project.size )
        self.assertIsNotNone( project.sub_domain )
        self.assertTrue( len(project.version_map.keys()) > 0 )
        
    def test_010_project_creation_lifecycle(self):
        
        join_session_data = self.sdk.base.sessions.create_new_project_from_template(
                template_name='demo_heat_stress',
                new_project_name='py_unittest',
                attempts=1000
            )
        
        self.sdk.base.sessions.kill_project_session(**join_session_data)
        
        result = self.sdk.base.projects.delete_project(join_session_data['new_project_name'])
        self.assertTrue(result)
    
if __name__ == '__main__':
    unittest.main()