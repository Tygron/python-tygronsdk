from ... import interfaces
from ... import items
from ... import utilities

import json

class TriggerImplementationHumanBuildingCounter(interfaces.Trigger):
    
    def get_description( self ):
        return '''
                This Trigger will count the amount of Buildings in a Session.
                It will count the total amount, the ones belonging to active Stakeholders, and the ones planned by active Stakeholders.
            '''
    def get_documented_results( self ):
        return '''
                The following Globals will be created/updated through TQL statements:
                COUNT_BUILDINGS
                COUNT_BUILDINGS_ACTIVE
                COUNT_BUILDINGS_ACTIVE_PLANNED
            '''
            
    def run( self ):

        try:
            print( 'This is an example for how to create an API trigger. This example does not include a full webservice but will demonstrate what the webservice has to do.' )
            
            print( 'This example derives from a generic "Trigger" interface, which receives a host and api token, readies a connector, and then calls "run" in this implementation class.' )
            
            sdk = self.get_sdk()
            connector = sdk.session.connector
            
            print ( 'The connector is created with the following settings, allowing communication: ')
            print( 'Host: '+connector.get_host() )
            print( 'Api token: '+connector.get_api_token() )

            print( 'The connector will facilitate all calls to '+connector.get_url_full() )
            
            print( 'Next, we can obtain some information, and perform computations with that information as desired')
            
            calc_results = {
                'buildings' : 0,
                'buildings_active': 0,
                'buildings_active_planned' : 0
                }
            playable_stakeholders = []

            stakeholders = sdk.session.items.load( items.Stakeholder )

            for stakeholder in stakeholders :
                if ( stakeholder.active ):
                    playable_stakeholders.append( stakeholder.id )

            print ( 'The following buildings correspond to human stakeholders in the project ' + str(playable_stakeholders) )
            
            buildings = sdk.session.items.load( 'buildings' )

            for  building in buildings  :
                calc_results['buildings'] += 1
                if (not (building.get('ownerID',-1) in playable_stakeholders )):
                    continue
                calc_results['buildings_active'] += 1
                if ( not(building.get('state', 'NONE') in ['PENDING_CONSTRUCTION']) ):
                    continue
                calc_results['buildings_active_planned'] += 1
            
            print( 'With the computation completed, we can set up a returnable object.' )
            returnable_results = {
                'UPDATE_GLOBAL_VALUE_WHERE_NAME_IS_COUNT_BUILDINGS' : calc_results['buildings'],
                'UPDATE_GLOBAL_VALUE_WHERE_NAME_IS_COUNT_BUILDINGS_ACTIVE' : calc_results['buildings_active'],
                'UPDATE_GLOBAL_VALUE_WHERE_NAME_IS_COUNT_BUILDINGS_ACTIVE_PLANNED' : calc_results['buildings_active_planned']
            }
            
            self.add_results( returnable_results )
            
            print( 'This completes the trigger\'s internal work.' )
            
        except Exception as err:
            #   The trigger interface will, in principle, swallow errors silently. However, it will also store it as part of the results.
            print( utilities.exceptions.stringify(err) )
            raise err
