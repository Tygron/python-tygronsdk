from ... import sdk as tygron

import sys
import importlib

import json

def main():

    #   A Trigger interface is provided to help in creating and documenting triggers. This example demonstraties how to activate such a Trigger.

    #   Triggers rely on authentication information, and potentially some additional parameters.
    #   To run this example, provide a reference to a Trigger which is derived from the Trigger interface, and provide host, api_token, and parameters if required
    if len(sys.argv) <= 3:
        raise IndexError('Arguments required: trigger module, host, apitoken, and optionally a json of parameters (tygronsdk.examples.triggers.* engine.tygron.com 12345678abcdabcdabcdabcd)')
        
    #   For this example, the arguments are read out and prepared in readable variables
    trigger     = sys.argv[1]
    host        = sys.argv[2]
    api_token    = sys.argv[3]
    parameters  = '{}' if len(sys.argv) <= 4 else sys.argv[4]

    print( 'Provided trigger data: ' )
    print( 'Trigger: ' + trigger )
    print( 'Host: ' + host )
    print( 'Api Token: '+ api_token )
    print( 'Parameters: '+ parameters )

    parameters = json.loads( parameters )

    #   The provided trigger is imported, so it can be instantiated and run
    trigger_module = importlib.import_module(trigger)
    trigger_class_name = ''.join(word.title() for word in trigger.rpartition('.')[-1].split('_'))
    trigger_class = getattr(trigger_module, trigger_class_name)

    #   With the trigger class known, it can now be created and run
    print( 'Instantiate a '+trigger_class_name+' trigger, with parameters:' + str([host, api_token, parameters]) )
    trigger_obj = trigger_class( host, api_token, parameters )
    
    #   This is where the actual trigger is run. Based on which trigger is run (example or otherwise) its content may differ
    print( 'Then run the trigger' )
    trigger_obj.trigger()

    #   Finally the trigger will contain the desired results, which can be obtained and returned
    print( 'The trigger has given the following response, which can be sent back as a response to the original call to run the trigger: ')
    print( json.dumps( trigger_obj.get_results(), indent=4 ) );
    
    #   If neccesary, a more expansive result can be returned which includes all available types and exceptions if applicable
    print ( 'It is also possible to dump a broader result structure, which is not compatible with the Tygron Platform, but allows for debugging: ')
    print( json.dumps( trigger_obj.get_results_structure(), indent=4 ) )

main()
