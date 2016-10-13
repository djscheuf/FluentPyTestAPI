# FluentPyTestAPI - Resources
This page will be a collection of resources used in the development or inception of this project.

## [Pluralsight Course - Designing Fluent APIs in C#](https://app.pluralsight.com/library/courses/designing-fluent-apis-c-sharp/table-of-contents)
This course was the inception for this project. I wanted to practice what I had learned, and a Unit testing API would be good practice.

## [Fluent Method Decorator](http://code.activestate.com/recipes/579078-fluent-api-method-decorator/)
This site provided the code, which is used to implement the Fluent API methods. Specifically if returns a complete copy of the DeclareATest instance.
This would in theory allow you to re-use partial test declarations. Like just declaring the arrangement, if it was complex. Not that this currently saves a lot.
I have used it, partly because I like the Decorator style for fluency better than others. But also because I like the protection that deepcopy provides when using the API.

Strictly speaking this might be a memory hog, and otherwise an un-useful feature. I will evaluate it later for its potential value in user-protiections againts memory and possibly performance concerns.

### Minor Resources
- [StackExchange Discussion-Fluent Interface vs. Args](http://stackoverflow.com/questions/3883907/designing-an-python-api-fluent-interface-or-arguments)
- - Consulted but not used, as I somewhat disagree.
