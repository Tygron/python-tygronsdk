import tygronsdk
from tygronsdk import sdk as tygron
from tygronsdk import items as items









from pathlib import Path
import json

def main():
        
    print('This is an example for an API trigger functions. This example does not include a full webservice but will demonstrate what the webservice has to do.')
    
    #First, data should be loaded. This will include command-line arguments, a data file with settings/configurations, and a credentials file
    print('The "init_data" call will load arguments from the command line, data from a data.json or data.txt file, and credentials from a credentials.json or credentials.txt file.')
    data = tygronsdk.init_data( credentials_create_if_missing=True )
    print('Created a '+str(data))
    
    
    
    if ( not ( data.get('server', None) or data.get('host', None) or data.get('platform', None) ) ):
        print('The SDK defaults to the LTS server.')
    
    origin = data.get('server', data.get('host', data.get('platform', 'engine.tygron.com (by default)')))
    api_token = data.get('api_token', None)
    print('Simulating a request from '+str( origin )+' (which would be read from the referrer header), with API token '+str(api_token)+' (which would be read from the query parameters)')
    
    
    
    #   The core of the SDK is an SDK object. Settings can be provided to configure it.
    sdk = tygron.sdk( data, computer_name='Python SDK Example' );


        
    #   The core of the SDK is an SDK object. Settings can be provided to configure it.
    print('Using the credentials set in the sdk, authentication can occur.' )
    auth_result = sdk.authenticate()
    print('The authentication result is: "'+str(auth_result)+'".')
    if ( not auth_result['session'] ):
        print('A running session\'s API token is required in order to interact with it.')
    
    print('The server now connected is: "'+sdk.session.connector.get_host()+'".')
        
    #   Next, obtain information regarding the session, and perform computations with that information as desired.
    calc_results = {
        'buildings' : 0,
        'active_stakeholder_buildings': 0,
        'active_stakeholder_buildings_planned' : 0
        }
        
    active_stakeholders = []

    #   To determine wbich Buildings belong to active Stakeholders, all Buildings and all Stakeholders must be obtained.
    stakeholders = sdk.session.items.load( items.Stakeholder )
    buildings = sdk.session.items.load( 'buildings' )

    for item in stakeholders :
        if ( item.active ):
            active_stakeholders.append(item.id)

    print('The following IDs correspond to stakeholders in the Session, for whom the buildings will be counted: '+ str(active_stakeholders))

    #   Next, check all Buildings and, depending on their matches, count them in a number of the result outputs.
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