from .. import interfaces

import json

class TriggerHumanBuildingCounter(interfaces.Trigger):
    
    def run( self ):

        print( 'This is an example for how to an API trigger. This example does not include a full webservice but will demonstrate what the webservice has to do.' )
        
        print( 'This example derives from a generic "Trigger" interface, which receives a host and api token, readies a connector, and then calls "run" in this implementation class.' )
        
        print( 'Set up a few assumptions first: A request is made, originating from the Tygron Platform. This request always includes the following information, which you should parse from the request:' )
        print( 'Host: '+self.get_session_connection().get_host() )
        print( 'Api token: '+self.get_session_connection().get_api_token() )
        
        print( 'With these parameters, the Trigger interface has readied a connector.')
        
        conn_session = self.get_session_connection()
        
        print( 'The connector will facilitate all calls to '+conn_session.get_url_full() )
        
        print( 'Next, we can obtain some information, and perform computations with that information as desired')
        
        calc_results = {
            'buildings' : 0,
            'human_buildings': 0,
            'human_buildings_planned' : 0
            }
        playable_stakeholders = []

        stakeholders_items = conn_session.request(
                method='GET',
                url='items/stakeholders'
            ).get_response_body_json()
        for item in stakeholders_items :
            if ( item.get('human',False) ):
                playable_stakeholders.append(item.get('id'))

        print ( 'The following buildings correspond to human stakeholders in the project ' + str(playable_stakeholders) )
        
        buildings_items = conn_session.request(
                method='GET',
                url='items/buildings'
            ).get_response_body_json()

        for  item in buildings_items  :
            calc_results['buildings'] += 1
            if (not (item.get('ownerID',-1) in playable_stakeholders )):
                continue
            calc_results['human_buildings'] += 1
            if ( not(item.get('state', 'NONE') in ['PENDING_CONSTRUCTION']) ):
                continue
            calc_results['human_buildings_planned'] += 1
        
        print( 'With the computation completed, we can set up a returnable object.' )
        returnable_results = {
            'UPDATE_GLOBAL_VALUE_WHERE_NAME_IS_COUNT_BUILDINGS' : calc_results['buildings'],
            'UPDATE_GLOBAL_VALUE_WHERE_NAME_IS_COUNT_BUILDINGS_HUMAN' : calc_results['human_buildings'],
            'UPDATE_GLOBAL_VALUE_WHERE_NAME_IS_COUNT_BUILDINGS_HUMAN_PLANNED' : calc_results['human_buildings_planned']
        }
        
        self.add_results( returnable_results )
        
        print( 'This completes the trigger\'s internal work.' )
        
