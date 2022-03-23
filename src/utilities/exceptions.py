import os, traceback



class Exceptions:

    @staticmethod
    def stringify( exception:Exception ):
        string = ''
        try:
            raise exception
        except Exception as e:
            for value in exception.args:
                if ( isinstance(value, Exception) ):
                    #TODO: Traces are printed a bit oddly now, but usable
                    string += Exceptions.stringify(value)
                else:
                    string += str(value)
                string += os.linesep
            tb = traceback.format_exc()
            string += tb
            string += os.linesep
            return string
        return None




