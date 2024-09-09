import tygronsdk
from tygronsdk import sdk as tygron
from tygronsdk import items as items
from tygronsdk import utilities as utilities








from pathlib import Path

def main():

    print('This example print some server version information.')

    #First, data should be loaded. This will include command-line arguments, a data file with settings/configurations, and a credentials file
    print('The "init_data" call will load arguments from the command line, data from a data.json or data.txt file, and credentials from a credentials.json or credentials.txt file.')
    data = tygronsdk.init_data( credentials_create_if_missing=True )
    print('Created a '+str(data))


    #   The core of the SDK is an SDK object. Settings can be provided to configure it.
    sdk = tygron.sdk( data, computer_name='Python SDK Example' );

    #   To check the server version, no authentication is required
        
    print('The server now connected is: "'+sdk.base.connector.get_host()+'".')
    
    print('The server version is: "'+sdk.platform_version()+'".')
    
    print('The internal module version is: "'+sdk.module_version()+'".')
        
    sdk.exit()
        
        
main()