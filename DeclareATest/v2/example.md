# Version 2 Example
This is not intended to be a complete example.

## Version 2 Simple Usage Example
```python
def commonArrange():
      TestSubject(False)

arrC = DeclareATest().ArrangedBy(self.commonArrange) #Returns an ArrangeContext

assertC = arrC.ThatExpects(lambda s: """Lambda to Check Expectation, returns true if passed.""","Error Massage for when check fails.")  #Returns an AssertContext

test = assertC.When(lambda context: """Act on context[TestComponents.Subject]""") #Returns a TestableContext

test.Run() #Executes the test, as before.
```

Since version 2 honors versions 1.1 improvements, please see [Example for v1](/DeclareATest/v1/example.md) for additional details.
