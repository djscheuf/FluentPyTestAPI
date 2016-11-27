"""
Purpose:
    The ArrangeContext is created either with a given subject or with an initialization protocol.
    It provides the API call to declare the first Expectation of the Test.
"""
from .core import ComponentEnum.TestComponents as TestComponents
from AssertContext import AssertContext as AssertContext

class ArrangeContext():
    def __init__():
        self._context = {}
        self._arrange = None

    def _bySubject(self,subject):
        self._context[TestComponents.Subject] = subject

    def _byMethod(self,method):
        self._arrange = method

    def ThatExpected(self,expectation,msgOnError="No Message Provided..."):
        """Takes a method that takes subject and that returns boolean for met or unmet expecation. Returns an AssertContext"""
        return AssertContext(self._arrange, self._context).ThatExpects(expectation,msgOnError)
