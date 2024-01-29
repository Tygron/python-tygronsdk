import unittest

import tygronsdk
from tygronsdk.tests.generic.tygron_test import TygronTest
from tygronsdk import sdk as tygron
from tygronsdk import items as items
from tygronsdk import utilities as utilities

class test(TygronTest):

    def setUp(self):
       self.setUpExistingProject()
        
        
    def test_000_session_get_data(self):    
        self.assertTrue( self.sdk.session.items.load( items.Geolink     ).count() >0 )
        self.assertTrue( self.sdk.session.items.load( items.Geoplugin   ).count() >0 )
        self.assertTrue( self.sdk.session.items.load( items.GeoTiff     ).count() >0 )
        self.assertTrue( self.sdk.session.items.load( items.Indicator   ).count() >0 )
        self.assertTrue( self.sdk.session.items.load( items.Overlay     ).count() >0 )
        self.assertTrue( self.sdk.session.items.load( items.Panel       ).count() >0 )
        self.assertTrue( self.sdk.session.items.load( items.Stakeholder ).count() >0 )
    
    
if __name__ == '__main__':
    unittest.main()