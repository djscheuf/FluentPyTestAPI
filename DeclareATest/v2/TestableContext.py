"""
Purpose:
    The Testable contexts holds the arrangement, and the expectations previously declared, as well as the specified action from previous contexts.
    It then provides a method so that the specified test may be fun.
"""
from .core import ComponentEnum.TestComponents as TestComponents

class TestableContext():
    def __init__(context,arrangeMethod,expectations,messagesOnError,actionMethod):
        self._context = context
        self._arrange = arrangeMethod
        self._expectations = expectations
        self._messages = messagesOnError
        self._action = actionMethod

    def Run(self):
        """Runs the test defined by the various contexts used to created this context."""

        import sys

        errors = []

        #TODO: Consider try-catching around discrete components to offer better debugging.
        try:
            #Arrange
            if self._context[TestComponents.Subject] is None:
                self._context[TestComponents.Subject] = self._arrange(self._context)

            #Act
            self._action(self._context)

            #Assert
            cnt = len(self._expectations) #Number of expectations
            for i in range(cnt):
                expectation = self._expectations[i]
                try:
                    flag = expectation(self._context[TestComponents.Subject]) #TODO: Convert to taking Context into assertions rather than just subject.
                    if not flag:
                        errors.append("Expecations not met: {0}".format(self._messages[i]))
                except Exception as e:
                    errors.append("Exception caught: {0}".format(e))
        except Exception as e:
            errors.append("Exception caught: {0}".format(e))

        if len(errors) != 0:
            raise AssertionError("Test did not pass. Errors {0}".format(errors)) #TODO: Find better way to format multiple errors issues.
