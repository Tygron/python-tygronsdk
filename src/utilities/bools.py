







class Bools:
    
    @staticmethod
    def to_bool( value = None, default:bool = False ):
        if str(value).lower() in ['true']:
            return True
        if str(value).lower() in ['false']:
            return False
        if ( not default ):
            return value
        return bool(value)