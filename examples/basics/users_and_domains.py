from ... import sdk as tygron
from ... import items as items

from ... import utilities as utilities

from pathlib import Path

def main():

    if ( Path('credentials.py').is_file() ):
        import credentials;
    else:
        print('Credentials can be defined in a credentials.py file in the root directory of where the example runs from. Should define tygron_username and tygron_password.');
    
    print('This example will read out details about the current user, about the domain, and explore a number of operations associated with them.')

    #   The core of the SDK is an SDK object. Settings can be provided to configure it.
    sdk = tygron.sdk( {
            'platform' : 'engine',
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
    
        print( '---' )
    
        user = sdk.base.users.get_my_user()
        print( user )
        print( 'Name: ' + user.get_name() )
        print( 'Username: ' + user.user_name )
        print( 'Has a phone number been registered: ' + ('yes' if user.has_phone() else 'no') )
        print( 'Most recent login: ' + utilities.datetimes.datetime_to_string_datetime(user.last_login) )

        print( '---' )

        domain = sdk.base.users.get_my_domain()
        print( domain )
        print( 'Organization: ' + domain.organisation )
        print( 'Domain: ' + domain.name )
        print( 'Domain contact: ' + domain.get_contact_name() )
        print( 'License number: ' + domain.license_number )
        print( 'License expires on: ' + utilities.datetimes.datetime_to_string_date(domain.expire_date) )
        
    except Exception as err:
        print('An error occured unexpectedly while running the example.')
        sdk.exit()
        raise err
        
    sdk.exit()
        
        
main()