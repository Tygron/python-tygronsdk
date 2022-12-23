from ... import sdk as tygron
from ... import items as items

from pathlib import Path

def main():

    if ( Path('credentials.py').is_file() ):
        import credentials;
    else:
        print('Credentials can be defined in a credentials.py file in the root directory of where the example runs from. Should define tygron_username and tygron_password.');
    
    project_to_run = 'demo_heat_stress'
    
    print('This example will attempt to start, read out details from, and gracefully close, a session for a specific project: "' + project_to_run + '".')

    #   The core of the SDK is an SDK object. Settings can be provided to configure it.
    sdk = tygron.sdk( {
            'platform' : 'preview',
            'computer_name' : 'Python SDK Example',
        } );

    #   Good practice is to set up rules on what to do when the SDK exits, either through completion or through error.
    sdk.configure_exit( {
            'save_project': False,
            'save_created_project': False,
            'close_session': True,
            'kill_session': True,
            'delete_created_project': False
        } )

    #   The API has multiple levels, which the SDK has seperate environments for.
    #   Each environment may require its own authentication, which must be explicitly set, and is separate from the SDK's settings.
    
    #   The base environment requires username-and-password authentication.
    username = str(credentials.tygron_username)
    password =  str(credentials.tygron_password)
    print('Authenticating base API environment as '+username)
    auth_result = sdk.base.authenticate( {
            'username' :username,
            'password' : password,
        } )  
             
    print('The authentication result is: "'+str(auth_result)+'".')
    
    try:
    
        #   First, obtain data about the Project. This verifies it exists, but is not required.
        project_data = sdk.base.projects.get_project( project_to_run )
        print('The Project\'s data is the following: ' + str(project_data) + '.')
        
        #   Next, we start a session of that Project. This returns a session_id.
        session_id = sdk.base.sessions.start_project_session( project_to_run )
        
        #   The session_id is added to the SDK's settings, so it can be closed when the SDK exits.
        sdk.settings = { 'session_id': session_id }
        
        #   Joining the session will provide details of the running session, and the API token neccesary to authenticate to the session environment.
        join_session_data = sdk.base.sessions.join_project_session( session_id )
        print('The Session\'s join data is the following: ' + str(join_session_data) + '.')
        auth_result = sdk.session.authenticate( {
                'api_token' :join_session_data['apiToken'],
            } )  
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
    except Exception as err:
        print('Could no longer retrieve data after exit. An erorr was thrown as a result of the call: '+str(err) )
        
        
main()
        