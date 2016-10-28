"""
Purpose:
    Defines DeclareATest fluent Testing API.

Intent:
    Planned to support basic testing:
        - Provide a pre-init subject
        - Declare Arrangement of subject
        - Declare expectations ( all evaluated one at a time)
        - Declare action.

Missing:
    This class is missing strong protections against mis-ordered Use.
    That is When could accidentally not be called and so action would be none.

Author: DJS
Date: 11OCT2016
"""
from .core import fluent.fluent as fluent # should import fluent method decorator
from .core import ComponentEnum.TestComponents as TestComponents

class DeclareATest():
    def __init__(self):
        self._arrange = None
        self._context = {} #Need to use Context to wrapp and allow mutation of Vars
            # Can extend this to later use. May refactor Arrange to take and mutate Context.
        self._expectations = []
        self._messages = []
        self._action = None

    @fluent
    def _For(self,subject):
        """Takes a pre-initialized subject to test against"""
        self._context[TestComponents.Subject] = subject

    @fluent
    def ArrangedBy(self, arrangeMethod):
        """Takes a Method taht takes a context for complex initialization and checking, which returns an initialized subject, executed at Run()"""
        self._arrange = arrangeMethod
        self._context[TestComponents.Subject] = None

    @fluent
    def ThatExpects(self,expectation, msgOnError="No Message Provided..."):
        """Takes a method that takes subject and that returns boolean for met or unmet expecation.
            Each is evaluated at Run(). Errors are collected and reported when all expectations evaluated."""
        self._expectations.append(expectation)
        self._messages.append(message)

    @fluent
    def When(self,actionMethod):
        """Takes a method that takes subject, and returns void. Executed at Run()"""
        self._action = actionMethod

    def Run(self):
        """Runs the test defined by the various assigned functions and expectations"""
        import sys

        errors = []

        try:
            #Arrange
            if self._context[TestComponents.Subject] is None:
                self._context[TestComponents.Subject] = self._arrange(self._context)

            #Act
            self._action(self._context)

            #Asssert
            cnt = len(self._expectations) # Number of expecations to verify, same as message count.
            for i in range(cnt):
                expectation = self._expectations[i]
                try:
                    flag = expectation(self._context[TestComponents.Subject])
                    if not flag:
                        errors.append("Expecations not met: {0}".format(self._messages[i]))
                except Exception as e:
                    errors.append("Exception caught: {0}".format(e))
        except Exception as e:
            errors.append("Exception caught: {0}".format(e))

        if len(errors) != 0:
            raise AssertionError("Test did not pass. Errors {0}".format(errors))
