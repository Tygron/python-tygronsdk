import unittest

import tygronsdk
from tygronsdk import utilities as utilities

from tygronsdk.tests.generic.tygron_test import TygronTest
import tygronsdk.dev.scripts.events as dev_script

import difflib

class test(TygronTest):

    def test_000_events(self):
        script = dev_script.Script()
        script.set_print_log_function(None)
        
        settings = self.load_settings().data( data=True, credentials=True)
        settings['credentials'] = settings.get('credentials_dev',settings.get('credentials',None))
        settings['existing_types_only'] = True
        settings['assume_unchanged_parameters'] = False
        settings['output_directory'] = 'test_output'
        settings['verbose'] = settings.get('verbose', False)
        
        result_files=script.run( **settings )
        
        matches = []
        differences = []
        for file in result_files:
            file_generated = file
            file_sdk = file.replace( settings['output_directory'], 'tygronsdk' )
        
            lines = difflib.unified_diff(
                    utilities.files.read_file_as_text(file_sdk).splitlines(),
                    utilities.files.read_file_as_text(file_generated).splitlines(), 
                    fromfile='sdk',
                    tofile='generated',
                    lineterm=''
                )
            lines = list(lines)
            if (len(lines)>0):
                differences.append( 'Difference in file: ' + file_generated + '   :   ' + str(len(lines) ) )
                if (settings['verbose']):
                    differences.append('\n'.join(lines))
        
        self.assertEqual(len(differences), 0, msg=utilities.strings.create_multiline_string(differences))
           
if __name__ == '__main__':
    unittest.main()