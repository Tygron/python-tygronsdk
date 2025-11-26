import tygronsdk
from tygronsdk import sdk as tygron
from tygronsdk import items as items









from pathlib import Path

def main():

    project_to_run = 'demo_heat_stress'
    location_to_generate = { 
            "type" : "MultiPolygon", 
            "coordinates" : [ [ [
                [ 631709.4865742056, 6794503.059652832 ],
                [ 631939.5860401992, 6794559.541931026 ],
                [ 631884.7398267782, 6794747.284466415 ],
                [ 631664.9148912611, 6794695.795402652 ],
                [ 631709.4865742056, 6794503.059652832 ]
            ] ] ]
        }
    print('This example will start a project, generate a parametric design, and apply it.')

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
        
        
        design_id = sdk.session.parametric.create_parametric_design(example_type='SUBURBAN_NEIGHBORHOOD')
        print('Parametric design created with ID: ' + str(design_id))
        design_data = sdk.session.parametric.generate_design(design_id, location_to_generate)
        print('Parametric design generation has created the following design data: ' + str(design_data))
        measure_id = sdk.session.parametric.save_design_as_measure(design_id, design_data)
        measure = sdk.session.items.get(items.Measure, measure_id)
        print('A new Measure is created with ID: ' + str(measure_id) + ', with ' + str(len(measure.building_ids)) + ' Building(s)')
        
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
        