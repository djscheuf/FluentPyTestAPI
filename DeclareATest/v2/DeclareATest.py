"""
Purpose:
    Provides the start point for the DeclareATestAPI, specifically returning the ArrangeContext.

Intent:
    Planned to support basic testing:
        - Provide a pre-init subject

Author: DJS
Date: 29NOV016
"""

from ArrangeContext import ArrangeContext as ArrangeContext

class DeclareATest():
    def __init__():
        pass

    def _For(self,subject):
        """Takes a pre-initialized subject to test against, returns an ArrangedContext"""
        return ArrangeContext()._bySubject(subject)

    def ArrangedBy(self, arrangeMethod):
        """Takes a Method taht takes a context for complex initialization and checking, which returns an initialized subject, executed at Run()"""
        return ArrangeContext()._byMethod(arrangeMethod)
