



From Wikipedia, the free encyclopedia




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


**Acceptance test–driven development** (**ATDD**) is a [development](/wiki/Software_development "Software development") methodology based on communication between the business customers, the developers, and the testers.[[1]](#cite_note-Pugh11-1) ATDD encompasses many of the same practices as [specification by example](/wiki/Specification_by_example "Specification by example") (SBE),[[2]](#cite_note-2)[[3]](#cite_note-3) [behavior-driven development](/wiki/Behavior-driven_development "Behavior-driven development") (BDD),[[4]](#cite_note-4) example-driven development (EDD),[[5]](#cite_note-5) and support-driven development also called story test–driven development (SDD).[[6]](#cite_note-6) All these processes aid developers and testers in understanding the customer's needs prior to implementation and allow customers to be able to converse in their own domain language.


ATDD is closely related to [test-driven development](/wiki/Test-driven_development "Test-driven development") (TDD).[[7]](#cite_note-7) It differs by the emphasis on developer-tester-business customer collaboration. ATDD encompasses [acceptance testing](/wiki/Acceptance_testing "Acceptance testing"), but highlights writing acceptance tests before developers begin coding.




Overview[[edit](/w/index.php?title=Acceptance_test-driven_development&action=edit&section=1 "Edit section: Overview")]
----------------------------------------------------------------------------------------------------------------------


Acceptance tests are from the user's point of view – the external view of the system.[[1]](#cite_note-Pugh11-1) They examine externally visible effects, such as specifying the correct output of a system given a particular input. Acceptance tests can verify how the state of something changes, such as an order that goes from "paid" to "shipped". They also can check the interactions with interfaces of other systems, such as shared databases or web services. In general, they are implementation independent, although automation of them may not be.[[8]](#cite_note-8)[[9]](#cite_note-9)



### Creation[[edit](/w/index.php?title=Acceptance_test-driven_development&action=edit&section=2 "Edit section: Creation")]


Acceptance tests are created when the requirements are analyzed and prior to coding.[[1]](#cite_note-Pugh11-1) They can be developed collaboratively by requirement requester (product owner, business analyst, customer representative, etc.), developer, and tester. Developers implement the system using the acceptance tests. Failing tests provide quick feedback that the requirements are not being met. The tests are specified in business domain terms. The terms then form a ubiquitous language that is shared between the customers, developers, and testers.[[10]](#cite_note-10) Tests and requirements are interrelated.[[11]](#cite_note-11) A requirement that lacks a test may not be implemented properly. A test that does not refer to a requirement is an unneeded test. An acceptance test that is developed after implementation begins represents a new requirement.[[12]](#cite_note-12)



### Testing strategy[[edit](/w/index.php?title=Acceptance_test-driven_development&action=edit&section=3 "Edit section: Testing strategy")]


Acceptance tests are a part of an overall testing strategy. They are the customer tests that demonstrate the business intent of a system. Component tests are technical acceptance tests developed by an architect that specify the behavior of large modules. Unit tests are created by the developer to drive easy-to-maintain code.[[13]](#cite_note-13) They are often derived from acceptance tests and unit tests. Cross-functional testing includes usability testing,[[14]](#cite_note-14) exploratory testing,[[15]](#cite_note-15) and property testing (scaling and security).[[16]](#cite_note-16)



Acceptance criteria and tests[[edit](/w/index.php?title=Acceptance_test-driven_development&action=edit&section=4 "Edit section: Acceptance criteria and tests")]
----------------------------------------------------------------------------------------------------------------------------------------------------------------


Acceptance criteria are a description of what would be checked by a test. Given a requirement such as "As a user, I want to check out a book from the library", an acceptance criterion might be, "verify the book is marked as checked out". An acceptance test for this requirement gives the details so that the test can be run with the same effect each time.



### Test format[[edit](/w/index.php?title=Acceptance_test-driven_development&action=edit&section=5 "Edit section: Test format")]


Acceptance tests usually follow this form:[[1]](#cite_note-Pugh11-1)


**Given (setup)**



A specified state of a system
**When (trigger)**



An action or event occurs
**Then (verification)**



The state of the system has changed or an output has been produced
Also, it is possible to add Statements that start with **AND** in any of the sections below (Given, When, Then).



For the example requirement, the steps could be listed as:


```
Given Book that has not been checked out
And User who is registered on the system
When User checks out a book
Then Book is marked as checked out

```

### Complete test[[edit](/w/index.php?title=Acceptance_test-driven_development&action=edit&section=6 "Edit section: Complete test")]


The previous steps do not include any specific example data, so that is added to complete the test:


**Given:**



Book that has not been checked out


| Books |  |
| --- | --- |
| Title | Checked out |
| Great book | No |


User who is registered on the system


| Users |
| --- |
| Name | Sam |


**When:**



User checks out a book


| Checkout action |
| --- |
| User | Sam | Checks out | Great book |


**Then:**



Book is marked as checked out


| Books |
| --- |
| Title | Checked out | User |
| Great book | Yes | Sam |


### Test examination[[edit](/w/index.php?title=Acceptance_test-driven_development&action=edit&section=7 "Edit section: Test examination")]


Examination of the test with specific data usually leads to many questions. For the sample, these might be:



* What if the book is already checked out?
* What if the book does not exist?
* What if the user is not registered on the system?
* Is there a date that the book is due to be checked-in?
* How many books can a user check out?


These questions help illuminate missing or ambiguous requirements. Additional details such as a due-date can be added to the expected result. Other acceptance tests can check that conditions such as attempting to check out a book that is already checked out produces the expected error.



### Another test example[[edit](/w/index.php?title=Acceptance_test-driven_development&action=edit&section=8 "Edit section: Another test example")]


Suppose the business customer wanted a business rule that a user could only check out one book at a time. The following test would demonstrate that:


**Scenario:**
Check that checkout business rule is enforced


**Given:**



Book that has been checked out


| Books |
| --- |
| Title | Checked out | User |
| Great book | Yes | Sam |
| Another great book | No |




| Users |
| --- |
| Name |
| Sam |


**When:**



User checks out another book


| Checkout action |
| --- |
| User | Sam | Checks out | Another great book |


**Then:**



Error occurs


| Error occurred |
| --- |
| Description |
| Violation of checkout business rule |


### Project acceptance tests[[edit](/w/index.php?title=Acceptance_test-driven_development&action=edit&section=9 "Edit section: Project acceptance tests")]


In addition to acceptance tests for requirements, acceptance tests can be used on a project as a whole.[[1]](#cite_note-Pugh11-1) For example, if this requirement was part of a library book checkout project, there could be acceptance tests for the whole project. These are often termed [SMART objectives](/wiki/SMART_criteria "SMART criteria"). An example test is "When the new library system is in production, the users will be able to check books in and out three times as fast as they do today".



See also[[edit](/w/index.php?title=Acceptance_test-driven_development&action=edit&section=10 "Edit section: See also")]
-----------------------------------------------------------------------------------------------------------------------


* [Concordion](/wiki/Concordion "Concordion")
* [FitNesse](/wiki/FitNesse "FitNesse")
* [Robot Framework](/wiki/Robot_Framework "Robot Framework")
* [Gauge (software)](/wiki/Gauge_(software) "Gauge (software)")
* [Cucumber (software)](/wiki/Cucumber_(software) "Cucumber (software)")


References[[edit](/w/index.php?title=Acceptance_test-driven_development&action=edit&section=11 "Edit section: References")]
---------------------------------------------------------------------------------------------------------------------------



1. ^ [***a***](#cite_ref-Pugh11_1-0) [***b***](#cite_ref-Pugh11_1-1) [***c***](#cite_ref-Pugh11_1-2) [***d***](#cite_ref-Pugh11_1-3) [***e***](#cite_ref-Pugh11_1-4) Pugh, Ken (2011). *Lean-Agile Acceptance Test-Driven Development: Better Software Through Collaboration*. Addison-Wesley. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-0321714084](/wiki/Special:BookSources/978-0321714084 "Special:BookSources/978-0321714084").
2. **[^](#cite_ref-2)** Adzic, Gojko. (2009) *Bridging the Communication Gap: Specification by Example and Agile Acceptance Testing*, Neuri Limited,
3. **[^](#cite_ref-3)** [Adzic, Gojko](/wiki/Gojko_Adzic "Gojko Adzic") (2011). *Specification by example: How successful teams deliver the right software*. Manning. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-0-321-27865-4](/wiki/Special:BookSources/978-0-321-27865-4 "Special:BookSources/978-0-321-27865-4").
4. **[^](#cite_ref-4)** Chelimsky, David, Dave Astels, Zach Dennis, Aslak Hellesøy, Bryan Helmkamp, and Dan North. *The RSpec Book: Behaviour Driven Development with RSpec, Cucumber, and Friends.* The Pragmatic Bookshelf.
5. **[^](#cite_ref-5)** ["Example Driven Design"](http://www.exampler.com/). Retrieved 2013-04-15.
6. **[^](#cite_ref-6)** ["Story Test-Driven Development"](http://industriallogic.com/papers/storytest.pdf) (PDF). Retrieved 2013-04-15.
7. **[^](#cite_ref-7)** Beck, Kent. Test Driven Development: By Example. Addison-Wesley Professional, 2002.
8. **[^](#cite_ref-8)** Melnik, Grigori, and Frank Maurer. Melnik, Grigori; Maurer, Frank (2007). "Multiple Perspectives on Executable Acceptance Test-Driven Development". *Agile Processes in Software Engineering and Extreme Programming*. Lecture Notes in Computer Science. Vol. 4536. pp. 245–249. [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.1007/978-3-540-73101-6\_46](https://doi.org/10.1007%2F978-3-540-73101-6_46). [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-3-540-73100-9](/wiki/Special:BookSources/978-3-540-73100-9 "Special:BookSources/978-3-540-73100-9").
9. **[^](#cite_ref-9)** Koskela, Lasse. (2007) Test Driven: TDD and Acceptance TDD for Java Developers. Manning Publications
10. **[^](#cite_ref-10)** Evans, Eric. (2003) *Domain-Driven Design: Tackling Complexity in the Heart of Software*. Addison-Wesley Professional.
11. **[^](#cite_ref-11)** [Weinberg, Gerald](/wiki/Gerald_Weinberg "Gerald Weinberg"); Gause, Donald (1989). [*Exploring Requirements: Quality Before Design*](https://archive.org/details/exploringrequire00gaus). Dorset House. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [0-932633-13-7](/wiki/Special:BookSources/0-932633-13-7 "Special:BookSources/0-932633-13-7").
12. **[^](#cite_ref-12)** Martin, Robert C., and Grigori Melnik.["Tests and Requirements, Requirements and Tests: A Möbius Strip"](http://www.gmelnik.com/papers/IEEE_Software_Moebius_GMelnik_RMartin.pdf) (PDF). Retrieved 2013-04-15.
13. **[^](#cite_ref-13)** [Test-driven\_development]
14. **[^](#cite_ref-14)** Meszaros, Gerard, and Janice Aston. (2006) "Adding Usability Testing to an Agile Project." Agile Conference
15. **[^](#cite_ref-15)** ["Exploratory Testing Explained"](http://www.satisfice.com/articles/et-article.pdf) (PDF).
16. **[^](#cite_ref-16)** Meszaros, Gerard.(2007) *xUnit Test Patterns: Refactoring Test Code*. Addison-Wesley.

External links[[edit](/w/index.php?title=Acceptance_test-driven_development&action=edit&section=12 "Edit section: External links")]
-----------------------------------------------------------------------------------------------------------------------------------


* [Example of automation frameworks](http://acceptancetestdrivendevelopment.com)





![](https://login.wikimedia.org/wiki/Special:CentralAutoLogin/start?type=1x1)
Retrieved from "<https://en.wikipedia.org/w/index.php?title=Acceptance_test-driven_development&oldid=1091258091>"
[Categories](/wiki/Help:Category "Help:Category"): * [Software development philosophies](/wiki/Category:Software_development_philosophies "Category:Software development philosophies")
* [Software testing](/wiki/Category:Software_testing "Category:Software testing")
* [Business analysis](/wiki/Category:Business_analysis "Category:Business analysis")

