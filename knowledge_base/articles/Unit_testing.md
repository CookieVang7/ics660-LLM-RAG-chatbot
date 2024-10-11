


(Top)





1
History








2
Unit








3
Execution








4
Testing criteria








5
Test case








6
Test double








7
Parameterized test








8
Agile








9
Test-driven development








10
Value




Toggle Value subsection





10.1
Early detection of problems in the development cycle








10.2
Reduced cost








10.3
More frequent releases








10.4
Allows for code refactoring








10.5
Detects changes which may break a design contract








10.6
Reduce uncertainty








10.7
Documentation of system behavior










11
Limitations and disadvantages




Toggle Limitations and disadvantages subsection





11.1
Difficulty in setting up realistic and useful tests








11.2
Requires discipline throughout the development process








11.3
Requires version control








11.4
Requires regular reviews








11.5
Limitations for embedded system software








11.6
Limitations for testing integration with external systems










12
Examples




Toggle Examples subsection





12.1
JUnit










13
As executable specifications








14
Applications




Toggle Applications subsection





14.1
Extreme programming








14.2
Automated testing frameworks








14.3
Language-level unit testing support










15
See also








16
References








17
Further reading








18
External links




























10.1
Early detection of problems in the development cycle








10.2
Reduced cost








10.3
More frequent releases








10.4
Allows for code refactoring








10.5
Detects changes which may break a design contract








10.6
Reduce uncertainty








10.7
Documentation of system behavior
























11.1
Difficulty in setting up realistic and useful tests








11.2
Requires discipline throughout the development process








11.3
Requires version control








11.4
Requires regular reviews








11.5
Limitations for embedded system software








11.6
Limitations for testing integration with external systems






















12.1
JUnit














14.1
Extreme programming








14.2
Automated testing frameworks








14.3
Language-level unit testing support






















Part of a series onSoftware development
Core activities
Data modeling
Processes
Requirements
Design
Construction
Engineering
Testing
Debugging
Deployment
Maintenance

Paradigms and models
Agile
Cleanroom
Incremental
Prototyping
Spiral
V model
Waterfall

Methodologies and frameworks
ASD
DevOps
DAD
DSDM
FDD
IID
Kanban
Lean SD
LeSS
MDD
MSF
PSP
RAD
RUP
SAFe
Scrum
SEMAT
TDD
TSP
UP
XP

Supporting disciplines
Configuration management
 Deployment management
Documentation
Software quality assurance
Project management
User experience

Practices
ATDD
BDD
CCO
CI
CD
DDD
PP
SBE
Stand-up
TDD

Tools
Compiler
Debugger
Profiler
GUI designer
UML Modeling
IDE
Build automation
Release automation
Infrastructure as code

Standards and bodies of knowledge
CMMI
IEEE standards
ISO 9001
ISO/IEC standards
PMBOK
SWEBOK
ITIL
IREB
OMG

Glossaries
Artificial intelligence
Computer science
Electrical and electronics engineering

Outlines
Outline of software development
vte
Data modeling
Processes
Requirements
Design
Construction
Engineering
Testing
Debugging
Deployment
Maintenance
Agile
Cleanroom
Incremental
Prototyping
Spiral
V model
Waterfall
ASD
DevOps
DAD
DSDM
FDD
IID
Kanban
Lean SD
LeSS
MDD
MSF
PSP
RAD
RUP
SAFe
Scrum
SEMAT
TDD
TSP
UP
XP
Configuration management
 Deployment management
Documentation
Software quality assurance
Project management
User experience
ATDD
BDD
CCO
CI
CD
DDD
PP
SBE
Stand-up
TDD
Compiler
Debugger
Profiler
GUI designer
UML Modeling
IDE
Build automation
Release automation
Infrastructure as code
CMMI
IEEE standards
ISO 9001
ISO/IEC standards
PMBOK
SWEBOK
ITIL
IREB
OMG
Artificial intelligence
Computer science
Electrical and electronics engineering
Outline of software development
vte
Unit testing, a.k.a. component or module testing, is a form of software testing by which isolated source code is tested to validate expected behavior.[1]

Unit testing describes tests that are run at the unit-level to contrast testing at the integration or system level.

Unit testing, as principle for testing separately smaller parts of large software systems dates back to the early days of software engineering. In June 1956, H.D. Benington presented at US Navy's Symposium on Advanced Programming Methods for Digital Computers the SAGE project and its specification based approach where the coding phase was followed by "parameter testing" to validate component subprograms against their specification, followed then by an "assembly testing" for parts put together.[2][3]

In 1964, a similar approach is described for the software of the Mercury project, where individual units developed by different programmes underwent "unit tests" before being integrated together.[4] In 1969, testing methodologies appear more structured, with unit tests, component tests and integration tests with the purpose of validating individual parts written separately and their progressive assembly into larger blocks.[5] Some public standards adopted end of the 60's, such as MIL-STD-483[6] and MIL-STD-490 contributed further to a wide acceptance of unit testing in large projects. 

Unit testing was in those times interactive[3] or automated,[7] using either coded tests or capture and replay testing tools. In 1989, Kent Beck described a testing framework for Smalltalk (later called SUnit) in "Simple Smalltalk Testing: With Patterns". In 1997, Kent Beck and Erich Gamma developed and released JUnit, a unit test framework that became popular with Java developers.[8] Google embraced automated testing around 2005–2006.[9]

Unit is defined as a single behaviour exhibited by the system under test (SUT), usually corresponding to a requirement. While it may imply it's a function or a module (in procedural programming) or a method or a class (in object-oriented programming) it doesn't mean functions/methods, modules or classes always correspond to units. From the system-requirements perspective only the perimeter of the system is relevant, thus only entry points to externally-visible system behaviours define units.[10]

Unit tests can be performed manually or via automated test execution. Automated tests include benefits such as: running tests often, running tests without staffing cost, and consistent and repeatable testing.

Testing is often performed by the programmer who writes and modifies the code under test.
Unit testing may be viewed as part of the process of writing code.

This section needs additional citations for verification. Please help improve this article by adding citations to reliable sources in this section. Unsourced material may be challenged and removed. (September 2019) (Learn how and when to remove this message)
During development, a programmer may code criteria, or results that are known to be good, into the test to verify the unit's correctness. 

During test execution, frameworks log tests that fail any criterion and report them in a summary. 

For this, the most commonly used approach is test - function - expected value.

A parameterized test is a test that accepts a set of values that can be used to enable the test to run with multiple, different input values. A testing framework that supports parametrized tests supports a way to encode parameter sets and to run the test with each set.

Use of parametrized tests can reduce test code duplication.

Parameterized tests are supported by TestNG, JUnit,[13] XUnit and NUnit, as well as in various JavaScript test frameworks.[citation needed]

Parameters for the unit tests may be coded manually or in some cases are automatically generated by the test framework. In recent years support was added for writing more powerful (unit) tests, leveraging the concept of theories, test cases that execute the same steps, but using test data generated at runtime, unlike regular parameterized tests that use the same execution steps with input sets that are pre-defined.[citation needed]

Sometimes, in the agile software development, unit testing is done per user story and comes in the later half of the sprint after requirements gathering and development are complete. Typically, the developers or other members from the development team, such as consultants, will write step-by-step 'test scripts' for the developers to execute in the tool. Test scripts are generally written to prove the effective and technical operation of specific developed features in the tool, as opposed to full fledged business processes that would be interfaced by the end user, which is typically done during user acceptance testing. If the test-script can be fully executed from start to finish without incident, the unit test is considered to have "passed", otherwise errors are noted and the user story is moved back to development in an 'in-progress' state. User stories that successfully pass unit tests are moved on to the final steps of the sprint - Code review, peer review, and then lastly a 'show-back' session demonstrating the developed tool to stakeholders.

In test-driven development (TDD), unit tests are written while the production code is written. Starting with working code, the developer adds test code for a required behavior, then adds just enough code to make the test pass, then refactors the code (including test code) as makes sense and then repeats by adding another test.

Unit testing is intended to ensure that the units meet their design and behave as intended.[14]

By writing tests first for the smallest testable units, then the compound behaviors between those, one can build up comprehensive tests for complex applications.[14]

One goal of unit testing is to isolate each part of the program and show that the individual parts are correct.[1] A unit test provides a strict, written contract that the piece of code must satisfy.

Unit testing finds problems early in the development cycle. This includes both bugs in the programmer's implementation and flaws or missing parts of the specification for the unit. The process of writing a thorough set of tests forces the author to think through inputs, outputs, and error conditions, and thus more crisply define the unit's desired behavior.[citation needed]

The cost of finding a bug before coding begins or when the code is first written is considerably lower than the cost of detecting, identifying, and correcting the bug later. Bugs in released code may also cause costly problems for the end-users of the software.[15][16][17] Code can be impossible or difficult to unit test if poorly written, thus unit testing can force developers to structure functions and objects in better ways.

Unit testing enables more frequent releases in software development. By testing individual components in isolation, developers can quickly identify and address issues, leading to faster iteration and release cycles.[18]

Unit testing allows the programmer to refactor code or upgrade system libraries at a later date, and make sure the module still works correctly (e.g., in regression testing). The procedure is to write test cases for all functions and methods so that whenever a change causes a fault, it can be identified quickly. 

Unit tests detect changes which may break a design contract.

Unit testing may reduce uncertainty in the units themselves and can be used in a bottom-up testing style approach. By testing the parts of a program first and then testing the sum of its parts, integration testing becomes much easier.[citation needed]

Some programmers contend that unit tests provide a form of documentation of the code. Developers wanting to learn what functionality is provided by a unit, and how to use it, can review the unit tests to gain an understanding of it.[citation needed]

Test cases can embody characteristics that are critical to the success of the unit. These characteristics can indicate appropriate/inappropriate use of a unit as well as negative behaviors that are to be trapped by the unit. A test case documents these critical characteristics, although many software development environments do not rely solely upon code to document the product in development.[citation needed]

In some processes, the act of writing tests and the code under test, plus associated refactoring, may take the place of formal design. Each unit test can be seen as a design element specifying classes, methods, and observable behavior.[citation needed]

Testing will not catch every error in the program, because it cannot evaluate every execution path in any but the most trivial programs. This problem is a superset of the halting problem, which is undecidable. The same is true for unit testing. Additionally, unit testing by definition only tests the functionality of the units themselves. Therefore, it will not catch integration errors or broader system-level errors (such as functions performed across multiple units, or non-functional test areas such as performance). Unit testing should be done in conjunction with other software testing activities, as they can only show the presence or absence of particular errors; they cannot prove a complete absence of errors. To guarantee correct behavior for every execution path and every possible input, and ensure the absence of errors, other techniques are required, namely the application of formal methods to prove that a software component has no unexpected behavior.[citation needed]

An elaborate hierarchy of unit tests does not equal integration testing. Integration with peripheral units should be included in integration tests, but not in unit tests.[citation needed] Integration testing typically still relies heavily on humans testing manually; high-level or global-scope testing can be difficult to automate, such that manual testing often appears faster and cheaper.[citation needed]

Software testing is a combinatorial problem. For example, every Boolean decision statement requires at least two tests: one with an outcome of "true" and one with an outcome of "false". As a result, for every line of code written, programmers often need 3 to 5 lines of test code.[citation needed] This obviously takes time and its investment may not be worth the effort. There are problems that cannot easily be tested at all – for example those that are nondeterministic or involve multiple threads. In addition, code for a unit test is as likely to be buggy as the code it is testing. Fred Brooks in The Mythical Man-Month quotes: "Never go to sea with two chronometers; take one or three."[19] Meaning, if two chronometers contradict, how do you know which one is correct?

Another challenge related to writing the unit tests is the difficulty of setting up realistic and useful tests. It is necessary to create relevant initial conditions so the part of the application being tested behaves like part of the complete system. If these initial conditions are not set correctly, the test will not be exercising the code in a realistic context, which diminishes the value and accuracy of unit test results.[citation needed]

To obtain the intended benefits from unit testing, rigorous discipline is needed throughout the software development process.

It is essential to keep careful records not only of the tests that have been performed, but also of all changes that have been made to the source code of this or any other unit in the software. Use of a version control system is essential. If a later version of the unit fails a particular test that it had previously passed, the version-control software can provide a list of the source code changes (if any) that have been applied to the unit since that time.[citation needed]

It is also essential to implement a sustainable process for ensuring that test case failures are reviewed regularly and addressed immediately.[20] If such a process is not implemented and ingrained into the team's workflow, the application will evolve out of sync with the unit test suite, increasing false positives and reducing the effectiveness of the test suite.

Unit testing embedded system software presents a unique challenge: Because the software is being developed on a different platform than the one it will eventually run on, you cannot readily run a test program in the actual deployment environment, as is possible with desktop programs.[21]

Unit tests tend to be easiest when a method has input parameters and some output. It is not as easy to create unit tests when a major function of the method is to interact with something external to the application. For example, a method that will work with a database might require a mock up of database interactions to be created, which probably won't be as comprehensive as the real database interactions.[22][better source needed]

Below is an example of a JUnit test suite. It focuses on the Adder class.

The test suite uses assert statements to verify the expected result of various input values to the sum method.

This section does not cite any sources. Please help improve this section by adding citations to reliable sources. Unsourced material may be challenged and removed. (September 2019) (Learn how and when to remove this message)
Using unit-tests as a design specification has one significant advantage over other design methods: The design document (the unit-tests themselves) can itself be used to verify the implementation. The tests will never pass unless the developer implements a solution according to the design.

Unit testing lacks some of the accessibility of a diagrammatic specification such as a UML diagram, but they may be generated from the unit test using automated tools. Most modern languages have free tools (usually available as extensions to IDEs). Free tools, like those based on the xUnit framework, outsource to another system the graphical rendering of a view for human consumption.

Unit testing is the cornerstone of extreme programming, which relies on an automated unit testing framework. This automated unit testing framework can be either third party, e.g., xUnit, or created within the development group.

Extreme programming uses the creation of unit tests for test-driven development. The developer writes a unit test that exposes either a software requirement or a defect. This test will fail because either the requirement isn't implemented yet, or because it intentionally exposes a defect in the existing code. Then, the developer writes the simplest code to make the test, along with other tests, pass.

Most code in a system is unit tested, but not necessarily all paths through the code. Extreme programming mandates a "test everything that can possibly break" strategy, over the traditional "test every execution path" method. This leads developers to develop fewer tests than classical methods, but this isn't really a problem, more a restatement of fact, as classical methods have rarely ever been followed methodically enough for all execution paths to have been thoroughly tested.[citation needed] Extreme programming simply recognizes that testing is rarely exhaustive (because it is often too expensive and time-consuming to be economically viable) and provides guidance on how to effectively focus limited resources.

Crucially, the test code is considered a first class project artifact in that it is maintained at the same quality as the implementation code, with all duplication removed. Developers release unit testing code to the code repository in conjunction with the code it tests. Extreme programming's thorough unit testing allows the benefits mentioned above, such as simpler and more confident code development and refactoring, simplified code integration, accurate documentation, and more modular designs. These unit tests are also constantly run as a form of regression test.

Unit testing is also critical to the concept of Emergent Design. As emergent design is heavily dependent upon refactoring, unit tests are an integral component.[citation needed]

An automated testing framework provides features for automating test execution and can accelerate writing and running tests. Frameworks have been developed for a wide variety of programming languages.

Generally, frameworks are third-party; not distributed with a compiler or integrated development environment (IDE). 

Tests can be written without using a framework to exercise the code under test using assertions, exception handling, and other control flow mechanisms to verify behavior and report failure. Some note that testing without a framework is valuable since there is a barrier to entry for the adoption of a framework; that having some tests is better than none, but once a framework is in place, adding tests can be easier.[23]

In some frameworks advanced test features are missing and must be hand-coded.

Some programming languages directly support unit testing. Their grammar allows the direct declaration of unit tests without importing a library (whether third party or standard). Additionally, the Boolean conditions of the unit tests can be expressed in the same syntax as Boolean expressions used in non-unit test code, such as what is used for if and while statements.

Languages with built-in unit testing support include:

Cobra
D[24]
Rust[25]
Languages with standard unit testing framework support include:

Apex
Crystal[26]
Erlang
Go[27]
Julia[28]
LabVIEW
MATLAB
Python[29]
Racket[30][31]
Ruby[32]
Some languages do not have built-in unit-testing support but have established unit testing libraries or frameworks. These languages include:

ABAP
C++
C#
Clojure[33]
Elixir
Java
JavaScript
Objective-C
Perl
PHP
PowerShell[34]
R with testthat
Scala
tcl
Visual Basic .NET
Xojo with XojoUnit
Acceptance testing
Characterization test
Component-based usability testing
Design predicates
Design by contract
Extreme programming
Functional testing
Integration testing
List of unit testing frameworks
Regression testing
Software archaeology
Software testing
System testing
Test case
Test-driven development
xUnit – a family of unit testing frameworks.
Unit testingExtreme programmingTypes of tools used in software development
CS1 maint: date and yearArticles with short descriptionShort description is different from WikidataUse dmy dates from April 2020Articles needing additional references from September 2019All articles needing additional referencesArticles with excerptsAll articles with unsourced statementsArticles with unsourced statements from November 2023Articles with unsourced statements from January 2013Articles with unsourced statements from September 2019Articles with unsourced statements from October 2010Articles with unsourced statements from January 2010All articles lacking reliable referencesArticles lacking reliable references from February 2019Articles with unsourced statements from November 2008Articles with example Java code




