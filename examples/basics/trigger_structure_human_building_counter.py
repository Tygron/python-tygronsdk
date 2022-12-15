from ... import sdk as tygron
from ... import items as items

from pathlib import Path
import json

def main():

    if ( Path('credentials.py').is_file() ):
        import credentials
    else:
        print('Credentials can be defined in a credentials.py file in the root directory of where the example runs from. Should define tygron_server and tygron_api_token.')

    print('This is an example for an API trigger functions. This example does not include a full webservice but will demonstrate what the webservice has to do.')
    
    if ( not hasattr(credentials, 'tygron_api_token') ):
        print('A running session\'s API token is required in order to interact with it.')
    if ( not hasattr(credentials, 'tygron_server') ):
        print('It is not required to configure a server. The SDK defaults to the LTS server.')
        credentials.tygron_server = 'engine.tygron.com'
    
    print('Simulating a request from '+str(credentials.tygron_server)+' (which would be read from the referrer header), with API token '+str(credentials.tygron_api_token)+' (which would be read from the query parameters)')
    
    #   The core of the SDK is an SDK object. Settings can be provided to configure it.
    sdk = tygron.sdk({
             'host' : credentials.tygron_server
        })
    auth_result = sdk.session.authenticate({
            'api_token' : credentials.tygron_api_token
        })
    print('The authentication result is: "'+str(auth_result)+'".')
        
    #   Next, obtain information regarding the session, and perform computations with that information as desired
    calc_results = {
        'buildings' : 0,
        'active_stakeholder_buildings': 0,
        'active_stakeholder_buildings_planned' : 0
        }
        
    active_stakeholders = []

    stakeholders = sdk.session.items.load( items.Stakeholder )
    buildings = sdk.session.items.load( 'buildings' )

    for item in stakeholders :
        if ( item.active ):
            active_stakeholders.append(item.id)

    print('The following IDs correspond to stakeholders in the Session, for whom the buildings will be counted: '+ str(active_stakeholders))

    for  item in buildings  :
        calc_results['buildings'] += 1
        if (not (item.get('ownerID') in active_stakeholders )):
            continue
        calc_results['active_stakeholder_buildings'] += 1
        if ( not(item.get('state') in ['PENDING_CONSTRUCTION']) ):
            continue
        calc_results['active_stakeholder_buildings_planned'] += 1
    
    #   With the computation completed, we can set up a returnable object.
    returnable_results = {
        'UPDATE_GLOBAL_VALUE_WHERE_NAME_IS_COUNT_BUILDINGS' : calc_results['buildings'],
        'UPDATE_GLOBAL_VALUE_WHERE_NAME_IS_COUNT_BUILDINGS_HUMAN' : calc_results['active_stakeholder_buildings'],
        'UPDATE_GLOBAL_VALUE_WHERE_NAME_IS_COUNT_BUILDINGS_HUMAN_PLANNED' : calc_results['active_stakeholder_buildings_planned']
    }
    
    print('The following json can be responded to the original web call, and will effect changes in the session which reached out to the trigger:')
    print( json.dumps( returnable_results, indent=4 ) )
    

main()