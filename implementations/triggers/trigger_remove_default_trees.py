from ... import interfaces
from ... import items
from ... import utilities

class TriggerRemoveDefaultTrees(interfaces.Trigger):
    
    def is_only_mode_editor( self ):
        return True
    def is_only_mode_session( self ):
        return False
    def get_supported_types( self ):
        return 'EVENT'
    
    def get_description( self ):
        return '''<p>
        Checks which trees have been automatically generated, and remove them from the Project. This prepares the Project for automatically adding custom tree datasets.</p>
        <p>'''
    
    def get_documented_results( self ):
        return 'Trees, the only source of which is a default source, are removed from the project.'   
    def get_documented_parameters( self ):
        return {
            'functions' : 'A list of the function ids of all functions considered trees. Default is '+str(self.default_function_ids())+'.'
        };
    def get_instructions_usage( self ):
        pass
    def get_usage_examples( self ):
        return None;
    
    def default_function_ids( self ):
        return [
                440,
                888,
                937,
                950,
                951,
                952,
                953,
                954,
            ]
    
    def run( self ):
        conn_session = self.get_session_connection()
        sdk = self.get_sdk()

        buildings = sdk.session.items.load( items.Building )

        # Get all buildings of the nature category
        # Check the function and source of all buildings
        # Add the ID of each affected, default building to a list
        # Create building removal event with those IDs
        
        functions = self.get_parameter( 'functions', self.default_function_ids() )
        functions = utilities.lists.coerce(functions)
        trees_to_remove = []
        
        for building in buildings:
            if ( (building.function_id in functions) and all(i < items.Item.CUSTOM_ID_START for i in building.source_ids) ):
                trees_to_remove.append(building.id)

        event = sdk.session.events.editorbuilding.remove( trees_to_remove )
        self.add_result( event.get_path(), event.get_arguments() )

