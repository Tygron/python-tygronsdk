import tygronsdk
from tygronsdk import sdk as tygron
from tygronsdk import items as items
from tygronsdk import utilities as utilities








from pathlib import Path

def main():

    try:
        credentials = tygronsdk.load_credentials_from_file( files=[
                './credentials.txt',
                './credentials.json'
            ], create_if_missing=True )
    except:
        print('Credentials must be provided, defining "username" and "password". Can either be a json object in "credentials.json", or key-value pairs in "credentials.txt".')
        return
   
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
    username = str(credentials.username)
    password = str(credentials.password)
    print('Authenticating base API environment as '+username)
    auth_result = sdk.base.authenticate( {
            'username' : username,
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
        
        print( '---' )
        
        license = sdk.base.domains.get_domain_license()
        usage = sdk.base.domains.get_domain_usage()
        allowance = sdk.base.domains.get_domain_allowance()
        
        print( license )
        print( usage )
        print( allowance )
        print( 'License name: ' + license.license )
        print( 'License enum: ' + license.license_enum )
        print( 'New projects per day allowed: ' + str(license.new_projects_per_day) )
        print( 'Total project area allowed: ' + str(license.max_total_area) )
        print( 'Geoshare storage usage allowed: ' + str(license.max_geoshare_storage) )
        print( 'New projects used today: ' + str(usage.new_projects_today) )
        print( 'New projects remaining today: ' + str(allowance.remaining_projects_today) )
        print( 'Percentage of new project allowance used today: ' + str(round( allowance.usage_fraction_projects_today*100)) + ' %' )
        
        
    except Exception as err:
        print('An error occured unexpectedly while running the example.')
        sdk.exit()
        raise err
        
    sdk.exit()
        
        
main()