import inspect
from typing import Type
from types import ModuleType

import importlib.util
import sys

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
            
    @staticmethod
    def get_module_dot_notation_string( module:Type[ModuleType] ):
        return module.__module__
            
    @staticmethod
    def get_class_dot_notation_string( cls:Type ):
        return cls.__module__ + '.' + cls.__class__.__name__