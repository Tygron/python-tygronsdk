import unittest

import tygronsdk
from tygronsdk.tests.generic.tygron_test import TygronTest




class test(TygronTest):

    def setUp(self):
       self.setUpExistingProject()
        
        
    def test_000_session_recalculate(self):    
        self.sdk.session.calculation.recalculate_direct(False)
    
    def test_001_session_recalculate_x(self):    
        self.sdk.session.calculation.recalculate_direct(True)
    
    def test_002_session_recalculate_scheduled(self):    
        self.sdk.session.calculation.recalculate_scheduled()
    
if __name__ == '__main__':
    unittest.main()