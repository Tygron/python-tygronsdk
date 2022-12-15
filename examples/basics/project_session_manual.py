from ... import items as items
Item = items.Item
ItemMap = items.ItemMap

from ... import events as tygron_events
from ... import environments as tygron_environments
ConnectorBaseApi = tygron_environments.base.Connector
ConnectorSessionApi = tygron_environments.session.Connector

from pathlib import Path


def main():

    if ( Path('credentials.py').is_file() ):
        import credentials;
    else:
        print( 'Credentials can be defined in a credentials.py file in the root directory of where the example runs from. Should define tygron_username and tygron_password.' );
    
    project_to_run = 'demo_heat_stress'
    
    print( 'This example will attempt to start, read out details from, and gracefully close, a session for a specific project: "' + project_to_run + '".' )
    print( 'Although it is recommended to use the "sdk" object and its interactions where possible, this example will do so through using the lower-level SDK components' )

    connection_settings = {
            'platform' : 'engine',
            'computer_name' : 'Python SDK Example',
        }

    #   The API has multiple levels, which the SDK has seperate environments for.
    #   Each environment also includes a specialized collection of low-level components for that specific level of the API.

    #   Get the connector for interacting with the base API
    connector_base_api = ConnectorBaseApi(connection_settings);
    #   Get a connector for interaction with the session API, as soon as it's set up
    connector_session_api = ConnectorSessionApi(connection_settings);
    
    
    #   Establish a session_id scoped such that it can be set by the running script, but also by any cleanup functionality
    session_id = None
    #   Do the same with the client_token, again so that during cleanup the client_token can be used to detach tidely
    client_token = None
    #   If an error occurs while running the example, store it so we can rethrow it after cleanup
    critical_error = None
    
    try:
    
        #   The base API requires authentication for http-basic authentication using a username and password
        username = str(credentials.tygron_username)
        password =  str(credentials.tygron_password)
        
        print( 'Authenticating base API environment as '+username )
        connector_base_api.set_http_basic_authentication( username, password )    
        success = connector_base_api.authenticate()
    
    
    
        #   First, obtain data about the Project. This verifies it exists, but is not required.
        event = tygron_events.io.get_project_data( project_name = project_to_run )
        print( 'Prepared an event to interact with the server: ' + str(event) )
        
        project_data_response = connector_base_api.fire_event(event)
        print( 'The response holds the Project\'s data, and is the following: ' + str(project_data_response) )
        
        #   Next, start the Project Session.
        event = tygron_events.io.start( project_name = project_to_run )
        print( 'Prepared an event to interact with the server: ' + str(event) )
        
        session_id_response = connector_base_api.fire_event(event)
        print( 'The response holds the newly started Session\'s sessionID, and is the following: ' + str(session_id_response) )
        
        #   Finally, join the Session.
        session_id = session_id_response.get_response_body_json()
        event = tygron_events.io.join( session_id = session_id, computer_name = connection_settings['computer_name'] )
        print( 'Prepared an event to interact with the server: ' + str(event) )
        
        join_response = connector_base_api.fire_event(event)
        print( 'The response holds information regarding the connection to the session, and is the following: ' + str(join_response) )
        api_token = join_response.get_response_body_json()['apiToken']
        client_token = join_response.get_response_body_json()['client']['clientToken']
        print( 'The vital part of the response if the api token, which is the following: '+api_token )
        print( 'Another important piece of information was the client token, which is the following: '+client_token )
        
        
        
        
        
        
        #   The session API requires authentication in the form of an API token
        print( 'Authenticating session API environment with token '+api_token )
        connector_session_api.set_api_token( api_token )    
        success = connector_session_api.authenticate()
        
        
        
        #   We can get data, called Items, from the session
        neighborhoods_response = connector_session_api.request(
                method='GET',
                url='items/neighborhoods' 
            )
        stakeholders_response = connector_session_api.request(
                method='GET',
                url='items/'+str( Item.maplink_from( items.Stakeholder ) )
            )
        neighborhoods = neighborhoods_response.get_response_body_json()
        stakeholders = stakeholders_response.get_response_body_json()

        print( 'The following Neighborhoods are present: ' + str([ item.get('name','Unknown') for item in neighborhoods ]) )
        print( 'The following Stakeholders are active: ' + str([ item.get('name','Unknown') for item in stakeholders if item.get('active',False) ]) )  
        
        #   Data can also be directly loaded into ItemMaps for easier access. The specific item type can be defined as well.
        stakeholders_item_map = items.ItemMap(stakeholders, as_item=items.Stakeholder)
        print( 'The size of a map is determined by the highest id, for bookkeeping purposes, and for stakeholders is: '+ str(stakeholders_item_map.size()) )
        print( 'The count of a map, conversly, is the number of items currently present, and for stakeholders is: '+ str(stakeholders_item_map.count()) )
        
        
        
    except Exception as err:
        #   If any error occurs, try and capture it, but still allow for any desired cleanup to occur
        print( 'An error occured. This was not supposed to happen.' )
        critical_error = err
        
    finally:
    
        #   After the script has concluded, either through completion or an unexpected or unrecoverable error, any sessions started should be closed.
        if ( not(session_id == None) ):
            event = tygron_events.io.close( session_id = session_id, client_token = client_token )
            print ( 'Prepared an event to interact with the server: ' + str(event) )
            
            close_response = connector_base_api.fire_event(event)
            print( 'The response indicates whether detaching the client succeeded or not: ' + str(close_response) )
        
    
    
    if ( not (critical_error is None) ):
        raise critical_error    
        
        
        
    try:
        neighborhoods_response = connector_session_api.request(
                method='GET',
                url='items/'+str( items.Item.maplink_from( items.Stakeholder ) )
            )
    except Exception as err:
        print( 'After closing the session, further calls to the session will fail. An erorr was thrown as a result of the call: '+str(err) )
    
main()