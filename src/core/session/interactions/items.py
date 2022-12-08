from ..connectors import Connector
from ..data.items import Item, ItemMap

import inspect

class Items:

    @staticmethod
    def load( conn: Connector, item_type, attribute:str = None, timeout_in_seconds = 30 ):
        item_type_to_get = Item.maplink_from( item_type )
        as_item = item_type if inspect.isclass(item_type) and issubclass(item_type, Item) else None
        attribute_postfix = '' if attribute == None else '-'attribute.lower()
        try:
            response = conn.request(
                    method='GET',
                    url='items/'+str(item_type_to_get)+str(attribute_postfix),
                    timeout=timeout_in_seconds
                )
            if ( response.is_success() ):
                return ItemMap(response.get_response_body_json(), as_item=as_item)
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