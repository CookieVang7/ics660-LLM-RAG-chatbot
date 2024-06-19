



From Wikipedia, the free encyclopedia


Software system design modeling tool
"UML" redirects here. For other uses, see [UML (disambiguation)](/wiki/UML_(disambiguation) "UML (disambiguation)").




[![](//upload.wikimedia.org/wikipedia/commons/thumb/d/d5/UML_logo.svg/220px-UML_logo.svg.png)](/wiki/File:UML_logo.svg)

UML logo


The **unified modeling language** (**UML**) is a general-purpose visual [modeling language](/wiki/Modeling_language "Modeling language") that is intended to provide a standard way to visualize the design of a system.[[1]](#cite_note-OMG-1)


UML provides a standard notation for many types of diagrams which can be roughly divided into three main groups: behavior diagrams, interaction diagrams, and structure diagrams. 


The creation of UML was originally motivated by the desire to standardize the disparate notational systems and approaches to software design. It was developed at [Rational Software](/wiki/Rational_Software "Rational Software") in 1994–1995, with further development led by them through 1996.[[2]](#cite_note-:1-2)


In 1997, UML was adopted as a standard by the [Object Management Group](/wiki/Object_Management_Group "Object Management Group") (OMG) and has been managed by this organization ever since. In 2005, UML was also published by the [International Organization for Standardization](/wiki/International_Organization_for_Standardization "International Organization for Standardization") (ISO) and the [International Electrotechnical Commission](/wiki/International_Electrotechnical_Commission "International Electrotechnical Commission") (IEC) as the **ISO/IEC 19501** standard.[[3]](#cite_note-3) Since then the standard has been periodically revised to cover the latest revision of UML.[[4]](#cite_note-4)


In software engineering, most practitioners do not use UML, but instead produce informal hand drawn diagrams; these diagrams, however, often include elements from UML.[[5]](#cite_note-5): 536




History[[edit](/w/index.php?title=Unified_Modeling_Language&action=edit&section=1 "Edit section: History")]
-----------------------------------------------------------------------------------------------------------


[![](//upload.wikimedia.org/wikipedia/commons/thumb/d/d1/OO_Modeling_languages_history.jpg/320px-OO_Modeling_languages_history.jpg)](/wiki/File:OO_Modeling_languages_history.jpg)

History of object-oriented methods and notation


### Before UML 1.0[[edit](/w/index.php?title=Unified_Modeling_Language&action=edit&section=2 "Edit section: Before UML 1.0")]


UML has evolved since the second half of the 1990s and has its roots in the [object-oriented programming](/wiki/Object-oriented_programming "Object-oriented programming") methods developed in the late 1980s and early 1990s. The timeline (see image) shows the highlights of the history of object-oriented modeling methods and notation.


It is originally based on the notations of the [Booch method](/wiki/Booch_method "Booch method"), the [object-modeling technique](/wiki/Object-modeling_technique "Object-modeling technique") (OMT), and [object-oriented software engineering](/wiki/Object-oriented_software_engineering "Object-oriented software engineering") (OOSE), which it has integrated into a single language.[[6]](#cite_note-:0-6)


[Rational Software Corporation](/wiki/Rational_Software_Corporation "Rational Software Corporation") hired [James Rumbaugh](/wiki/James_Rumbaugh "James Rumbaugh") from [General Electric](/wiki/General_Electric "General Electric") in 1994 and after that, the company became the source for two of the most popular object-oriented modeling approaches of the day:[[7]](#cite_note-7) Rumbaugh's [object-modeling technique](/wiki/Object-modeling_technique "Object-modeling technique") (OMT) and [Grady Booch](/wiki/Grady_Booch "Grady Booch")'s method. They were soon assisted in their efforts by [Ivar Jacobson](/wiki/Ivar_Jacobson "Ivar Jacobson"), the creator of the [object-oriented software engineering](/wiki/Object-oriented_software_engineering "Object-oriented software engineering") (OOSE) method, who joined them at Rational in 1995.[[2]](#cite_note-:1-2)



### UML 1.x[[edit](/w/index.php?title=Unified_Modeling_Language&action=edit&section=3 "Edit section: UML 1.x")]


Under the technical leadership of those three (Rumbaugh, Jacobson, and Booch), a consortium called the [UML Partners](/wiki/UML_Partners "UML Partners") was organized in 1996 to complete the *Unified Modeling Language (UML)* specification and propose it to the Object Management Group (OMG) for standardization. The partnership also contained additional interested parties (for example [HP](/wiki/Hewlett-Packard "Hewlett-Packard"), [DEC](/wiki/Digital_Equipment_Corporation "Digital Equipment Corporation"), [IBM](/wiki/IBM "IBM"), and [Microsoft](/wiki/Microsoft "Microsoft")). The UML Partners' UML 1.0 draft was proposed to the OMG in January 1997 by the consortium. During the same month, the UML Partners formed a group, designed to define the exact meaning of language constructs, chaired by [Cris Kobryn](/wiki/Cris_Kobryn "Cris Kobryn") and administered by Ed Eykholt, to finalize the specification and integrate it with other standardization efforts. The result of this work, UML 1.1, was submitted to the OMG in August 1997 and adopted by the OMG in November 1997.[[2]](#cite_note-:1-2)[[8]](#cite_note-8)


After the first release, a task force was formed[[2]](#cite_note-:1-2) to improve the language, which released several minor revisions, 1.3, 1.4, and 1.5.[[9]](#cite_note-9)


The standards it produced (as well as the original standard) have been noted as being ambiguous and inconsistent.[[10]](#cite_note-10)



#### Cardinality notation[[edit](/w/index.php?title=Unified_Modeling_Language&action=edit&section=4 "Edit section: Cardinality notation")]


As with database Chen, Bachman, and ISO [ER diagrams](/wiki/ER_diagram "ER diagram"), class models are specified to use "look-across" [cardinalities](/wiki/Cardinality_(data_modeling) "Cardinality (data modeling)"), even though several authors ([Merise](/wiki/Merise "Merise"),[[11]](#cite_note-11)
Elmasri & Navathe,[[12]](#cite_note-12)
amongst others[[13]](#cite_note-13))
prefer same-side or "look-here" for roles and both minimum and maximum cardinalities. Recent researchers (Feinerer[[14]](#cite_note-14)
and Dullea et al.
[[15]](#cite_note-15))
have shown that the "look-across" technique used by UML and ER diagrams is less effective and less coherent when applied to *n*-ary relationships of order strictly greater than 2.


Feinerer says: "Problems arise if we operate under the look-across semantics as used for UML associations. Hartmann[[16]](#cite_note-16)
investigates this situation and shows how and why different transformations fail.", and: "As we will see on the next few pages, the look-across interpretation introduces several difficulties which prevent the extension of simple mechanisms from binary to *n*-ary associations."



### UML 2[[edit](/w/index.php?title=Unified_Modeling_Language&action=edit&section=5 "Edit section: UML 2")]


UML 2.0 major revision replaced version 1.5 in 2005, which was developed with an enlarged consortium to improve the language further to reflect new experiences on the usage of its features.[[17]](#cite_note-17)


Although UML 2.1 was never released as a formal specification, versions 2.1.1 and 2.1.2 appeared in 2007, followed by UML 2.2 in February 2009. UML 2.3 was formally released in May 2010.[[18]](#cite_note-spec-18) UML 2.4.1 was formally released in August 2011.[[18]](#cite_note-spec-18) UML 2.5 was released in October 2012 as an "In progress" version and was officially released in June 2015.[[18]](#cite_note-spec-18)
The formal version 2.5.1 was adopted in December 2017.[[1]](#cite_note-OMG-1)


There are four parts to the UML 2.x specification:



* The Superstructure that defines the notation and semantics for diagrams and their model elements
* The Infrastructure that defines the core metamodel on which the Superstructure is based
* The [Object Constraint Language](/wiki/Object_Constraint_Language "Object Constraint Language") (OCL) for defining rules for model elements
* The UML Diagram Interchange that defines how UML 2 diagram layouts are exchanged


Until UML 2.4.1, the latest versions of these standards were:[[19]](#cite_note-Versions2.4.1-19)



* UML Superstructure version 2.4.1
* UML Infrastructure version 2.4.1
* OCL version 2.3.1
* UML Diagram Interchange version 1.0.


Since version 2.5, the UML Specification has been simplified (without Superstructure and Infrastructure), and the latest versions of these standards are now:[[20]](#cite_note-LatestVersions-20)



* UML Specification 2.5.1
* OCL version 2.4


It continues to be updated and improved by the revision task force, who resolve any issues with the language.[[21]](#cite_note-21)



Design[[edit](/w/index.php?title=Unified_Modeling_Language&action=edit&section=6 "Edit section: Design")]
---------------------------------------------------------------------------------------------------------


[![](//upload.wikimedia.org/wikipedia/commons/8/83/Component-based-Software-Engineering-example2.png)](/wiki/File:Component-based-Software-Engineering-example2.png)

An example of components in a travel reservation system


UML offers a way to visualize a system's architectural blueprints in a diagram, including elements such as:[[6]](#cite_note-:0-6)



* any [activities](/wiki/Activity_(UML) "Activity (UML)") (jobs);
* individual [components](/wiki/Component_(UML) "Component (UML)") of the system;
	+ and how they can interact with other [software components](/wiki/Software_component "Software component");
* how the system will run;
* how entities interact with others (components and interfaces);
* external [user interface](/wiki/User_interface "User interface").


Although originally intended for object-oriented design documentation, UML has been extended to a larger set of design documentation (as listed above),[[22]](#cite_note-22) and has been found useful in many contexts.[[23]](#cite_note-UML,_Success_Stories-23)



### Software development methods[[edit](/w/index.php?title=Unified_Modeling_Language&action=edit&section=7 "Edit section: Software development methods")]


UML is not a development method by itself;[[24]](#cite_note-24) however, it was designed to be compatible with the leading object-oriented software development methods of its time, for example, [OMT](/wiki/Object-modeling_technique "Object-modeling technique"), [Booch method](/wiki/Booch_method "Booch method"), [Objectory](/wiki/Objectory "Objectory"), and especially [RUP](/wiki/Rational_Unified_Process "Rational Unified Process") it was originally intended to be used with when work began at Rational Software.



### Modeling[[edit](/w/index.php?title=Unified_Modeling_Language&action=edit&section=8 "Edit section: Modeling")]


It is important to distinguish between the UML model and the set of diagrams of a system. A diagram is a partial graphic representation of a system's model. The set of diagrams need not completely cover the model and deleting a diagram does not change the model. The model may also contain documentation that drives the model elements and diagrams (such as written use cases).


UML diagrams represent two different views of a system model:[[25]](#cite_note-25)



* Static (or *structural*) view: emphasizes the static structure of the system using objects, attributes, operations and relationships. It includes [class diagrams](/wiki/Class_diagram "Class diagram") and [composite structure diagrams](/wiki/Composite_structure_diagram "Composite structure diagram").
* Dynamic (or *behavioral*) view: emphasizes the dynamic behavior of the system by showing collaborations among objects and changes to the internal states of objects. This view includes [sequence diagrams](/wiki/Sequence_diagram "Sequence diagram"), [activity diagrams](/wiki/Activity_diagram "Activity diagram") and [state machine diagrams](/wiki/UML_state_machine "UML state machine").


UML models can be exchanged among [UML tools](/wiki/UML_tool "UML tool") by using the [XML Metadata Interchange](/wiki/XML_Metadata_Interchange "XML Metadata Interchange") (XMI) format.


In UML, one of the key tools for behavior modeling is the use-case model, caused by [OOSE](/wiki/OOSE "OOSE"). Use cases are a way of specifying required usages of a system. Typically, they are used to capture the requirements of a system, that is, what a system is supposed to do.[[26]](#cite_note-26)



Diagrams[[edit](/w/index.php?title=Unified_Modeling_Language&action=edit&section=9 "Edit section: Diagrams")]
-------------------------------------------------------------------------------------------------------------




| [UML diagram types](#Diagrams) |
| --- |
| Structural UML diagrams |
| * [Class diagram](/wiki/Class_diagram "Class diagram") * [Component diagram](/wiki/Component_diagram "Component diagram") * [Composite structure diagram](/wiki/Composite_structure_diagram "Composite structure diagram") * [Deployment diagram](/wiki/Deployment_diagram "Deployment diagram") * [Object diagram](/wiki/Object_diagram "Object diagram") * [Package diagram](/wiki/Package_diagram "Package diagram") * [Profile diagram](/wiki/Profile_diagram "Profile diagram") |
| Behavioral UML diagrams |
| * [Activity diagram](/wiki/Activity_diagram "Activity diagram") * [Communication diagram](/wiki/Communication_diagram "Communication diagram") * [Interaction overview diagram](/wiki/Interaction_overview_diagram "Interaction overview diagram") * [Sequence diagram](/wiki/Sequence_diagram "Sequence diagram") * [State diagram](/wiki/UML_state_machine "UML state machine") * [Timing diagram](/wiki/Timing_diagram_(Unified_Modeling_Language) "Timing diagram (Unified Modeling Language)") * [Use case diagram](/wiki/Use_case_diagram "Use case diagram") |
| * [v](/wiki/Template:UML_diagram_types "Template:UML diagram types") * [t](/w/index.php?title=Template_talk:UML_diagram_types&action=edit&redlink=1 "Template talk:UML diagram types (page does not exist)") * [e](/wiki/Special:EditPage/Template:UML_diagram_types "Special:EditPage/Template:UML diagram types") |


UML 2 has many types of diagrams, which are divided into two categories.[[6]](#cite_note-:0-6) Some types represent *structural* information, and the rest represent general types of *behavior*, including a few that represent different aspects of *interactions*. These diagrams can be categorized hierarchically as shown in the following class diagram:[[6]](#cite_note-:0-6)



[![Hierarchy of UML 2.2 Diagrams, shown as a class diagram](//upload.wikimedia.org/wikipedia/commons/thumb/e/ed/UML_diagrams_overview.svg/600px-UML_diagrams_overview.svg.png)](/wiki/File:UML_diagrams_overview.svg "Hierarchy of UML 2.2 Diagrams, shown as a class diagram")

Hierarchy of UML 2.2 Diagrams, shown as a [class diagram](/wiki/Class_diagram "Class diagram")


These diagrams may all contain comments or notes explaining usage, constraint, or intent.



### Structure diagrams[[edit](/w/index.php?title=Unified_Modeling_Language&action=edit&section=10 "Edit section: Structure diagrams")]


Structure diagrams represent the static aspects of the system. It emphasizes the things that must be present in the system being modeled. Since structure diagrams represent the structure, they are used extensively in documenting the [software architecture](/wiki/Software_architecture "Software architecture") of software systems. For example, the [component diagram](/wiki/Component_diagram "Component diagram") describes how a software system is split up into components and shows the dependencies among these components.



* [![Component diagram](//upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Policy_Admin_Component_Diagram.PNG/120px-Policy_Admin_Component_Diagram.PNG)](/wiki/File:Policy_Admin_Component_Diagram.PNG "Component diagram")
[Component diagram](/wiki/Component_diagram "Component diagram")
* [![Class diagram](//upload.wikimedia.org/wikipedia/commons/thumb/4/41/BankAccount1.svg/120px-BankAccount1.svg.png)](/wiki/File:BankAccount1.svg "Class diagram")
[Class diagram](/wiki/Class_diagram "Class diagram")


### Behavior diagrams[[edit](/w/index.php?title=Unified_Modeling_Language&action=edit&section=11 "Edit section: Behavior diagrams")]


Behavior diagrams represent the dynamic aspect of the system. It emphasizes what must happen in the system being modeled. Since behavior diagrams illustrate the behavior of a system, they are used extensively to describe the functionality of software systems. As an example, the [activity diagram](/wiki/Activity_diagram "Activity diagram") describes the business and operational step-by-step activities of the components in a system.



* [![Activity diagram](//upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Activity_conducting.svg/111px-Activity_conducting.svg.png)](/wiki/File:Activity_conducting.svg "Activity diagram")
[Activity diagram](/wiki/Activity_diagram "Activity diagram")
* [![Use case diagram](//upload.wikimedia.org/wikipedia/commons/thumb/7/71/UML_Use_Case_diagram.svg/120px-UML_Use_Case_diagram.svg.png)](/wiki/File:UML_Use_Case_diagram.svg "Use case diagram")
[Use case diagram](/wiki/Use_case_diagram "Use case diagram")


#### Interaction diagrams[[edit](/w/index.php?title=Unified_Modeling_Language&action=edit&section=12 "Edit section: Interaction diagrams")]


Interaction diagrams, a subset of behavior diagrams, emphasize the [flow of control](/wiki/Flow_of_control "Flow of control") and data among the things in the system being modeled. For example, the [sequence diagram](/wiki/Sequence_diagram "Sequence diagram") shows how objects communicate with each other regarding a sequence of messages.



* [![Sequence diagram](//upload.wikimedia.org/wikipedia/commons/thumb/9/9b/CheckEmail.svg/120px-CheckEmail.svg.png)](/wiki/File:CheckEmail.svg "Sequence diagram")
[Sequence diagram](/wiki/Sequence_diagram "Sequence diagram")
* [![Communication diagram](//upload.wikimedia.org/wikipedia/commons/thumb/b/b4/UML_Communication_diagram.svg/120px-UML_Communication_diagram.svg.png)](/wiki/File:UML_Communication_diagram.svg "Communication diagram")
[Communication diagram](/wiki/Communication_diagram "Communication diagram")


Metamodeling[[edit](/w/index.php?title=Unified_Modeling_Language&action=edit&section=13 "Edit section: Metamodeling")]
----------------------------------------------------------------------------------------------------------------------


Main article: [Meta-Object Facility](/wiki/Meta-Object_Facility "Meta-Object Facility")
[![](//upload.wikimedia.org/wikipedia/commons/thumb/9/93/M0-m3.png/320px-M0-m3.png)](/wiki/File:M0-m3.png)

Illustration of the Meta-Object Facility


The [Object Management Group](/wiki/Object_Management_Group "Object Management Group") (OMG) has developed a [metamodeling](/wiki/Metamodeling "Metamodeling") architecture to define the UML, called the [Meta-Object Facility](/wiki/Meta-Object_Facility "Meta-Object Facility").[[27]](#cite_note-27) MOF is designed as a four-layered architecture, as shown in the image at right. It provides a meta-meta model at the top, called the M3 layer. This M3-model is the language used by Meta-Object Facility to build metamodels, called M2-models.


The most prominent example of a Layer 2 Meta-Object Facility model is the UML metamodel, which describes the UML itself. These M2-models describe elements of the M1-layer, and thus M1-models. These would be, for example, models written in UML. The last layer is the M0-layer or data layer. It is used to describe runtime instances of the system.[[28]](#cite_note-28)


The meta-model can be extended using a mechanism called [stereotyping](/wiki/Stereotype_(UML) "Stereotype (UML)"). This has been criticized as being insufficient/untenable by [Brian Henderson-Sellers](/wiki/Brian_Henderson-Sellers "Brian Henderson-Sellers") and Cesar Gonzalez-Perez in "Uses and Abuses of the Stereotype Mechanism in UML 1.x and 2.0".[[29]](#cite_note-UsesAbusesStereotype-29)



Adoption[[edit](/w/index.php?title=Unified_Modeling_Language&action=edit&section=14 "Edit section: Adoption")]
--------------------------------------------------------------------------------------------------------------


In 2013, UML had been marketed by OMG for many contexts, but aimed primarily at software development with limited success.[[23]](#cite_note-UML,_Success_Stories-23)[[30]](#cite_note-30)


It has been treated, at times, as a design [silver bullet](/wiki/No_silver_bullet "No silver bullet"), which leads to problems. UML misuse includes overuse (designing every part of the system with it, which is unnecessary) and assuming that novices can design with it.[[31]](#cite_note-31)


It is considered a large language, with many [constructs](/wiki/Syntax_(programming_languages) "Syntax (programming languages)"). Some people (including [Jacobson](/wiki/Ivar_Jacobson "Ivar Jacobson")) feel that UML's size hinders learning (and therefore using) it.[[32]](#cite_note-32)


MS Visual Studio dropped support for UML in 2016 due to lack of usage.[[33]](#cite_note-33)


According to Google Trends UML has been on a steady decline since 2004.[[34]](#cite_note-34)



See also[[edit](/w/index.php?title=Unified_Modeling_Language&action=edit&section=15 "Edit section: See also")]
--------------------------------------------------------------------------------------------------------------


* [Applications of UML](/wiki/Applications_of_UML "Applications of UML")
* [Business Process Model and Notation](/wiki/Business_Process_Model_and_Notation "Business Process Model and Notation") (BPMN)
* [C4 model](/wiki/C4_model "C4 model")
* [Department of Defense Architecture Framework](/wiki/Department_of_Defense_Architecture_Framework "Department of Defense Architecture Framework")
* [DOT (graph description language)](/wiki/DOT_(graph_description_language) "DOT (graph description language)")
* [List of Unified Modeling Language tools](/wiki/List_of_Unified_Modeling_Language_tools "List of Unified Modeling Language tools")
* [MODAF](/wiki/MODAF "MODAF")
* [Model-based testing](/wiki/Model-based_testing "Model-based testing")
* [Model-driven engineering](/wiki/Model-driven_engineering "Model-driven engineering")
* [Object-oriented role analysis and modeling](/wiki/Object-oriented_role_analysis_and_modeling "Object-oriented role analysis and modeling")
* [Process Specification Language](/wiki/Process_Specification_Language "Process Specification Language")
* [Systems Modeling Language](/wiki/Systems_Modeling_Language "Systems Modeling Language") (SysML)


References[[edit](/w/index.php?title=Unified_Modeling_Language&action=edit&section=16 "Edit section: References")]
------------------------------------------------------------------------------------------------------------------



1. ^ [***a***](#cite_ref-OMG_1-0) [***b***](#cite_ref-OMG_1-1) [*Unified Modeling Language 2.5.1*](https://www.omg.org/spec/UML/2.5.1/PDF). [OMG](/wiki/Object_Management_Group "Object Management Group") Document Number formal/2017-12-05. [Object Management Group](/wiki/Object_Management_Group "Object Management Group") Standards Development Organization (OMG SDO). December 2017.
2. ^ [***a***](#cite_ref-:1_2-0) [***b***](#cite_ref-:1_2-1) [***c***](#cite_ref-:1_2-2) [***d***](#cite_ref-:1_2-3) [*Unified Modeling Language User Guide, The*](http://www.informit.com/store/unified-modeling-language-user-guide-9780321267979) (2 ed.). Addison-Wesley. 2005. p. 496. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [0321267974](/wiki/Special:BookSources/0321267974 "Special:BookSources/0321267974").
See the sample content: look for history
3. **[^](#cite_ref-3)** ["ISO/IEC 19501:2005 - Information technology - Open Distributed Processing - Unified Modeling Language (UML) Version 1.4.3"](http://www.iso.org/iso/home/store/catalogue_tc/catalogue_detail.htm?csnumber=32620). Iso.org. 1 April 2005. Retrieved 7 May 2015.
4. **[^](#cite_ref-4)** ["ISO/IEC 19505-1:2012 - Information technology - Object Management Group Unified Modeling Language (OMG UML) - Part 1: Infrastructure"](http://www.iso.org/iso/iso_catalogue/catalogue_tc/catalogue_detail.htm?csnumber=32624). Iso.org. 20 April 2012. Retrieved 10 April 2014.
5. **[^](#cite_ref-5)** Sebastian Baltes; Stephan Diehl (11 November 2014). ["Sketches and diagrams in practice"](https://doi.org/10.1145/2635868.2635891). *Proceedings of the 22nd [ACM SIGSOFT](/wiki/ACM_SIGSOFT "ACM SIGSOFT") International Symposium on Foundations of Software Engineering*. FSE 2014. [Association for Computing Machinery](/wiki/Association_for_Computing_Machinery "Association for Computing Machinery"). pp. 530–541. [arXiv](/wiki/ArXiv_(identifier) "ArXiv (identifier)"):[1706.09172](https://arxiv.org/abs/1706.09172). [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.1145/2635868.2635891](https://doi.org/10.1145%2F2635868.2635891). [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-1-4503-3056-5](/wiki/Special:BookSources/978-1-4503-3056-5 "Special:BookSources/978-1-4503-3056-5"). [S2CID](/wiki/S2CID_(identifier) "S2CID (identifier)") [2436333](https://api.semanticscholar.org/CorpusID:2436333).
6. ^ [***a***](#cite_ref-:0_6-0) [***b***](#cite_ref-:0_6-1) [***c***](#cite_ref-:0_6-2) [***d***](#cite_ref-:0_6-3) ["OMG Unified Modeling Language (OMG UML), Superstructure. Version 2.4.1"](http://www.omg.org/spec/UML/2.4.1/Superstructure/PDF). Object Management Group. Retrieved 9 April 2014.
7. **[^](#cite_ref-7)** Andreas Zendler (1997) *Advanced Concepts, Life Cycle Models and Tools for Objeckt-Oriented Software Development*. p. 122
8. **[^](#cite_ref-8)** ["UML Specification version 1.1 (OMG document ad/97-08-11)"](http://www.omg.org/cgi-bin/doc?ad/97-08-11). Omg.org. Retrieved 22 September 2011.
9. **[^](#cite_ref-9)** ["UML"](http://www.omg.org/spec/UML/). Omg.org. Retrieved 10 April 2014.
10. **[^](#cite_ref-10)** Génova et alia 2004 "Open Issues in Industrial Use Case Modeling"
11. **[^](#cite_ref-11)** Hubert Tardieu, Arnold Rochfeld and René Colletti La methode MERISE: Principes et outils (Paperback - 1983)
12. **[^](#cite_ref-12)** Elmasri, Ramez, B. Shamkant, Navathe, Fundamentals of Database Systems, third ed., Addison-Wesley, Menlo Park, CA, USA, 2000.
13. **[^](#cite_ref-13)** Paolo Atzeni; Wesley Chu; Hongjun Lu; Shuigeng Zhou; Tok Wang Ling, eds. (27 October 2004). [*Conceptual Modeling – ER 2004: 23rd International Conference on Conceptual Modeling, Shanghai, China, November 8–12, 2004*](https://www.amazon.com/Conceptual-Modeling-International-Conference-Proceedings/dp/3540237232). [Lecture Notes in Computer Science](/wiki/Lecture_Notes_in_Computer_Science "Lecture Notes in Computer Science") 3288 (2004 ed.). [Springer](/wiki/Springer_Publishing "Springer Publishing").
14. **[^](#cite_ref-14)** Ingo Feinerer (March 2007). [*A Formal Treatment of UML Class Diagrams as an Efficient Method for Configuration Management*](https://publik.tuwien.ac.at/files/pub-inf_4582.pdf) (PDF) (Doctor of Technical Sciences thesis). Vienna: Technical University of Vienna.
15. **[^](#cite_ref-15)** James Dullea; Il-Yeol Song; Ioanna Lamprou (1 November 2003). "An analysis of structural validity in entity-relationship modeling". *Data & Knowledge Engineering*. **47** (2): 167–205. [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.1016/S0169-023X(03)00049-1](https://doi.org/10.1016%2FS0169-023X%2803%2900049-1).
16. **[^](#cite_ref-16)** Sven Hartmann (17 January 2003). [*Reasoning about participation constraints and Chen's constraints*](https://dl.acm.org/doi/abs/10.5555/820085.820110). ADC '03: Proceedings of the 14th Australasian database conference. [Australian Computer Society](/wiki/Australian_Computer_Society "Australian Computer Society"). pp. 105–113. [![Open access icon](//upload.wikimedia.org/wikipedia/commons/thumb/7/77/Open_Access_logo_PLoS_transparent.svg/9px-Open_Access_logo_PLoS_transparent.svg.png)](/wiki/Open_access "open access publication – free to read")
17. **[^](#cite_ref-17)** ["UML 2.0"](http://www.omg.org/spec/UML/2.0/). Omg.org. Retrieved 22 September 2011.
18. ^ [***a***](#cite_ref-spec_18-0) [***b***](#cite_ref-spec_18-1) [***c***](#cite_ref-spec_18-2) ["UML"](http://www.omg.org/spec/UML/). Omg.org. Retrieved 22 September 2011.
19. **[^](#cite_ref-Versions2.4.1_19-0)** OMG. ["OMG Formal Specifications (Modeling and Metadata paragraph)"](http://www.omg.org/spec/#M&M). Retrieved 12 February 2016.
20. **[^](#cite_ref-LatestVersions_20-0)** OMG. ["about the unified modeling language specification"](https://www.omg.org/spec/UML/About-UML/). Retrieved 22 February 2020.
21. **[^](#cite_ref-21)** ["Issues for UML 2.6 Revision task Force mailing list"](https://issues.omg.org/issues/lists/uml2-rtf). Omg.org. Retrieved 10 April 2014.
22. **[^](#cite_ref-22)** Satish Mishra (1997). ["Visual Modeling & Unified Modeling Language (UML): Introduction to UML"](http://www2.informatik.hu-berlin.de/~hs/Lehre/2004-WS_SWQS/20050107_Ex_UML.ppt) [Archived](https://web.archive.org/web/20110720091651/http://www2.informatik.hu-berlin.de/~hs/Lehre/2004-WS_SWQS/20050107_Ex_UML.ppt) 20 July 2011 at the [Wayback Machine](/wiki/Wayback_Machine "Wayback Machine"). Rational Software Corporation. Accessed 9 November 2008.
23. ^ [***a***](#cite_ref-UML,_Success_Stories_23-0) [***b***](#cite_ref-UML,_Success_Stories_23-1) ["UML, Success Stories"](http://www.uml.org/uml_success_stories/index.htm). Retrieved 9 April 2014.
24. **[^](#cite_ref-24)** John Hunt (2000). *The Unified Process for Practitioners: Object-oriented Design, UML and Java*. Springer, 2000. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [1-85233-275-1](/wiki/Special:BookSources/1-85233-275-1 "Special:BookSources/1-85233-275-1"). p. 5.door
25. **[^](#cite_ref-25)** Jon Holt Institution of Electrical Engineers (2004). *UML for Systems Engineering: Watching the Wheels* IET, 2004, [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [0-86341-354-4](/wiki/Special:BookSources/0-86341-354-4 "Special:BookSources/0-86341-354-4"). p. 58
26. **[^](#cite_ref-26)** Manuel Almendros-Jiménez, Jesús & Iribarne, Luis. (2007). Describing Use-Case Relationships with Sequence Diagrams. Comput. J.. 50. 116-128. 10.1093/comjnl/bxl053.
27. **[^](#cite_ref-27)** Iman Poernomo (2006) "[The Meta-Object Facility Typed](http://calcium.dcs.kcl.ac.uk/1259/1/acm-paper.pdf) [Archived](https://web.archive.org/web/20160630002118/http://calcium.dcs.kcl.ac.uk/1259/1/acm-paper.pdf) 30 June 2016 at the [Wayback Machine](/wiki/Wayback_Machine "Wayback Machine")" in: *Proceeding SAC '06 Proceedings of the 2006 ACM symposium on Applied computing*. pp. 1845–1849
28. **[^](#cite_ref-28)** ["UML 2.4.1 Infrastructure"](http://www.omg.org/spec/UML/2.4.1/Infrastructure/PDF/). Omg.org. 5 August 2011. Retrieved 10 April 2014.
29. **[^](#cite_ref-UsesAbusesStereotype_29-0)** [Brian Henderson-Sellers](/wiki/Brian_Henderson-Sellers "Brian Henderson-Sellers"); Cesar Gonzalez-Perez (1 October 2006). "Uses and abuses of the stereotype mechanism in UML 1.x and 2.0". *MoDELS '06: Proceedings of the 9th international conference on Model Driven Engineering Languages and Systems*. [Lecture Notes in Computer Science](/wiki/Lecture_Notes_in_Computer_Science "Lecture Notes in Computer Science") 4199. [Berlin](/wiki/Berlin "Berlin"), Germany: [Springer-Verlag](/wiki/Springer-Verlag "Springer-Verlag"): 16–26. [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.1007/11880240\_2](https://doi.org/10.1007%2F11880240_2).
30. **[^](#cite_ref-30)** ["UML 2.5: Do you even care?"](http://www.drdobbs.com/architecture-and-design/uml-25-do-you-even-care/240163702?queryText=uml). "UML truly is ubiquitous"
31. **[^](#cite_ref-31)** ["Death by UML Fever"](http://queue.acm.org/detail.cfm?id=984495).
32. **[^](#cite_ref-32)** ["Ivar Jacobson on UML, MDA, and the future of methodologies"](http://www.infoq.com/interviews/Ivar_Jacobson).
33. **[^](#cite_ref-33)** Krill, Paul (18 October 2016). ["UML to be ejected from Microsoft Visual Studio"](https://www.infoworld.com/article/3131600/uml-to-be-ejected-from-microsoft-visual-studio.html). *InfoWorld*. Retrieved 23 July 2023.
34. **[^](#cite_ref-34)** ["Google Trends"](https://web.archive.org/web/20230723193301/https://trends.google.com/trends/explore?date=all&geo=US&q=UML&hl=en). *Google Trends*. Archived from [the original](https://trends.google.com/trends/explore?date=all&geo=US&q=UML&hl=en) on 23 July 2023. Retrieved 23 July 2023.

Further reading[[edit](/w/index.php?title=Unified_Modeling_Language&action=edit&section=17 "Edit section: Further reading")]
----------------------------------------------------------------------------------------------------------------------------


* Ambler, Scott William (2004). [*The Object Primer: Agile Model Driven Development with UML 2*](https://web.archive.org/web/20100131215505/http://www.ambysoft.com/books/theObjectPrimer.html). Cambridge University Press. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [0-521-54018-6](/wiki/Special:BookSources/0-521-54018-6 "Special:BookSources/0-521-54018-6"). Archived from [the original](http://www.ambysoft.com/books/theObjectPrimer.html) on 31 January 2010. Retrieved 29 April 2006.
* Chonoles, Michael Jesse; James A. Schardt (2003). [*UML 2 for Dummies*](https://archive.org/details/uml2fordummies00chon). Wiley Publishing. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [0-7645-2614-6](/wiki/Special:BookSources/0-7645-2614-6 "Special:BookSources/0-7645-2614-6").
* [Fowler, Martin](/wiki/Martin_Fowler_(software_engineer) "Martin Fowler (software engineer)") (2004). *UML Distilled: A Brief Guide to the Standard Object Modeling Language* (3rd ed.). Addison-Wesley. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [0-321-19368-7](/wiki/Special:BookSources/0-321-19368-7 "Special:BookSources/0-321-19368-7").
* [Jacobson, Ivar](/wiki/Ivar_Jacobson "Ivar Jacobson"); Grady Booch; James Rumbaugh (1998). *The Unified Software Development Process*. Addison Wesley Longman. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [0-201-57169-2](/wiki/Special:BookSources/0-201-57169-2 "Special:BookSources/0-201-57169-2").
* [Martin, Robert Cecil](/wiki/Robert_Cecil_Martin "Robert Cecil Martin") (2003). [*UML for Java Programmers*](https://archive.org/details/umlforjavaprogra00mart). Prentice Hall. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [0-13-142848-9](/wiki/Special:BookSources/0-13-142848-9 "Special:BookSources/0-13-142848-9").
* Noran, Ovidiu S. ["Business Modelling: UML vs. IDEF"](https://www.area-c54.it/public/business%20modelling%20-%20uml%20vs%20idef.pdf) (PDF). Retrieved 14 November 2022.
* Horst Kargl. ["Interactive UML Metamodel with additional Examples"](http://umlnotation.sparxsystems.eu/).
* Penker, Magnus; [Hans-Erik Eriksson](/wiki/Hans-Erik_Eriksson "Hans-Erik Eriksson") (2000). [*Business Modeling with UML*](https://archive.org/details/businessmodeling00erik). John Wiley & Sons. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [0-471-29551-5](/wiki/Special:BookSources/0-471-29551-5 "Special:BookSources/0-471-29551-5").
* Douglass, Bruce Powel. ["Bruce Douglass: Real-Time Agile Systems and Software Development"](https://www.bruce-douglass.com/) (web). Retrieved 1 January 2019.
* Douglass, Bruce (2014). [*Real-Time UML Workshop 2nd Edition*](https://archive.org/details/businessmodeling00erik). Newnes. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-0-471-29551-8](/wiki/Special:BookSources/978-0-471-29551-8 "Special:BookSources/978-0-471-29551-8").
* Douglass, Bruce (2004). *Real-Time UML 3rd Edition*. Newnes. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-0321160768](/wiki/Special:BookSources/978-0321160768 "Special:BookSources/978-0321160768").
* Douglass, Bruce (2002). *Real-Time Design Patterns*. Addison-Wesley Professional. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-0201699562](/wiki/Special:BookSources/978-0201699562 "Special:BookSources/978-0201699562").
* Douglass, Bruce (2009). *Real-Time Agility*. Addison-Wesley Professional. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-0321545497](/wiki/Special:BookSources/978-0321545497 "Special:BookSources/978-0321545497").
* Douglass, Bruce (2010). *Design Patterns for Embedded Systems in C*. Newnes. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-1856177078](/wiki/Special:BookSources/978-1856177078 "Special:BookSources/978-1856177078").


External links[[edit](/w/index.php?title=Unified_Modeling_Language&action=edit&section=18 "Edit section: External links")]
--------------------------------------------------------------------------------------------------------------------------




![](//upload.wikimedia.org/wikipedia/en/thumb/4/4a/Commons-logo.svg/30px-Commons-logo.svg.png)
Wikimedia Commons has media related to [Unified Modeling Language](https://commons.wikimedia.org/wiki/Unified_Modeling_Language "commons:Unified Modeling Language").



![](//upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Wikiversity_logo_2017.svg/40px-Wikiversity_logo_2017.svg.png)
Wikiversity has learning resources about ***[UML](https://en.wikiversity.org/wiki/UML "v:UML")***

* [Official website](http://uml.org) [![Edit this at Wikidata](//upload.wikimedia.org/wikipedia/en/thumb/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg/10px-OOjs_UI_icon_edit-ltr-progressive.svg.png)](https://www.wikidata.org/wiki/Q169411#P856 "Edit this at Wikidata")
* Current UML specification: [*Unified Modeling Language 2.5.1*](https://www.omg.org/spec/UML/2.5.1/PDF). [OMG](/wiki/Object_Management_Group "Object Management Group") Document Number formal/2017-12-05. [Object Management Group](/wiki/Object_Management_Group "Object Management Group") Standards Development Organization (OMG SDO). December 2017.




| * [v](/wiki/Template:Unified_Modeling_Language "Template:Unified Modeling Language") * [t](/wiki/Template_talk:Unified_Modeling_Language "Template talk:Unified Modeling Language") * [e](/wiki/Special:EditPage/Template:Unified_Modeling_Language "Special:EditPage/Template:Unified Modeling Language") Unified Modeling Language | | |
| --- | --- | --- |
| Actors | * *Organizations* 	+ [Object Management Group](/wiki/Object_Management_Group "Object Management Group") 	+ [UML Partners](/wiki/UML_Partners "UML Partners") * *Persons* 	+ [Grady Booch](/wiki/Grady_Booch "Grady Booch") 	+ [Ivar Jacobson](/wiki/Ivar_Jacobson "Ivar Jacobson") 	+ [James Rumbaugh](/wiki/James_Rumbaugh "James Rumbaugh") |  |
| Concepts | | Object oriented | * [Object-oriented programming](/wiki/Object-oriented_programming "Object-oriented programming") * [Object-oriented analysis and design](/wiki/Object-oriented_analysis_and_design "Object-oriented analysis and design") * [Object-oriented modeling](/wiki/Object-oriented_modeling "Object-oriented modeling") | | --- | --- | | Structure | * [Actor](/wiki/Actor_(UML) "Actor (UML)") * [Attribute](/wiki/Attribute_(computing) "Attribute (computing)") * [Artifact](/wiki/Artifact_(UML) "Artifact (UML)") * [Class](/wiki/Class_(computer_programming) "Class (computer programming)") * [Component](/wiki/Component_(UML) "Component (UML)") * [Interface](/wiki/Protocol_(object-oriented_programming) "Protocol (object-oriented programming)") * [Object](/wiki/Object_(computer_science) "Object (computer science)") * [Package](/wiki/Package_(UML) "Package (UML)") * [Profile diagram](/wiki/Profile_diagram "Profile diagram") | | Behavior | * [Activity](/wiki/Activity_(UML) "Activity (UML)") * [Event](/wiki/Event_(UML) "Event (UML)") * [Message](/wiki/Message_passing "Message passing") * [Method](/wiki/Method_(computer_programming) "Method (computer programming)") * [State](/wiki/State_(computer_science) "State (computer science)") * [Use case](/wiki/Use_case "Use case") | | Relationships | * [Association](/wiki/Association_(object-oriented_programming) "Association (object-oriented programming)") * [Composition](/wiki/Object_composition "Object composition") * [Dependency](/wiki/Coupling_(computer_programming) "Coupling (computer programming)") * [Generalization](/wiki/Generalization "Generalization") (or [Inheritance](/wiki/Inheritance_(object-oriented_programming) "Inheritance (object-oriented programming)")) | | Extensibility | * [Profile](/wiki/Profile_(UML) "Profile (UML)") * [Stereotype](/wiki/Stereotype_(UML) "Stereotype (UML)") | | Other | * [Multiplicity](/wiki/Class_diagram#Multiplicity "Class diagram") | |
| Diagrams | | Structure | * [Class](/wiki/Class_diagram "Class diagram") * [Component](/wiki/Component_diagram "Component diagram") * [Composite structure](/wiki/Composite_structure_diagram "Composite structure diagram") * [Deployment](/wiki/Deployment_diagram "Deployment diagram") * [Object](/wiki/Object_diagram "Object diagram") * [Package](/wiki/Package_diagram "Package diagram") | | --- | --- | | Behaviour | * [Activity](/wiki/Activity_diagram "Activity diagram") * [State Machine](/wiki/UML_state_machine "UML state machine") * [Use case](/wiki/Use_case_diagram "Use case diagram") | | Interaction | * [Communications](/wiki/Communication_diagram "Communication diagram") * [Sequence](/wiki/Sequence_diagram "Sequence diagram") * [Interaction overview](/wiki/Interaction_overview_diagram "Interaction overview diagram") * [Timing](/wiki/Timing_diagram_(Unified_Modeling_Language) "Timing diagram (Unified Modeling Language)") | |
| Derived languages | * [Systems Modeling Language (SysML)](/wiki/Systems_Modeling_Language "Systems Modeling Language") * [UML eXchange Format (UXF)](/wiki/UXF "UXF") * [XML Metadata Interchange (XMI)](/wiki/XML_Metadata_Interchange "XML Metadata Interchange") * [Executable UML (xUML)](/wiki/Executable_UML "Executable UML") |
| Other topics | * [Glossary of UML terms](/wiki/Glossary_of_Unified_Modeling_Language_terms "Glossary of Unified Modeling Language terms") * [Rational Unified Process](/wiki/Rational_Unified_Process "Rational Unified Process") * [List of Unified Modeling Language tools](/wiki/List_of_Unified_Modeling_Language_tools "List of Unified Modeling Language tools") * [Object Modeling in Color](/wiki/Object_Modeling_in_Color "Object Modeling in Color") |




| * [v](/wiki/Template:Software_engineering "Template:Software engineering") * [t](/wiki/Template_talk:Software_engineering "Template talk:Software engineering") * [e](/wiki/Special:EditPage/Template:Software_engineering "Special:EditPage/Template:Software engineering") [Software engineering](/wiki/Software_engineering "Software engineering") | |
| --- | --- |
| Fields | * [Computer programming](/wiki/Computer_programming "Computer programming") * [DevOps](/wiki/DevOps "DevOps") * [Empirical software engineering](/wiki/Empirical_software_engineering "Empirical software engineering") * [Experimental software engineering](/wiki/Experimental_software_engineering "Experimental software engineering") * [Formal methods](/wiki/Formal_methods "Formal methods") * [Requirements engineering](/wiki/Requirements_engineering "Requirements engineering") * [Search-based software engineering](/wiki/Search-based_software_engineering "Search-based software engineering") * [Site reliability engineering](/wiki/Site_reliability_engineering "Site reliability engineering") * [Social software engineering](/wiki/Social_software_engineering "Social software engineering") * [Software deployment](/wiki/Software_deployment "Software deployment") * [Software design](/wiki/Software_design "Software design") * [Software maintenance](/wiki/Software_maintenance "Software maintenance") * [Software testing](/wiki/Software_testing "Software testing") * [Systems analysis](/wiki/Systems_analysis "Systems analysis") |
| Concepts | * [Abstraction](/wiki/Abstraction_(computer_science) "Abstraction (computer science)") * [Component-based software engineering](/wiki/Component-based_software_engineering "Component-based software engineering") * [Software compatibility](/wiki/Computer_compatibility "Computer compatibility") 	+ [Backward compatibility](/wiki/Backward_compatibility "Backward compatibility") 	+ [Compatibility layer](/wiki/Compatibility_layer "Compatibility layer") 	+ [Compatibility mode](/wiki/Compatibility_mode "Compatibility mode") 	+ [Forward compatibility](/wiki/Forward_compatibility "Forward compatibility") 	+ [Software incompatibility](/wiki/Software_incompatibility "Software incompatibility") * [Data modeling](/wiki/Data_modeling "Data modeling") * [Enterprise architecture](/wiki/Enterprise_architecture "Enterprise architecture") * [Functional specification](/wiki/Functional_specification "Functional specification") * [Modeling language](/wiki/Modeling_language "Modeling language") * [Programming paradigm](/wiki/Programming_paradigm "Programming paradigm") * [Software](/wiki/Software "Software") * [Software archaeology](/wiki/Software_archaeology "Software archaeology") * [Software architecture](/wiki/Software_architecture "Software architecture") * [Software configuration management](/wiki/Software_configuration_management "Software configuration management") * [Software development process/methodology](/wiki/Software_development_process "Software development process") * [Software quality](/wiki/Software_quality "Software quality") * [Software quality assurance](/wiki/Software_quality_assurance "Software quality assurance") * [Software verification and validation](/wiki/Software_verification_and_validation "Software verification and validation") * [Software system](/wiki/Software_system "Software system") * [Structured analysis](/wiki/Structured_analysis "Structured analysis") 	+ [Essential analysis](/wiki/Essential_systems_analysis "Essential systems analysis") * [CI/CD](/wiki/CI/CD "CI/CD") |
| Orientations | * [Agile](/wiki/Agile_software_development "Agile software development") * [Aspect-oriented](/wiki/Aspect-oriented_programming "Aspect-oriented programming") * [Object orientation](/wiki/Object-oriented_programming "Object-oriented programming") * [Ontology](/wiki/Ontology_(information_science) "Ontology (information science)") * [Service orientation](/wiki/Service-oriented_architecture "Service-oriented architecture") * [SDLC](/wiki/Systems_development_life_cycle "Systems development life cycle") |
| Models | | Developmental | * [Agile](/wiki/Agile_software_development "Agile software development") * [EUP](/wiki/Enterprise_unified_process "Enterprise unified process") * [Executable UML](/wiki/Executable_UML "Executable UML") * [Incremental model](/wiki/Incremental_build_model "Incremental build model") * [Iterative model](/wiki/Iterative_and_incremental_development "Iterative and incremental development") * [Prototype model](/wiki/Software_prototyping "Software prototyping") * [RAD](/wiki/Rapid_application_development "Rapid application development") * [UP](/wiki/Unified_Process "Unified Process") * [Scrum](/wiki/Scrum_(software_development) "Scrum (software development)") * [Spiral model](/wiki/Spiral_model "Spiral model") * [V-model](/wiki/V-model_(software_development) "V-model (software development)") * [Waterfall model](/wiki/Waterfall_model "Waterfall model") * [XP](/wiki/Extreme_programming "Extreme programming") * [Model-driven engineering](/wiki/Model-driven_engineering "Model-driven engineering") * [Round-trip engineering](/wiki/Round-trip_engineering "Round-trip engineering") | | --- | --- | | Other | * [SPICE](/wiki/ISO/IEC_15504 "ISO/IEC 15504") * [CMMI](/wiki/Capability_Maturity_Model_Integration "Capability Maturity Model Integration") * [Data model](/wiki/Data_model "Data model") * [ER model](/wiki/Entity%E2%80%93relationship_model "Entity–relationship model") * [Function model](/wiki/Function_model "Function model") * [Information model](/wiki/Information_model "Information model") * [Metamodeling](/wiki/Metamodeling "Metamodeling") * [Object model](/wiki/Object_model "Object model") * [Systems model](/wiki/Systems_modeling "Systems modeling") * [View model](/wiki/View_model "View model") | | Languages | * [IDEF](/wiki/IDEF "IDEF") * UML * [USL](/wiki/Universal_Systems_Language "Universal Systems Language") * [SysML](/wiki/Systems_modeling_language "Systems modeling language") | |
| Related fields | * [Computer science](/wiki/Computer_science "Computer science") * [Computer engineering](/wiki/Computer_engineering "Computer engineering") * [Information science](/wiki/Information_science "Information science") * [Project management](/wiki/Project_management "Project management") * [Risk management](/wiki/Risk_management "Risk management") * [Systems engineering](/wiki/Systems_engineering "Systems engineering") |
| * [Commons](https://commons.wikimedia.org/wiki/Category:Software_engineering "commons:Category:Software engineering") * [Category](/wiki/Category:Software_engineering "Category:Software engineering") | |




| * [v](/wiki/Template:ISO_standards "Template:ISO standards") * [t](/wiki/Template_talk:ISO_standards "Template talk:ISO standards") * [e](/wiki/Special:EditPage/Template:ISO_standards "Special:EditPage/Template:ISO standards") [ISO](/wiki/International_Organization_for_Standardization "International Organization for Standardization") standards by standard number | |
| --- | --- |
| List of [ISO standards](/wiki/List_of_ISO_standards "List of ISO standards") – [ISO romanizations](/wiki/List_of_ISO_romanizations "List of ISO romanizations") – [IEC standards](/wiki/List_of_IEC_standards "List of IEC standards") | |
| 1–9999 | * [1](/wiki/ISO_1 "ISO 1") * [2](/wiki/ISO_2 "ISO 2") * [3](/wiki/Renard_series "Renard series") * [4](/wiki/ISO_4 "ISO 4") * [6](/wiki/Film_speed "Film speed") * [7](/wiki/British_Standard_Pipe "British Standard Pipe") * [9](/wiki/ISO_9 "ISO 9") * [16](/wiki/A440_(pitch_standard) "A440 (pitch standard)") * [17](/wiki/Renard_series "Renard series") * [31](/wiki/ISO_31 "ISO 31") 	+ [-0](/wiki/ISO_31-0 "ISO 31-0") 	+ [-1](/wiki/ISO_31-1 "ISO 31-1") 	+ [-3](/wiki/ISO_31-3 "ISO 31-3") 	+ [-4](/wiki/ISO_31-4 "ISO 31-4") 	+ [-5](/wiki/ISO_31-5 "ISO 31-5") 	+ [-6](/wiki/ISO_31-6 "ISO 31-6") 	+ [-7](/wiki/ISO_31-7 "ISO 31-7") 	+ [-8](/wiki/ISO_31-8 "ISO 31-8") 	+ [-9](/wiki/ISO_31-9 "ISO 31-9") 	+ [-10](/wiki/ISO_31-10 "ISO 31-10") 	+ [-11](/wiki/ISO_31-11 "ISO 31-11") 	+ [-12](/wiki/ISO_31-12 "ISO 31-12") 	+ [-13](/wiki/ISO_31-13 "ISO 31-13") * [68-1](/wiki/ISO_metric_screw_thread "ISO metric screw thread") * [128](/wiki/ISO_128 "ISO 128") * [216](/wiki/ISO_216 "ISO 216") * [217](/wiki/ISO_217 "ISO 217") * [226](/wiki/Equal-loudness_contour "Equal-loudness contour") * [228](/wiki/British_Standard_Pipe "British Standard Pipe") * [233](/wiki/ISO_233 "ISO 233") * [259](/wiki/ISO_259 "ISO 259") * [261](/wiki/ISO_metric_screw_thread "ISO metric screw thread") * [262](/wiki/ISO_metric_screw_thread "ISO metric screw thread") * [302](/wiki/Kappa_number "Kappa number") * [306](/wiki/Vicat_softening_point "Vicat softening point") * [361](/wiki/Hazard_symbol#Ionizing_radiation_symbol "Hazard symbol") * [500](/wiki/Power_take-off "Power take-off") * [518](/wiki/Hot_shoe "Hot shoe") * [519](/wiki/Prontor-Compur "Prontor-Compur") * [639](/wiki/ISO_639 "ISO 639") 	+ [-1](/wiki/ISO_639-1 "ISO 639-1") 	+ [-2](/wiki/ISO_639-2 "ISO 639-2") 	+ [-3](/wiki/ISO_639-3 "ISO 639-3") 	+ [-5](/wiki/ISO_639-5 "ISO 639-5") 	+ [-6](/wiki/ISO_639-6 "ISO 639-6") * [646](/wiki/ISO/IEC_646 "ISO/IEC 646") * [657](/wiki/ISO_657 "ISO 657") * [668](/wiki/ISO_668 "ISO 668") * [690](/wiki/ISO_690 "ISO 690") * [704](/wiki/ISO_704 "ISO 704") * [732](/wiki/ISO_732 "ISO 732") * [764](/wiki/Antimagnetic_watch "Antimagnetic watch") * [838](/wiki/Hole_punch "Hole punch") * [843](/wiki/ISO_843 "ISO 843") * [860](/wiki/ISO_860 "ISO 860") * [898](/wiki/ISO_898 "ISO 898") * [965](/wiki/ISO_965 "ISO 965") * [999](/wiki/ISO_999 "ISO 999") * [1000](/wiki/ISO_1000 "ISO 1000") * [1004](/wiki/Magnetic_ink_character_recognition "Magnetic ink character recognition") * [1007](/wiki/135_film "135 film") * [1073-1](/wiki/OCR-A "OCR-A") * [1073-2](/wiki/OCR-B "OCR-B") * [1155](/wiki/Longitudinal_redundancy_check "Longitudinal redundancy check") * [1413](/wiki/Shock-resistant_watch#ISO_1413_shock-resistant_standard "Shock-resistant watch") * [1538](/wiki/ALGOL_60 "ALGOL 60") * [1629](/wiki/ISO_1629 "ISO 1629") * [1745](/wiki/ISO_1745 "ISO 1745") * [1989](/wiki/COBOL "COBOL") * [2014](/wiki/ISO_2014 "ISO 2014") * [2015](/wiki/ISO_2015 "ISO 2015") * [2022](/wiki/ISO/IEC_2022 "ISO/IEC 2022") * [2033](/wiki/ISO_2033 "ISO 2033") * [2047](/wiki/ISO_2047 "ISO 2047") * [2108](/wiki/ISBN "ISBN") * [2145](/wiki/ISO_2145 "ISO 2145") * [2146](/wiki/ISO_2146 "ISO 2146") * [2240](/wiki/Film_speed "Film speed") * [2281](/wiki/Water_Resistant_mark "Water Resistant mark") * [2533](/wiki/International_Standard_Atmosphere "International Standard Atmosphere") * [2709](/wiki/ISO_2709 "ISO 2709") * [2711](/wiki/ISO_2711 "ISO 2711") * [2720](/wiki/Film_speed "Film speed") * [2788](/wiki/ISO_2788 "ISO 2788") * [2848](/wiki/ISO_2848 "ISO 2848") * [2852](/wiki/ISO_2852 "ISO 2852") * [2921](/wiki/ISO_2921 "ISO 2921") * [3029](/wiki/126_film "126 film") * [3103](/wiki/ISO_3103 "ISO 3103") * [3166](/wiki/ISO_3166 "ISO 3166") 	+ [-1](/wiki/ISO_3166-1 "ISO 3166-1") 	+ [-2](/wiki/ISO_3166-2 "ISO 3166-2") 	+ [-3](/wiki/ISO_3166-3 "ISO 3166-3") * [3297](/wiki/International_Standard_Serial_Number "International Standard Serial Number") * [3307](/wiki/ISO_3307 "ISO 3307") * [3601](/wiki/O-ring "O-ring") * [3602](/wiki/Kunrei-shiki_romanization "Kunrei-shiki romanization") * [3864](/wiki/ISO_3864 "ISO 3864") * [3901](/wiki/International_Standard_Recording_Code "International Standard Recording Code") * [3950](/wiki/FDI_World_Dental_Federation_notation "FDI World Dental Federation notation") * [3977](/wiki/ISO_3977 "ISO 3977") * [4031](/wiki/ISO_4031 "ISO 4031") * [4157](/wiki/ISO_4157 "ISO 4157") * [4165](/wiki/ISO_4165 "ISO 4165") * [4217](/wiki/ISO_4217 "ISO 4217") * [4909](/wiki/ISO/IEC_4909 "ISO/IEC 4909") * [5218](/wiki/ISO/IEC_5218 "ISO/IEC 5218") * [5426](/wiki/ISO_5426 "ISO 5426") * [5427](/wiki/ISO_5427 "ISO 5427") * [5428](/wiki/ISO_5428 "ISO 5428") * [5725](/wiki/Accuracy_and_precision "Accuracy and precision") * [5775](/wiki/ISO_5775 "ISO 5775") * [5776](/wiki/ISO_5776 "ISO 5776") * [5800](/wiki/Film_speed "Film speed") * [5807](/wiki/Flowchart "Flowchart") * [5964](/wiki/ISO_5964 "ISO 5964") * [6166](/wiki/International_Securities_Identification_Number "International Securities Identification Number") * [6344](/wiki/ISO_6344 "ISO 6344") * [6346](/wiki/ISO_6346 "ISO 6346") * [6373](/wiki/Minimal_BASIC "Minimal BASIC") * [6385](/wiki/ISO_6385 "ISO 6385") * [6425](/wiki/Water_Resistant_mark "Water Resistant mark") * [6429](/wiki/ANSI_escape_code "ANSI escape code") * [6438](/wiki/ISO_6438 "ISO 6438") * [6523](/wiki/ISO/IEC_6523 "ISO/IEC 6523") * [6709](/wiki/ISO_6709 "ISO 6709") * [6943](/wiki/ISO_6943 "ISO 6943") * [7001](/wiki/ISO_7001 "ISO 7001") * [7002](/wiki/ISO_7002 "ISO 7002") * [7010](/wiki/ISO_7010 "ISO 7010") * [7027](/wiki/ISO_7027 "ISO 7027") * [7064](/wiki/ISO/IEC_7064 "ISO/IEC 7064") * [7098](/wiki/Pinyin "Pinyin") * [7185](/wiki/Pascal_(programming_language) "Pascal (programming language)") * [7200](/wiki/ISO_7200 "ISO 7200") * [7498](/wiki/OSI_model "OSI model") 	+ [-1](/wiki/OSI_model "OSI model") * [7637](/wiki/ISO_7637 "ISO 7637") * [7736](/wiki/ISO_7736 "ISO 7736") * [7810](/wiki/ISO/IEC_7810 "ISO/IEC 7810") * [7811](/wiki/ISO/IEC_7811 "ISO/IEC 7811") * [7812](/wiki/ISO/IEC_7812 "ISO/IEC 7812") * [7813](/wiki/ISO/IEC_7813 "ISO/IEC 7813") * [7816](/wiki/ISO/IEC_7816 "ISO/IEC 7816") * [7942](/wiki/Graphical_Kernel_System "Graphical Kernel System") * [8000](/wiki/ISO_8000 "ISO 8000") * [8093](/wiki/On-board_diagnostics "On-board diagnostics") * [8178](/wiki/ISO_8178 "ISO 8178") * [8217](/wiki/Fuel_oil "Fuel oil") * [8373](/wiki/ISO_8373 "ISO 8373") * [8501-1](/wiki/ISO_8501-1 "ISO 8501-1") * [8571](/wiki/FTAM "FTAM") * [8583](/wiki/ISO_8583 "ISO 8583") * [8601](/wiki/ISO_8601 "ISO 8601") * [8613](/wiki/Open_Document_Architecture "Open Document Architecture") * [8632](/wiki/Computer_Graphics_Metafile "Computer Graphics Metafile") * [8651](/wiki/Graphical_Kernel_System "Graphical Kernel System") * [8652](/wiki/ISO/IEC_8652 "ISO/IEC 8652") * [8691](/wiki/ISO_8691 "ISO 8691") * [8805/8806](/wiki/Graphical_Kernel_System "Graphical Kernel System") * [8807](/wiki/Language_Of_Temporal_Ordering_Specification "Language Of Temporal Ordering Specification") * [8820-5](/wiki/Fuse_(automotive) "Fuse (automotive)") * [8859](/wiki/ISO/IEC_8859 "ISO/IEC 8859") 	+ [-1](/wiki/ISO/IEC_8859-1 "ISO/IEC 8859-1") 	+ [-2](/wiki/ISO/IEC_8859-2 "ISO/IEC 8859-2") 	+ [-3](/wiki/ISO/IEC_8859-3 "ISO/IEC 8859-3") 	+ [-4](/wiki/ISO/IEC_8859-4 "ISO/IEC 8859-4") 	+ [-5](/wiki/ISO/IEC_8859-5 "ISO/IEC 8859-5") 	+ [-6](/wiki/ISO/IEC_8859-6 "ISO/IEC 8859-6") 	+ [-7](/wiki/ISO/IEC_8859-7 "ISO/IEC 8859-7") 	+ [-8](/wiki/ISO/IEC_8859-8 "ISO/IEC 8859-8") 	+ [-8-I](/wiki/ISO-8859-8-I "ISO-8859-8-I") 	+ [-9](/wiki/ISO/IEC_8859-9 "ISO/IEC 8859-9") 	+ [-10](/wiki/ISO/IEC_8859-10 "ISO/IEC 8859-10") 	+ [-11](/wiki/ISO/IEC_8859-11 "ISO/IEC 8859-11") 	+ [-12](/wiki/ISO/IEC_8859-12 "ISO/IEC 8859-12") 	+ [-13](/wiki/ISO/IEC_8859-13 "ISO/IEC 8859-13") 	+ [-14](/wiki/ISO/IEC_8859-14 "ISO/IEC 8859-14") 	+ [-15](/wiki/ISO/IEC_8859-15 "ISO/IEC 8859-15") 	+ [-16](/wiki/ISO/IEC_8859-16 "ISO/IEC 8859-16") * [8879](/wiki/Standard_Generalized_Markup_Language "Standard Generalized Markup Language") * [9000/9001](/wiki/ISO_9000 "ISO 9000") * [9036](/wiki/ASMO_449 "ASMO 449") * [9075](/wiki/SQL "SQL") * [9126](/wiki/ISO/IEC_9126 "ISO/IEC 9126") * [9141](/wiki/On-board_diagnostics "On-board diagnostics") * [9227](/wiki/Salt_spray_test "Salt spray test") * [9241](/wiki/ISO_9241 "ISO 9241") * [9293](/wiki/File_Allocation_Table "File Allocation Table") * [9314](/wiki/Fiber_Distributed_Data_Interface "Fiber Distributed Data Interface") * [9362](/wiki/ISO_9362 "ISO 9362") * [9407](/wiki/Shoe_size "Shoe size") * [9496](/wiki/CHILL "CHILL") * [9506](/wiki/Manufacturing_Message_Specification "Manufacturing Message Specification") * [9529](/wiki/ISO/IEC_9529 "ISO/IEC 9529") * [9564](/wiki/ISO_9564 "ISO 9564") * [9592/9593](/wiki/PHIGS "PHIGS") * [9594](/wiki/X.500 "X.500") * [9660](/wiki/ISO_9660 "ISO 9660") * [9797-1](/wiki/ISO/IEC_9797-1 "ISO/IEC 9797-1") * [9897](/wiki/ISO_9897 "ISO 9897") * [9899](/wiki/ANSI_C "ANSI C") * [9945](/wiki/POSIX "POSIX") * [9984](/wiki/Romanization_of_Georgian "Romanization of Georgian") * [9985](/wiki/Romanization_of_Armenian "Romanization of Armenian") * [9995](/wiki/ISO/IEC_9995 "ISO/IEC 9995") |
| 10000–19999 | * [10006](/wiki/ISO_10006 "ISO 10006") * [10007](/wiki/ISO_10007 "ISO 10007") * [10116](/wiki/ISO/IEC_10116 "ISO/IEC 10116") * [10118-3](/wiki/Whirlpool_(hash_function) "Whirlpool (hash function)") * [10160](/wiki/ISO_10160 "ISO 10160") * [10161](/wiki/ISO_10161 "ISO 10161") * [10165](/wiki/Guidelines_for_the_Definition_of_Managed_Objects "Guidelines for the Definition of Managed Objects") * [10179](/wiki/Document_Style_Semantics_and_Specification_Language "Document Style Semantics and Specification Language") * [10206](/wiki/Pascal_(programming_language)#ISO/IEC_10206:1990_Extended_Pascal "Pascal (programming language)") * [10218](/wiki/ISO_10218 "ISO 10218") * [10279](/wiki/Full_BASIC "Full BASIC") * [10303](/wiki/ISO_10303 "ISO 10303") 	+ [-11](/wiki/EXPRESS_(data_modeling_language) "EXPRESS (data modeling language)") 	+ [-21](/wiki/ISO_10303-21 "ISO 10303-21") 	+ [-22](/wiki/ISO_10303-22 "ISO 10303-22") 	+ [-28](/wiki/ISO_10303-28 "ISO 10303-28") 	+ [-238](/wiki/STEP-NC "STEP-NC") * [10383](/wiki/Market_Identifier_Code "Market Identifier Code") * [10585](/wiki/ArmSCII "ArmSCII") * [10589](/wiki/IS-IS "IS-IS") * [10628](/wiki/ISO_10628 "ISO 10628") * [10646](/wiki/Universal_Coded_Character_Set "Universal Coded Character Set") * [10664](/wiki/Torx "Torx") * [10746](/wiki/RM-ODP "RM-ODP") * [10861](/wiki/Multibus "Multibus") * [10957](/wiki/International_Standard_Music_Number "International Standard Music Number") * [10962](/wiki/ISO_10962 "ISO 10962") * [10967](/wiki/ISO/IEC_10967 "ISO/IEC 10967") * [11073](/wiki/ISO/IEEE_11073 "ISO/IEEE 11073") * [11170](/wiki/ISO_11170 "ISO 11170") * [11172](/wiki/MPEG-1 "MPEG-1") * [11179](/wiki/ISO/IEC_11179 "ISO/IEC 11179") * [11404](/wiki/ISO/IEC_11404 "ISO/IEC 11404") * [11544](/wiki/JBIG "JBIG") * [11783](/wiki/ISO_11783 "ISO 11783") * [11784](/wiki/ISO_11784_and_ISO_11785 "ISO 11784 and ISO 11785") * [11785](/wiki/ISO_11784_and_ISO_11785 "ISO 11784 and ISO 11785") * [11801](/wiki/ISO/IEC_11801 "ISO/IEC 11801") * [11889](/wiki/Trusted_Platform_Module "Trusted Platform Module") * [11898](/wiki/CAN_bus#CAN_lower-layer_standards "CAN bus") * [11940](/wiki/ISO_11940 "ISO 11940") ([-2](/wiki/ISO_11940-2 "ISO 11940-2")) * [11941](/wiki/ISO/TR_11941 "ISO/TR 11941") * [11941 (TR)](/wiki/ISO/TR_11941 "ISO/TR 11941") * [11992](/wiki/ISO_11992 "ISO 11992") * [12006](/wiki/ISO_12006 "ISO 12006") * [12052](/wiki/DICOM "DICOM") * [12182](/wiki/ISO/IEC_TR_12182 "ISO/IEC TR 12182") * [12207](/wiki/ISO/IEC_12207 "ISO/IEC 12207") * [12234-2](/wiki/TIFF/EP "TIFF/EP") * [12620](/wiki/Linguistic_categories#ISO_12620_(ISO_TC37_Data_Category_Registry,_ISOcat) "Linguistic categories") * [13211](/wiki/Prolog "Prolog") 	+ [-1](/wiki/Prolog "Prolog") 	+ [-2](/wiki/Prolog "Prolog") * [13216](/wiki/Isofix "Isofix") * [13250](/wiki/Topic_map "Topic map") * [13399](/wiki/ISO_13399 "ISO 13399") * [13406-2](/wiki/ISO_13406-2 "ISO 13406-2") * [13450](/wiki/110_film "110 film") * [13485](/wiki/ISO_13485 "ISO 13485") * [13490](/wiki/ISO_13490 "ISO 13490") * [13567](/wiki/ISO_13567 "ISO 13567") * [13568](/wiki/Z_notation "Z notation") * [13584](/wiki/ISO_13584 "ISO 13584") * [13616](/wiki/International_Bank_Account_Number "International Bank Account Number") * [13816](/wiki/ISLISP "ISLISP") * [13818](/wiki/MPEG-2 "MPEG-2") * [14000](/wiki/ISO_14000 "ISO 14000") * [14031](/wiki/ISO_14031 "ISO 14031") * [14224](/wiki/ISO_14224 "ISO 14224") * [14289](/wiki/PDF/UA "PDF/UA") * [14396](/wiki/Horsepower "Horsepower") * [14443](/wiki/ISO/IEC_14443 "ISO/IEC 14443") * [14496](/wiki/MPEG-4 "MPEG-4") 	+ [-2](/wiki/MPEG-4_Part_2 "MPEG-4 Part 2") 	+ [-3](/wiki/MPEG-4_Part_3 "MPEG-4 Part 3") 	+ [-6](/wiki/Delivery_Multimedia_Integration_Framework "Delivery Multimedia Integration Framework") 	+ [-10](/wiki/Advanced_Video_Coding "Advanced Video Coding") 	+ [-11](/wiki/MPEG-4_Part_11 "MPEG-4 Part 11") 	+ [-12](/wiki/ISO_base_media_file_format "ISO base media file format") 	+ [-14](/wiki/MP4_file_format "MP4 file format") 	+ [-17](/wiki/MP4_file_format "MP4 file format") 	+ [-20](/wiki/MP4_file_format "MP4 file format") * [14617](/wiki/ISO_14617 "ISO 14617") * [14644](/wiki/ISO_14644 "ISO 14644") * [14649](/wiki/STEP-NC "STEP-NC") * [14651](/wiki/ISO/IEC_14651 "ISO/IEC 14651") * [14698](/wiki/ISO_14698 "ISO 14698") * [14764](/wiki/Software_maintenance "Software maintenance") * [14882](/wiki/C%2B%2B "C++") * [14971](/wiki/ISO_14971 "ISO 14971") * [15022](/wiki/ISO_15022 "ISO 15022") * [15189](/wiki/ISO_15189 "ISO 15189") * [15288](/wiki/ISO/IEC_15288 "ISO/IEC 15288") * [15291](/wiki/Ada_Semantic_Interface_Specification "Ada Semantic Interface Specification") * [15292](/wiki/ISO_15292 "ISO 15292") * [15398](/wiki/ISO_15398 "ISO 15398") * [15408](/wiki/Common_Criteria "Common Criteria") * [15444](/wiki/JPEG_2000 "JPEG 2000") 	+ [-3](/wiki/Motion_JPEG_2000 "Motion JPEG 2000") 	+ [-9](/wiki/JPIP "JPIP") * [15445](/wiki/HTML "HTML") * [15438](/wiki/PDF417 "PDF417") * [15504](/wiki/ISO/IEC_15504 "ISO/IEC 15504") * [15511](/wiki/International_Standard_Identifier_for_Libraries_and_Related_Organizations "International Standard Identifier for Libraries and Related Organizations") * [15686](/wiki/ISO_15686 "ISO 15686") * [15693](/wiki/ISO/IEC_15693 "ISO/IEC 15693") * [15706](/wiki/International_Standard_Audiovisual_Number "International Standard Audiovisual Number") 	+ [-2](/wiki/International_Standard_Audiovisual_Number "International Standard Audiovisual Number") * [15707](/wiki/International_Standard_Musical_Work_Code "International Standard Musical Work Code") * [15897](/wiki/ISO/IEC_15897 "ISO/IEC 15897") * [15919](/wiki/ISO_15919 "ISO 15919") * [15924](/wiki/ISO_15924 "ISO 15924") * [15926](/wiki/ISO_15926 "ISO 15926") * [15926 WIP](/wiki/ISO_15926_WIP "ISO 15926 WIP") * [15930](/wiki/PDF/X "PDF/X") * [15938](/wiki/MPEG-7 "MPEG-7") * [16023](/wiki/MaxiCode "MaxiCode") * [16262](/wiki/ECMAScript "ECMAScript") * [16355-1](/wiki/Quality_function_deployment "Quality function deployment") * [16485](/wiki/Mixed_raster_content "Mixed raster content") * [16612-2](/wiki/PDF/VT "PDF/VT") * [16750](/wiki/ISO_16750 "ISO 16750") * [16949 (TS)](/wiki/IATF_16949 "IATF 16949") * [17024](/wiki/ISO/IEC_17024 "ISO/IEC 17024") * [17025](/wiki/ISO/IEC_17025 "ISO/IEC 17025") * [17100](/wiki/ISO_17100 "ISO 17100") * [17203](/wiki/Open_Virtualization_Format "Open Virtualization Format") * [17369](/wiki/SDMX "SDMX") * [17442](/wiki/Legal_Entity_Identifier "Legal Entity Identifier") * [17506](/wiki/COLLADA "COLLADA") * [17799](/wiki/ISO/IEC_27002 "ISO/IEC 27002") * [18004](/wiki/QR_code "QR code") * [18014](/wiki/ISO/IEC_18014 "ISO/IEC 18014") * [18181](/wiki/JPEG_XL "JPEG XL") * [18245](/wiki/ISO_18245 "ISO 18245") * [18629](/wiki/Process_Specification_Language "Process Specification Language") * [18916](/wiki/Photographic_Activity_Test "Photographic Activity Test") * [19005](/wiki/PDF/A "PDF/A") * [19011](/wiki/ISO_19011 "ISO 19011") * [19092](/wiki/ISO_19092-1 "ISO 19092-1") 	+ [-1](/wiki/ISO_19092-1 "ISO 19092-1") 	+ [-2](/wiki/ISO_19092-2 "ISO 19092-2") * [19114](/wiki/ISO_19114 "ISO 19114") * [19115](/wiki/Geospatial_metadata#ISO_19115:_Geographic_information_–_Metadata "Geospatial metadata") * [19125](/wiki/Simple_Features "Simple Features") * [19136](/wiki/Geography_Markup_Language#ISO_19136 "Geography Markup Language") * [19407](/wiki/Shoe_size "Shoe size") * [19439](/wiki/ISO_19439 "ISO 19439") * [19500](/wiki/Common_Object_Request_Broker_Architecture "Common Object Request Broker Architecture") * 19501 * [19502](/wiki/Meta-Object_Facility "Meta-Object Facility") * [19503](/wiki/XML_Metadata_Interchange "XML Metadata Interchange") * 19505 * [19506](/wiki/Knowledge_Discovery_Metamodel "Knowledge Discovery Metamodel") * [19507](/wiki/Object_Constraint_Language "Object Constraint Language") * [19508](/wiki/Meta-Object_Facility "Meta-Object Facility") * [19509](/wiki/XML_Metadata_Interchange "XML Metadata Interchange") * [19510](/wiki/Business_Process_Model_and_Notation "Business Process Model and Notation") * [19600](/wiki/ISO_19600 "ISO 19600") * [19752](/wiki/ISO/IEC_19752 "ISO/IEC 19752") * [19757](/wiki/RELAX_NG "RELAX NG") * [19770](/wiki/ISO/IEC_19770 "ISO/IEC 19770") * [19775-1](/wiki/X3D "X3D") * [19794-5](/wiki/ISO/IEC_19794-5 "ISO/IEC 19794-5") * [19831](/wiki/Cloud_Infrastructure_Management_Interface "Cloud Infrastructure Management Interface") |
| 20000–29999 | * [20000](/wiki/ISO/IEC_20000 "ISO/IEC 20000") * [20022](/wiki/ISO_20022 "ISO 20022") * [20121](/wiki/ISO_20121 "ISO 20121") * [20400](/wiki/ISO_20400 "ISO 20400") * [20802](/wiki/Open_Data_Protocol "Open Data Protocol") * [20830](/wiki/Han_Xin_code "Han Xin code") * [21000](/wiki/MPEG-21 "MPEG-21") * [21001](/wiki/ISO_21001 "ISO 21001") * [21047](/wiki/International_Standard_Text_Code "International Standard Text Code") * [21122](/wiki/JPEG_XS "JPEG XS") * [21500](/wiki/ISO_21500 "ISO 21500") * [21827](/wiki/ISO/IEC_21827 "ISO/IEC 21827") * [22000](/wiki/ISO_22000 "ISO 22000") * [22275](/wiki/ECMAScript "ECMAScript") * [22300](/wiki/ISO_22300 "ISO 22300") * [22301](/wiki/ISO_22301 "ISO 22301") * [22395](/wiki/ISO_22395 "ISO 22395") * [22537](/wiki/ECMAScript_for_XML "ECMAScript for XML") * [23000](/wiki/MPEG-A "MPEG-A") * [23003](/wiki/MPEG-D "MPEG-D") * [23008](/wiki/MPEG-H "MPEG-H") * [23009](/wiki/Dynamic_Adaptive_Streaming_over_HTTP "Dynamic Adaptive Streaming over HTTP") * [23090-3](/wiki/Versatile_Video_Coding "Versatile Video Coding") * [23092](/wiki/MPEG-G "MPEG-G") * [23094-1](/wiki/Essential_Video_Coding "Essential Video Coding") * [23094-2](/wiki/LCEVC "LCEVC") * [23270](/wiki/C_Sharp_(programming_language) "C Sharp (programming language)") * [23271](/wiki/Common_Language_Infrastructure "Common Language Infrastructure") * [23360](/wiki/Linux_Standard_Base "Linux Standard Base") * [23941](/wiki/Rectangular_Micro_QR_Code "Rectangular Micro QR Code") * [24517](/wiki/PDF/E "PDF/E") * [24613](/wiki/Lexical_Markup_Framework "Lexical Markup Framework") * [24617](/wiki/ISO-TimeML "ISO-TimeML") * [24707](/wiki/Common_Logic "Common Logic") * [24728](/wiki/MicroPDF417 "MicroPDF417") * [25178](/wiki/ISO_25178 "ISO 25178") * [25964](/wiki/ISO_25964 "ISO 25964") * [26000](/wiki/ISO_26000 "ISO 26000") * [26262](/wiki/ISO_26262 "ISO 26262") * [26300](/wiki/OpenDocument "OpenDocument") * [26324](/wiki/Digital_object_identifier "Digital object identifier") * [27000 series](/wiki/ISO/IEC_27000-series "ISO/IEC 27000-series") * [27000](/wiki/ISO/IEC_27000 "ISO/IEC 27000") * [27001](/wiki/ISO/IEC_27001 "ISO/IEC 27001") * [27002](/wiki/ISO/IEC_27002 "ISO/IEC 27002") * [27005](/wiki/ISO/IEC_27005 "ISO/IEC 27005") * [27006](/wiki/ISO/IEC_27006 "ISO/IEC 27006") * [27729](/wiki/International_Standard_Name_Identifier "International Standard Name Identifier") * [28000](/wiki/ISO_28000 "ISO 28000") * 29110 * [29148](/wiki/Requirements_engineering "Requirements engineering") * [29199-2](/wiki/JPEG_XR "JPEG XR") * [29500](/wiki/Office_Open_XML "Office Open XML") |
| 30000+ | * [30170](/wiki/Ruby_(programming_language) "Ruby (programming language)") * [31000](/wiki/ISO_31000 "ISO 31000") * [32000](/wiki/PDF "PDF") * [37001](/wiki/ISO_37001 "ISO 37001") * [38500](/wiki/ISO/IEC_38500 "ISO/IEC 38500") * [39075](/wiki/Graph_Query_Language "Graph Query Language") * [40500](/wiki/Web_Content_Accessibility_Guidelines "Web Content Accessibility Guidelines") * [42010](/wiki/ISO/IEC_42010 "ISO/IEC 42010") * [45001](/wiki/ISO_45001 "ISO 45001") * [50001](/wiki/ISO_50001 "ISO 50001") * [55000](/wiki/ISO_55000 "ISO 55000") * [56000](/wiki/ISO_56000 "ISO 56000") * [80000](/wiki/ISO/IEC_80000 "ISO/IEC 80000") |
| * [Category](/wiki/Category:ISO_standards "Category:ISO standards") | |




| [Authority control databases](/wiki/Help:Authority_control "Help:Authority control") [Edit this at Wikidata](https://www.wikidata.org/wiki/Q169411#identifiers "Edit this at Wikidata") | |
| --- | --- |
| International | * [FAST](http://id.worldcat.org/fast/1160249/) |
| National | * [France](https://catalogue.bnf.fr/ark:/12148/cb131836959) * [BnF data](https://data.bnf.fr/ark:/12148/cb131836959) * [Germany](https://d-nb.info/gnd/4469781-8) * [Israel](http://olduli.nli.org.il/F/?func=find-b&local_base=NLX10&find_code=UID&request=987007563763605171) * [United States](https://id.loc.gov/authorities/sh97003561) * [Czech Republic](https://aleph.nkp.cz/F/?func=find-c&local_base=aut&ccl_term=ica=ph135581&CON_LNG=ENG) |





![](https://login.wikimedia.org/wiki/Special:CentralAutoLogin/start?type=1x1)
Retrieved from "<https://en.wikipedia.org/w/index.php?title=Unified_Modeling_Language&oldid=1229229584>"
[Categories](/wiki/Help:Category "Help:Category"): * [Unified Modeling Language](/wiki/Category:Unified_Modeling_Language "Category:Unified Modeling Language")
* [Architecture description language](/wiki/Category:Architecture_description_language "Category:Architecture description language")
* [Data modeling languages](/wiki/Category:Data_modeling_languages "Category:Data modeling languages")
* [Data modeling diagrams](/wiki/Category:Data_modeling_diagrams "Category:Data modeling diagrams")
* [Diagrams](/wiki/Category:Diagrams "Category:Diagrams")
* [Knowledge representation](/wiki/Category:Knowledge_representation "Category:Knowledge representation")
* [ISO standards](/wiki/Category:ISO_standards "Category:ISO standards")
* [Specification languages](/wiki/Category:Specification_languages "Category:Specification languages")
* [Software modeling language](/wiki/Category:Software_modeling_language "Category:Software modeling language")
* [Modeling languages](/wiki/Category:Modeling_languages "Category:Modeling languages")
Hidden categories: * [Webarchive template wayback links](/wiki/Category:Webarchive_template_wayback_links "Category:Webarchive template wayback links")
* [Articles with short description](/wiki/Category:Articles_with_short_description "Category:Articles with short description")
* [Short description matches Wikidata](/wiki/Category:Short_description_matches_Wikidata "Category:Short description matches Wikidata")
* [Use American English from March 2020](/wiki/Category:Use_American_English_from_March_2020 "Category:Use American English from March 2020")
* [All Wikipedia articles written in American English](/wiki/Category:All_Wikipedia_articles_written_in_American_English "Category:All Wikipedia articles written in American English")
* [Use dmy dates from September 2020](/wiki/Category:Use_dmy_dates_from_September_2020 "Category:Use dmy dates from September 2020")
* [Commons link from Wikidata](/wiki/Category:Commons_link_from_Wikidata "Category:Commons link from Wikidata")
* [Articles with FAST identifiers](/wiki/Category:Articles_with_FAST_identifiers "Category:Articles with FAST identifiers")
* [Articles with BNF identifiers](/wiki/Category:Articles_with_BNF_identifiers "Category:Articles with BNF identifiers")
* [Articles with BNFdata identifiers](/wiki/Category:Articles_with_BNFdata_identifiers "Category:Articles with BNFdata identifiers")
* [Articles with GND identifiers](/wiki/Category:Articles_with_GND_identifiers "Category:Articles with GND identifiers")
* [Articles with J9U identifiers](/wiki/Category:Articles_with_J9U_identifiers "Category:Articles with J9U identifiers")
* [Articles with LCCN identifiers](/wiki/Category:Articles_with_LCCN_identifiers "Category:Articles with LCCN identifiers")
* [Articles with NKC identifiers](/wiki/Category:Articles_with_NKC_identifiers "Category:Articles with NKC identifiers")

