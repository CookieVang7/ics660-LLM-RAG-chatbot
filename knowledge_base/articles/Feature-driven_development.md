


(Top)





1
History








2
Overview




Toggle Overview subsection





2.1
Develop overall model








2.2
Build feature list








2.3
Plan by feature








2.4
Design by feature








2.5
Build by feature










3
Milestones








4
Best practices








5
Metamodel (Metamodelling)








6
See also








7
References








8
External links












2.1
Develop overall model








2.2
Build feature list








2.3
Plan by feature








2.4
Design by feature








2.5
Build by feature




























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
Feature-driven development (FDD) is an iterative and incremental software development process. It is a lightweight[according to whom?] or Agile method for developing software. FDD blends several industry-recognized[according to whom?] best practices into a cohesive whole. These practices are driven from a client-valued functionality (feature) perspective[clarification needed]. Its main purpose[according to whom?] is to deliver tangible, working software repeatedly in a timely manner in accordance with the Principles behind the Agile Manifesto.[1]

FDD was initially devised by Jeff De Luca to meet the specific needs of a 15-month, 50-person software development project at a large Singapore bank in 1997. This resulted in a set of five processes that covered the development of an overall model and the listing, planning, design, and building of features. The first process is heavily influenced by Peter Coad's approach to object modeling. The second process incorporates Coad's ideas of using a feature list to manage functional requirements and development tasks. The other processes are a result of Jeff De Luca's experience. There have been several implementations of FDD since its successful use on the Singapore project.

The description of FDD was first introduced to the world in Chapter 6 of the book Java modelling in Color with UML[1] by Peter Coad, Eric Lefebvre, and Jeff De Luca in 1999. Later, in Stephen Palmer and Mac Felsing's book A Practical Guide to Feature-Driven Development[2] (published in 2002), a more general description of FDD was given decoupled from Java modelling.

FDD is a model-driven short-iteration process that consists of five basic activities. For accurate state reporting and keeping track of the software development project, milestones that mark the progress made on each feature are defined. This section gives a high-level overview of the activities. In the figure on the right, the meta-process model for these activities is displayed. During the first two sequential activities, an overall model shape is established. The final three activities are iterated for each feature.

The FDD project starts with a high-level walkthrough of the scope of the system and its context. Next, detailed domain models are created for each modelling area by small groups and presented for peer review. One or more of the proposed models are selected to become the model for each domain area. Domain area models are progressively merged into an overall model.

Knowledge gathered during the initial modeling is used to identify a list of features by functionally decomposing the domain into subject areas. Subject areas each contain business activities, and the steps within each business activity form the basis for a categorized feature list. Features in this respect are small pieces of client-valued functions expressed in the form "  ", for example: 'Calculate the total of a sale' or 'Validate the password of a user'. Features should not take more than two weeks to complete, else they should be broken down into smaller pieces.

After the feature list is completed, the next step is to produce the development plan and assign ownership of features (or feature sets) as classes to programmers.

A design package is produced for each feature. A chief programmer selects a small group of features that are to be developed within two weeks. Together with the corresponding class owners, the chief programmer works out detailed sequence diagrams for each feature and refines the overall model. Next, the class and method prologues are written, and finally a design inspection is held.

After a successful design inspection for each activity to produce a feature is planned, the class owners develop code for their classes. After unit testing and successful code inspection, the completed feature is promoted to the main build.

Since features are small, completing a feature is a relatively small task. For accurate state reporting and keeping track of the software development project, it is important to mark the progress made on each feature. FDD therefore defines six milestones per feature that are to be completed sequentially. The first three milestones are completed during the Design By Feature activity, and the last three are completed during the Build By Feature activity. To track progress, a percentage complete is assigned to each milestone. In the table below the milestones and their completion percentage are shown. At the point that coding begins, a feature is already 44% complete (Domain Walkthrough 1%, Design 40% and Design Inspection 3% = 44%).


Domain Walkthrough

Design

Design Inspection

Code

Code Inspection

Promote To Build


1%

40%

3%

45%

10%

1%

Feature-driven development is built on a core set of software engineering best practices aimed at a client-valued feature perspective.

Domain Object modelling. Domain Object modeling consists of exploring and explaining the domain of the problem to be solved. The resulting domain object model provides an overall framework in which to add features.
Developing by Feature. Any function that is too complex to be implemented within two weeks is further decomposed into smaller functions until each sub-problem is small enough to be called a feature. This makes it easier to deliver correct functions and to extend or modify the system.
Individual Class (Code) Ownership. Individual class ownership means that distinct pieces or grouping of code are assigned to a single owner. The owner is responsible for the consistency, performance, and conceptual integrity of the class.
Feature Teams. A feature team is a small, dynamically formed team that develops a small activity. Multiple minds are always applied to each design decision, and multiple design options are evaluated before one is chosen.
Inspections. Inspections are carried out to ensure good quality design and code primarily by the detection of defects.
Configuration Management. Configuration management helps with identifying the source code for all features that have been completed to date and maintaining a history of changes to classes as feature teams enhance them.
Regular Builds. Regular builds ensure there is always an up-to-date system that can be demonstrated to the client and help highlight integration errors of source code for the features early.
Visibility of progress and results. Managers steer a project using frequent, appropriate, and accurate progress reporting from all levels inside and outside the project based on completed work.
Metamodelling helps visualize both the processes and the data of a method. This allows methods to be compared, and method fragments in the method engineering process can easily be reused. The usage of this technique is consistent with UML standards.

The left side of the metadata model shows the five basic activities involved in a software development project using FDD. The activities all contain sub-activities that corresponding to sub-activities in the FDD process description. The right side of the model shows the concepts involved. These concepts originate from the activities depicted in the left side of the diagram.

Agile software development
Behavior-driven development
Project lifecycle
Software architecture
Software development process
Software engineering
Agile software developmentSoftware project managementSoftware features
Articles with short descriptionShort description is different from WikidataAll articles with specifically marked weasel-worded phrasesArticles with specifically marked weasel-worded phrases from January 2021Wikipedia articles needing clarification from January 2021Articles with Curlie links




