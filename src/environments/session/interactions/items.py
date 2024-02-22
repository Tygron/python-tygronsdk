from ..connectors import Connector
from ..data.items import Item, ItemMap
from ....utilities.lists import Lists

from typing import Union
import inspect

class Items:

    @staticmethod
    def load( conn: Connector, item_type, filter:Union[str, list] = [], timeout_in_seconds = 30 ):
        item_type_to_get = Item.maplink_from( item_type )
        as_item = item_type if inspect.isclass(item_type) and issubclass(item_type, Item) else None
        
        if ( type(filter) == list and len(filter) > 0 ):
            filter = '-'.join(filter)
        filter_postfix = '' if (not (type(filter) == str)) else '-'+filter
            
        try:
            response = conn.request(
                    method='GET',
                    url='items/'+str(item_type_to_get)+str(filter_postfix),
                    timeout=timeout_in_seconds
                )
            if ( response.is_success() ):
                return ItemMap(response.get_response_body_json(), as_item=as_item)
        except Exception as err:
            raise err
        return None
    
    @staticmethod
    def get( conn:Connector, item_type, item_id:int, timeout_in_seconds = 30 ):
        item_type_to_get = Item.maplink_from( item_type )
        item_type = item_type if inspect.isclass(item_type) and issubclass(item_type, Item) else Item
        
        try:
            response = conn.request(
                    method='GET',
                    url='items/'+str(item_type_to_get)+'/'+str(item_id),
                    timeout=timeout_in_seconds
                )
            if ( response.is_success() ):
                return item_type( response.get_response_body_json() )
        except Exception as err:
            raise err
        return None
    
    @staticmethod
    def size( conn: Connector, item_type, timeout_in_seconds = 30 ):
        item_type_to_get = Item.maplink_from( item_type )
        try:
            response = conn.request(
                    method='GET',
                    url='items/'+str(item_type_to_get)+'/size',
                    timeout=timeout_in_seconds
                )
            if ( response.is_success() ):
                return response.get_response_body_json()
        except Exception as err:
            raise err
        return None

    @staticmethod
    def version( conn: Connector, item_type, timeout_in_seconds = 30 ):
        item_type_to_get = Item.maplink_from( item_type )
        if ( inspect.isclass(item_type) and issubclass(item_type,Item) ):
            item_type_to_get = item_type.get_item_maplink()
            as_item = item_type
        try:
            response = conn.request(
                    method='GET',
                    url='items/'+str(item_type_to_get)+'/version',
                    timeout=timeout_in_seconds
                )
            if ( response.is_success() ):
                return response.get_response_body_json()
        except Exception as err:
            raise err
        return None
    
    @staticmethod
    def get_matching( conn: Connector, item_type, matchables, timeout_in_seconds = 30, 
            try_match_on_id:bool = True,  try_match_on_name:bool = True,  try_match_on_attribute:bool = True, try_str_as_int:bool = True ):
        if ( matchables == False ):
            return ItemMap([], as_item = item_type)
            
        items = Items.load( conn, 
                item_type=item_type, 
                timeout_in_seconds=timeout_in_seconds
            )
        if ( matchables == True ):
            return items
            
        matched_items = []        
        matchables = list(Lists.coerce(matchables))
        if (try_str_as_int):
            for matchable in matchables:
                try:
                    if int(matchable) not in matchables:
                        matchables.append( int(matchable) ) 
                except:
                    pass
        
        for item in items:
            if (try_match_on_id and item.id in matchables):
                matched_items.append(item)
            elif (try_match_on_name and item.name in matchables):
                matched_items.append(item)
            elif (try_match_on_attribute):
                for attr in matchables :
                    attr_value = item.get_attribute_value( attribute=attr, include_maquette = False, default_zero = False )
                    if ( attr_value is None ):
                        continue
                    matched_items.append(item)
                    break
        
        item_map = ItemMap(matched_items, as_item = items.get_item_type())
        return item_map