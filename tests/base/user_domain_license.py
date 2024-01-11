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

    def test_000_base_authenticate(self):
        auth_result = self.sdk.base.authenticate( {
            'username' : self.credentials.username,
            'password' : self.credentials.password,
        } )
        self.assertTrue(auth_result)

    def test_010_my_user(self):
        user = self.sdk.base.users.get_my_user()
        self.assertIsNotNone(user.user_name)
        self.assertTrue(user.active)
        self.assertIsNotNone(user.domain)
        self.assertIsNotNone(user.sub_domain)
        self.assertIsNotNone(user.rights)
        self.assertIsNotNone(user.first_name)
        self.assertIsNotNone(user.last_name)
        self.assertIsNotNone(user.nick_name)
        self.assertNotEqual(user.phone, '')
        self.assertIsNotNone(user.last_login)
      
    def test_011_my_domain(self):
        domain = self.sdk.base.domains.get_domain()
        self.assertIsNotNone(domain.id)
        self.assertIsNotNone(domain.name)
        
        self.assertIsNotNone(domain.license)
        
        self.assertIsNotNone(domain.login_key_expiration)
        self.assertIsNotNone(domain.min_password_length)
        self.assertIsNotNone(domain.two_factor_level)
        
        self.assertIsNotNone(domain.address)
        self.assertIsNotNone(domain.city)
        self.assertIsNotNone(domain.zip_code)
        self.assertIsNotNone(domain.country)
        
        self.assertIsNotNone(domain.organisation)
        
        self.assertIsNotNone(domain.contact_email)
        self.assertIsNotNone(domain.contact_first_name)
        self.assertIsNotNone(domain.contact_last_name)
        self.assertIsNotNone(domain.contact_phone)
        
        self.assertIsNotNone(domain.license_number)
        
        self.assertIsNotNone(domain.creation_date)
        self.assertIsNotNone(domain.expire_date)
        
        self.assertIsNotNone(domain.state)
        
    def test_012_my_license(self):
        license = self.sdk.base.domains.get_domain_license()
        
        self.assertIsNotNone(license.license)
        self.assertIsNotNone(license.license_enum)
        self.assertIsNotNone(license.max_projects_per_day)
        self.assertTrue( isinstance(license.max_projects_per_day, int) )
        self.assertTrue( isinstance(license.max_project_area, int) )
        self.assertTrue( isinstance(license.max_total_area, int) )
        self.assertTrue( isinstance(license.max_users, int) )
        self.assertTrue( isinstance(license.max_geoshare_storage, int) )
        self.assertTrue( isinstance(license.price, int) )
        self.assertTrue( isinstance(license.min_cell_size, int) )
        self.assertTrue( isinstance(license.min_project_cells, int) )
        self.assertTrue( isinstance(license.max_project_cells, int) )
        self.assertTrue( isinstance(license.max_project_versions, int) )
        
        self.assertTrue( license.max_projects_per_day > 0 )
        self.assertTrue( license.max_project_area > 0 )
        self.assertTrue( license.max_total_area > 0 )
        self.assertTrue( license.max_users > 0 )
        self.assertTrue( license.max_geoshare_storage > 0 )
        self.assertTrue( license.price > 0 )
        self.assertTrue( license.min_cell_size > 0 )
        self.assertTrue( license.min_project_cells > 0 )
        self.assertTrue( license.max_project_cells > 0 )
        self.assertTrue( license.max_project_versions > 0 )
    
    
if __name__ == '__main__':
    unittest.main()