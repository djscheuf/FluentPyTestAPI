# Version 1 Example
This is not intended to be a complete example. Please see the [UnitTestWithVersion1](/DeclareATest/v1/UnitTestWithVersion1.py) for that.

## Version 1.1 Simple Usage Example
```python
def commonArrange():
      TestSubject(False)

test = DeclareATest().ArrangedBy(self.commonArrange)\
            .ThatExpects(lambda s: """Lambda to Check Expectation, returns true if passed.""","Error Massage for when check fails.")\
            .When(lambda context: """Act on context[TestComponents.Subject]""")
    test.Run()
```

You can do multiple actions in your action function, and you can setup multiple expectations:
```python
def action(context):
        context[TestComponents.Subject].SetFlagTrue()
        context[TestComponents.Subject].SetName('John')

test = DeclareAtest().ArrangedBy(self.commonArrange)\
        .ThatExpects(lambda s: s.GetFlag() is True,"Subject flag was not True")\
        .ThatExpects(lambda s: s.GetName() == 'John',"Subject name was not John")\
        .When(action)
test.Run()
```
