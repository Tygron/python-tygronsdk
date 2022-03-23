import os



class Files:

    @staticmethod
    def write_file( directory:str, file:str, content:str = None, append:bool = False ):
        Files.ensure_directory(directory)
        f = open( os.path.join( directory, file), 'w')
        f.write(str(content))
        f.close()

    def ensure_directory( directory:str ):
        if ( not os.path.exists(directory) ):
            os.makedirs(directory)

    @staticmethod
    def move_file( file:str, source_location:str, target_location:str ):
        source = os.path.join( source_location, file )
        target = os.path.join( target_location, file )
        if ( not Path(source).is_file() ):
            raise Exception('File not found: ' + str( source ) )
        if ( not os.path.exists(target_location) ):
            os.makedirs(target_location)
        if ( Path(target).is_file() ):
            raise Exception('File already exists: ' + str( target ) )
        os.replace( os.path.join( source ) , os.path.join( target ) )  