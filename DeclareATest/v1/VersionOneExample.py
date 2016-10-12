"""
Purpose:
    Implement a UnitTest demonstration of DeclareATest API.
    Will Use TestSubject from Core, and v1.DeclareaTest to declare a simple
        series of test.

Author: DJS
Date: 11OCT2016
"""

import DeclareATest
from core.TestSubject import TestSubject

def InitDemo():

    def action(context):
    	print("	Input subject: {}".format(context["Subject"]))
    	context["Subject"]=1
    	print("	Acted subject: {}".format(context["Subject"]))

    subject=125
    test = DeclareATest()._For(subject).ThatExpects(lambda s: s==1).When(action)
    #test = test.ThatExpects(lambda s: s==1)
    #test = test.When(action)
    test.Run()

def TestSubjectDemo():

    def action(context):
        print(" Setting Flag to True")
        context["Subject"].SetFlagTrue()

    test = DeclareATest().ArrangedBy(lambda : TestSubject(False))\
            .ThatExpects(lambda s: s.GetFlag()).When(action)
    test.Run()
    print("")

    def action2(context):
    	print("	Setting Name to John")
    	context["Subject"].SetName("John")


    test2 = DeclareATest().ArrangedBy(lambda : TestSubject(True))\
    			.ThatExpects(lambda s: s.GetName() == "John")\
    			.When(action2)
    test2.Run()
    print("")

    def action3(context):
    	print("	Setting Name to John")
    	context["Subject"].SetName("John")
    	print("	Setting Flag to True")
    	context["Subject"].SetFlagTrue()


    test3 = DeclareATest().ArrangedBy(lambda : TestSubject(False))\
    			.ThatExpects(lambda s: s.GetName() == "John")\
    			.ThatExpects(lambda s: s.GetFlag())\
    			.When(action3)
    test3.Run()
    print("")

    def action4(context):
    	print("	Setting Name to James")
    	context["Subject"].SetName("James")
    	print("	Setting Flag to True")
    	context["Subject"].SetFlagTrue()


    test4 = DeclareATest().ArrangedBy(lambda : TestSubject(False))\
    			.ThatExpects(lambda s: s.GetName() == "John")\
    			.ThatExpects(lambda s: s.GetFlag())\
    			.When(action4)
    try:
        test4.Run()
    except AssertionError:
        print("Test 4 has failed, as expected. Validating Name against John is incorrect.")

    print("")

if _name_ == "_main_":
    TestSubjectDemo()
