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
        
        
    def test_000_session_simple_lifecycle(self):
        
        session_id = self.sdk.base.sessions.start_project_session(
                project_name='demo_heat_stress',
            )
        join_session_data = self.sdk.base.sessions.join_project_session(
                session_id=session_id,
            )
            
        result = self.sdk.base.sessions.close_project_session(**join_session_data)
        self.assertTrue(result)
    
    def test_001_session_keep_alive_lifecycle(self):
        session_id = self.sdk.base.sessions.start_project_session(
                project_name='demo_heat_stress',
            )
        
        session = self.sdk.base.sessions.get_joinable_session(session_id)
        self.assertIsNotNone( session)
        
        for mode in ['NEVER', 'SHORT', 'NEVER']:
            self.sdk.base.sessions.set_session_keep_alive(session_id, mode)
            self.assertEqual( mode, self.sdk.base.sessions.get_session_keep_alive(session_id) )

        self.sdk.base.sessions.kill_project_session(session_id)                
        
    
if __name__ == '__main__':
    unittest.main()