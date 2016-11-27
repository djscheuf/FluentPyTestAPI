#Version 2 Version History/Doc

##Current Version: 2.0
Version 2.0 completely changed the implementations of the API. The functions remain the same, but have been moved to discrete classes to form better context flow. By thus separating the functions, IDE prompts can better guide the users of the API in its proper usage.

Summary:
- Version 1.1 changes have been honored
- DeclareATest now returns an ArrangeContext
- ArrangeContext now returns an AssertContext
- AssertContext now returns a TestableContext
-- AssertContext can also loop to return an AssertContext, for multiple assertions
- A TestableContext can be Run().
--The Run function operates as it always has in Version 1
- Finally, all API function names remain the same, including method signatures.

Please see [Example.md](/DeclareATest/v2/example.md) for simplified usage details.

###Previous Versions
 Version  | Started  | Notes
---       |---       |---
v2.0      |11/29/2016| Improving Guided Usage by pulling functions into more limited contexts. Flagged locations for improvement.
