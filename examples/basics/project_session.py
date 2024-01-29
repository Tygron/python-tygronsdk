import tygronsdk
from tygronsdk import sdk as tygron
from tygronsdk import items as items









from pathlib import Path

def main():

    project_to_run = 'demo_heat_stress'
    print('This example will attempt to start, read out details from, and gracefully close, a session for a specific project: "' + project_to_run + '".')

    #First, data should be loaded. This will include command-line arguments, a data file with settings/configurations, and a credentials file
    print('The "init_data" call will load arguments from the command line, data from a data.json or data.txt file, and credentials from a credentials.json or credentials.txt file.')
    data = tygronsdk.init_data( credentials_create_if_missing=True )
    print('Created a '+str(data))
    


    #   The core of the SDK is an SDK object. Settings can be provided to configure it.
    sdk = tygron.sdk( data, computer_name='Python SDK Example' );

    #   The API has multiple levels, which the SDK has seperate environments for.
    
    #   The base environment requires username-and-password authentication.
    print('Using the credentials set in the sdk, authentication can occur.' )
    auth_result = sdk.authenticate()  
             
    print('The authentication result is: "'+str(auth_result)+'".')
    if ( not auth_result['base'] ):
        print( 'Could not authenticate against the base API. This means the username and password are missing or incorrect.' )
        return
        
    print('The server now connected is: "'+sdk.base.connector.get_host()+'".')
    
    
    #   Good practice is to set up rules on what to do when the SDK exits, either through completion or through error.
    sdk.configure_exit( {
            'save_project': False,
            'save_created_project': False,
            'close_session': True,
            'kill_session': True,
            'delete_created_project': False
        } )
    
    try:
    
        #   First, obtain data about the Project. This verifies it exists, but is not required.
        project_data = sdk.base.projects.get_project( project_to_run )
        print('The Project\'s data is the following: ' + str(project_data) + '.')
        
        #   Next, we start a session of that Project. This returns a session_id.
        session_id = sdk.base.sessions.start_project_session( project_to_run )
        
        #   The session_id is added to the SDK's data, so it can be closed when the SDK exits.
        sdk.data = { 'session_id': session_id }
        
        #   Joining the session will provide details of the running session, and the API token neccesary to authenticate to the session environment.
        join_session_data = sdk.base.sessions.join_project_session( session_id )
        print('The Session\'s join data is the following: ' + str(join_session_data) + '.')
        
        sdk.data = {'api_token' : join_session_data['apiToken']}
        auth_result = sdk.authenticate()
        print('The authentication result is: "'+str(auth_result)+'".')
        
        
        #   Data from a session, known as Items, can be obtained either by providing a string of the desired Item type, or the relevant Item class.
        neighborhoods = sdk.session.items.load( 'neighborhoods' );
        stakeholders = sdk.session.items.load( items.Stakeholder );

        print( 'The following Neighborhoods are present: ' + str([item.name for item in neighborhoods]) )
        print( 'The following Stakeholders are active: ' + str([item.name for item in stakeholders if item.active]) )

        #   Meta-information about the datasets can be retrieved as well.
        buildings_size = sdk.session.items.size( 'buildings' );
        buildings_version = sdk.session.items.version( 'buildings' );

        print( 'There are ' + str( buildings_size ) + ' Buildings present in the Project\'s initial state' )
        print( 'The Building ItemMap is at version ' + str( buildings_version ) )

        
    except Exception as err:
        print('An error occured unexpectedly while running the example.')
        sdk.exit()
        raise err
        
    sdk.exit()
    
    #   After the SDK exits, the session will have been closed gracefully.
    #   Subsequent requests to the same session will cause exceptions.

    try:
        stakeholders = sdk.session.items.load( items.Stakeholder );
        print('If this line is reached, the session did not close down correctly.')
    except Exception as err:
        print('Could no longer retrieve data after exit. An erorr was thrown as a result of the call: '+str(err) )
        
        
main()
        