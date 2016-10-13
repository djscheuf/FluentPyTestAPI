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
                .ThatExpects(lambda s: s.GetFlag() is True)\
                .When(lambda c: c["Subject"].SetFlagTrue())
        test.Run()

    def test_SetFlagFalse(self):
        test = DeclareATest().ArrangedBy(self.commonArrange)\
                .ThatExpects(lambda s: s.GetFlag is False)\
                .When(lambda c: c["Subject"].SetFlagFalse())
        test.Run()

    def test_SetNameToJohn(self):
        test = DeclareATest().ArrangedBy(self.commonArrange)\
                .ThatExpects(lambda s: s.GetName() == 'John')\
                .When(lambda c: c["Subject"].SetName('John'))
        test.Run()

    def test_MultiPass(self):
        def action(context):
            context["Subject"].SetFlagTrue()
            context["Subject"].SetName('John')
        test = DeclareAtest().ArrangedBy(self.commonArrange)\
                .ThatExpects(lambda s: s.GetFlag() is True)\
                .ThatExpects(lambda s: s.GetName() == 'John')\
                .When(action)
        test.Run()

    @unittest.expectedFailure
    def test_MultiFail(self):
        test = DeclareATest().ArrangedBy(self.commonArrange)\
                .ThatExpects(lambda s: s.GetFlag() is True)\
                .ThatExpects(lambda s: s.GetName() == 'John')\
                .When(lambda c: """Do Nothing""" )
        test.Run()

    @unittest.expectedFailure
    def test_Mixed(self):
        test = DeclareATest().ArrangedBy(self.commonArrange)\
                .ThatExpects(lambda s: s.GetFlag() is True)\
                .ThatExpects(lambda s: s.GetName() == 'John')\
                .When(lambda c: c["Subject"].SetFlagTrue())
        test.Run()

if _name_ == '_main_':
    unittest.main()
