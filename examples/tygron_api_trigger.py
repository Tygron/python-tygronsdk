from .. import sdk as tygron

import sys
import importlib

import json

def main():
    if len(sys.argv) <= 3:
        raise IndexError('Arguments required: trigger module, host, apitoken, and optionally a json of parameters (tygronsdk.example.* engine.tygron.com 12345678abcdabcdabcdabcd)')
        
        
    trigger     = sys.argv[1]
    host        = sys.argv[2]
    apitoken    = sys.argv[3]
    parameters  = '{}'
    
    if not len(sys.argv) <= 4:
        parameters  = sys.argv[4]

    parameters = json.loads( parameters )

    trigger_module = importlib.import_module(trigger)
    trigger_class_name = ''.join(word.title() for word in trigger.rpartition('.')[2].split('_'))

    print(trigger_class_name)
    trigger_class = getattr(trigger_module, trigger_class_name)

    print( 'Instantiate a '+trigger_class_name+' trigger, with parameters:' + str([host, apitoken, parameters]) )
    trigger_obj = trigger_class( host, apitoken, parameters )
    
    print( 'Then run the trigger' )
    result = trigger_obj.trigger()

    print(' The trigger has given the following response, which can be sent back as a response to the original call to run the trigger: ')
    print( json.dumps( result, indent=4 ) );

main()
