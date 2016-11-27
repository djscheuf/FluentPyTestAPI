# FluentPyTestAPI - Intent
DeclareATest is a personal project inspire by a [Pluralsight Course](https://app.pluralsight.com/library/courses/designing-fluent-apis-c-sharp/table-of-contents) on Fluent APIs.
I decided to develop a Unit Testing API because the ones I have seen available on the web did not meet my needs.
Mostly they seemed clunky or did not support what I though a reasonable use case would be.

##Version 1
### A Proof of Concept
With Version 1, I am planning to provide the basic Arrange, Act, Assert structure for a test.
The API will not involve controlled API contexts by separating the functions into different classes, as would seem typical in strongly-typed language.
Instead, I plan to provide these functions in a single class. Naturally this will make version 1 weaker to mis-use, as it cannot truly protect the user from incorrect usage.
It does however make it much easier to develop and test since the code resides in a single class.

##Version 2
### Enhanced User Protection
Version 2 is presently planned to implement class-based protections against mis-use. I plan to do this by separating the functionality into multiple API contexts.
Through the use of multiple contexts, the proper usage can be made clearer to the user, even though Python is duck-typed.
I will admit that I do not know if this will be an improvement in the design or a detriment. Further considerations for Version 2 are postponed until Version 1 is complete.
