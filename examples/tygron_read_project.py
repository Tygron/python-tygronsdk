from .. import sdk as tygron

from pathlib import Path

def main():

    try:

        if ( Path('credentials.py').is_file() ):
            import credentials;
        else:
            raise Exception('For the sake of this example, Credentials can be defined in a credentials.py file in the root. Should define tygron_username and tygron_password. (Consider alternative ways to provide credentials in production environments.)');


        print('Creating an API connector via the SDK');
        
        sdk = tygron.sdk( {
                'platform' : 'engine',
                'username' : str(credentials.tygron_username),
                'password' : str(credentials.tygron_password)
        
            } );
        conn_api = sdk.create_connector_api();
        conn_api.set_exception_on_error();
        print( 'This connector will connect to the root API at: '+conn_api.get_url_full() );
        
        
        
        print( 'First see if we can authenticate succesfully. Who is your user? ' );
        response = conn_api.request( 
                method='GET',
                url='myuser'
            );
        
        user = response.get_response_body_json();
        print(user);
        
        
        
        template_project = 'climategame_5_2';
        print('Next, can you see the intended project? ('+template_project+')');
        response = conn_api.request( 
                method='POST', 
                url='event/io/get_domain_startable_templates',
                data=[user['domain']]
            );
        
        found_project = False;
        for entry in response.get_response_body_json():
            if ( entry['fileName'] == template_project ):
                found_project = True;
                break;
        if ( not found_project ):
            raise Exception( 'The project ('+template_project+') does not exist' );
        
        
        
        print('We found it. We can now start that project, in EDITOR mode.');
        response = conn_api.request( 
                method='POST',
                url='event/io/start', 
                data=['EDITOR', template_project]
            );
        session_id = response.get_response_body();
        
        print('The project was started with session id '+session_id);
        
        
        
        print('We will now join the project, as an EDITOR client.');
        response = conn_api.request(
                method='POST',
                url='event/io/join', 
                data=[session_id, 'EDITOR']
            );
        session_data = response.get_response_body_json();
        print(session_data);
        
        
        print('We use the obtained API token and client token to create a new connector to connect to the session specifically');
        conn_session = sdk.create_connector_session(session_data);
        conn_session.set_exception_on_error();
        print( 'This connector will connect to the session API at: '+conn_session.get_url_full() );
        
        
        
        print('Print some details about the contents of the project')
        stakeholders_items = conn_session.request(
                method='GET',
                url='items/stakeholders'
            ).get_response_body_json()
        neighborhoods_items = conn_session.request(
                method='GET',
                url='items/neighborhoods'
            ).get_response_body_json()
        buildings_count = conn_session.request(
                method='GET',
                url='items/buildings/size'
            ).get_response_body_json()
        
        print( 'The following neighborhoods are present: ' + str([item.get('name') for item in neighborhoods_items]) )
        print( 'The following stakeholders are "human" actors: '+ str([item.get('name') for item in stakeholders_items if item.get('human')]) )
        print( 'There are ' + str(buildings_count) + ' constructions present in the project\'s initial state' )
        
        
        
        print( 'We are now done in the project, so we can close it.' )
        response = conn_api.request(
                method='POST',
                url='event/io/close', 
                data=[session_id, conn_session.get_client_token(), False]
            );
        
        print( 'Done!' )
        
        
        
    except Exception as e:
        print('Something went wrong!');
        for value in e.args:
            print(value);
        exit();
main()