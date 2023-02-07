from ... import interfaces
from ... import items
from ... import utilities

import json

class TriggerImplementationGeotiffFromGeoshareViaStream(interfaces.Trigger):
    
    def get_description( self ):
        return '''
                This Trigger will check whether there are GeoTiffs in a Session, and whether those GeoTiffs are used by GeoTiff Overlays.
                If that is the case, this Trigger will stream data from the GeoShare to the GeoTiff in the Session.
            '''
    def get_documented_results( self ):
        return '''
                The Trigger will not return any TQL statements or Events, but will operate on the Session directly.
            '''
    
    def run( self ):
    
        try:
            print( 'This is an example for how to create an API trigger. This example does not include a full webservice but will demonstrate what the webservice has to do.' )
            print( 'This example derives from a generic "Trigger" interface, which receives a host and api token, readies a connector, and then calls "run" in this implementation class.' )
            
            sdk = self.get_sdk()
            connector = sdk.session.connector
            
            print ( 'The connector is created with the following settings, allowing communication: ')
            print( 'Host: '+connector.get_host() )
            print( 'Api token: '+connector.get_api_token() )

            print( 'The connector will facilitate all calls to '+connector.get_url_full() )
            
            print( 'Next, we can obtain some information, and perform computations with that information as desired')
            
            overlays = sdk.session.items.load( items.Overlay )
            geotiffs = sdk.session.items.load ( 'geotiffs' )
            
            print( 'We can check per Overlay whether it uses a GeoTiff, and whether it requires an update' )
            for overlay in overlays:
                if overlay.get('type', None) != 'GEO_TIFF':
                    continue
                    
                print( 'Checking GeoTiff Overlay ' + str(overlay.name) + ' ('+str(overlay.id)+')' )
                for tiff_index, tiff_id in enumerate( overlay.get('geoTiffIDs',[]) ):
                    value = connector.run_query( 'SELECT_GRIDVOLUME_WHERE_GRID_IS_'+ str(overlay.id)+'_AND_TIMEFRAME_IS_'+str(tiff_index) ).get_response_body()
                    print( 'GeoTiff Overlay ' + geotiffs.get(tiff_id).get('name','(No name)') + ' has a volume value of ' + str(value) )
                    
                    #It's possible to check whether the GeoTiff warrents updating based on its volume value, but for the example all are updated
                    tiff = geotiffs.get(tiff_id)
                    if ( tiff == None ):
                        print( 'No Tiff was found with id '+str(tiff_id) )
                        continue
                    
                    #Check whether a parameter was provided indicating from which url the geotiff should be updated
                    asset_name = str(tiff.name)
                    geoshare_path = self.determine_geoshare_path( asset_name, tiff_id )
                    if ( geoshare_path == None ):
                        print( 'GeoTiff ' + asset_name + '('+str(tiff_id)+')'
                                + ' can be updated by adding the following parameter'
                                + 'to the call of the trigger (escaped if neccesary): '
                                + json.dumps({asset_name: 'public/path/on/the/share'})
                            )
                        continue
                    
                    print( 'GeoTiff ' + asset_name + ' ('+str(tiff_id)+')' + ' can be updated with data from : ' + str(geoshare_path) )    
                    self.import_geotiff_from_geoshare( geoshare_path, tiff_id, asset_name )

            print( 'This completes the trigger\'s internal work.' )

        except Exception as err:
            #   The trigger interface will, in principle, swallow errors silently. However, it will also store it as part of the results.
            print( utilities.exceptions.stringify(err) )
            raise err
            
            
            
    def determine_geoshare_path( self, tiff_name, tiff_id ):
        #check whether tiff_id is part of parameters. If not, check whether asset name is part of parameters
        #invalid urls cause ip block, so don't blindly attempt to load in files
        geoshare_path = self.get_parameter( tiff_id, None )
        if ( geoshare_path == None ):
            geoshare_path = self.get_parameter( tiff_name, None )
        return geoshare_path 
        
        
        
    def import_geotiff_from_geoshare( self, asset_url:str, asset_id:int = None, asset_name:str = None ):
        sdk = self.get_sdk()
        connector_session = sdk.session.connector
        connector_geoshare = sdk.share.connector
        
        print( 'Opening a stream from ' + str(asset_url) ) 
        geotiff_file_response = connector_geoshare.request(
                url=asset_url,
                stream=True
            )
         
        print( 'Connecting stream to ' + str(asset_name)+ ' ('+str(asset_id)+')' ) 
        upload_response = connector_session.stream_upload_geotiff(
                asset_name=asset_name,
                asset_id=asset_id,
                file_data=geotiff_file_response
            )
            
        print( 'GeoTiff ' + asset_name + '('+str(asset_id)+')' + ' stream result: ' + str(upload_response) ) 
        
        return upload_response.get_response_body()
        
        
        