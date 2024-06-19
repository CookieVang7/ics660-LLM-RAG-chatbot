



From Wikipedia, the free encyclopedia




| Part of a series on |
| --- |
| [Software development](/wiki/Software_development "Software development") |
| Core activities * [Data modeling](/wiki/Data_modeling "Data modeling") * [Processes](/wiki/Software_development_process "Software development process") * [Requirements](/wiki/Requirements_analysis "Requirements analysis") * [Design](/wiki/Software_design "Software design") * [Construction](/wiki/Software_construction "Software construction") * [Engineering](/wiki/Software_engineering "Software engineering") * [Testing](/wiki/Software_testing "Software testing") * [Debugging](/wiki/Debugging "Debugging") * [Deployment](/wiki/Software_deployment "Software deployment") * [Maintenance](/wiki/Software_maintenance "Software maintenance") |
| Paradigms and models * [Agile](/wiki/Agile_software_development "Agile software development") * [Cleanroom](/wiki/Cleanroom_software_engineering "Cleanroom software engineering") * [Incremental](/wiki/Incremental_build_model "Incremental build model") * [Prototyping](/wiki/Software_prototyping "Software prototyping") * [Spiral](/wiki/Spiral_model "Spiral model") * [V model](/wiki/V-model_(software_development) "V-model (software development)") * [Waterfall](/wiki/Waterfall_model "Waterfall model") |
| [Methodologies](/wiki/Software_development_methodology "Software development methodology") and frameworks * [ASD](/wiki/Adaptive_software_development "Adaptive software development") * [DevOps](/wiki/DevOps "DevOps") * [DAD](/wiki/Disciplined_agile_delivery "Disciplined agile delivery") * [DSDM](/wiki/Dynamic_systems_development_method "Dynamic systems development method") * [FDD](/wiki/Feature-driven_development "Feature-driven development") * [IID](/wiki/Iterative_and_incremental_development "Iterative and incremental development") * [Kanban](/wiki/Kanban_(development) "Kanban (development)") * [Lean SD](/wiki/Lean_software_development "Lean software development") * [LeSS](/wiki/Scrum_(software_development)#Large-scale_Scrum "Scrum (software development)") * [MDD](/wiki/Model-driven_development "Model-driven development") * [MSF](/wiki/Microsoft_Solutions_Framework "Microsoft Solutions Framework") * [PSP](/wiki/Personal_software_process "Personal software process") * [RAD](/wiki/Rapid_application_development "Rapid application development") * [RUP](/wiki/Rational_Unified_Process "Rational Unified Process") * [SAFe](/wiki/Scaled_agile_framework "Scaled agile framework") * [Scrum](/wiki/Scrum_(software_development) "Scrum (software development)") * [SEMAT](/wiki/SEMAT "SEMAT") * [TDD](/wiki/Test-driven_development "Test-driven development") * [TSP](/wiki/Team_software_process "Team software process") * [OpenUP](/wiki/OpenUP "OpenUP") * [UP](/wiki/Unified_Process "Unified Process") * [XP](/wiki/Extreme_programming "Extreme programming") |
| Supporting disciplines * [Configuration management](/wiki/Software_configuration_management "Software configuration management") * [Documentation](/wiki/Software_documentation "Software documentation") * [Software quality assurance](/wiki/Software_quality_assurance "Software quality assurance") * [Project management](/wiki/Software_project_management "Software project management") * [User experience](/wiki/User_experience "User experience") |
| Practices * [ATDD](/wiki/Acceptance_test%E2%80%93driven_development "Acceptance test–driven development") * [BDD](/wiki/Behavior-driven_development "Behavior-driven development") * [CCO](/wiki/Extreme_programming_practices#Collective_code_ownership "Extreme programming practices") * [CI](/wiki/Continuous_integration "Continuous integration") * [CD](/wiki/Continuous_delivery "Continuous delivery") * [DDD](/wiki/Domain-driven_design "Domain-driven design") * [PP](/wiki/Pair_programming "Pair programming") * SBE * [Stand-up](/wiki/Stand-up_meeting "Stand-up meeting") * [TDD](/wiki/Test-driven_development "Test-driven development") |
| [Tools](/wiki/Programming_tool "Programming tool") * [Compiler](/wiki/Compiler "Compiler") * [Debugger](/wiki/Debugger "Debugger") * [Profiler](/wiki/Profiling_(computer_programming) "Profiling (computer programming)") * [GUI designer](/wiki/Graphical_user_interface_builder "Graphical user interface builder") * [UML Modeling](/wiki/UML_tool "UML tool") * [IDE](/wiki/Integrated_development_environment "Integrated development environment") * [Build automation](/wiki/Build_automation "Build automation") * [Release automation](/wiki/Application-release_automation "Application-release automation") * [Infrastructure as code](/wiki/Infrastructure_as_code "Infrastructure as code") |
| Standards and bodies of knowledge * [CMMI](/wiki/Capability_Maturity_Model_Integration "Capability Maturity Model Integration") * [IEEE standards](/wiki/IEEE_Standards_Association "IEEE Standards Association") * [ISO 9001](/wiki/ISO_9001 "ISO 9001") * [ISO/IEC standards](/wiki/ISO/IEC_JTC_1/SC_7 "ISO/IEC JTC 1/SC 7") * [PMBOK](/wiki/Project_Management_Body_of_Knowledge "Project Management Body of Knowledge") * [SWEBOK](/wiki/Software_Engineering_Body_of_Knowledge "Software Engineering Body of Knowledge") * [ITIL](/wiki/ITIL "ITIL") * [IREB](/wiki/International_Requirements_Engineering_Board "International Requirements Engineering Board") * [OMG](/wiki/Object_Management_Group "Object Management Group") |
| Glossaries * [Artificial intelligence](/wiki/Glossary_of_artificial_intelligence "Glossary of artificial intelligence") * [Computer science](/wiki/Glossary_of_computer_science "Glossary of computer science") * [Electrical and electronics engineering](/wiki/Glossary_of_electrical_and_electronics_engineering "Glossary of electrical and electronics engineering") |
| Outlines * [Outline of software development](/wiki/Outline_of_software_development "Outline of software development") |
| * [v](/wiki/Template:Software_development_process "Template:Software development process") * [t](/wiki/Template_talk:Software_development_process "Template talk:Software development process") * [e](/wiki/Special:EditPage/Template:Software_development_process "Special:EditPage/Template:Software development process") |


**Specification by example** (**SBE**) is a collaborative approach to defining [requirements](/wiki/Software_requirement "Software requirement") and business-oriented [functional tests](/wiki/Functional_test "Functional test") for software products based on capturing and illustrating requirements using realistic examples instead of abstract statements. It is applied in the context of [agile software development](/wiki/Agile_software_development "Agile software development") methods, in particular [behavior-driven development](/wiki/Behavior-driven_development "Behavior-driven development"). This approach is particularly successful for managing requirements and functional tests on large-scale projects of significant domain and organisational complexity.[[1]](#cite_note-Adzic11-1)


Specification by example is also known as example-driven development, executable requirements, [acceptance test–driven development](/wiki/Acceptance_test%E2%80%93driven_development "Acceptance test–driven development") (ATDD[[2]](#cite_note-Pugh11-2) or A-TDD[[3]](#cite_note-Larman10-3)), Agile Acceptance Testing,[[4]](#cite_note-Adzic09-4) Test-Driven Requirements (TDR).




Advantages[[edit](/w/index.php?title=Specification_by_example&action=edit&section=1 "Edit section: Advantages")]
----------------------------------------------------------------------------------------------------------------


Highly abstract or novel new concepts can be difficult to understand without concrete examples.[*[citation needed](/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")*] Specification by example is intended to construct an accurate understanding, and significantly reduces feedback loops in software development, leading to less rework, higher product quality, faster turnaround time for software changes and better alignment of activities of various roles involved in software development such as testers, analysts and developers.[[1]](#cite_note-Adzic11-1)



Examples as a single source of truth[[edit](/w/index.php?title=Specification_by_example&action=edit&section=2 "Edit section: Examples as a single source of truth")]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------


A key aspect of specification by example is creating a [single source of truth](/wiki/Single_source_of_truth "Single source of truth") about required changes from all perspectives. When [business analysts](/wiki/Business_analyst "Business analyst") work on their own documents, [software developers](/wiki/Software_developer "Software developer") maintain their own documentation and testers maintain a separate set of functional tests, [software delivery](/wiki/Software_delivery "Software delivery") effectiveness is significantly reduced by the need to constantly coordinate and synchronise those different versions of truth. With short iterative cycles, such coordination is often required on weekly or biweekly basis. With Specification by example, different roles participate in creating a single source of truth that captures everyone's understanding. Examples are used to provide clarity and precision, so that the same information can be used both as a [specification](/wiki/Specification "Specification") and a business-oriented functional test. Any additional information discovered during development or delivery, such as clarification of functional gaps, missing or incomplete requirements or additional tests, is added to this single source of truth. As there is only one source of truth about the functionality, there is no need for coordination, translation and interpretation of knowledge inside the delivery cycle.


When applied to required changes, a refined set of examples is effectively a specification and a business-oriented [test for acceptance](/wiki/Acceptance_testing "Acceptance testing") of software functionality. After the change is implemented, specification with examples becomes a document explaining existing functionality. As the validation of such documents is automated, when they are validated frequently, such documents are a reliable source of information on business functionality of underlying software. To distinguish between such documents and typical printed documentation, which quickly gets outdated,[[4]](#cite_note-Adzic09-4) a complete set of specifications with examples is called Living Documentation.[[1]](#cite_note-Adzic11-1)



Key practices[[edit](/w/index.php?title=Specification_by_example&action=edit&section=3 "Edit section: Key practices")]
----------------------------------------------------------------------------------------------------------------------


Teams that apply Specification by example successfully commonly apply the following process patterns:[[1]](#cite_note-Adzic11-1)



* Deriving scope from goals
* Specifying collaboratively - through all-team specification workshops, smaller meetings or teleconference reviews
* Illustrating requirements using examples
* Refining specifications
* Automating tests based on examples
* Validating the underlying software frequently using the tests
* Evolving a documentation system from specifications with examples to support future development


Software teams that apply specification by example within a Scrum framework typically spend 5%-10% of their time in refining the product backlog, including specifying collaboratively, illustrating requirements using examples and refining examples.[[3]](#cite_note-Larman10-3)



### Example Mapping[[edit](/w/index.php?title=Specification_by_example&action=edit&section=4 "Edit section: Example Mapping")]


Example Mapping is a simple technique that can steer the conversation and derive Acceptance criteria in a short time. The process breaks stories into Rules and Examples documented in the form of specification by example, and is a widely used technique in the BDD sphere.[[5]](#cite_note-ccblog-wynne-5)



Applicability[[edit](/w/index.php?title=Specification_by_example&action=edit&section=5 "Edit section: Applicability")]
----------------------------------------------------------------------------------------------------------------------


Specification by example applies to projects with sufficient organisational and domain complexity to cause problems in understanding or communicating requirements from a business domain perspective. It does not apply to purely technical problems or where the key complexity is not in understanding or communicating knowledge. There are documented usages of this approach in domains including investment banking, financial trading, insurance, airline ticket reservation, online gaming and price comparison.[[1]](#cite_note-Adzic11-1) A similar approach is documented also in a nuclear-power plant simulation project.[[3]](#cite_note-Larman10-3)


Tests based on shared examples fit best in the category of tests designed to support a team while delivering software from a business perspective (see Agile Testing Quadrants[[6]](#cite_note-6)) - ensuring that the right product is built. They do not replace tests that look at a software system from a purely technical perspective (those that evaluate whether a product is built the right way, such as unit tests, component or technical integration tests) or tests that evaluate a product after it was developed (such as security penetration tests).



History[[edit](/w/index.php?title=Specification_by_example&action=edit&section=6 "Edit section: History")]
----------------------------------------------------------------------------------------------------------


The earliest documented usage of realistic examples as a single source of truth, requirements and automated tests, on software projects is the WyCash+ project, described by [Ward Cunningham](/wiki/Ward_Cunningham "Ward Cunningham") in the paper A Pattern Language of Competitive Development [[7]](#cite_note-Cunningham06-7)[[8]](#cite_note-Cunningham06-2-8) in 1996. The name Specification by Example was coined by [Martin Fowler](/wiki/Martin_Fowler_(software_engineer) "Martin Fowler (software engineer)") in 2004.[[9]](#cite_note-9)


Specification by Example is an evolution of the Customer Test[[10]](#cite_note-Beck99-10) practice of [Extreme Programming](/wiki/Extreme_Programming "Extreme Programming") proposed around 1997 and Ubiquitous Language[[11]](#cite_note-Evans04-11) idea from [Domain-driven design](/wiki/Domain-driven_design "Domain-driven design") from 2004, using the idea of black-box tests as requirements described by Weinberg and Gause[[12]](#cite_note-Weinberg89-12) in 1989.



Automation[[edit](/w/index.php?title=Specification_by_example&action=edit&section=7 "Edit section: Automation")]
----------------------------------------------------------------------------------------------------------------


Successful application of Specification by example on large scale projects requires frequent validation of software functionality against a large set of examples (tests). In practice, this requires tests based on examples to be automated. A common approach is to automate the tests but keep examples in a form readable and accessible to non-technical and technical team members, keeping the examples as a single source of truth. This process is supported by a class of test automation tools which work with tests divided into two aspects - the specification and the automation layer. The specification of a test which is often in a plain text or HTML form and contains the examples and auxiliary descriptions. The automation layer connects the example to a software system under test. Examples of such tools are:



* [Behat](/wiki/Behat_(computer_science) "Behat (computer science)")
* [Concordion](/wiki/Concordion "Concordion")
* [Cucumber](/wiki/Cucumber_(software) "Cucumber (software)")
* [FitNesse](/wiki/FitNesse "FitNesse")
* [Framework for Integrated Test](/wiki/Framework_for_Integrated_Test "Framework for Integrated Test")
* [Robot Framework](/wiki/Robot_Framework "Robot Framework")
* [SpecFlow](https://specflow.org/) for .NET
* [Gauge (software)](/wiki/Gauge_(software) "Gauge (software)")


References[[edit](/w/index.php?title=Specification_by_example&action=edit&section=8 "Edit section: References")]
----------------------------------------------------------------------------------------------------------------



1. ^ [***a***](#cite_ref-Adzic11_1-0) [***b***](#cite_ref-Adzic11_1-1) [***c***](#cite_ref-Adzic11_1-2) [***d***](#cite_ref-Adzic11_1-3) [***e***](#cite_ref-Adzic11_1-4) [Adzic, Gojko](/wiki/Gojko_Adzic "Gojko Adzic") (2011). *Specification by example: How successful teams deliver the right software*. Manning. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [9781617290084](/wiki/Special:BookSources/9781617290084 "Special:BookSources/9781617290084").
2. **[^](#cite_ref-Pugh11_2-0)** Pugh, Ken (2011). *Lean-Agile Acceptance Test Driven Development: Better Software Through Collaboration: A Tale of Lean-Agile Acceptance Test Driven Development*. Addison Wesley. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-0-321-71408-4](/wiki/Special:BookSources/978-0-321-71408-4 "Special:BookSources/978-0-321-71408-4").
3. ^ [***a***](#cite_ref-Larman10_3-0) [***b***](#cite_ref-Larman10_3-1) [***c***](#cite_ref-Larman10_3-2) Larman, Craig; Vodde, Bas (2010). [*Practices for Scaling Lean and Agile Development: Large, Multisite, and Offshore Product Development with Large-Scale Scrum*](https://archive.org/details/practicesforscal00larm_0). Pearson. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-0-321-63640-9](/wiki/Special:BookSources/978-0-321-63640-9 "Special:BookSources/978-0-321-63640-9").
4. ^ [***a***](#cite_ref-Adzic09_4-0) [***b***](#cite_ref-Adzic09_4-1) [Adzic, Gojko](/wiki/Gojko_Adzic "Gojko Adzic") (2009). *Bridging the Communication Gap: Specification by Example and Agile Acceptance Testing*. Neuri. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [0-9556836-1-0](/wiki/Special:BookSources/0-9556836-1-0 "Special:BookSources/0-9556836-1-0").
5. **[^](#cite_ref-ccblog-wynne_5-0)** Wynne, Matt (8 December 2015). ["Introducing Example Mapping"](https://cucumber.io/blog/bdd/example-mapping-introduction/). *Cucumber Blog*. Retrieved 10 May 2021.
6. **[^](#cite_ref-6)** [Crispin, Lisa](/w/index.php?title=Lisa_Crispin&action=edit&redlink=1 "Lisa Crispin (page does not exist)"); Gregory, Janet (2008). *Agile Testing: A Practical Guide for Testers and Agile Teams*. Addison Wesley. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-0-321-53446-0](/wiki/Special:BookSources/978-0-321-53446-0 "Special:BookSources/978-0-321-53446-0").
7. **[^](#cite_ref-Cunningham06_7-0)** *Pattern Languages of Program Design 2*. Addison-Wesley. 1996. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-0-201-89527-8](/wiki/Special:BookSources/978-0-201-89527-8 "Special:BookSources/978-0-201-89527-8").
8. **[^](#cite_ref-Cunningham06-2_8-0)** Ward Cunningham. ["EPISODES: A Pattern Language of Competitive Development Part I"](http://c2.com/ppr/episodes.html). C2.com. Retrieved 2014-01-08.
9. **[^](#cite_ref-9)** Martin Fowler 18 March 2004 (2004-03-18). ["SpecificationByExample"](http://martinfowler.com/bliki/SpecificationByExample.html). Martinfowler.com. Retrieved 2014-01-08.`{{[cite web](/wiki/Template:Cite_web "Template:Cite web")}}`: CS1 maint: numeric names: authors list ([link](/wiki/Category:CS1_maint:_numeric_names:_authors_list "Category:CS1 maint: numeric names: authors list"))
10. **[^](#cite_ref-Beck99_10-0)** [Beck, K.](/wiki/Kent_Beck "Kent Beck") (1999). *Extreme Programming Explained: Embrace Change*. Addison-Wesley. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-0-321-27865-4](/wiki/Special:BookSources/978-0-321-27865-4 "Special:BookSources/978-0-321-27865-4").
11. **[^](#cite_ref-Evans04_11-0)** [Evans, Eric](/w/index.php?title=Eric_Evans_(technologist)&action=edit&redlink=1 "Eric Evans (technologist) (page does not exist)") (2004). *Domain-Driven Design:Tackling Complexity in the Heart of Software*. Addison-Wesley. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [0-321-12521-5](/wiki/Special:BookSources/0-321-12521-5 "Special:BookSources/0-321-12521-5").
12. **[^](#cite_ref-Weinberg89_12-0)** [Weinberg, Gerald](/wiki/Gerald_Weinberg "Gerald Weinberg"); Gause, Donald (1989). [*Exploring Requirements: Quality Before Design*](https://archive.org/details/exploringrequire00gaus). Dorset House. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [0-932633-13-7](/wiki/Special:BookSources/0-932633-13-7 "Special:BookSources/0-932633-13-7").

External links[[edit](/w/index.php?title=Specification_by_example&action=edit&section=9 "Edit section: External links")]
------------------------------------------------------------------------------------------------------------------------


* [Google discussion group](https://groups.google.com/group/specificationbyexample)
* [Books, videos, tools and presentations from Specificationbyexample.com](http://specificationbyexample.com/resources.html)
* [Definition on Martin Fowler's bliki](http://martinfowler.com/bliki/SpecificationByExample.html)





![](https://login.wikimedia.org/wiki/Special:CentralAutoLogin/start?type=1x1)
Retrieved from "<https://en.wikipedia.org/w/index.php?title=Specification_by_example&oldid=1038243035>"
[Categories](/wiki/Help:Category "Help:Category"): * [Software development philosophies](/wiki/Category:Software_development_philosophies "Category:Software development philosophies")
* [Software testing](/wiki/Category:Software_testing "Category:Software testing")
* [Business analysis](/wiki/Category:Business_analysis "Category:Business analysis")
Hidden categories: * [CS1 maint: numeric names: authors list](/wiki/Category:CS1_maint:_numeric_names:_authors_list "Category:CS1 maint: numeric names: authors list")
* [All articles with unsourced statements](/wiki/Category:All_articles_with_unsourced_statements "Category:All articles with unsourced statements")
* [Articles with unsourced statements from May 2021](/wiki/Category:Articles_with_unsourced_statements_from_May_2021 "Category:Articles with unsourced statements from May 2021")

