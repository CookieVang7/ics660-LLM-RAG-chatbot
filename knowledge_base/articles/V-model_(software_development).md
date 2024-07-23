


(Top)





1
Project definition phases




Toggle Project definition phases subsection





1.1
Requirements analysis








1.2
System design








1.3
Architecture design








1.4
Module design










2
Validation phases




Toggle Validation phases subsection





2.1
Unit testing








2.2
Integration testing








2.3
System testing








2.4
User acceptance testing










3
Criticism








4
Current state








5
See also








6
References








7
Further reading










1.1
Requirements analysis








1.2
System design








1.3
Architecture design








1.4
Module design


















2.1
Unit testing








2.2
Integration testing








2.3
System testing








2.4
User acceptance testing
























This article needs additional citations for verification. Please help improve this article by adding citations to reliable sources. Unsourced material may be challenged and removed.Find sources: "V-model" software development – news · newspapers · books · scholar · JSTOR (September 2018) (Learn how and when to remove this message)
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
In software development, the V-model[2] represents a development process that may be considered an extension of the waterfall model and is an example of the more general V-model. Instead of moving down linearly, the process steps are bent upwards after the coding phase, to form the typical V shape. The V-Model demonstrates the relationships between each phase of the development life cycle and its associated phase of testing. The horizontal and vertical axes represent time or project completeness (left-to-right) and level of abstraction (coarsest-grain abstraction uppermost), respectively.

In the requirements analysis phase, the first step in the verification process, the requirements of the system are collected by analyzing the needs of the user(s). This phase is concerned with establishing what the ideal system has to perform. However, it does not determine how the software will be designed or built. Usually, the users are interviewed and a document called the user requirements document is generated.

The user requirements document will typically describe the system's functional, interface, performance, data, security, etc. requirements as expected by the user. It is used by business analysts to communicate their understanding of the system to the users. The users carefully review this document as this document would serve as the guideline for the system designers in the system design phase. The user acceptance tests are designed in this phase. See also Functional requirements.

There are different methods for gathering requirements of both soft and hard methodologies including; interviews, questionnaires, document analysis, observation, throw-away prototypes, use case, and static and dynamic views with users.

Systems design is the phase where system engineers analyze and understand the business of the proposed system by studying the user requirements document. They figure out possibilities and techniques by which the user requirements can be implemented. If any of the requirements are not feasible, the user is informed of the issue. A resolution is found and the user requirement document is edited accordingly.

The software specification document which serves as a blueprint for the development phase is generated. This document contains the general system organization, menu structures, data structures etc. It may also hold example business scenarios, sample windows, and reports to aid understanding. Other technical documentation like entity diagrams, and data dictionaries will also be produced in this phase. The documents for system testing are prepared.

The phase of the design of computer architecture and software architecture can also be referred to as high-level design. The baseline in selecting the architecture is that it should realize all which typically consists of the list of modules, brief functionality of each module, their interface relationships, dependencies, database tables, architecture diagrams, technology details, etc. The integration testing design is carried out in the particular phase.[3]

The module design phase can also be referred to as low-level design. The designed system is broken up into smaller units or modules and each of them is explained so that the programmer can start coding directly.
The low-level design document or program specifications will contain a detailed functional logic of the module, in pseudocode:

database tables, with all elements, including their type and size
all interface details with complete API references
all dependency issues
error message listings
complete input and outputs for a module.
The unit test design is developed in this stage.

In the V-model, each stage of the verification phase has a corresponding stage in the validation phase.[4] The following are the typical phases of validation in the V-Model, though they may be known by other names.

In the V-Model, Unit Test Plans (UTPs) are developed during the module design phase. These UTPs are executed to eliminate bugs at the code level or unit level. A unit is the smallest entity that can independently exist, e.g. a program module. Unit testing verifies that the smallest entity can function correctly when isolated from the rest of the codes/units.

Integration Test Plans are developed during the Architectural Design Phase. These tests verify that units created and tested independently can coexist and communicate among themselves. Test results are shared with the customer's team.

System Tests Plans are developed during the System Design Phase. Unlike Unit and Integration Test Plans, System Test Plans are composed by the client's business team. System Test ensures that expectations from the application developed are met. The whole application is tested for its functionality, interdependency, and communication. System Testing verifies that functional and non-functional requirements have been met. Load and performance testing, stress testing, regression testing, etc., are subsets of system testing.

User Acceptance Test (UAT) Plans are developed during the Requirements Analysis phase. Test Plans are composed by business users. UAT is performed in a user environment that resembles the production environment, using realistic data. UAT verifies that the delivered system meets the user's requirement and the system is ready for use in real-time.

The V-Model has been criticized by Agile advocates and others as an inadequate model of software development for numerous reasons.[5][6][7] Criticisms include:

It is too simple to accurately reflect the software development process, and can lead managers into a false sense of security. The V-Model reflects a project management view of software development and fits the needs of project managers, accountants and lawyers rather than software developers or users.
Although it is easily understood by novices, that early understanding is useful only if the novice goes on to acquire a deeper understanding of the development process and how the V-Model must be adapted and extended in practice. If practitioners persist with their naive view of the V-Model they will have great difficulty applying it successfully.
It is inflexible and encourages a rigid and linear view of software development and has no inherent ability to respond to change.
It provides only a slight variant on the waterfall model and is therefore subject to the same criticisms as that model. It provides greater emphasis on testing, and particularly the importance of early test planning. However, a common practical criticism of the V-Model is that it leads to testing being squeezed into tight windows at the end of development when earlier stages have overrun but the implementation date remains fixed.
It is consistent with, and therefore implicitly encourages, inefficient and ineffective approaches to testing. It implicitly promotes writing test scripts in advance rather than exploratory testing; it encourages testers to look for what they expect to find, rather than discover what is truly there. It also encourages a rigid link between the equivalent levels of either leg (e.g. user acceptance test plans being derived from user requirements documents), rather than encouraging testers to select the most effective and efficient way to plan and execute testing.
It lacks coherence and precision. There is widespread confusion about what exactly the V-Model is. If one boils it down to those elements that most people would agree upon it becomes a trite and unhelpful representation of software development. Disagreement about the merits of the V-Model often reflects a lack of shared understanding of its definition.
Supporters of the V-Model argue that it has evolved and supports flexibility and agility throughout the development process.[8] They argue that in addition to being a highly disciplined approach, it promotes meticulous design, development, and documentation necessary to build stable software products. Lately, it is being adopted by the medical device industry.[9][10]

Product lifecycle management
Systems development life cycle
Software development process
Webarchive template wayback linksArticles with short descriptionShort description matches WikidataArticles needing additional references from September 2018All articles needing additional referencesCommons category link is locally definedModule:Interwiki extra: additional interwiki links




