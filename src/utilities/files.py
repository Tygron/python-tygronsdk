import os

from pathlib import Path

class Files:

    @staticmethod
    def write_file( directory:str, file:str, content:str = None, append:bool = False ):
        Files.ensure_directory(directory)
        f = open( os.path.join( directory, file), 'w')
        f.write(str(content))
        f.close()

    @staticmethod
    def ensure_directory( directory:str ):
        if ( not os.path.exists(directory) ):
            os.makedirs(directory, exist_ok=True)

    @staticmethod
    def move_file( file:str, source_location:str, target_location:str ):
        source = os.path.join( source_location, file )
        target = os.path.join( target_location, file )
        if ( not Path(source).is_file() ):
            raise Exception('File not found: ' + str( source ) )
        Files.ensure_directory(target_location)
        if ( Path(target).is_file() ):
            raise Exception('File already exists: ' + str( target ) )
        os.replace( os.path.join( source ) , os.path.join( target ) )
        

    @staticmethod
    def get_content_of_directory( directory:str, error_if_not_exists:bool = False ):
        if ( not os.path.exists(directory) and not error_if_not_exists):
            return []
        return os.listdir( directory )
        
    @staticmethod
    def get_filename( file_path:str, include_extension:bool = True ):
        filename = Path(file_path).stem
        if ( not include_extension ):
            filename = filename.split('.')[0]
        return filename