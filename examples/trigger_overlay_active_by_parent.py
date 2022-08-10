from .. import interfaces
from .. import items

import json
import base64
import re

class TriggerOverlayActiveByParent(interfaces.Trigger):
    
    def is_only_mode_editor( self ):
        return True
    def is_only_mode_session( self ):
        return False
    def get_supported_types( self ):
        return 'EVENT'
    
    def get_description( self ):
        return '''<p>Checks Grid Overlays which are the children of parent Overlays, and ensures that the children of active Overlays are active and the children of inactive parents are inactive.</p>
        
        <p>Overlays which are not children of other Overlays are not affected. Overlays which are formal RESULT_CHILD Overlays of complex calculation models are not affected. Overlays which are not Grid Overlays or are not the child Overlays of Grid Overlays are not affected.</p>'''
    
    def get_documented_results( self ):
        return 'Child overlays will be set to active or inactive based on the state of the parents.'   
    def get_documented_parameters( self ):
        return {
            'overlays' : 'An id or a list of ids of Overlays. Overlays will only be set to active or inactive if either their id or the id of their parent are provided. When this parameter is absent, all overlays are checked.'
            };
    def get_instructions_usage( self ):
        pass
    def get_usage_examples( self ):
        return {
            '&overlays=5' : 'Will only change the state of the overlay with id 5, or of the children of the overlay with id 5.',
            '&overlays=[4,5,6]' : 'Will only change the state of overlays which are either themselves the overlays with id 4, 5, or 6, or of the overlays which are children of the overlays with ids 4, 5, or 6',
        }
            
    def run( self ):
        conn_session = self.get_session_connection()

        # Get all buildings with a specified attribute
        # Ensure buildings in timestate NOTHING are included
        # Ensure buildings in measures are included

        # Get all Overlays
        # Get list of affectable Overlays
        # Loop through all Overlays
        # If Overlay has a parent
        # If the parent overlay is in list, or if child is in list, or if list is empty:
            # If child overlay is result child, or does not have an active property, or parent does not have active property
                # Continue
            # If child.active != parent.active
                # Add operation to output

        nonce_counter = 0
        
        affected_overlays = self.get_parameter( 'overlays', None )
        if ( not isinstance(affected_overlays, list) and affected_overlays is not None ):
            affected_overlays = [affected_overlays]
        
        
        overlays = conn_session.request(
                url='items/overlays'
            ).get_response_body_json()
        overlays = items.ItemMap( overlays, False )

        
        for child_overlay in overlays:
            try:
                overlay_child_id = child_overlay['id']
                overlay_parent_id = child_overlay['parentID']
                
                print( 'Checking '+str(overlay_child_id)+', part of '+str(overlay_parent_id) )
                
                if ( overlay_parent_id == items.Item.NONE ):
                    print( str(overlay_child_id)+' does not have a parent overlay')
                    continue
                if ( affected_overlays is not None ):
                    if ( not ( 
                            overlay_child_id in affected_overlays or
                            overlay_parent_id in affected_overlays or
                            str(overlay_child_id) in affected_overlays or
                            str(overlay_parent_id) in affected_overlays
                        ) ):
                        print( str(overlay_child_id)+' and '+str(overlay_parent_id)+' are not listed as affected' )
                        continue
                        
                parent_overlay = overlays.get( child_overlay['parentID'] )
                
                if ( not ('active' in parent_overlay) ):
                    print( str(overlay_parent_id)+' does not have an active state')
                    continue
                if ( not ('active' in child_overlay) ):
                    print( str(overlay_child_id)+' does not have an active state')
                    continue
                    
                if ( ('type' in child_overlay) and child_overlay['type'] == 'RESULT_CHILD' ):
                    print( str(overlay_child_id)+' is a RESULT_CHILD, which is set automatically')
                    continue
                    
                if ( parent_overlay['active'] is not child_overlay['active'] ):
                    print( str(overlay_child_id)+' does not match, and should be set to the state of '+str(overlay_parent_id) )
                    nonce_counter += 1
                    self.add_result( 'editoroverlay/set_grid_active/nonce'+ str(nonce_counter), [
                        overlay_child_id, parent_overlay['active']
                    ])
            except Exception as e:
                raise e

