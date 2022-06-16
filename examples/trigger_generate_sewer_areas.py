from .. import interfaces
from .. import items

import json
import base64
import re

class TriggerGenerateSewerAreas(interfaces.Trigger):
    
    def is_only_mode_editor( self ):
        return True
    
    def is_only_mode_session( self ):
        return False
    
    def get_supported_types( self ):
        return 'EVENT'
    
    def get_description( self ):
        return '''<p>Checks whether Areas with a SEWER_STORAGE Attribute exist and, if not, run the Sewer Area Generation process.</p>
        
        <p>This allows for the automatic addition of default sewers in a project, which is especially useful for automatic application of Templates for the creation of new Projects.</p>
        
        <p>This does <em>not</em> generate Sewer Overflows.</p>'''
    
    def get_documented_results( self ):
        return 'Sewer Areas generated automatically with default settings based on the urbanization of the neighborhoods present.'
    
    def get_documented_parameters( self ):
        return {
            'urbanization' : 'The minimum "URBANIZATION" value of Neighborhoods to generate Sewer Areas for. Default is 3.',
            'storage' : 'The storage in sewers, in mm. Default is 4',
            'storageBefore65' : 'The storage in sewers for neighborhoods from before 1965, in mm. If not provided, it defaults to the "storage" parameter\'s value. If that value is not provided either, uses a default value. Default is 0.7',
            'pumpCapacity' :  'The pump capacity for the sewer areas, dictating the rate at which water is pumped out of the sewers, in mm/hour Default is 0.7'
            };
    
    def get_instructions_usage( self ):
        pass
    
    def get_usage_examples( self ):
        return {
            '&storage=5' : 'Will generate sewers, with each sewer having 5mm of storage capacity.',
            '&storage=5&storageBefore65=0.9' : 'Will generate sewers, with sewers from before 1965 having 0.9mm of storage, and other sewers having 5mm of storage.',
            '&urbanization=5' : 'Will generate sewers for all neighborhoods.',
        }
    
    def run( self ):
        conn_session = self.get_session_connection()
        
        sewer_areas = conn_session.request(
                url='items/areas-sewer_storage'
            ).get_response_body_json()        
        
        if len(sewer_areas) > 0:
            return
            
        parameters = [
                self.get_parameter( 'urbanization', 3 ),
                float(self.get_parameter( 'storageBefore65', self.get_parameter( 'storage', 0.7 ) ))*0.001,
                float(self.get_parameter( 'storage', 4 ))*0.001,
                float(self.get_parameter( 'pumpCapacity', 0.7 ))*0.001,
                self.get_trigger_name()
            ]
         
        self.add_result( 'editorarea/generate_sewer_areas', parameters)   
        
