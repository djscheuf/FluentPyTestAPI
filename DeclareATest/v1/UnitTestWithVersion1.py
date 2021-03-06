"""
Purpose:
    Use Python Unit Test testcases composed by DeclareATest.

Date: 13OCT2016
Author: DJS
"""

import DeclareATest
from .core.TestSubject import TestSubject
import unittest

class VersionOneUnitTests(unittest.TestCase):
    def commonArrange():
        TestSubject(False)

    def test_SetFlagTrue(self):
        test = DeclareATest().ArrangedBy(self.commonArrange)\
                .ThatExpects(lambda s: s.GetFlag() is True,"Subject Falg is false.")\
                .When(lambda c: c[TestComponents.Subject].SetFlagTrue())
        test.Run()

    def test_SetFlagFalse(self):
        test = DeclareATest().ArrangedBy(self.commonArrange)\
                .ThatExpects(lambda s: s.GetFlag is False,"Subject flag is true")\
                .When(lambda c: c[TestComponents.Subject].SetFlagFalse())
        test.Run()

    def test_SetNameToJohn(self):
        test = DeclareATest().ArrangedBy(self.commonArrange)\
                .ThatExpects(lambda s: s.GetName() == 'John',"Subject Name was not john")\
                .When(lambda c: c[TestComponents.Subject].SetName('John'))
        test.Run()

    def test_MultiPass(self): #*wink* hehe multi-pass
        def action(context):
            context[TestComponents.Subject].SetFlagTrue()
            context[TestComponents.Subject].SetName('John')
        test = DeclareAtest().ArrangedBy(self.commonArrange)\
                .ThatExpects(lambda s: s.GetFlag() is True,"Subject flag was not true")\
                .ThatExpects(lambda s: s.GetName() == 'John',"Subject name was not john")\
                .When(action)
        test.Run()

    @unittest.expectedFailure
    def test_MultiFail(self):
        test = DeclareATest().ArrangedBy(self.commonArrange)\
                .ThatExpects(lambda s: s.GetFlag() is True,"Subject flag was not true")\
                .ThatExpects(lambda s: s.GetName() == 'John',"Subject name was not john")\
                .When(lambda c: """Do Nothing""" )
        test.Run()

    @unittest.expectedFailure
    def test_Mixed(self):
        test = DeclareATest().ArrangedBy(self.commonArrange)\
                .ThatExpects(lambda s: s.GetFlag() is True,"Subject flag awas not true")\
                .ThatExpects(lambda s: s.GetName() == 'John',"Subject name was not john")\
                .When(lambda c: c[TestComponents.Subject].SetFlagTrue())
        test.Run()

if _name_ == '_main_':
    unittest.main()
