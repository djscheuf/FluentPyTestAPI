"""
Purpose:
    Declare a re-usable TestSubject supporting various test cases.
    Including:
        - Postive Test cases
        - Negative Test cases
        - Short Construction
        - Long Construction
        - Multiple Assetions
            - Multi-Pass
            - Multi-Fail
            - Mixed

Author: DJS
Date: 11OCT2016
"""

class TestSubject():
    def __init__(self,DoAdvCtor):
        if DoAdvCtor:
            self._AdvCtor()
        else:
            self._BasicCtor()

        self._flag = False
        self._name = ""

    def _AdvCtor(self):
        print("Performing Advanced, slower construction.")
        import time
        time.sleep(5)
        print("Advnaced constrction completed.")

    def _BasicCtor(self):
        print("Simple Construction...")

    def SetFlagTrue(self):
        self._flag = True

    def SetFlagFalse(self):
        self._flag = False

    def SetName(self,name):
        self._name = name

    def GetFlag(self):
        return self._flag

    def GetName(self):
        return self._name
