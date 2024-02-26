from ... import interfaces
from ... import items
from ... import utilities

class TriggerSetFloors(interfaces.Trigger):
    
    def is_only_mode_editor( self ):
        return True
    def is_only_mode_session( self ):
        return False
    def get_supported_types( self ):
        return 'EVENT'
    
    def get_description( self ):
        return '''<p>
        Checks all Buildings in a Project, and sets all Sections of all Buildings found to the FLOORS Attribute of that Building. Removes the FLOORS attribute afterwards to prevent rechecking.</p>
        </p><p>
        Also checks all Buildings of Measures, if any of the Buildings of a Measure has a FLOORS Attribute.
        <p>'''
    
    def get_documented_results( self ):
        return 'All Buildings with a FLOORS Attribute attached directly will have their min and max floors, and the floors of their Sections, set to that exact value. The FLOORS Attribute will be removed.'   
    def get_documented_parameters( self ):
        return {
            'attribute' : 'The Attribute to search for. Default is '+str(self.default_attribute())+'.',
        };
    def get_instructions_usage( self ):
        pass
    def get_usage_examples( self ):
        return None
    
    def default_attribute( self ):
        return 'FLOORS'
    
    def floors_valid_value( self, floors ):
        return ( (floors > 0) and (floors == int(floors)) )
    
    def run( self ):
        conn_session = self.get_session_connection()
        sdk = self.get_sdk()

        attribute = self.get_parameter( 'attribute', self.default_attribute() )

        buildings = sdk.session.items.load( items.Building, attribute )
        measures = sdk.session.items.load( items.Measure, attribute )
       
        measure_buildings = []
        for measure in measures:
            for measure_building_id in measure.building_ids:
                measure_building = sdk.session.items.get( items.Building, measure_building_id )
                if ( measure_building is None ):
                    continue
                if ( measure_building.get_attribute_value( attribute, default_zero=False ) is None ):
                    continue
                measure_buildings.append( measure_building )
        buildings.set_data(measure_buildings)
        
        print( [str(building.id)+': '+str(building.name) for building in buildings] )
        
        attribute_building_ids = []
        attribute_names = []
        attribute_values = []
        
        section_building_ids = []
        section_section_ids = []
        section_floors = []
        
        
        removal_building_ids = []
        removal_names = []
        
        for building in buildings:
            floors = building.get_attribute_value( attribute, first_only = True )
            if ( not self.floors_valid_value( floors ) ):
                continue
                
            attribute_building_ids.extend( [building.id, building.id] )
            attribute_names.extend( ['MIN_FLOORS', 'MAX_FLOORS'] )
            attribute_values.extend( [floors, floors] )
            
            for section in building.sections:
                section_building_ids.append( building.id )
                section_section_ids.append( section.get('id',None) )
                section_floors.append(floors)
              
            removal_building_ids.append( building.id )  
            removal_names.append( attribute )  
            
        if ( len(section_building_ids) == 0 ):
            return
        
        attributes_event = sdk.session.events.editorbuilding.set_attributes( attribute_building_ids, attribute_names, attribute_values )
        section_floors_event = sdk.session.events.editorbuilding.set_floors( section_building_ids, section_section_ids, section_floors )
        remove_attribute_event = sdk.session.events.editorbuilding.remove_attribute( removal_building_ids, removal_names )
        
        self.add_result( attributes_event.get_path(), attributes_event.get_arguments() )
        self.add_result( section_floors_event.get_path(), section_floors_event.get_arguments() )
        self.add_result( remove_attribute_event.get_path(), remove_attribute_event.get_arguments() )
        
        return
