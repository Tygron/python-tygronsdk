import unittest

import tygronsdk
from tygronsdk.tests.generic.tygron_test import TygronTest
from tygronsdk import sdk as tygron
from tygronsdk import items as items
from tygronsdk import utilities as utilities

class test(TygronTest):

    def setUp(self):
        super().setUpNewProject()
        
    def test_000_session_create_project(self):    
        self.sdk.session.creation.generate_map(
            size_x=1000,
            size_y=1000,
            location_x=480923.54,
            location_y=6816089.27
        )
        self.assertTrue( self.sdk.session.items.load('buildings').count()>0 )
    
    
if __name__ == '__main__':
    unittest.main()