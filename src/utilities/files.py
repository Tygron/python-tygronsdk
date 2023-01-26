from .lists import Lists
from .exceptions import Exceptions

import json, os, re, shutil
from pathlib import Path
from typing import Union

class Files:

    @staticmethod
    def write_file( directory:str, file:str, content:None, append:bool = False ):
        if ( isinstance(content, bytes) ):
            Files.write_file_binary(
                    directory=directory,
                    file=file,
                    content=content,
                    append=append
                )
        else:
            Files.write_file_text(
                    directory=directory,
                    file=file,
                    content=content,
                    append=append
                )
        
    @staticmethod
    def write_file_text( directory:str, file:str, content:str = None, append:bool = False ):
        flag = 'a' if append else 'w'
        Files.ensure_directory(directory)
        f = open( os.path.join( directory, file), flag)
        f.write(str(content))
        f.close()
        
    @staticmethod
    def write_file_binary( directory:str, file:str, content = None, append:bool = False ):
        flag = 'ab' if append else 'b'
        Files.ensure_directory(directory)
        f = open( os.path.join( directory, file), flag)
        f.write(content)
        f.close()


        
    @staticmethod
    def read_file_as_text( file ):
        if ( (not file) or (not Path( file ).is_file()) ):
            raise Exception( str(file) + ' is not a valid file' )
            
        with open(file, encoding='utf8') as f:
            return ''.join(f.readlines())
        
    @staticmethod
    def read_file_as_json( file ):
        content = Files.read_file_as_text( file )
        return json.loads( content )
    
 
 
    @staticmethod
    def ensure_directory( directory:Union[str, list] ):
        errors = []
        try:
            for d in Lists.coerce(directory):
                if ( d == '' ):
                    return
                if ( not os.path.exists(d) ):
                    os.makedirs(d, exist_ok=True)
        except Exception as err:
            errors.append(err)
        Exceptions.raise_multiple_exceptions('ensuring directories exist', *errors)
            
    @staticmethod
    def get_content_of_directory( directory:str, regex:str=None, error_if_not_exists:bool = False ):
        if ( not os.path.exists(directory) and not error_if_not_exists):
            return []
            
        files_list = os.listdir( directory )
        
        if ( regex is None ):
            return files_list
            
        r = re.compile(regex)
        return list( filter(r.search, files_list) )



    @staticmethod
    def move_file( file:Union[str, list], source_location:str, target_location:str ):  
        errors = []
        try:
            for f in Lists.coerce(file):
                source = os.path.join( source_location, f )
                target = os.path.join( target_location, f )
                if ( not Path(source).is_file() ):
                    raise Exception('File not found: ' + str( source ) )
                Files.ensure_directory(target_location)
                if ( Path(target).is_file() ):
                    raise Exception('File already exists: ' + str( target ) )
                if ( Path(target).is_dir() ):
                    raise Exception('Directory already exists: ' + str( target ) )
                os.replace( os.path.join( source ) , os.path.join( target ) )
        except Exception as err:
            errors.append(err)
        Exceptions.raise_multiple_exceptions('moving files', *errors)
 
    @staticmethod
    def delete_file( file:Union[str, list], also_directories:bool = False ):
        #if ( also_directories ):
        #    raise Exception('The deletion of directories is not yet implemented.')
            
        errors = []
        try:
            for f in Lists.coerce(file):
                path = Path(f)
                if ( path.is_file() ):
                    path.unlink()
                elif ( path.is_dir() and also_directories ):
                    shutil.rmtree(path)
        except Exception as err:
            errors.append(err)
        Exceptions.raise_multiple_exceptions('deleting files', *errors)


    @staticmethod
    def get_filename( file_path:str, include_extension:bool = True ):
        filename = Path(file_path).stem
        if ( not include_extension ):
            filename = filename.split('.')[0]
        return filename
        
    @staticmethod
    def remove_invalid_chars_from_filename( filename:str, replacements:Union[str,dict] = None ):
        if ( replacements is None ):
            replacements = ''
            
        if ( isinstance(replacements,str ) ):
            return re.sub(r'[\\/*?:"<>|]',replacements,filename)
            
        for term, replacement in replacements.items():
            filename = filename.replace(term, '' if replacement is None else replacement)
        return filename