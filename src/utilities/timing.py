from typing import Callable
import time


class Timing:

    @staticmethod
    def wait_for( wait_function: Callable, interval_in_seconds: int = 5 ):
        result = None
        while( result == None ):
            time.sleep(interval_in_seconds)
            try:
                result = wait_function()
            except Exception as err:
                raise err
        return result