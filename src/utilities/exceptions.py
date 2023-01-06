import os, traceback



class Exceptions:

    @staticmethod
    def stringify( exception:Exception,  ):
        string = ''
        
        for value in exception.args:
            if ( isinstance(value, Exception) ):
                string += Exceptions.stringify(value)
                
        tb = traceback.format_exception(exception)
        string += ''.join(tb)
        
        string += os.linesep
        return string




