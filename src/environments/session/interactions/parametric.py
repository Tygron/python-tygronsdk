from ....core.interactions.interaction_set import InteractionSet

from ..connectors import Connector
from ..data import events, objects, items

from .items import Items
from .... import utilities

class Parametric:

    @staticmethod
    def create_parametric_design( conn:Connector, design_type = None, example_type = None ):
        if (design_type is None) and (example_type is None):
            design_type = 'ROAD'
        
        versioned_events = InteractionSet.versioned(conn, events)
            
        response = None
        if example_type:
            response = conn.fire_event( 
                versioned_events.editorparametric.add_example (
                    example_type
                ) )
        elif design_type:
            response = conn.fire_event( 
                versioned_events.editorparametric.add (
                    design_type
                ) )
        
        return response.get_response_body_json()
        
    def generate_design( conn:Connector, design_id:int, multipolygon = None ):
        versioned_events = InteractionSet.versioned(conn, events)
        
        response = conn.fire_event( 
            versioned_events.editorparametric.set_polygons (
                design_id,
                multipolygon
            ) )
        response = conn.fire_event( 
            versioned_events.editorparametric.generate (
                design_id
            ) )
            
        design_data = objects.ParametricDesignData(response.get_response_body_json())
        return design_data
    
    def save_design_as_measure( conn:Connector, design_id:int, design:objects.ParametricDesignData, stakeholder_id:int = None):
        versioned_events = InteractionSet.versioned(conn, events)
        
        stakeholders = Items.load(conn, items.Stakeholder).get_data()
        if stakeholder_id is None:
            stakeholder_id =  next(iter(stakeholders))
        
        event = versioned_events.editorparametric.save_as_measure (
                design_id,
                stakeholder_id,
                design.get_function_types(),
                design.get_plot_types(),
                design.get_plot_polygons()
            )
        
        response = conn.request(
                method='POST',
                url='event/'+event.get_path(),
                query_params={ 'crs' : 'LOCAL' },
                data=event.get_arguments(),
            )
            
        return response.get_response_body_json()
        
        
        