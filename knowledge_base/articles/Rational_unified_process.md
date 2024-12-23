


(Top)





1
History








2
Rational unified process topics




Toggle Rational unified process topics subsection





2.1
RUP building blocks








2.2
Four project life-cycle phases






2.2.1
Inception phase








2.2.2
Elaboration phase








2.2.3
Construction phase








2.2.4
Transition phase










2.3
The IBM Rational Method Composer product








2.4
Certification








2.5
Six best practices










3
See also








4
References








5
Further reading








6
External links












2.1
RUP building blocks








2.2
Four project life-cycle phases






2.2.1
Inception phase








2.2.2
Elaboration phase








2.2.3
Construction phase








2.2.4
Transition phase










2.3
The IBM Rational Method Composer product








2.4
Certification








2.5
Six best practices












2.2.1
Inception phase








2.2.2
Elaboration phase








2.2.3
Construction phase








2.2.4
Transition phase




























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
The rational unified process (RUP) is an iterative software development process framework created by the Rational Software Corporation, a division of IBM since 2003.[1] RUP is not a single concrete prescriptive process, but rather an adaptable process framework, intended to be tailored by the development organizations and software project teams that will select the elements of the process that are appropriate for their needs. RUP is a specific implementation of the Unified Process.

Rational Software originally developed the rational unified process as a software process product. The product includes a hyperlinked knowledge-base with sample artifacts and detailed descriptions for many different types of activities. RUP is included in the IBM Rational Method Composer (RMC) product which allows customization of the process.

Philippe Kruchten, an experienced Rational technical representative was tasked with heading up the original RUP team.

These initial versions combined the Rational Software organisation's extensive field experience building object-oriented systems (referred to by Rational field staff as the Rational Approach) with Objectory's guidance on practices such as use cases, and incorporated extensive content from Jim Rumbaugh's Object Modeling Technology (OMT) approach to modeling, Grady Booch's Booch method, and the newly released UML 0.8.[2][3]

To help make this growing knowledge base more accessible, Philippe Kruchten was tasked with the assembly of an explicit process framework for modern software engineering. This effort employed the HTML-based process delivery mechanism developed by Objectory. The resulting "Rational Unified Process" (RUP) completed a strategic tripod for Rational:

a tailorable process that guided development
tools that automated the application of that process
services that accelerated adoption of both the process and the tools.
This guidance was augmented in subsequent versions with knowledge based on the experience of companies that Rational had acquired.

In 1997, a requirements and test discipline were added to the approach, much of the additional material sourced from the Requirements College method developed by Dean Leffingwell et al. at Requisite, Inc., and the SQA Process method developed at SQA Inc., both companies having been acquired by Rational Software.

In 1998 Rational Software added two new disciplines:

business modeling, much of this content had already been in the Objectory Process
a Configuration and Change Management discipline, sourced through the acquisition of Pure Atria Corporation.
These additions lead to an overarching set of principles that were defined by Rational and articulated within RUP as the six best practices for modern software engineering:

Develop iteratively, with risk as the primary iteration driver[4]
Manage requirements
Employ a component-based architecture
Model software visually
Continuously verify quality
Control changes
These best practices were tightly aligned with Rational's product line, and both drove the ongoing development of Rational's products, as well as being used by Rational's field teams to help customers improve the quality and predictability of their software development efforts.

Additional techniques including performance testing, UI Design, data engineering were included, and an update to reflect changes in UML 1.1.

In 1999, a project management discipline was introduced, as well as techniques to support real-time software development and updates to reflect UML 1.3. Besides, the first book to describe the process, The Unified Software Development Process (ISBN 0-201-57169-2) by Ivar Jacobson, Grady Booch and James Rumbaugh., was published in the same year.

Between 2000 and 2003, a number of changes introduced guidance from ongoing Rational field experience with iterative development, in addition to tool support for enacting RUP instances and for customization of the RUP framework. These changes included:

the introduction of concepts and techniques from approaches such as eXtreme Programming (XP), that would later come to be known collectively as agile methods. This included techniques such as pair programming, test-first design, and papers that explained how RUP enabled XP to scale for use on larger projects.
a complete overhaul of the testing discipline to better reflect how testing work was conducted in different iterative development contexts.
the introduction of supporting guidance - known as "tool mentors" - for enacting the RUP practices in various tools. These essentially provided step-by-step method support to Rational tool users.
automating the customization of RUP in a way that would allow customers to select parts from the RUP process framework, customize their selection with their own additions, and still incorporate improvements in subsequent releases from Rational.
IBM acquired Rational Software in February 2003.

In 2006, IBM created a subset of RUP tailored for the delivery of Agile projects - released as an OpenSource method called OpenUP through the Eclipse web-site.[5]

RUP is based on a set of building blocks and content elements, describing what is to be produced, the necessary skills required and the step-by-step explanation describing how specific development goals are to be achieved. The main building blocks, or content elements, are the following:

Roles (who) – A role defines a set of related skills, competencies and responsibilities.
Work products (what) – A work product represents something resulting from a task, including all the documents and models produced while working through the process.
Tasks (how) – A task describes a unit of work assigned to a Role that provides a meaningful result.
Within each iteration, the tasks are categorized into nine disciplines:

Six "engineering disciplines"
Business modelling
Requirements
Analysis and design
Implementation
Test
Deployment
Three supporting disciplines
Configuration and change management
Project management
Environment
Business modelling
Requirements
Analysis and design
Implementation
Test
Deployment
Configuration and change management
Project management
Environment
The RUP has determined a project life-cycle consisting of four phases. These phases allow the process to be presented at a high level in a similar way to how a 'waterfall'-styled project might be presented, although in essence the key to the process lies in the iterations of development that lie within all of the phases. Also, each phase has one key objective and milestone at the end that denotes the objective being accomplished. The visualization of RUP phases and disciplines over time is referred to as the RUP hump chart.

The primary objective is to scope the system adequately as a basis for validating initial costing and budgets.
In this phase the business case which includes business context, success factors (expected revenue, market recognition, etc.), and financial forecast is established. To complement the business case, a basic use case model, project plan, initial risk assessment and project description (the core project requirements, constraints and key features) are generated.
After these are completed, the project is checked against the following criteria:

Stakeholder concurrence on scope definition and cost/schedule estimates.
Requirements understanding as evidenced by the fidelity of the primary use cases.
Credibility of the cost/schedule estimates, priorities, risks, and development process.
Depth and breadth of any architectural prototype that was developed.
Establishing a baseline by which to compare actual expenditures versus planned expenditures.
If the project does not pass this milestone, called the life cycle objective milestone, it either can be cancelled or repeated after being redesigned to better meet the criteria.

The primary objective is to mitigate the key risk items identified by analysis up to the end of this phase.
The elaboration phase is where the project starts to take shape. In this phase the problem domain analysis is made and the architecture of the project gets its basic form.

The outcome of the elaboration phase is:

A use-case model in which the use-cases and the actors have been identified and most of the use-case descriptions are developed. The use-case model should be 80% complete.
A description of the software architecture in a software system development process.
An executable architecture that realizes architecturally significant use cases.
Business case and risk list which are revised.
A development plan for the overall project.
Prototypes that demonstrably mitigate each identified technical risk.
A preliminary user manual (optional)
This phase must pass the lifecycle architecture milestone criteria answering the following questions:

Is the vision of the product stable?
Is the architecture stable?
Does the executable demonstration indicate that major risk elements are addressed and resolved?
Is the construction phase plan sufficiently detailed and accurate?
Do all stakeholders agree that the current vision can be achieved using current plan in the context of the current architecture?
Is the actual vs. planned resource expenditure acceptable?
If the project cannot pass this milestone, there is still time for it to be canceled or redesigned. However, after leaving this phase, the project transitions into a high-risk operation where changes are much more difficult and detrimental when made.

The key domain analysis for the elaboration is the system architecture.

The primary objective is to build the software system.
In this phase, the main focus is on the development of components and other features of the system. This is the phase when the bulk of the coding takes place. In larger projects, several construction iterations may be developed in an effort to divide the use cases into manageable segments to produce demonstrable prototypes.

The primary objective is to 'transit' the system from development into production, making it available to and understood by the end user.
The activities of this phase include training the end users and maintainers and beta testing the system to validate it against the end users' expectations. The system also goes through an evaluation phase, any developer which is not producing the required work is replaced or removed. The product is also checked against the quality level set in the Inception phase.

If all objectives are met, the product release milestone is reached and the development cycle is finished.

The IBM Rational Method Composer product is a tool for authoring, configuring, viewing, and publishing processes. See IBM Rational Method Composer and an open source version Eclipse process framework (EPF) project for more details.

In January 2007 the new RUP certification examination for IBM Certified Solution Designer - Rational Unified Process 7.0 was released which replaces the previous version of the course called IBM Rational Certified Specialist - Rational Unified Process.[6] The new examination will not only test knowledge related to the RUP content but also to the process structure elements.[7]

To pass the new RUP certification examination, a person must take IBM's Test 839: Rational Unified Process v7.0. You are given 75 minutes to take the 52 question exam. The passing score is 62%.[8]

Six best software engineering practices are defined for software projects to minimize faults and increase productivity. These are:[9][10]

Macroscope (methodology suite)
Agile modeling (AM)
Agile unified process (AUP)
Disciplined agile delivery (DAD)
Dynamic systems development method (DSDM)
Computer programming
Feature-driven development (FDD)
Project life cycle
Quality control and quality assurance
Scaled agile framework — a descendant of RUP that incorporates agile software development methods such as extreme programming (XP)
Software architecture
Software component
Software development process
Software engineering
Software testing
Test-driven development (TDD)
Formal methodsRational Software softwareSoftware project management
All articles with dead external linksArticles with dead external links from July 2022Articles with permanently dead external linksWebarchive template wayback linksArticles with short descriptionShort description matches WikidataArticles with GND identifiers




