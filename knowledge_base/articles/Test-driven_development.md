


(Top)





1
History








2
Coding cycle








3
Test-driven work








4
Development style




Toggle Development style subsection





4.1
Code visibility








4.2
Fakes, mocks and integration tests








4.3
Keep the unit small










5
Best practices




Toggle Best practices subsection





5.1
Test structure








5.2
Individual best practices








5.3
Practices to avoid, or "anti-patterns"










6
Comparison and demarcation




Toggle Comparison and demarcation subsection





6.1
TDD and ATDD








6.2
TDD and BDD










7
Software for TDD




Toggle Software for TDD subsection





7.1
xUnit frameworks








7.2
TAP results










8
TDD for complex systems




Toggle TDD for complex systems subsection





8.1
Designing for testability








8.2
Managing tests for large teams










9
Advantages and Disadvantages of Test Driven Development




Toggle Advantages and Disadvantages of Test Driven Development subsection





9.1
Advantages








9.2
Disadvantages








9.3
Benefits








9.4
Psychological benefits to programmer








9.5
Limitations










10
Conference








11
See also








12
References








13
External links
















4.1
Code visibility








4.2
Fakes, mocks and integration tests








4.3
Keep the unit small
















5.1
Test structure








5.2
Individual best practices








5.3
Practices to avoid, or "anti-patterns"
















6.1
TDD and ATDD








6.2
TDD and BDD














7.1
xUnit frameworks








7.2
TAP results














8.1
Designing for testability








8.2
Managing tests for large teams














9.1
Advantages








9.2
Disadvantages








9.3
Benefits








9.4
Psychological benefits to programmer








9.5
Limitations
























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
Test-driven development (TDD) is a way of writing code that involves writing an automated unit-level test case that fails, then writing just enough code to make the test pass, then refactoring both the test code and the production code, then repeating with another new test case.

Alternative approaches to writing automated tests is to write all of the production code before starting on the test code or to write all of the test code before starting on the production code. With TDD, both are written together, therefore shortening debugging time necessities[1].

TDD is related to the test-first programming concepts of extreme programming, begun in 1999,[2] but more recently has created more general interest in its own right.[3]

Programmers also apply the concept to improving and debugging legacy code developed with older techniques.[4]

Software engineer Kent Beck, who is credited with having developed or "rediscovered"[5] the technique, stated in 2003 that TDD encourages simple designs and inspires confidence.[6]

The original description of TDD was in an ancient book about programming. It said you take the input tape, manually type in the output tape you expect, then program until the actual output tape matches the expected output. After I'd written the first xUnit framework in Smalltalk I remembered reading this and tried it out. That was the origin of TDD for me. When describing TDD to older programmers, I often hear, "Of course. How else could you program?" Therefore I refer to my role as "rediscovering" TDD.
The TDD steps vary somewhat by author in count and description, but are generally as follows. These are based on the book Test-Driven Development by Example,[6] and Kent Beck's Canon TDD article.

moving code to where it most logically belongs
removing duplicate code
making names self-documenting
splitting methods into smaller pieces
re-arranging inheritance hierarchies
Each tests should be small and commits made often. If new code fails some tests, the programmer can undo or revert rather than debug excessively. 

When using external libraries, it is important not to write tests that are so small as to effectively test merely the library itself,[3] unless there is some reason to believe that the library is buggy or not feature-rich enough to serve all the needs of the software under development.

TDD has been adopted outside of software development, in both product and service teams, as test-driven work.[7] For testing to be successful, it needs to be practiced at the micro and macro levels. Every method in a class, every input data value, log message, and error code, amongst other data points, need to be tested.[8] Similar to TDD, non-software teams develop quality control (QC) checks (usually manual tests rather than automated tests) for each aspect of the work prior to commencing. These QC checks are then used to inform the design and validate the associated outcomes. The six steps of the TDD sequence are applied with minor semantic changes:

"Add a check" replaces "Add a test"
"Run all checks" replaces "Run all tests"
"Do the work" replaces "Write some code"
"Run all checks" replaces "Run tests"
"Clean up the work" replaces "Refactor code"
"Repeat"
There are various aspects to using test-driven development, for example the principles of "keep it simple, stupid" (KISS) and "You aren't gonna need it" (YAGNI). By focusing on writing only the code necessary to pass tests, designs can often be cleaner and clearer than is achieved by other methods.[6] In Test-Driven Development by Example, Kent Beck also suggests the principle "Fake it till you make it".

To achieve some advanced design concept such as a design pattern, tests are written that generate that design. The code may remain simpler than the target pattern, but still pass all required tests. This can be unsettling at first but it allows the developer to focus only on what is important.

Writing the tests first: The tests should be written before the functionality that is to be tested. This has been claimed to have many benefits. It helps ensure that the application is written for testability, as the developers must consider how to test the application from the outset rather than adding it later. It also ensures that tests for every feature gets written. Additionally, writing the tests first leads to a deeper and earlier understanding of the product requirements, ensures the effectiveness of the test code, and maintains a continual focus on software quality.[9] When writing feature-first code, there is a tendency by developers and organizations to push the developer on to the next feature, even neglecting testing entirely. The first TDD test might not even compile at first, because the classes and methods it requires may not yet exist. Nevertheless, that first test functions as the beginning of an executable specification.[10]

Each test case fails initially: This ensures that the test really works and can catch an error. Once this is shown, the underlying functionality can be implemented. This has led to the "test-driven development mantra", which is "red/green/refactor", where red means fail and green means pass. Test-driven development constantly repeats the steps of adding test cases that fail, passing them, and refactoring. Receiving the expected test results at each stage reinforces the developer's mental model of the code, boosts confidence and increases productivity.

Test code needs access to the code it is testing, but testing should not compromise normal design goals such as information hiding, encapsulation and the separation of concerns. Therefore, unit test code is usually located in the same project or module as the code being tested.

In object oriented design this still does not provide access to private data and methods. Therefore, extra work may be necessary for unit tests. In Java and other languages, a developer can use reflection to access private fields and methods.[11] Alternatively, an inner class can be used to hold the unit tests so they have visibility of the enclosing class's members and attributes. In the .NET Framework and some other programming languages, partial classes may be used to expose private methods and data for the tests to access.

It is important that such testing hacks do not remain in the production code. In C and other languages, compiler directives such as #if DEBUG ... #endif can be placed around such additional classes and indeed all other test-related code to prevent them being compiled into the released code. This means the released code is not exactly the same as what was unit tested. The regular running of fewer but more comprehensive, end-to-end, integration tests on the final release build can ensure (among other things) that no production code exists that subtly relies on aspects of the test harness.

There is some debate among practitioners of TDD, documented in their blogs and other writings, as to whether it is wise to test private methods and data anyway. Some argue that private members are a mere implementation detail that may change, and should be allowed to do so without breaking numbers of tests. Thus it should be sufficient to test any class through its public interface or through its subclass interface, which some languages call the "protected" interface.[12] Others say that crucial aspects of functionality may be implemented in private methods and testing them directly offers advantage of smaller and more direct unit tests.[13][14]

Unit tests are so named because they each test one unit of code. A complex module may have a thousand unit tests and a simple module may have only ten. The unit tests used for TDD should never cross process boundaries in a program, let alone network connections. Doing so introduces delays that make tests run slowly and discourage developers from running the whole suite. Introducing dependencies on external modules or data also turns unit tests into integration tests. If one module misbehaves in a chain of interrelated modules, it is not so immediately clear where to look for the cause of the failure.

When code under development relies on a database, a web service, or any other external process or service, enforcing a unit-testable separation is also an opportunity and a driving force to design more modular, more testable and more reusable code.[15] Two steps are necessary:

Whenever external access is needed in the final design, an interface should be defined that describes the access available. See the dependency inversion principle for a discussion of the benefits of doing this regardless of TDD.
The interface should be implemented in two ways, one of which really accesses the external process, and the other of which is a fake or mock. Fake objects need do little more than add a message such as "Person object saved" to a trace log, against which a test assertion can be run to verify correct behaviour. Mock objects differ in that they themselves contain test assertions that can make the test fail, for example, if the person's name and other data are not as expected.
Fake and mock object methods that return data, ostensibly from a data store or user, can help the test process by always returning the same, realistic data that tests can rely upon. They can also be set into predefined fault modes so that error-handling routines can be developed and reliably tested. In a fault mode, a method may return an invalid, incomplete or null response, or may throw an exception. Fake services other than data stores may also be useful in TDD: A fake encryption service may not, in fact, encrypt the data passed; a fake random number service may always return 1. Fake or mock implementations are examples of dependency injection.

A test double is a test-specific capability that substitutes for a system capability, typically a class or function, that the UUT depends on. There are two times at which test doubles can be introduced into a system: link and execution. Link time substitution is when the test double is compiled into the load module, which is executed to validate testing. This approach is typically used when running in an environment other than the target environment that requires doubles for the hardware level code for compilation. The alternative to linker substitution is run-time substitution in which the real functionality is replaced during the execution of a test case. This substitution is typically done through the reassignment of known function pointers or object replacement.

Test doubles are of a number of different types and varying complexities:

Dummy – A dummy is the simplest form of a test double. It facilitates linker time substitution by providing a default return value where required.
Stub – A stub adds simplistic logic to a dummy, providing different outputs.
Spy – A spy captures and makes available parameter and state information, publishing accessors to test code for private information allowing for more advanced state validation.
Mock – A mock is specified by an individual test case to validate test-specific behavior, checking parameter values and call sequencing.
Simulator – A simulator is a comprehensive component providing a higher-fidelity approximation of the target capability (the thing being doubled). A simulator typically requires significant additional development effort.[9]
A corollary of such dependency injection is that the actual database or other external-access code is never tested by the TDD process itself. To avoid errors that may arise from this, other tests are needed that instantiate the test-driven code with the "real" implementations of the interfaces discussed above. These are integration tests and are quite separate from the TDD unit tests. There are fewer of them, and they must be run less often than the unit tests. They can nonetheless be implemented using the same testing framework.

Integration tests that alter any persistent store or database should always be designed carefully with consideration of the initial and final state of the files or database, even if any test fails. This is often achieved using some combination of the following techniques:

The TearDown method, which is integral to many test frameworks.
try...catch...finally exception handling structures where available.
Database transactions where a transaction atomically includes perhaps a write, a read and a matching delete operation.
Taking a "snapshot" of the database before running any tests and rolling back to the snapshot after each test run. This may be automated using a framework such as Ant or NAnt or a continuous integration system such as CruiseControl.
Initialising the database to a clean state before tests, rather than cleaning up after them. This may be relevant where cleaning up may make it difficult to diagnose test failures by deleting the final state of the database before detailed diagnosis can be performed.
For TDD, a unit is most commonly defined as a class, or a group of related functions often called a module. Keeping units relatively small is claimed to provide critical benefits, including:

Reduced debugging effort – When test failures are detected, having smaller units aids in tracking down errors.
Self-documenting tests – Small test cases are easier to read and to understand.[9]
Advanced practices of test-driven development can lead to acceptance test–driven development (ATDD) and specification by example where the criteria specified by the customer are automated into acceptance tests, which then drive the traditional unit test-driven development (UTDD) process.[16] This process ensures the customer has an automated mechanism to decide whether the software meets their requirements. With ATDD, the development team now has a specific target to satisfy – the acceptance tests – which keeps them continuously focused on what the customer really wants from each user story.

Effective layout of a test case ensures all required actions are completed, improves the readability of the test case, and smooths the flow of execution. Consistent structure helps in building a self-documenting test case. A commonly applied structure for test cases has (1) setup, (2) execution, (3) validation, and (4) cleanup.

Setup: Put the Unit Under Test (UUT) or the overall test system in the state needed to run the test.
Execution: Trigger/drive the UUT to perform the target behavior and capture all output, such as return values and output parameters. This step is usually very simple.
Validation: Ensure the results of the test are correct. These results may include explicit outputs captured during execution or state changes in the UUT.
Cleanup: Restore the UUT or the overall test system to the pre-test state. This restoration permits another test to execute immediately after this one. In some cases, in order to preserve the information for possible test failure analysis, the cleanup should be starting the test just before the test's setup run. [9]
Some best practices that an individual could follow would be to separate common set-up and tear-down logic into test support services utilized by the appropriate test cases, to keep each test oracle focused on only the results necessary to validate its test, and to design time-related tests to allow tolerance for execution in non-real time operating systems. The common practice of allowing a 5-10 percent margin for late execution reduces the potential number of false negatives in test execution. It is also suggested to treat test code with the same respect as production code. Test code must work correctly for both positive and negative cases, last a long time, and be readable and maintainable. Teams can get together and review tests and test practices to share effective techniques and catch bad habits.[17]

Having test cases depend on system state manipulated from previously executed test cases (i.e., you should always start a unit test from a known and pre-configured state).
Dependencies between test cases. A test suite where test cases are dependent upon each other is brittle and complex. Execution order should not be presumed. Basic refactoring of the initial test cases or structure of the UUT causes a spiral of increasingly pervasive impacts in associated tests.
Interdependent tests. Interdependent tests can cause cascading false negatives. A failure in an early test case breaks a later test case even if no actual fault exists in the UUT, increasing defect analysis and debug efforts.
Testing precise execution, behavior, timing or performance.
Building "all-knowing oracles". An oracle that inspects more than necessary is more expensive and brittle over time. This very common error is dangerous because it causes a subtle but pervasive time sink across the complex project.[17][clarification needed]
Testing implementation details.
Slow running tests.
Test-driven development is related to, but different from acceptance test–driven development (ATDD).[18] TDD is primarily a developer's tool to help create well-written unit of code (function, class, or module) that correctly performs a set of operations. ATDD is a communication tool between the customer, developer, and tester to ensure that the requirements are well-defined. TDD requires test automation. ATDD does not, although automation helps with regression testing. Tests used in TDD can often be derived from ATDD tests, since the code units implement some portion of a requirement. ATDD tests should be readable by the customer. TDD tests do not need to be.

BDD (behavior-driven development) combines practices from TDD and from ATDD.[19]
It includes the practice of writing tests first, but focuses on tests which describe behavior, rather than tests which test a unit of implementation. Tools such as JBehave, Cucumber, Mspec and Specflow provide syntaxes which allow product owners, developers and test engineers to define together the behaviors which can then be translated into automated tests.

There are many testing frameworks and tools that are useful in TDD.

Developers may use computer-assisted testing frameworks, commonly collectively named xUnit (which are derived from SUnit, created in 1998), to create and automatically run the test cases. xUnit frameworks provide assertion-style test validation capabilities and result reporting. These capabilities are critical for automation as they move the burden of execution validation from an independent post-processing activity to one that is included in the test execution. The execution framework provided by these test frameworks allows for the automatic execution of all system test cases or various subsets along with other features.[20]

Testing frameworks may accept unit test output in the language-agnostic Test Anything Protocol created in 1987.

Exercising TDD on large, challenging systems requires a modular architecture, well-defined components with published interfaces, and disciplined system layering with maximization of platform independence. These proven practices yield increased testability and facilitate the application of build and test automation.[9]

Complex systems require an architecture that meets a range of requirements. A key subset of these requirements includes support for the complete and effective testing of the system. Effective modular design yields components that share traits essential for effective TDD.

High Cohesion ensures each unit provides a set of related capabilities and makes the tests of those capabilities easier to maintain.
Low Coupling allows each unit to be effectively tested in isolation.
Published Interfaces restrict Component access and serve as contact points for tests, facilitating test creation and ensuring the highest fidelity between test and production unit configuration.
A key technique for building effective modular architecture is Scenario Modeling where a set of sequence charts is constructed, each one focusing on a single system-level execution scenario. The Scenario Model provides an excellent vehicle for creating the strategy of interactions between components in response to a specific stimulus. Each of these Scenario Models serves as a rich set of requirements for the services or functions that a component must provide, and it also dictates the order in which these components and services interact together. Scenario modeling can greatly facilitate the construction of TDD tests for a complex system.[9]

In a larger system, the impact of poor component quality is magnified by the complexity of interactions. This magnification makes the benefits of TDD accrue even faster in the context of larger projects. However, the complexity of the total population of tests can become a problem in itself, eroding potential gains. It sounds simple, but a key initial step is to recognize that test code is also important software and should be produced and maintained with the same rigor as the production code.

Creating and managing the architecture of test software within a complex system is just as important as the core product architecture. Test drivers interact with the UUT, test doubles and the unit test framework.[9]

Test Driven Development (TDD) is a software development approach where tests are written before the actual code. It offers several advantages:

Comprehensive Test Coverage: TDD ensures that all new code is covered by at least one test, leading to more robust software.
Enhanced Confidence in Code: Developers gain greater confidence in the code's reliability and functionality.
Well-Documented Code: The process naturally results in well-documented code, as each test clarifies the purpose of the code it tests.
Requirement Clarity: TDD encourages a clear understanding of requirements before coding begins.
Facilitates Continuous Integration: It integrates well with continuous integration processes, allowing for frequent code updates and testing.
Boosts Productivity: Many developers find that TDD increases their productivity.
Reinforces Code Mental Model: TDD helps in building a strong mental model of the code's structure and behavior.
Emphasis on Design and Functionality: It encourages a focus on the design, interface, and overall functionality of the program.
Reduces Need for Debugging: By catching issues early in the development process, TDD reduces the need for extensive debugging later.
System Stability: Applications developed with TDD tend to be more stable and less prone to bugs.[21]
However, TDD is not without its drawbacks:

Increased Code Volume: Implementing TDD can result in a larger codebase as tests add to the total amount of code written.
False Security from Tests: A large number of passing tests can sometimes give a misleading sense of security regarding the code's robustness[22].
Maintenance Overheads: Maintaining a large suite of tests can add overhead to the development process.
Time-Consuming Test Processes: Writing and maintaining tests can be time-consuming.
Testing Environment Set-Up: TDD requires setting up and maintaining a suitable testing environment.
Learning Curve: It takes time and effort to become proficient in TDD practices.
Overcomplication: An overemphasis on TDD can lead to code that is more complex than necessary.
Neglect of Overall Design: Focusing too narrowly on passing tests can sometimes lead to neglect of the bigger picture in software design.
Increased Costs: The additional time and resources required for TDD can result in higher development costs.
A 2005 study found that using TDD meant writing more tests and, in turn, programmers who wrote more tests tended to be more productive.[23] Hypotheses relating to code quality and a more direct correlation between TDD and productivity were inconclusive.[24]

Programmers using pure TDD on new ("greenfield") projects reported they only rarely felt the need to invoke a debugger. Used in conjunction with a version control system, when tests fail unexpectedly, reverting the code to the last version that passed all tests may often be more productive than debugging.[25]

Test-driven development offers more than just simple validation of correctness, but can also drive the design of a program.[26] By focusing on the test cases first, one must imagine how the functionality is used by clients (in the first case, the test cases). So, the programmer is concerned with the interface before the implementation. This benefit is complementary to design by contract as it approaches code through test cases rather than through mathematical assertions or preconceptions.

Test-driven development offers the ability to take small steps when required. It allows a programmer to focus on the task at hand as the first goal is to make the test pass. Exceptional cases and error handling are not considered initially, and tests to create these extraneous circumstances are implemented separately. Test-driven development ensures in this way that all written code is covered by at least one test. This gives the programming team, and subsequent users, a greater level of confidence in the code.

While it is true that more code is required with TDD than without TDD because of the unit test code, the total code implementation time could be shorter based on a model by Müller and Padberg.[27] Large numbers of tests help to limit the number of defects in the code. The early and frequent nature of the testing helps to catch defects early in the development cycle, preventing them from becoming endemic and expensive problems. Eliminating defects early in the process usually avoids lengthy and tedious debugging later in the project.

TDD can lead to more modularized, flexible, and extensible code. This effect often comes about because the methodology requires that the developers think of the software in terms of small units that can be written and tested independently and integrated together later. This leads to smaller, more focused classes, looser coupling, and cleaner interfaces. The use of the mock object design pattern also contributes to the overall modularization of the code because this pattern requires that the code be written so that modules can be switched easily between mock versions for unit testing and "real" versions for deployment.

Because no more code is written than necessary to pass a failing test case, automated tests tend to cover every code path. For example, for a TDD developer to add an else branch to an existing if statement, the developer would first have to write a failing test case that motivates the branch. As a result, the automated tests resulting from TDD tend to be very thorough: they detect any unexpected changes in the code's behaviour. This detects problems that can arise where a change later in the development cycle unexpectedly alters other functionality.

Madeyski[28] provided empirical evidence (via a series of laboratory experiments with over 200 developers) regarding the superiority of the TDD practice over the traditional Test-Last approach or testing for correctness approach, with respect to the lower coupling between objects (CBO). The mean effect size represents a medium (but close to large) effect on the basis of meta-analysis of the performed experiments which is a substantial finding. It suggests a better modularization (i.e., a more modular design), easier reuse and testing of the developed software products due to the TDD programming practice.[28] Madeyski also measured the effect of the TDD practice on unit tests using branch coverage (BC) and mutation score indicator (MSI),[29][30][31] which are indicators of the thoroughness and the fault detection effectiveness of unit tests, respectively. The effect size of TDD on branch coverage was medium in size and therefore is considered substantive effect.[28] These findings have been subsequently confirmed by further, smaller experimental evaluations of TDD.[32][33][34][35]

Increased Confidence: TDD allows programmers to make changes or add new features with confidence. Knowing that the code is constantly tested reduces the fear of breaking existing functionality. This safety net can encourage more innovative and creative approaches to problem-solving.
Reduced Fear of Change, Reduced Stress: In traditional development, changing existing code can be daunting due to the risk of introducing bugs. TDD, with its comprehensive test suite, reduces this fear, as tests will immediately reveal any problems caused by changes. Knowing that the codebase has a safety net of tests can reduce stress and anxiety associated with programming. Developers might feel more relaxed and open to experimenting and refactoring.
Improved Focus: Writing tests first helps programmers concentrate on requirements and design before writing the code. This focus can lead to clearer, more purposeful coding, as the developer is always aware of the goal they are trying to achieve.
Sense of Achievement and Job Satisfaction: Passing tests can provide a quick, regular sense of accomplishment, boosting morale. This can be particularly motivating in long-term projects where the end goal might seem distant. The combination of all these factors can lead to increased job satisfaction. When developers feel confident, focused, and part of a collaborative team, their overall job satisfaction can significantly improve.
This section needs additional citations for verification. Please help improve this article by adding citations to reliable sources in this section. Unsourced material may be challenged and removed. (August 2013) (Learn how and when to remove this message)
Test-driven development does not perform sufficient testing in situations where full functional tests are required to determine success or failure, due to extensive use of unit tests.[36] Examples of these are user interfaces, programs that work with databases, and some that depend on specific network configurations. TDD encourages developers to put the minimum amount of code into such modules and to maximize the logic that is in testable library code, using fakes and mocks to represent the outside world.[37]

Management support is essential. Without the entire organization believing that test-driven development is going to improve the product, management may feel that time spent writing tests is wasted.[38]

Unit tests created in a test-driven development environment are typically created by the developer who is writing the code being tested. Therefore, the tests may share blind spots with the code: if, for example, a developer does not realize that certain input parameters must be checked, most likely neither the test nor the code will verify those parameters. Another example: if the developer misinterprets the requirements for the module they are developing, the code and the unit tests they write will both be wrong in the same way. Therefore, the tests will pass, giving a false sense of correctness.

A high number of passing unit tests may bring a false sense of security, resulting in fewer additional software testing activities, such as integration testing and compliance testing.

Tests become part of the maintenance overhead of a project. Badly written tests, for example ones that include hard-coded error strings, are themselves prone to failure, and they are expensive to maintain. This is especially the case with fragile tests.[39] There is a risk that tests that regularly generate false failures will be ignored, so that when a real failure occurs, it may not be detected. It is possible to write tests for low and easy maintenance, for example by the reuse of error strings, and this should be a goal during the code refactoring phase described above.

Writing and maintaining an excessive number of tests costs time. Also, more-flexible modules (with limited tests) might accept new requirements without the need for changing the tests. For those reasons, testing for only extreme conditions, or a small sample of data, can be easier to adjust than a set of highly detailed tests.

The level of coverage and testing detail achieved during repeated TDD cycles cannot easily be re-created at a later date. Therefore, these original, or early, tests become increasingly precious as time goes by. The tactic is to fix it early. Also, if a poor architecture, a poor design, or a poor testing strategy leads to a late change that makes dozens of existing tests fail, then it is important that they are individually fixed. Merely deleting, disabling or rashly altering them can lead to undetectable holes in the test coverage.

First TDD Conference was held during July 2021.[40] Conferences were recorded on YouTube[41]

Acceptance testing
Behavior-driven development
Design by contract
Inductive programming
Integration testing
List of software development philosophies
List of unit testing frameworks
Mock object
Programming by example
Sanity check
Self-testing code
Software testing
Test case
Transformation Priority Premise
Unit testing
Continuous test-driven development
Extreme programmingSoftware development philosophiesSoftware development processSoftware testing
Articles with short descriptionShort description is different from WikidataWikipedia articles needing clarification from February 2022Articles needing additional references from August 2013All articles needing additional references




