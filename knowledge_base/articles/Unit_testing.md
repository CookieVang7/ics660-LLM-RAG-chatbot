



From Wikipedia, the free encyclopedia


Validating the behavior of isolated source code






| Part of a series on |
| --- |
| [Software development](/wiki/Software_development "Software development") |
| Core activities * [Data modeling](/wiki/Data_modeling "Data modeling") * [Processes](/wiki/Software_development_process "Software development process") * [Requirements](/wiki/Requirements_analysis "Requirements analysis") * [Design](/wiki/Software_design "Software design") * [Construction](/wiki/Software_construction "Software construction") * [Engineering](/wiki/Software_engineering "Software engineering") * [Testing](/wiki/Software_testing "Software testing") * [Debugging](/wiki/Debugging "Debugging") * [Deployment](/wiki/Software_deployment "Software deployment") * [Maintenance](/wiki/Software_maintenance "Software maintenance") |
| Paradigms and models * [Agile](/wiki/Agile_software_development "Agile software development") * [Cleanroom](/wiki/Cleanroom_software_engineering "Cleanroom software engineering") * [Incremental](/wiki/Incremental_build_model "Incremental build model") * [Prototyping](/wiki/Software_prototyping "Software prototyping") * [Spiral](/wiki/Spiral_model "Spiral model") * [V model](/wiki/V-model_(software_development) "V-model (software development)") * [Waterfall](/wiki/Waterfall_model "Waterfall model") |
| [Methodologies](/wiki/Software_development_methodology "Software development methodology") and frameworks * [ASD](/wiki/Adaptive_software_development "Adaptive software development") * [DevOps](/wiki/DevOps "DevOps") * [DAD](/wiki/Disciplined_agile_delivery "Disciplined agile delivery") * [DSDM](/wiki/Dynamic_systems_development_method "Dynamic systems development method") * [FDD](/wiki/Feature-driven_development "Feature-driven development") * [IID](/wiki/Iterative_and_incremental_development "Iterative and incremental development") * [Kanban](/wiki/Kanban_(development) "Kanban (development)") * [Lean SD](/wiki/Lean_software_development "Lean software development") * [LeSS](/wiki/Scrum_(software_development)#Large-scale_Scrum "Scrum (software development)") * [MDD](/wiki/Model-driven_development "Model-driven development") * [MSF](/wiki/Microsoft_Solutions_Framework "Microsoft Solutions Framework") * [PSP](/wiki/Personal_software_process "Personal software process") * [RAD](/wiki/Rapid_application_development "Rapid application development") * [RUP](/wiki/Rational_Unified_Process "Rational Unified Process") * [SAFe](/wiki/Scaled_agile_framework "Scaled agile framework") * [Scrum](/wiki/Scrum_(software_development) "Scrum (software development)") * [SEMAT](/wiki/SEMAT "SEMAT") * [TDD](/wiki/Test-driven_development "Test-driven development") * [TSP](/wiki/Team_software_process "Team software process") * [OpenUP](/wiki/OpenUP "OpenUP") * [UP](/wiki/Unified_Process "Unified Process") * [XP](/wiki/Extreme_programming "Extreme programming") |
| Supporting disciplines * [Configuration management](/wiki/Software_configuration_management "Software configuration management") * [Documentation](/wiki/Software_documentation "Software documentation") * [Software quality assurance](/wiki/Software_quality_assurance "Software quality assurance") * [Project management](/wiki/Software_project_management "Software project management") * [User experience](/wiki/User_experience "User experience") |
| Practices * [ATDD](/wiki/Acceptance_test%E2%80%93driven_development "Acceptance test–driven development") * [BDD](/wiki/Behavior-driven_development "Behavior-driven development") * [CCO](/wiki/Extreme_programming_practices#Collective_code_ownership "Extreme programming practices") * [CI](/wiki/Continuous_integration "Continuous integration") * [CD](/wiki/Continuous_delivery "Continuous delivery") * [DDD](/wiki/Domain-driven_design "Domain-driven design") * [PP](/wiki/Pair_programming "Pair programming") * [SBE](/wiki/Specification_by_example "Specification by example") * [Stand-up](/wiki/Stand-up_meeting "Stand-up meeting") * [TDD](/wiki/Test-driven_development "Test-driven development") |
| [Tools](/wiki/Programming_tool "Programming tool") * [Compiler](/wiki/Compiler "Compiler") * [Debugger](/wiki/Debugger "Debugger") * [Profiler](/wiki/Profiling_(computer_programming) "Profiling (computer programming)") * [GUI designer](/wiki/Graphical_user_interface_builder "Graphical user interface builder") * [UML Modeling](/wiki/UML_tool "UML tool") * [IDE](/wiki/Integrated_development_environment "Integrated development environment") * [Build automation](/wiki/Build_automation "Build automation") * [Release automation](/wiki/Application-release_automation "Application-release automation") * [Infrastructure as code](/wiki/Infrastructure_as_code "Infrastructure as code") |
| Standards and bodies of knowledge * [CMMI](/wiki/Capability_Maturity_Model_Integration "Capability Maturity Model Integration") * [IEEE standards](/wiki/IEEE_Standards_Association "IEEE Standards Association") * [ISO 9001](/wiki/ISO_9001 "ISO 9001") * [ISO/IEC standards](/wiki/ISO/IEC_JTC_1/SC_7 "ISO/IEC JTC 1/SC 7") * [PMBOK](/wiki/Project_Management_Body_of_Knowledge "Project Management Body of Knowledge") * [SWEBOK](/wiki/Software_Engineering_Body_of_Knowledge "Software Engineering Body of Knowledge") * [ITIL](/wiki/ITIL "ITIL") * [IREB](/wiki/International_Requirements_Engineering_Board "International Requirements Engineering Board") * [OMG](/wiki/Object_Management_Group "Object Management Group") |
| Glossaries * [Artificial intelligence](/wiki/Glossary_of_artificial_intelligence "Glossary of artificial intelligence") * [Computer science](/wiki/Glossary_of_computer_science "Glossary of computer science") * [Electrical and electronics engineering](/wiki/Glossary_of_electrical_and_electronics_engineering "Glossary of electrical and electronics engineering") |
| Outlines * [Outline of software development](/wiki/Outline_of_software_development "Outline of software development") |
| * [v](/wiki/Template:Software_development_process "Template:Software development process") * [t](/wiki/Template_talk:Software_development_process "Template talk:Software development process") * [e](/wiki/Special:EditPage/Template:Software_development_process "Special:EditPage/Template:Software development process") |


**Unit testing**, a.k.a. **component** or **module** testing, is a form of [software testing](/wiki/Software_testing "Software testing") by which isolated [source code](/wiki/Source_code "Source code") is tested to validate expected behavior.[[1]](#cite_note-kolawa-1)


Unit testing describes tests that are run at the unit-level to contrast testing at the [integration](/wiki/Integration_testing "Integration testing") or [system](/wiki/System_testing "System testing") level.




History[[edit](/w/index.php?title=Unit_testing&action=edit&section=1 "Edit section: History")]
----------------------------------------------------------------------------------------------


Unit testing, as principle for testing separately smaller parts of large software systems dates back to the early days of software engineering. In June 1956, H.D. Benington presented at US Navy's Symposium on Advanced Programming Methods for Digital Computers the [SAGE](/wiki/Semi-Automatic_Ground_Environment "Semi-Automatic Ground Environment") project and its specification based approach where the coding phase was followed by "parameter testing" to validate component subprograms against their specification, followed then by an "assembly testing" for parts put together.[[2]](#cite_note-2)[[3]](#cite_note-:0-3)


In 1964, a similar approach is described for the software of the [Mercury project](/wiki/Project_Mercury "Project Mercury"), where individual units developed by different programmes underwent "unit tests" before being integrated together.[[4]](#cite_note-4) In 1969, testing methodologies appear more structured, with unit tests, component tests and integration tests with the purpose of validating individual parts written separately and their progressive assembly into larger blocks.[[5]](#cite_note-5) Some public standards adopted end of the 60's, such as MIL-STD-483[[6]](#cite_note-6) and MIL-STD-490 contributed further to a wide acceptance of unit testing in large projects. 


Unit testing was in those times interactive[[3]](#cite_note-:0-3) or automated,[[7]](#cite_note-7) using either coded tests or [capture and replay testing](/wiki/Capture_and_replay_testing "Capture and replay testing") tools. In 1989, [Kent Beck](/wiki/Kent_Beck "Kent Beck") described a testing framework for [Smalltalk](/wiki/Smalltalk "Smalltalk") (later called [SUnit](/wiki/SUnit "SUnit")) in "[Simple Smalltalk Testing: With Patterns](https://web.archive.org/web/20150315073817/http://www.xprogramming.com/testfram.htm)". In 1997, [Kent Beck](/wiki/Kent_Beck "Kent Beck") and [Erich Gamma](/wiki/Erich_Gamma "Erich Gamma") developed and released [JUnit](/wiki/JUnit "JUnit"), a unit test framework that became popular with [Java](/wiki/Java_(programming_language) "Java (programming language)") developers.[[8]](#cite_note-8) [Google](/wiki/Google "Google") embraced automated testing around 2005–2006.[[9]](#cite_note-9)



Unit[[edit](/w/index.php?title=Unit_testing&action=edit&section=2 "Edit section: Unit")]
----------------------------------------------------------------------------------------


Unit is defined as a single behaviour exhibited by the system under test (SUT), usually corresponding to a requirement. While it may imply it's a function or a module (in [procedural programming](/wiki/Procedural_programming "Procedural programming")) or a method or a class (in [object-oriented programming](/wiki/Object-oriented_programming "Object-oriented programming")) it doesn't mean functions/methods, modules or classes always correspond to units. From the system-requirements perspective only the perimeter of the system is relevant, thus only entry points to externally-visible system behaviours define units.[[10]](#cite_note-10)



Execution[[edit](/w/index.php?title=Unit_testing&action=edit&section=3 "Edit section: Execution")]
--------------------------------------------------------------------------------------------------


Unit tests can be performed manually or via [automated test](/wiki/Automated_test "Automated test") execution. Automated tests include benefits such as: running tests often, running tests without staffing cost, and consistent and repeatable testing.


Testing is often performed by the programmer who writes and modifies the code under test.
Unit testing may be viewed as part of the process of writing code.



Testing criteria[[edit](/w/index.php?title=Unit_testing&action=edit&section=4 "Edit section: Testing criteria")]
----------------------------------------------------------------------------------------------------------------




|  | This section **needs additional citations for [verification](/wiki/Wikipedia:Verifiability "Wikipedia:Verifiability")**. Please help [improve this article](/wiki/Special:EditPage/Unit_testing "Special:EditPage/Unit testing") by [adding citations to reliable sources](/wiki/Help:Referencing_for_beginners "Help:Referencing for beginners") in this section. Unsourced material may be challenged and removed. *(September 2019)* *([Learn how and when to remove this message](/wiki/Help:Maintenance_template_removal "Help:Maintenance template removal"))* |
| --- | --- |


During development, a programmer may code criteria, or results that are known to be good, into the test to verify the unit's correctness. 


During test execution, frameworks [log](/wiki/Computer_data_logging "Computer data logging") tests that fail any criterion and report them in a summary. 


For this, the most commonly used approach is test - function - expected value.



Test case[[edit](/w/index.php?title=Unit_testing&action=edit&section=5 "Edit section: Test case")]
--------------------------------------------------------------------------------------------------


This paragraph is an excerpt from [Test case](/wiki/Test_case "Test case").[[edit](https://en.wikipedia.org/w/index.php?title=Test_case&action=edit)]
In [software engineering](/wiki/Software_engineering "Software engineering"), a [test case](/wiki/Test_case "Test case") is a specification of the inputs, execution conditions, testing procedure, and expected results that define a single test to be executed to achieve a particular [software testing](/wiki/Software_testing "Software testing") objective, such as to exercise a particular program path or to verify compliance with a specific requirement.[[11]](#cite_note-11) Test cases underlie testing that is methodical rather than haphazard. A [battery of test cases](/wiki/Test_suite "Test suite") can be built to produce the desired coverage of the software being tested. Formally defined test cases allow the same tests to be run repeatedly against successive versions of the software, allowing for effective and consistent [regression testing](/wiki/Regression_testing "Regression testing").[[12]](#cite_note-12)
Test double[[edit](/w/index.php?title=Unit_testing&action=edit&section=6 "Edit section: Test double")]
------------------------------------------------------------------------------------------------------


This paragraph is an excerpt from [Test double](/wiki/Test_double "Test double").[[edit](https://en.wikipedia.org/w/index.php?title=Test_double&action=edit)]
A [test double](/wiki/Test_double "Test double") is [software](/wiki/Software "Software") used in [software](/wiki/Software_testing "Software testing") [test automation](/wiki/Test_automation "Test automation") that satisfies a [dependency](/wiki/Dependency_(computer_science) "Dependency (computer science)") so that the test need not depend on production code. A test double provides functionality via an [interface](/wiki/Interface_(computing) "Interface (computing)") that the software under test cannot distinguish from production code.
Parameterized test[[edit](/w/index.php?title=Unit_testing&action=edit&section=7 "Edit section: Parameterized test")]
--------------------------------------------------------------------------------------------------------------------


A [parameterized test](/wiki/Parameterized_test "Parameterized test") is a test that accepts a set of values that can be used to enable the test to run with multiple, different input values. A testing framework that supports parametrized tests supports a way to encode parameter sets and to run the test with each set.


Use of parametrized tests can reduce test code duplication.


Parameterized tests are supported by [TestNG](/wiki/TestNG "TestNG"), [JUnit](/wiki/JUnit "JUnit"),[[13]](#cite_note-FOOTNOTEGulatiSharma2017133–137Chapter_§7_JUnit_5_Extension_Model_-_Parameterized_Test-13) [XUnit](/wiki/XUnit "XUnit") and [NUnit](/wiki/NUnit "NUnit"), as well as in various JavaScript test frameworks.[*[citation needed](/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")*]


Parameters for the unit tests may be coded manually or in some cases are automatically generated by the test framework. In recent years support was added for writing more powerful (unit) tests, leveraging the concept of theories, test cases that execute the same steps, but using test data generated at runtime, unlike regular parameterized tests that use the same execution steps with input sets that are pre-defined.[*[citation needed](/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")*]



Agile[[edit](/w/index.php?title=Unit_testing&action=edit&section=8 "Edit section: Agile")]
------------------------------------------------------------------------------------------


Main article: [Agile software development](/wiki/Agile_software_development "Agile software development")
Sometimes, in the agile software development, unit testing is done per [user story](/wiki/User_story "User story") and comes in the later half of the sprint after requirements gathering and development are complete. Typically, the developers or other members from the development team, such as [consultants](/wiki/Information_technology_consulting "Information technology consulting"), will write step-by-step 'test scripts' for the developers to execute in the tool. Test scripts are generally written to prove the effective and technical operation of specific developed features in the tool, as opposed to full fledged business processes that would be interfaced by the [end user](/wiki/End_user "End user"), which is typically done during [user acceptance testing](/wiki/User_acceptance_test "User acceptance test"). If the test-script can be fully executed from start to finish without incident, the unit test is considered to have "passed", otherwise errors are noted and the user story is moved back to development in an 'in-progress' state. User stories that successfully pass unit tests are moved on to the final steps of the sprint - Code review, peer review, and then lastly a 'show-back' session demonstrating the developed tool to stakeholders.



Test-driven development[[edit](/w/index.php?title=Unit_testing&action=edit&section=9 "Edit section: Test-driven development")]
------------------------------------------------------------------------------------------------------------------------------


Main article: [Test-driven development](/wiki/Test-driven_development "Test-driven development")
In test-driven development (TDD), unit tests are written while the production code is written. Starting with working code, the developer adds test code for a required behavior, then adds *just enough* code to make the test pass, then refactors the code (including test code) as makes sense and then repeats by adding another test.



Value[[edit](/w/index.php?title=Unit_testing&action=edit&section=10 "Edit section: Value")]
-------------------------------------------------------------------------------------------


Unit testing is intended to ensure that the units meet their [design](/wiki/Software_design "Software design") and behave as intended.[[14]](#cite_note-hamill-14)


By writing tests first for the smallest testable units, then the compound behaviors between those, one can build up comprehensive tests for complex applications.[[14]](#cite_note-hamill-14)


One goal of unit testing is to isolate each part of the program and show that the individual parts are correct.[[1]](#cite_note-kolawa-1) A unit test provides a strict, written [contract](/wiki/Design_by_Contract "Design by Contract") that the piece of code must satisfy.



### Early detection of problems in the development cycle[[edit](/w/index.php?title=Unit_testing&action=edit&section=11 "Edit section: Early detection of problems in the development cycle")]


Unit testing finds problems early in the [development cycle](/wiki/Development_cycle "Development cycle"). This includes both bugs in the programmer's implementation and flaws or missing parts of the specification for the unit. The process of writing a thorough set of tests forces the author to think through inputs, outputs, and error conditions, and thus more crisply define the unit's desired behavior.[*[citation needed](/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")*]



### Reduced cost[[edit](/w/index.php?title=Unit_testing&action=edit&section=12 "Edit section: Reduced cost")]


The cost of finding a bug before coding begins or when the code is first written is considerably lower than the cost of detecting, identifying, and correcting the bug later. Bugs in released code may also cause costly problems for the end-users of the software.[[15]](#cite_note-15)[[16]](#cite_note-16)[[17]](#cite_note-17) Code can be impossible or difficult to unit test if poorly written, thus unit testing can force developers to structure functions and objects in better ways.



### More frequent releases[[edit](/w/index.php?title=Unit_testing&action=edit&section=13 "Edit section: More frequent releases")]


Unit testing enables more frequent releases in software development. By testing individual components in isolation, developers can quickly identify and address issues, leading to faster iteration and release cycles.[[18]](#cite_note-18)



### Allows for code refactoring[[edit](/w/index.php?title=Unit_testing&action=edit&section=14 "Edit section: Allows for code refactoring")]


Unit testing allows the programmer to [refactor](/wiki/Refactoring "Refactoring") code or upgrade system libraries at a later date, and make sure the module still works correctly (e.g., in [regression testing](/wiki/Regression_testing "Regression testing")). The procedure is to write test cases for all [functions](/wiki/Subroutine "Subroutine") and [methods](/wiki/Method_(computer_science) "Method (computer science)") so that whenever a change causes a fault, it can be identified quickly. 



### Detects changes which may break a design contract[[edit](/w/index.php?title=Unit_testing&action=edit&section=15 "Edit section: Detects changes which may break a design contract")]


Unit tests detect changes which may break a [design contract](/wiki/Design_by_contract "Design by contract").



### Reduce uncertainty[[edit](/w/index.php?title=Unit_testing&action=edit&section=16 "Edit section: Reduce uncertainty")]


Unit testing may reduce uncertainty in the units themselves and can be used in a [bottom-up](/wiki/Top-down_and_bottom-up_design "Top-down and bottom-up design") testing style approach. By testing the parts of a program first and then testing the sum of its parts, [integration testing](/wiki/Integration_testing "Integration testing") becomes much easier.[*[citation needed](/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")*]



### Documentation of system behavior[[edit](/w/index.php?title=Unit_testing&action=edit&section=17 "Edit section: Documentation of system behavior")]


Some programmers contend that unit tests provide a form of documentation of the code. Developers wanting to learn what functionality is provided by a unit, and how to use it, can review the unit tests to gain an understanding of it.[*[citation needed](/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")*]


Test cases can embody characteristics that are critical to the success of the unit. These characteristics can indicate appropriate/inappropriate use of a unit as well as negative behaviors that are to be trapped by the unit. A test case documents these critical characteristics, although many software development environments do not rely solely upon code to document the product in development.[*[citation needed](/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")*]


In some processes, the act of writing tests and the code under test, plus associated refactoring, may take the place of formal design. Each unit test can be seen as a design element specifying classes, methods, and observable behavior.[*[citation needed](/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")*]



Limitations and disadvantages[[edit](/w/index.php?title=Unit_testing&action=edit&section=18 "Edit section: Limitations and disadvantages")]
-------------------------------------------------------------------------------------------------------------------------------------------


Testing will not catch every error in the program, because it cannot evaluate every execution path in any but the most trivial programs. This [problem](/wiki/Decision_problem "Decision problem") is a superset of the [halting problem](/wiki/Halting_problem "Halting problem"), which is [undecidable](/wiki/Undecidable_problem "Undecidable problem"). The same is true for unit testing. Additionally, unit testing by definition only tests the functionality of the units themselves. Therefore, it will not catch integration errors or broader system-level errors (such as functions performed across multiple units, or non-functional test areas such as [performance](/wiki/Software_performance_testing "Software performance testing")). Unit testing should be done in conjunction with other [software testing](/wiki/Software_testing "Software testing") activities, as they can only show the presence or absence of particular errors; they cannot prove a complete absence of errors. To guarantee correct behavior for every execution path and every possible input, and ensure the absence of errors, other techniques are required, namely the application of [formal methods](/wiki/Formal_verification "Formal verification") to prove that a software component has no unexpected behavior.[*[citation needed](/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")*]


An elaborate hierarchy of unit tests does not equal integration testing. Integration with peripheral units should be included in integration tests, but not in unit tests.[*[citation needed](/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")*] Integration testing typically still relies heavily on humans [testing manually](/wiki/Manual_testing "Manual testing"); high-level or global-scope testing can be difficult to automate, such that manual testing often appears faster and cheaper.[*[citation needed](/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")*]


Software testing is a combinatorial problem. For example, every Boolean decision statement requires at least two tests: one with an outcome of "true" and one with an outcome of "false". As a result, for every line of code written, programmers often need 3 to 5 lines of test code.[*[citation needed](/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")*] This obviously takes time and its investment may not be worth the effort. There are problems that cannot easily be tested at all – for example those that are [nondeterministic](/wiki/Nondeterministic_algorithm "Nondeterministic algorithm") or involve multiple [threads](/wiki/Thread_(computer_science) "Thread (computer science)"). In addition, code for a unit test is as likely to be buggy as the code it is testing. [Fred Brooks](/wiki/Fred_Brooks "Fred Brooks") in *[The Mythical Man-Month](/wiki/The_Mythical_Man-Month "The Mythical Man-Month")* quotes: "Never go to sea with two chronometers; take one or three."[[19]](#cite_note-19) Meaning, if two [chronometers](/wiki/Marine_chronometer "Marine chronometer") contradict, how do you know which one is correct?



### Difficulty in setting up realistic and useful tests[[edit](/w/index.php?title=Unit_testing&action=edit&section=19 "Edit section: Difficulty in setting up realistic and useful tests")]


Another challenge related to writing the unit tests is the difficulty of setting up realistic and useful tests. It is necessary to create relevant initial conditions so the part of the application being tested behaves like part of the complete system. If these initial conditions are not set correctly, the test will not be exercising the code in a realistic context, which diminishes the value and accuracy of unit test results.[*[citation needed](/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")*]



### Requires discipline throughout the development process[[edit](/w/index.php?title=Unit_testing&action=edit&section=20 "Edit section: Requires discipline throughout the development process")]


To obtain the intended benefits from unit testing, rigorous discipline is needed throughout the software development process.



### Requires version control[[edit](/w/index.php?title=Unit_testing&action=edit&section=21 "Edit section: Requires version control")]


It is essential to keep careful records not only of the tests that have been performed, but also of all changes that have been made to the source code of this or any other unit in the software. Use of a [version control](/wiki/Version_control "Version control") system is essential. If a later version of the unit fails a particular test that it had previously passed, the version-control software can provide a list of the source code changes (if any) that have been applied to the unit since that time.[*[citation needed](/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")*]



### Requires regular reviews[[edit](/w/index.php?title=Unit_testing&action=edit&section=22 "Edit section: Requires regular reviews")]


It is also essential to implement a sustainable process for ensuring that test case failures are reviewed regularly and addressed immediately.[[20]](#cite_note-20) If such a process is not implemented and ingrained into the team's workflow, the application will evolve out of sync with the unit test suite, increasing false positives and reducing the effectiveness of the test suite.



### Limitations for embedded system software[[edit](/w/index.php?title=Unit_testing&action=edit&section=23 "Edit section: Limitations for embedded system software")]


Unit testing embedded system software presents a unique challenge: Because the software is being developed on a different platform than the one it will eventually run on, you cannot readily run a test program in the actual deployment environment, as is possible with desktop programs.[[21]](#cite_note-21)



### Limitations for testing integration with external systems[[edit](/w/index.php?title=Unit_testing&action=edit&section=24 "Edit section: Limitations for testing integration with external systems")]


Unit tests tend to be easiest when a method has input parameters and some output. It is not as easy to create unit tests when a major function of the method is to interact with something external to the application. For example, a method that will work with a database might require a mock up of database interactions to be created, which probably won't be as comprehensive as the real database interactions.[[22]](#cite_note-22)[*[better source needed](/wiki/Wikipedia:NOTRS "Wikipedia:NOTRS")*]



Examples[[edit](/w/index.php?title=Unit_testing&action=edit&section=25 "Edit section: Examples")]
-------------------------------------------------------------------------------------------------


### JUnit[[edit](/w/index.php?title=Unit_testing&action=edit&section=26 "Edit section: JUnit")]


Below is an example of a JUnit test suite. It focuses on the `Adder` class.




```
class Adder {
    public int add(int a, int b) {
        return a + b;
    }
}

```

The test suite uses [assert](/wiki/Assertion_(computing) "Assertion (computing)") statements to verify the expected result of various input values to the `sum` method.




```
import static org.junit.Assert.assertEquals;
import org.junit.Test;
public class AdderUnitTest {
    @Test
    public void sumReturnsZeroForZeroInput() {
        Adder adder = new Adder();
        assertEquals(0, adder.add(0, 0));
    }

    @Test
    public void sumReturnsSumOfTwoPositiveNumbers() {
        Adder adder = new Adder();
        assertEquals(3, adder.add(1, 2));
    }

    @Test
    public void sumReturnsSumOfTwoNegativeNumbers() {
        Adder adder = new Adder();
        assertEquals(-3, adder.add(-1, -2));
    }

    @Test
    public void sumReturnsSumOfLargeNumbers() {
        Adder adder = new Adder();
        assertEquals(2222, adder.add(1234, 988));
    }
}

```

As executable specifications[[edit](/w/index.php?title=Unit_testing&action=edit&section=27 "Edit section: As executable specifications")]
-----------------------------------------------------------------------------------------------------------------------------------------




|  | This section **does not [cite](/wiki/Wikipedia:Citing_sources "Wikipedia:Citing sources") any [sources](/wiki/Wikipedia:Verifiability "Wikipedia:Verifiability")**. Please help [improve this section](/wiki/Special:EditPage/Unit_testing "Special:EditPage/Unit testing") by [adding citations to reliable sources](/wiki/Help:Referencing_for_beginners "Help:Referencing for beginners"). Unsourced material may be challenged and [removed](/wiki/Wikipedia:Verifiability#Burden_of_evidence "Wikipedia:Verifiability"). *(September 2019)* *([Learn how and when to remove this message](/wiki/Help:Maintenance_template_removal "Help:Maintenance template removal"))* |
| --- | --- |


Using unit-tests as a design specification has one significant advantage over other design methods: The design document (the unit-tests themselves) can itself be used to verify the implementation. The tests will never pass unless the developer implements a solution according to the design.


Unit testing lacks some of the accessibility of a diagrammatic specification such as a [UML](/wiki/Unified_Modeling_Language "Unified Modeling Language") diagram, but they may be generated from the unit test using automated tools. Most modern languages have free tools (usually available as extensions to [IDEs](/wiki/Integrated_development_environment "Integrated development environment")). Free tools, like those based on the [xUnit](/wiki/XUnit "XUnit") framework, outsource to another system the graphical rendering of a view for human consumption.



Applications[[edit](/w/index.php?title=Unit_testing&action=edit&section=28 "Edit section: Applications")]
---------------------------------------------------------------------------------------------------------


### Extreme programming[[edit](/w/index.php?title=Unit_testing&action=edit&section=29 "Edit section: Extreme programming")]


Unit testing is the cornerstone of [extreme programming](/wiki/Extreme_programming "Extreme programming"), which relies on an automated [unit testing framework](/wiki/List_of_unit_testing_frameworks "List of unit testing frameworks"). This automated unit testing framework can be either third party, e.g., [xUnit](/wiki/XUnit "XUnit"), or created within the development group.


Extreme programming uses the creation of unit tests for [test-driven development](/wiki/Test-driven_development "Test-driven development"). The developer writes a unit test that exposes either a software requirement or a defect. This test will fail because either the requirement isn't implemented yet, or because it intentionally exposes a defect in the existing code. Then, the developer writes the simplest code to make the test, along with other tests, pass.


Most code in a system is unit tested, but not necessarily all paths through the code. Extreme programming mandates a "test everything that can possibly break" strategy, over the traditional "test every execution path" method. This leads developers to develop fewer tests than classical methods, but this isn't really a problem, more a restatement of fact, as classical methods have rarely ever been followed methodically enough for all execution paths to have been thoroughly tested.[*[citation needed](/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")*] Extreme programming simply recognizes that testing is rarely exhaustive (because it is often too expensive and time-consuming to be economically viable) and provides guidance on how to effectively focus limited resources.


Crucially, the test code is considered a first class project artifact in that it is maintained at the same quality as the implementation code, with all duplication removed. Developers release unit testing code to the code repository in conjunction with the code it tests. Extreme programming's thorough unit testing allows the benefits mentioned above, such as simpler and more confident code development and [refactoring](/wiki/Refactoring "Refactoring"), simplified code integration, accurate documentation, and more modular designs. These unit tests are also constantly run as a form of [regression test](/wiki/Regression_test "Regression test").


Unit testing is also critical to the concept of [Emergent Design](/wiki/Emergent_Design "Emergent Design"). As emergent design is heavily dependent upon refactoring, unit tests are an integral component.[*[citation needed](/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")*]



### Automated testing frameworks[[edit](/w/index.php?title=Unit_testing&action=edit&section=30 "Edit section: Automated testing frameworks")]


An automated testing framework provides features for automating test execution and can accelerate writing and running tests. Frameworks have been developed for [a wide variety of programming languages](/wiki/List_of_unit_testing_frameworks "List of unit testing frameworks").


Generally, frameworks are [third-party](/wiki/Third-party_software_component "Third-party software component"); not distributed with a compiler or [integrated development environment](/wiki/Integrated_development_environment "Integrated development environment") (IDE). 


Tests can be written without using a framework to exercise the code under test using [assertions](/wiki/Assertion_(software_development) "Assertion (software development)"), [exception handling](/wiki/Exception_handling "Exception handling"), and other [control flow](/wiki/Control_flow "Control flow") mechanisms to verify behavior and report failure. Some note that testing without a framework is valuable since there is a [barrier to entry](/wiki/Barrier_to_entry "Barrier to entry") for the adoption of a framework; that having some tests is better than none, but once a framework is in place, adding tests can be easier.[[23]](#cite_note-23)


In some frameworks advanced test features are missing and must be hand-coded.



### Language-level unit testing support[[edit](/w/index.php?title=Unit_testing&action=edit&section=31 "Edit section: Language-level unit testing support")]


Some programming languages directly support unit testing. Their grammar allows the direct declaration of unit tests without importing a library (whether third party or standard). Additionally, the Boolean conditions of the unit tests can be expressed in the same syntax as Boolean expressions used in non-unit test code, such as what is used for `if` and `while` statements.


Languages with built-in unit testing support include:




* [Cobra](/wiki/Cobra_(programming_language) "Cobra (programming language)")
* [D](/wiki/D_(programming_language) "D (programming language)")[[24]](#cite_note-24)
* [Rust](/wiki/Rust_(programming_language) "Rust (programming language)")[[25]](#cite_note-25)



Languages with standard unit testing framework support include:




* [Apex](/wiki/Apex_(programming_language) "Apex (programming language)")
* [Crystal](/wiki/Crystal_(programming_language) "Crystal (programming language)")[[26]](#cite_note-26)
* [Erlang](/wiki/Erlang_(programming_language) "Erlang (programming language)")
* [Go](/wiki/Go_(programming_language) "Go (programming language)")[[27]](#cite_note-27)
* [Julia](/wiki/Julia_(programming_language) "Julia (programming language)")[[28]](#cite_note-28)
* [LabVIEW](/wiki/LabVIEW "LabVIEW")
* [MATLAB](/wiki/MATLAB "MATLAB")
* [Python](/wiki/Python_(programming_language) "Python (programming language)")[[29]](#cite_note-29)
* [Racket](/wiki/Racket_(programming_language) "Racket (programming language)")[[30]](#cite_note-Racket_Unit_Testing-30)[[31]](#cite_note-Racket_Unit_Testing_Main_dist-31)
* [Ruby](/wiki/Ruby_(programming_language) "Ruby (programming language)")[[32]](#cite_note-32)



Some languages do not have built-in unit-testing support but have established unit testing libraries or frameworks. These languages include:




* [ABAP](/wiki/ABAP "ABAP")
* [C++](/wiki/C%2B%2B "C++")
* [C#](/wiki/C_Sharp_(programming_language) "C Sharp (programming language)")
* [Clojure](/wiki/Clojure "Clojure")[[33]](#cite_note-Clojure_Unit_Testing_Framework-33)
* [Elixir](/wiki/Elixir_(programming_language) "Elixir (programming language)")
* [Java](/wiki/Java_(programming_language) "Java (programming language)")
* [JavaScript](/wiki/JavaScript "JavaScript")
* [Objective-C](/wiki/Objective-C "Objective-C")
* [Perl](/wiki/Perl "Perl")
* [PHP](/wiki/PHP "PHP")
* [PowerShell](/wiki/Windows_PowerShell "Windows PowerShell")[[34]](#cite_note-34)
* [R](/wiki/R_(programming_language) "R (programming language)") with testthat
* [Scala](/wiki/Scala_(programming_language) "Scala (programming language)")
* [tcl](/wiki/Tcl "Tcl")
* [Visual Basic .NET](/wiki/Visual_Basic_.NET "Visual Basic .NET")
* [Xojo](/wiki/Xojo "Xojo") with XojoUnit



See also[[edit](/w/index.php?title=Unit_testing&action=edit&section=32 "Edit section: See also")]
-------------------------------------------------------------------------------------------------



* [Acceptance testing](/wiki/Acceptance_testing "Acceptance testing")
* [Characterization test](/wiki/Characterization_test "Characterization test")
* [Component-based usability testing](/wiki/Component-based_usability_testing "Component-based usability testing")
* [Design predicates](/wiki/Design_predicates "Design predicates")
* [Design by contract](/wiki/Design_by_contract "Design by contract")
* [Extreme programming](/wiki/Extreme_programming "Extreme programming")
* [Functional testing](/wiki/Functional_testing "Functional testing")
* [Integration testing](/wiki/Integration_testing "Integration testing")
* [List of unit testing frameworks](/wiki/List_of_unit_testing_frameworks "List of unit testing frameworks")
* [Regression testing](/wiki/Regression_testing "Regression testing")
* [Software archaeology](/wiki/Software_archaeology "Software archaeology")
* [Software testing](/wiki/Software_testing "Software testing")
* [System testing](/wiki/System_testing "System testing")
* [Test case](/wiki/Test_case "Test case")
* [Test-driven development](/wiki/Test-driven_development "Test-driven development")
* [xUnit](/wiki/XUnit "XUnit") – a family of unit testing frameworks.



References[[edit](/w/index.php?title=Unit_testing&action=edit&section=33 "Edit section: References")]
-----------------------------------------------------------------------------------------------------



1. ^ [***a***](#cite_ref-kolawa_1-0) [***b***](#cite_ref-kolawa_1-1) Kolawa, Adam; Huizinga, Dorota (2007). *Automated Defect Prevention: Best Practices in Software Management*. Wiley-IEEE Computer Society Press. p. 75. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-0-470-04212-0](/wiki/Special:BookSources/978-0-470-04212-0 "Special:BookSources/978-0-470-04212-0").
2. **[^](#cite_ref-2)** Benington, Herbert D. (1956). "Production of large computer programs". *Proceedings of the Symposium on Advanced Programming Methods for Digital Computers, Washington, D.C., June 28-29, 1956*. Office of Naval Research, Department of the Navy: 15–28.
3. ^ [***a***](#cite_ref-:0_3-0) [***b***](#cite_ref-:0_3-1) Benington, H. D. (1 March 1987). ["Production of large computer programs (reprint of the 1956 paper with an updated foreword)"](https://dl.acm.org/doi/10.5555/41765.41799). *Proceedings of the 9th International Conference on Software Engineering*. ICSE '87. Washington, DC, USA: IEEE Computer Society Press: 299–310. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-0-89791-216-7](/wiki/Special:BookSources/978-0-89791-216-7 "Special:BookSources/978-0-89791-216-7").
4. **[^](#cite_ref-4)** Donegan, James J.; Packard, Calvin; Pashby, Paul (1 January 1964). ["Experiences with the goddard computing system during manned spaceflight missions"](https://dl.acm.org/doi/10.1145/800257.808889). *Proceedings of the 1964 19th ACM national conference*. ACM '64. New York, NY, USA: Association for Computing Machinery. pp. 12.101–12.108. [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.1145/800257.808889](https://doi.org/10.1145%2F800257.808889). [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-1-4503-7918-2](/wiki/Special:BookSources/978-1-4503-7918-2 "Special:BookSources/978-1-4503-7918-2").
5. **[^](#cite_ref-5)** Zimmerman, Norman A. (26 August 1969). ["System integration as a programming function"](https://dl.acm.org/doi/10.1145/800195.805951). *Proceedings of the 1969 24th national conference*. ACM '69. New York, NY, USA: Association for Computing Machinery. pp. 459–467. [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.1145/800195.805951](https://doi.org/10.1145%2F800195.805951). [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-1-4503-7493-4](/wiki/Special:BookSources/978-1-4503-7493-4 "Special:BookSources/978-1-4503-7493-4").
6. **[^](#cite_ref-6)** *MIL-STD-483 Military standard: configuration management practices for systems, equipment, munitions, and computer programs*. United states, Department of Defense. 31 December 1970. pp. Section 3.4.7.2. The contractor shall then code and test software Units, and enter the source and object code, and associated listings of each successfully tested Unit into the Developmental Configuration`{{[cite book](/wiki/Template:Cite_book "Template:Cite book")}}`: CS1 maint: date and year ([link](/wiki/Category:CS1_maint:_date_and_year "Category:CS1 maint: date and year"))
7. **[^](#cite_ref-7)** Tighe, Michael F. (1 January 1978). ["The value of a proper software quality assurance methodology"](https://dl.acm.org/doi/10.1145/1007775.811118). *ACM SIGMETRICS Performance Evaluation Review*. **7** (3–4): 165–172. [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.1145/1007775.811118](https://doi.org/10.1145%2F1007775.811118). [ISSN](/wiki/ISSN_(identifier) "ISSN (identifier)") [0163-5999](https://www.worldcat.org/issn/0163-5999).
8. **[^](#cite_ref-8)** Gulati, Shekhar (2017). *Java Unit Testing with JUnit 5 : Test Driven Development with JUnit 5*. Rahul Sharma. Berkeley, CA: Apress. p. 8. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-1-4842-3015-2](/wiki/Special:BookSources/978-1-4842-3015-2 "Special:BookSources/978-1-4842-3015-2"). [OCLC](/wiki/OCLC_(identifier) "OCLC (identifier)") [1012347252](https://www.worldcat.org/oclc/1012347252).
9. **[^](#cite_ref-9)** Winters, Titus (2020). *Software engineering at Google : lessons learned from programming over time*. Tom Manshreck, Hyrum Wright (1st ed.). Sebastopol, CA: O'Reilly. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-1-4920-8274-3](/wiki/Special:BookSources/978-1-4920-8274-3 "Special:BookSources/978-1-4920-8274-3"). [OCLC](/wiki/OCLC_(identifier) "OCLC (identifier)") [1144086840](https://www.worldcat.org/oclc/1144086840).
10. **[^](#cite_ref-10)** [Beck, Kent](/wiki/Kent_Beck "Kent Beck") (2002). *Test-Driven Development by Example*. Addison-Wesley. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-0321146533](/wiki/Special:BookSources/978-0321146533 "Special:BookSources/978-0321146533").
11. **[^](#cite_ref-11)** *Systems and software engineering -- Vocabulary*. Iso/Iec/IEEE 24765:2010(E). 1 December 2010. pp. 1–418. [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.1109/IEEESTD.2010.5733835](https://doi.org/10.1109%2FIEEESTD.2010.5733835). [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-0-7381-6205-8](/wiki/Special:BookSources/978-0-7381-6205-8 "Special:BookSources/978-0-7381-6205-8").
12. **[^](#cite_ref-12)** Kaner, Cem (May 2003). ["What Is a Good Test Case?"](http://www.kaner.com/pdfs/GoodTest.pdf) (PDF). *STAR East*: 2.
13. **[^](#cite_ref-FOOTNOTEGulatiSharma2017133–137Chapter_§7_JUnit_5_Extension_Model_-_Parameterized_Test_13-0)** [Gulati & Sharma 2017](#CITEREFGulatiSharma2017), pp. 133–137, Chapter §7 JUnit 5 Extension Model - Parameterized Test.
14. ^ [***a***](#cite_ref-hamill_14-0) [***b***](#cite_ref-hamill_14-1) Hamill, Paul (2004). [*Unit Test Frameworks: Tools for High-Quality Software Development*](https://books.google.com/books?id=2ksvdhhnWQsC). O'Reilly Media, Inc. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [9780596552817](/wiki/Special:BookSources/9780596552817 "Special:BookSources/9780596552817").
15. **[^](#cite_ref-15)** [Boehm, Barry W.](/wiki/Barry_Boehm "Barry Boehm"); Papaccio, Philip N. (October 1988). ["Understanding and Controlling Software Costs"](https://web.archive.org/web/20161009084506/http://faculty.ksu.edu.sa/ghazy/Cost_MSc/R6.pdf) (PDF). *IEEE Transactions on Software Engineering*. **14** (10): 1462–1477. [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.1109/32.6191](https://doi.org/10.1109%2F32.6191). Archived from [the original](http://faculty.ksu.edu.sa/ghazy/Cost_MSc/R6.pdf) (PDF) on 9 October 2016. Retrieved 13 May 2016.
16. **[^](#cite_ref-16)** ["Test Early and Often"](https://msdn.microsoft.com/en-us/library/ee330950%28v=vs.110%29.aspx). Microsoft.
17. **[^](#cite_ref-17)** ["Prove It Works: Using the Unit Test Framework for Software Testing and Validation"](http://www.ni.com/white-paper/8082/en/). [National Instruments](/wiki/National_Instruments "National Instruments"). 21 August 2017.
18. **[^](#cite_ref-18)** Erik (10 March 2023). ["You Still Don't Know How to Do Unit Testing (and Your Secret is Safe with Me)"](https://stackify.com/unit-testing-basics-best-practices/). *Stackify*. Retrieved 10 March 2023.
19. **[^](#cite_ref-19)** [Brooks, Frederick J.](/wiki/Fred_Brooks "Fred Brooks") (1995) [1975]. [*The Mythical Man-Month*](/wiki/The_Mythical_Man-Month "The Mythical Man-Month"). Addison-Wesley. p. [64](https://archive.org/details/mythicalmonth00broo/page/64). [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-0-201-83595-3](/wiki/Special:BookSources/978-0-201-83595-3 "Special:BookSources/978-0-201-83595-3").
20. **[^](#cite_ref-20)** [daVeiga, Nada](/w/index.php?title=Nada_daVeiga&action=edit&redlink=1 "Nada daVeiga (page does not exist)") (6 February 2008). ["Change Code Without Fear: Utilize a regression safety net"](http://www.ddj.com/development-tools/206105233). Retrieved 8 February 2008.
21. **[^](#cite_ref-21)** [Kucharski, Marek](/w/index.php?title=Marek_Kucharski&action=edit&redlink=1 "Marek Kucharski (page does not exist)") (23 November 2011). ["Making Unit Testing Practical for Embedded Development"](https://www.electronicdesign.com/technologies/embedded-revolution/article/21794376/making-unit-testing-practical-for-embedded-development). Retrieved 20 July 2020.
22. **[^](#cite_ref-22)** ["Unit Tests And Databases"](http://wiki.c2.com/?UnitTestsAndDatabases). Retrieved 29 January 2024.
23. **[^](#cite_ref-23)** Bullseye Testing Technology (2006–2008). ["Intermediate Coverage Goals"](http://www.bullseye.com/coverage.html). Retrieved 24 March 2009.
24. **[^](#cite_ref-24)** ["Unit Tests - D Programming Language"](http://dlang.org/spec/unittest.html). *D Programming Language*. D Language Foundation. Retrieved 5 August 2017.
25. **[^](#cite_ref-25)** Steve Klabnik and Carol Nichols, with contributions from the Rust Community (2015–2023). ["How to Write Tests"](https://doc.rust-lang.org/book/ch11-01-writing-tests.html). Retrieved 21 August 2023.
26. **[^](#cite_ref-26)** ["Crystal Spec"](https://crystal-lang.org/api/0.23.1/Spec.html). crystal-lang.org. Retrieved 18 September 2017.
27. **[^](#cite_ref-27)** ["testing - The Go Programming Language"](https://golang.org/pkg/testing/). golang.org. Retrieved 3 December 2013.
28. **[^](#cite_ref-28)** ["Unit Testing · The Julia Language"](https://docs.julialang.org/en/v1/stdlib/Test/). docs.julialang.org. Retrieved 15 June 2022.
29. **[^](#cite_ref-29)** Python Documentation (2016). ["unittest -- Unit testing framework"](https://docs.python.org/3/library/unittest.html). Retrieved 18 April 2016.
30. **[^](#cite_ref-Racket_Unit_Testing_30-0)** Welsh, Noel; Culpepper, Ryan. ["RackUnit: Unit Testing"](http://docs.racket-lang.org/rackunit/index.html). PLT Design Inc. Retrieved 26 February 2019.
31. **[^](#cite_ref-Racket_Unit_Testing_Main_dist_31-0)** Welsh, Noel; Culpepper, Ryan. ["RackUnit Unit Testing package part of Racket main distribution"](https://pkgs.racket-lang.org/package/rackunit). PLT Design Inc. Retrieved 26 February 2019.
32. **[^](#cite_ref-32)** ["Minitest (Ruby 2.0)"](http://ruby-doc.org/stdlib-2.0.0/libdoc/minitest/rdoc/MiniTest.html). Ruby-Doc.org.
33. **[^](#cite_ref-Clojure_Unit_Testing_Framework_33-0)** Sierra, Stuart. ["API for clojure.test - Clojure v1.6 (stable)"](https://clojure.github.io/clojure/clojure.test-api.html). Retrieved 11 February 2015.
34. **[^](#cite_ref-34)** ["Pester Framework"](https://github.com/pester/Pester). *[GitHub](/wiki/GitHub "GitHub")*. Retrieved 28 January 2016.

Further reading[[edit](/w/index.php?title=Unit_testing&action=edit&section=34 "Edit section: Further reading")]
---------------------------------------------------------------------------------------------------------------


* Feathers, Michael C. (2005). *Working Effectively with Legacy Code*. Upper Saddle River, NJ: Prentice Hall Professional Technical Reference. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-0131177055](/wiki/Special:BookSources/978-0131177055 "Special:BookSources/978-0131177055").
* Gulati, Shekhar; Sharma, Rahul (2017). *Java Unit Testing with JUnit 5*. [Apress](/wiki/Apress "Apress").


External links[[edit](/w/index.php?title=Unit_testing&action=edit&section=35 "Edit section: External links")]
-------------------------------------------------------------------------------------------------------------


* [Test Driven Development (Ward Cunningham's Wiki)](http://c2.com/cgi/wiki?TestDrivenDevelopment)




| * [v](/wiki/Template:Software_testing "Template:Software testing") * [t](/wiki/Template_talk:Software_testing "Template talk:Software testing") * [e](/wiki/Special:EditPage/Template:Software_testing "Special:EditPage/Template:Software testing") [Software testing](/wiki/Software_testing "Software testing") | |
| --- | --- |
| The "box" approach | * [Black-box testing](/wiki/Black-box_testing "Black-box testing") 	+ [All-pairs testing](/wiki/All-pairs_testing "All-pairs testing") 	+ [Exploratory testing](/wiki/Exploratory_testing "Exploratory testing") 	+ [Fuzz testing](/wiki/Fuzz_testing "Fuzz testing") 	+ [Model-based testing](/wiki/Model-based_testing "Model-based testing") 	+ [Scenario testing](/wiki/Scenario_testing "Scenario testing") * [Grey-box testing](/wiki/Grey-box_testing "Grey-box testing") * [White-box testing](/wiki/White-box_testing "White-box testing") 	+ [API testing](/wiki/API_testing "API testing") 	+ [Mutation testing](/wiki/Mutation_testing "Mutation testing") 	+ [Static testing](/wiki/Static_testing "Static testing") |
| Testing levels | * [Acceptance testing](/wiki/Acceptance_testing "Acceptance testing") * [Integration testing](/wiki/Integration_testing "Integration testing") * [System testing](/wiki/System_testing "System testing") * Unit testing |
| Testing types, techniques,and [tactics](/wiki/Software_testing_tactics "Software testing tactics") | * [A/B testing](/wiki/A/B_testing "A/B testing") * [Benchmark](/wiki/Benchmark_(computing) "Benchmark (computing)") * [Compatibility testing](/wiki/Compatibility_testing "Compatibility testing") * [Concolic testing](/wiki/Concolic_testing "Concolic testing") * [Concurrent testing](/wiki/Concurrent_testing "Concurrent testing") * [Conformance testing](/wiki/Conformance_testing "Conformance testing") * [Continuous testing](/wiki/Continuous_testing "Continuous testing") * [Destructive testing](/wiki/Destructive_testing "Destructive testing") * [Development testing](/wiki/Development_testing "Development testing") * [Differential testing](/wiki/Differential_testing "Differential testing") * [Dynamic program analysis](/wiki/Dynamic_program_analysis "Dynamic program analysis") * [Installation testing](/wiki/Installation_testing "Installation testing") * [Negative testing](/wiki/Negative_testing "Negative testing") * [Random testing](/wiki/Random_testing "Random testing") * [Regression testing](/wiki/Regression_testing "Regression testing") * [Security testing](/wiki/Security_testing "Security testing") * [Smoke testing (software)](/wiki/Smoke_testing_(software) "Smoke testing (software)") * [Software performance testing](/wiki/Software_performance_testing "Software performance testing") * [Stress testing](/wiki/Stress_testing_(software) "Stress testing (software)") * [Symbolic execution](/wiki/Symbolic_execution "Symbolic execution") * [Test automation](/wiki/Test_automation "Test automation") * [Usability testing](/wiki/Usability_testing "Usability testing") |
| See also | * [Graphical user interface testing](/wiki/Graphical_user_interface_testing "Graphical user interface testing") * [Manual testing](/wiki/Manual_testing "Manual testing") * [Orthogonal array testing](/wiki/Orthogonal_array_testing "Orthogonal array testing") * [Pair testing](/wiki/Pair_testing "Pair testing") * [Soak testing](/wiki/Soak_testing "Soak testing") * [Software reliability testing](/wiki/Software_reliability_testing "Software reliability testing") * [Stress testing](/wiki/Stress_testing "Stress testing") * [Web testing](/wiki/Web_testing "Web testing") |





![](https://login.wikimedia.org/wiki/Special:CentralAutoLogin/start?type=1x1)
Retrieved from "<https://en.wikipedia.org/w/index.php?title=Unit_testing&oldid=1228828406>"
[Categories](/wiki/Help:Category "Help:Category"): * [Unit testing](/wiki/Category:Unit_testing "Category:Unit testing")
* [Extreme programming](/wiki/Category:Extreme_programming "Category:Extreme programming")
* [Types of tools used in software development](/wiki/Category:Types_of_tools_used_in_software_development "Category:Types of tools used in software development")
Hidden categories: * [CS1 maint: date and year](/wiki/Category:CS1_maint:_date_and_year "Category:CS1 maint: date and year")
* [Articles with short description](/wiki/Category:Articles_with_short_description "Category:Articles with short description")
* [Short description is different from Wikidata](/wiki/Category:Short_description_is_different_from_Wikidata "Category:Short description is different from Wikidata")
* [Use dmy dates from April 2020](/wiki/Category:Use_dmy_dates_from_April_2020 "Category:Use dmy dates from April 2020")
* [Articles needing additional references from September 2019](/wiki/Category:Articles_needing_additional_references_from_September_2019 "Category:Articles needing additional references from September 2019")
* [All articles needing additional references](/wiki/Category:All_articles_needing_additional_references "Category:All articles needing additional references")
* [Articles with excerpts](/wiki/Category:Articles_with_excerpts "Category:Articles with excerpts")
* [All articles with unsourced statements](/wiki/Category:All_articles_with_unsourced_statements "Category:All articles with unsourced statements")
* [Articles with unsourced statements from November 2023](/wiki/Category:Articles_with_unsourced_statements_from_November_2023 "Category:Articles with unsourced statements from November 2023")
* [Articles with unsourced statements from January 2013](/wiki/Category:Articles_with_unsourced_statements_from_January_2013 "Category:Articles with unsourced statements from January 2013")
* [Articles with unsourced statements from September 2019](/wiki/Category:Articles_with_unsourced_statements_from_September_2019 "Category:Articles with unsourced statements from September 2019")
* [Articles with unsourced statements from October 2010](/wiki/Category:Articles_with_unsourced_statements_from_October_2010 "Category:Articles with unsourced statements from October 2010")
* [Articles with unsourced statements from January 2010](/wiki/Category:Articles_with_unsourced_statements_from_January_2010 "Category:Articles with unsourced statements from January 2010")
* [All articles lacking reliable references](/wiki/Category:All_articles_lacking_reliable_references "Category:All articles lacking reliable references")
* [Articles lacking reliable references from February 2019](/wiki/Category:Articles_lacking_reliable_references_from_February_2019 "Category:Articles lacking reliable references from February 2019")
* [Articles with unsourced statements from November 2008](/wiki/Category:Articles_with_unsourced_statements_from_November_2008 "Category:Articles with unsourced statements from November 2008")
* [Articles with example Java code](/wiki/Category:Articles_with_example_Java_code "Category:Articles with example Java code")

