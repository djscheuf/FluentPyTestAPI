"""
Purpose:
    Declare a fluent API method decorator, which provides a copy of the object
    used rather than mutating the given caller.

Source:
    http://code.activestate.com/recipes/579078-fluent-api-method-decorator/
"""

from functools import wraps
from copy import deepcopy

def fluent(method):
    """"Used to define fluent API class methods"""
    @wraps(method)
    def wrapped(self,*args,**kwargs):
            dupe = deepcopy(self)
            method(dupe,*args,**kwargs)
            return dupe
    return wrapped
