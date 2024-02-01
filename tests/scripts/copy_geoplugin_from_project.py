import unittest

import tygronsdk
from tygronsdk import items
from tygronsdk import utilities

from tygronsdk.tests.generic.tygron_test import TygronTest
import tygronsdk.examples.scripts.copy_geoplugin_from_project as example_script

class test(TygronTest):

    def test_000_copy_by_token(self):
        script = example_script.Script()
        
        self.setUpExistingProject()
        api_token = self.sdk.session.connector.get_api_token()
        
        self.inner_test(
            origin_platform = 'engine',
            target_session_token = api_token
        )

    def test_001_copy_by_session_id(self):
        script = example_script.Script()
        
        self.setUpExistingProject()
        api_token = self.sdk.session.connector.get_api_token()
        session_id = self.sdk.data.get('session_id', None)
        
        self.inner_test(
            origin_platform = 'engine',
            target_session_id = session_id
        )

    def test_002_copy_by_token_custom_name(self):
        script = example_script.Script()
        
        self.setUpExistingProject()
        api_token = self.sdk.session.connector.get_api_token()
        name = 'Custom name'
        
        self.inner_test(
            origin_platform = 'engine',
            target_session_token = api_token,
            name=name,
            target_geoplugin_name=name
        )

    def inner_test(self, name:str='NLCS', **kwargs):
        script = example_script.Script()
        script.set_print_log_function(None)
        
        geoplugins = self.sdk.session.items.load(items.Geoplugin)
        geoplugins_start_count = geoplugins.count()

        try:
            script.start(
                **kwargs
            )
        except Exception as err:
            raise Exception(utilities.exceptions.stringify(err))
        
        geoplugins = self.sdk.session.items.load(items.Geoplugin)
        newest_geoplugin = geoplugins.get(geoplugins.size()-1)
        
        self.assertTrue(geoplugins.count() > geoplugins_start_count, msg='No Geoplugin added')
        self.assertTrue(name in newest_geoplugin.name, msg='Incorrect Geoplugin name')
        self.assertTrue(len(newest_geoplugin.geolink_ids)>0, msg='No geolinks')
           
if __name__ == '__main__':
    unittest.main()