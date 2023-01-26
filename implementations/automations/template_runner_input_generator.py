from ... import utilities

import os, sys, json

class TemplateRunnerInputGenerator:

    def __init__( self, settings:dict = {}, **kwargs ):
        self.settings = {

                'base_directory' : 'automations',
        
                'template_directory' : 'template',
                'input_directory' : 'input',
                'data_directory' : 'data',
                'output_directory' : 'output',
                
                
                'input_file' : None,
                'geojson_file' : None,
                
                
                'geojson_feature_import': True,
                'geojson_feature_name_attribute': 'NAME',
                'geojson_feature_buffer': None,
                
                
                'geojson_name': '{geojson_file_name}-{feature_index}-{feature_name}.geojson',
                'json_name': '{input_file_name}-{run_name}.json',
                'run_name': '{feature_name}-{feature_index}',
            }
        
        self.settings.update({
                'input_file': 'template_input.json',
                'geojson_file': 'locations.geojson',
                **settings, 
                **kwargs
            })
    
    def get_template_dir_or_file( self, file:str = '' ):
        return os.path.join(
                self.settings['base_directory'], self.settings['template_directory'], file
            )
    def get_input_dir_or_file( self, file:str = '' ):
        return os.path.join(
                self.settings['base_directory'], self.settings['input_directory'], file
            )
    def get_data_dir_or_file( self, file:str = '' ):
        return os.path.join(
                self.settings['base_directory'], self.settings['data_directory'], file
            )
    def get_output_dir_or_file( self, file:str = '' ):
        return os.path.join(
                self.settings['base_directory'], self.settings['output_directory'], file
            )
        
    def read_input_file( self, input_file:str ):
        try:
            input_json = utilities.files.read_file_as_json(input_file)
            return input_json
        except:
            pass
        input_json = utilities.files.read_file_as_json( self.get_template_dir_or_file(input_file) )
        return input_json
    
    def read_geojson_file( self, geojson_file:str ):
        try:
            input_geojson = utilities.files.read_file_as_json(geojson_file)
            return input_geojson
        except:
            pass
        input_geojson = utilities.files.read_file_as_json( self.get_template_dir_or_file(geojson_file) )
        return input_geojson
        
    def write_input_file( self, input_file_name:str, input_data:str ):
        utilities.files.write_file( self.get_input_dir_or_file(), input_file_name, json.dumps(input_data, indent=4) )
    
    def write_geojson_file( self, geojson_file_name:str, geojson_data:str ):
        utilities.files.write_file( self.get_data_dir_or_file(), geojson_file_name, json.dumps(geojson_data, indent=4) )
    

    
    def run( self, input_file_name:str = None, geojson_file_name:str = None ):    
        if (input_file_name is None):
            input_file_name = self.settings['input_file']
        if (geojson_file_name is None):
            geojson_file_name = self.settings['geojson_file']
        
        input_data = self.read_input_file(input_file_name)
        geojson_data = self.read_geojson_file(geojson_file_name)
    
        individual_geojsons = self.create_individual_geojsons( geojson_data )
        
        for index, individual_geojson in enumerate(individual_geojsons):
        
            terms = {
                    **self.settings,
                    'input_file_name': utilities.files.get_filename( input_file_name, False ),
                    'geojson_file_name': utilities.files.get_filename( geojson_file_name, False )
                }
        
            individual_input = self.create_individual_run_file( input_data, individual_geojson, index, terms )
            
            terms.update(individual_input)
            
            individual_input_file_name = self.format_string( self.settings['json_name'], terms )
            
            if ( self.settings['geojson_feature_import'] ):
                individual_geojson_file_name = self.format_string( self.settings['geojson_name'], terms )
                self.write_geojson_file(individual_geojson_file_name, individual_geojson)
                
                geojson_definition = self.create_geojson_definition_for_run_file( individual_geojson_file_name )
                
                individual_input['geojson_files'].append( geojson_definition )
                
            self.write_input_file(individual_input_file_name, individual_input)
    
        
    def create_individual_run_file( self, input_data:dict, geojson_data:dict, index:int, terms:dict = {} ):
        feature = None if (len(geojson_data['features']) == 0) else geojson_data['features'][0]
        
        geometry_center = utilities.geometries.feature_get_center( feature )
        if ( geometry_center is None ):
            raise Exception('Provided feature has no geometry from which a center can be derived.')
        
        run_data = {**input_data}
        run_data['geojson_files'] = run_data.get('geojson_files',[])
        run_data['location_x'] = geometry_center[0]
        run_data['location_y'] = geometry_center[1]
        run_data['export_location'] = run_data.get('export_location',self.get_output_dir_or_file())
        
        run_data['feature_index'] = index
        run_data['feature_name'] = self.get_feature_name(feature, index)
    
        run_data['run_name'] = self.format_string( run_data.get('run_name', self.settings['run_name']), {**terms, **run_data} )
    
        return run_data
    
    
    def create_individual_geojsons( self, geojson_data:dict ):
        individual_geojsons = []
        
        geo_data_features = geojson_data.get( 'features', [] )
        
        for feature in geo_data_features:
            individual_geojson = {**geojson_data}
            individual_geojson['features'] = [feature]
            individual_geojsons.append(individual_geojson)
            
        return individual_geojsons
    
    def create_geojson_definition_for_run_file( self, geojson_filename:str ):
        return {
                'file_name': geojson_filename,
                'name_attribute': self.settings['geojson_feature_name_attribute'],
                'buffer': self.settings['geojson_feature_buffer']
            }
    
    def get_feature_name( self, feature:dict, index:int = None):
        try:
            feature_name = feature['properties'].get(self.settings['geojson_feature_name_attribute'])
            if (not feature_name is None):
                return feature_name
        except:
            pass
        return 'Unnamed feature '+str(index)
        
        
    def format_string( self, string_to_format:str, terms:dict ):
        return utilities.strings.format( string_to_format, **terms )
        
        
def main():
    settings = {}
    
    if ( len(sys.argv)>1 ):
        settings = None
        input_args = sys.argv[1]
        try:
            settings = utilities.files.read_file_as_json(input_args)
        except Exception as err:
            print (err)
            settings = json.loads(input_args)
    if ( settings is None ):
        print('Failed to read settings.')
        exit()
    input_generator = TemplateRunnerInputGenerator( settings )
    input_generator.run()

if __name__ == '__main__':
    main()       