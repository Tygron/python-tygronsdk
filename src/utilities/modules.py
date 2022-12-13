import inspect
from typing import Type
from types import ModuleType

class Modules:
            
    @staticmethod
    def get_content_from_module( module:Type[ModuleType] = None, cls:Type = None ):
        try:
            content = {}
            if ( module == None):
                return content
            if ( not isinstance(module, ModuleType) ):
                return content
            submodules = inspect.getmembers(module)
            
            for key, submodule in submodules:
                if ( (cls == None) or isinstance(submodule, cls) ):
                    content[key] = submodule
            return content
        except Exception as err:
            raise err
    
    @staticmethod
    def get_classes_from_module( module:Type[ModuleType] = None ):
        try:
            classes = {}
            if ( module == None):
                return classes
            if ( not isinstance(module, ModuleType) ):
                return classes
            submodules = inspect.getmembers(module)
            for key, submodule in submodules:
                if ( not inspect.isclass(submodule) ):
                    continue
                classes[key] = submodule
            return classes
        except Exception as err:
            raise err