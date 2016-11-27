"""
Purpose:
    The Assert Context maintains the arrangement of the test, and collects expectations.
    Finally when all expectations have been declared, the tested Actions is given and a TestableContext is returned.
"""

from TestableContext import TestableContext as TestableContext

#TODO: Provide an option for an Expected Exception upon Action.
class AssertContext():
    def __init__(context,arrangeMethod):
        self._context = context
        self._arrange = arrangeMethod
        self._expectations = []
        self._messages = []

    def ThatExpects(self,expectation, msgOnError="No Message Provided..."):
        """Takes a method that takes subject and that returns boolean for met or unmet expecation."""
        self._expectations.append(expectation)
        self._messages.append(msgOnError)

    def When(self,actionMethod):
        """Takes a method that takes subject, and returns void. Returns a TestableContext"""
        return TestableContext(self._context,self._arrange,self._expecations,self._messages,actionMethod)
