import unittest

import tygronsdk
from tygronsdk.tests.generic.tygron_test import TygronTest
from tygronsdk import sdk as tygron
from tygronsdk import items as items
from tygronsdk import utilities as utilities
from tygronsdk.src.environments.base.data import objects as objects

class test(TygronTest):
    
    def test_000_maintenance_window(self):
        maintenance_window = self.sdk.base.platform.get_maintenance_window()
        
        self.assertIsNotNone(maintenance_window)
        self.assertIsNotNone(maintenance_window.start_in_seconds)
        self.assertIsNotNone(maintenance_window.end_in_seconds)
    
if __name__ == '__main__':
    unittest.main()