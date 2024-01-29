from .event_set_collection import EventSetCollection
from .event_set import EventSet

import inspect

#Containing class/object for ApiEnvironments to hold their events
class EventSetMultiCollection():

    def __init__( self, collection:str = None, *event_sets_list, **event_sets_dict ):
        self.collections = {}
        self.collection_domains = []
        self.collection = collection
    
        self.add_event_sets( collection, *event_sets_list, **event_sets_dict)
        pass
    
    def set_collection( self, collection:str ):
        self.set_event_set_collection( collection )
        
    def get_collection( self, collection:str = None ):
        return self.get_event_set_collection( collection )
    
    def set_event_set_collection( self, collection:str ):
        if ( not (self.collection is None) ):
            for event_domain in self.collection_domains:
                delattr(self, event_domain) 
        self.collection_domains = []
            
        self.collection = collection
        
        event_collection = self.get_event_set_collection()
        if ( not (event_collection is None) ):
            for event_domain in event_collection.domains:
                setattr( self, event_domain, getattr(event_collection, event_domain) ) 
                self.collection_domains.append(event_domain)
            
    def get_event_set_collection( self, collection:str = None ):
        if ( collection is None ):
            return self.collections.get(self.collection, None)
        return self.collections.get(collection, None)
    
    
    
    def add_event_sets( self, collection:str, *event_sets_list, **event_sets_dict ):
        for event_set in event_sets_list:
            self.add_event_set(collection, event_set)
        for event_domain, event_set in event_sets_dict.items():
            self.add_event_set(collection, event_set, event_domain)
        self.set_event_set_collection(self.collection)
    
    def add_event_set( self, collection:str, event_set:EventSet, event_domain:str = None ):
        self.collection = self.collection or collection
        event_domain = event_set.event_domain if event_domain == None else event_domain
        self.ensure_event_set_collection( collection ).add_event_set( event_set, event_domain )
        
    def ensure_event_set_collection( self, collection:str ):
        self.collections[collection] = self.collections.get( collection, EventSetCollection() )
        return self.collections[collection]