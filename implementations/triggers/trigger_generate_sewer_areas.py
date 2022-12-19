from ... import interfaces
from ... import items

class TriggerGenerateSewerAreas(interfaces.Trigger):
    
    def is_only_mode_editor( self ):
        return True
    
    def is_only_mode_session( self ):
        return False
    
    def get_supported_types( self ):
        return 'EVENT'
    
    def get_description( self ):
        return '''<p>Checks whether Areas with a SEWER_STORAGE Attribute exist and, if not, run the Sewer Area Generation process.</p>
        
        <p>This allows for the automatic addition of default sewers in a Project, which is especially useful for automatic application of Templates for the creation of new Projects.</p>
        
        <p>This does generate Sewer Overflows by default, but can be configured to do so.</p>'''
    
    def get_documented_results( self ):
        return 'Sewer Areas generated automatically with default settings based on the urbanization of the neighborhoods present. If so configured, Sewer Overflows as well.'
    
    def get_documented_parameters( self ):
        return {
            'urbanization' : 'The minimum "URBANIZATION" value of Neighborhoods to generate Sewer Areas for. Default is 3.',
            'storage' : 'The storage in sewers, in mm. Default is 4',
            'storageBefore65' : 'The storage in sewers for neighborhoods from before 1965, in mm. If not provided, it defaults to the "storage" parameter\'s value. If that value is not provided either, uses a default value. Default is 0.7',
            'pumpCapacity' :  'The pump capacity for the Sewer Areas, dictating the rate at which water is pumped out of the sewers, in mm/hour Default is 0.7',
            'waterAreaAttribute' : 'The Attribute used to indicate Water Areas. When provided, allows for the creation of Sewer Overflows.'
            };
    
    def get_instructions_usage( self ):
        pass
    
    def get_usage_examples( self ):
        return {
            '&storage=5' : 'Will generate sewers, with each sewer having 5mm of storage capacity.',
            '&storage=5&storageBefore65=0.9' : 'Will generate sewers, with sewers from before 1965 having 0.9mm of storage, and other sewers having 5mm of storage.',
            '&urbanization=5' : 'Will generate sewers for all neighborhoods.',
            '&waterAreaAttribute=WATER_LEVEL' : 'Will generate Sewer Overflows in locations where Sewer Areas, Water Areas, and Water Terrains overlap.'
        }
    
    def run( self ):
        sdk = self.get_sdk()
        areas = sdk.session.items.load( 
            'areas',
            filter='SEWER_STORAGE'
        )

        if ( areas.count() > 0 ):
            return
        parameters = [
                self.get_parameter( 'urbanization', 3 ),
                float(self.get_parameter( 'storageBefore65', self.get_parameter( 'storage', 0.7 ) ))*0.001,
                float(self.get_parameter( 'storage', 4 ))*0.001,
                float(self.get_parameter( 'pumpCapacity', 0.7 ))*0.001,
                self.get_parameter( 'waterAreaAttribute','' )
            ]
        event = sdk.session.events.editorarea.generate_sewer_areas( *parameters )
        
        self.add_result( event.get_path(), event.get_arguments() )   
        
