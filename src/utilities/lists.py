from typing import Union, List

class Lists:
    
    @staticmethod
    def coerce( value ):
        return value if isinstance(value,list) else [value]
    
    @staticmethod
    def get( value, index:int, default = None ):
        if ( not isinstance(value, list) ):
            return default
        if ( (len(value) > index) and (not value[index] == None) ):
            return value[index]
        return default
    
    @staticmethod
    def list_of_lists_fill_up( list_of_lists:list = [], filler=None):
        new_list_of_lists = [l[:] for l in list_of_lists]
        max_len = max( [len(l) for l in new_list_of_lists] )
        for l in new_list_of_lists:
            l.extend( filler for _ in range( max_len - len(l) )  )
        return new_list_of_lists
            
    
    @staticmethod
    def list_of_lists_to_dict( list_of_lists:list = [], indexes:Union[int,list] = 0, keys:list = None ):
        output = {}
        
        list_of_lists = Lists.list_of_lists_fill_up(list_of_lists)
        
        for index, l in enumerate(list_of_lists):
            key = indexes[index] if isinstance(indexes, list) else l[indexes]
            
            if ( keys is None ):                    
                output[key] = l
                continue
            output[key] = {}
            for sub_index, sub_key in enumerate(keys):
                output[key][sub_key] = l[sub_index]
        return output