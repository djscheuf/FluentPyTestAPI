"""
Purpose:
    Implement a UnitTest demonstration of DeclareATest API.
    Will Use TestSubject from Core, and v1.DeclareaTest to declare a simple
        series of test.

Author: DJS
Date: 11OCT2016
"""

import DeclareATest

def action(context):
	print("	Input subject: {}".format(context["Subject"]))
	context["Subject"]=1
	print("	Acted subject: {}".format(context["Subject"]))

subject=125
test = DeclareATest()._For(subject).ThatExpects(lambda s: s==1).When(action)
#test = test.ThatExpects(lambda s: s==1)
#test = test.When(action)
test.Run()
