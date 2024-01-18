import os, importlib
from inspect import getmembers, isfunction

directory = os.path.dirname(os.path.realpath(__file__))
for filename in os.listdir( directory ):
    full_file_path = os.path.realpath( os.path.join(directory , filename) ) 
    if ( __file__ == full_file_path ):
        continue
    if ( not os.path.isfile( full_file_path ) ):
        continue

    module_name = filename.replace('.py','')
    
    locals()[module_name] = importlib.import_module(__name__+'.'+ module_name)
        
    try:
        locals()[module_name] = locals()[module_name].event_set
    except:
        continue