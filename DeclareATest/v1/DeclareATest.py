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

class DeclareATest():
    def __init__(self):
        self._arrange = None
        self._subject = None
        self._expectations = []
        self._action

    @fluent
    def _For(self,subject):
        """Takes a pre-initialized subject to test against"""
        self._subject = subject

    @fluent
    def ArrangedBy(self, arrangeMethod):
        """Takes a Method which returns an initialized subject, executed at Run()"""
        self._arrange = arrangeMethod
        self._subject = None

    @fluent
    def ThatExpected(self,expectation):
        """Takes a method that takes subject and that returns boolean for met or unmet expecation.
            Each is evaluated at Run(). Errors are collected and reported when all expectations evaluated."""
        self._expectations.append(expectation)

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
            if self._subject is None:
                self._subject = self._arrange()

            #Act
            self._action(self._subject)

            #Asssert
            for expectation in self._expectations:
                try:
                    flag = expecation(self._subject)
                    if !flag:
                        errors.append("Expecations not met: {0}".format(expectation))
                except:
                    errors.append("Exception caught: {0}".format(sys.exec_info()[0]))
        except:
            errors.append("Exception caught: {0}".format(sys.exec_info()[0]))

        if len(errors) != 0:
            msg = '\n'.join('{},\n'.format(errors)
            raise AssertionError("Test did not succeed. Errors {0}".format(msg))
