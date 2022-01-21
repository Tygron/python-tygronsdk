from .. import sdk as tygron

import json

def main():

    print('This is an example for how to create/run an API trigger. This example does not include a full webservice but will demonstrate what the webservice has to do.')
    
    query_parameter_apitoken = query_parameter_apitoken or None
    if (not query_parameter_apitoken):
        print('Also note that this example won\'t run, unless a real "query_parameter_apitoken" is provided.')
    
    print('Set up a few assumptions first: A request is made, originating from the Tygron Platform. This request always includes the following information, which you should parse from the request:')
    
    header_referer = 'engine.tygron.com'
    print('Referer (sic) header : ' + header_referer )
    
    query_parameter_apitoken = query_parameter_apitoken or '[Some token]'
    print('Api token is '+query_parameter_apitoken)
    
    print('We can then set up a connection to the session which made the request')
    sdk = tygron.sdk({
             'host' : header_referer
        } );
    conn_session = sdk.create_connector_session()
    conn_session.set_api_token( query_parameter_apitoken )
    
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

    print ('The following buildings correspond to human stakeholders in the project ' + str(playable_stakeholders) )
    
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
    
    print('With the computation completed, we can set up a returnable object.')
    returnable_results = {
        'UPDATE_GLOBAL_VALUE_WHERE_NAME_IS_COUNT_BUILDINGS' : calc_results['buildings'],
        'UPDATE_GLOBAL_VALUE_WHERE_NAME_IS_COUNT_BUILDINGS_HUMAN' : calc_results['human_buildings'],
        'UPDATE_GLOBAL_VALUE_WHERE_NAME_IS_COUNT_BUILDINGS_HUMAN_PLANNED' : calc_results['human_buildings_planned']
    }
    
    print('The following json can be responded to the original web call, and will effect changes in the session which reached out to the trigger:')
    print( json.dumps( returnable_results, indent=4 ) );
    

main()