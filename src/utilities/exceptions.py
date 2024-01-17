import os, traceback

from .lists import Lists
from typing import Union

class Exceptions:

    @staticmethod
    def stringify( exception:Union[Exception,str],  ):
        string = ''
        
        if ( not isinstance(exception, Exception) ):
            return exception
        
        for value in exception.args:
            if ( isinstance(value, Exception) ):
                string += Exceptions.stringify(value)
                
        tb = traceback.format_exception(exception)
        string += ''.join(tb)
        
        string += os.linesep
        return string

    @staticmethod
    def raise_multiple_exceptions( operation:str = None, *exceptions:Exception ):
        if ( len(exceptions) == 0 ):
            return
        
        if ( isinstance(exceptions[0],list) ):
            return Exceptions.raise_multiple_exceptions(operation, *exceptions)
        
        description = ''
        if ( len(exceptions) == 1):
            description = 'An exception occured'
        else:
            description = str(len(exceptions))+' exceptions occured'

        if ( not (operation is None) ):
            description+= ' while '+str(operation)
        
        raise Exception( description, *exceptions )

