


(Top)





1
Advantages








2
Examples as a single source of truth








3
Key practices




Toggle Key practices subsection





3.1
Example Mapping










4
Applicability








5
History








6
Automation








7
References








8
External links














3.1
Example Mapping


















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
Specification by example (SBE) is a collaborative approach to defining requirements and business-oriented functional tests for software products based on capturing and illustrating requirements using realistic examples instead of abstract statements. It is applied in the context of agile software development methods, in particular behavior-driven development. This approach is particularly successful for managing requirements and functional tests on large-scale projects of significant domain and organisational complexity.[1]

Specification by example is also known as example-driven development, executable requirements, acceptance test–driven development (ATDD[2] or A-TDD[3]), Agile Acceptance Testing,[4] Test-Driven Requirements (TDR).

Highly abstract or novel new concepts can be difficult to understand without concrete examples.[citation needed] Specification by example is intended to construct an accurate understanding, and significantly reduces feedback loops in software development, leading to less rework, higher product quality, faster turnaround time for software changes and better alignment of activities of various roles involved in software development such as testers, analysts and developers.[1]

A key aspect of specification by example is creating a single source of truth about required changes from all perspectives. When business analysts work on their own documents, software developers maintain their own documentation and testers maintain a separate set of functional tests, software delivery effectiveness is significantly reduced by the need to constantly coordinate and synchronise those different versions of truth. With short iterative cycles, such coordination is often required on weekly or biweekly basis. With Specification by example, different roles participate in creating a single source of truth that captures everyone's understanding. Examples are used to provide clarity and precision, so that the same information can be used both as a specification and a business-oriented functional test. Any additional information discovered during development or delivery, such as clarification of functional gaps, missing or incomplete requirements or additional tests, is added to this single source of truth. As there is only one source of truth about the functionality, there is no need for coordination, translation and interpretation of knowledge inside the delivery cycle.

When applied to required changes, a refined set of examples is effectively a specification and a business-oriented test for acceptance of software functionality. After the change is implemented, specification with examples becomes a document explaining existing functionality. As the validation of such documents is automated, when they are validated frequently, such documents are a reliable source of information on business functionality of underlying software. To distinguish between such documents and typical printed documentation, which quickly gets outdated,[4] a complete set of specifications with examples is called Living Documentation.[1]

Teams that apply Specification by example successfully commonly apply the following process patterns:[1]

Deriving scope from goals
Specifying collaboratively - through all-team specification workshops, smaller meetings or teleconference reviews
Illustrating requirements using examples
Refining specifications
Automating tests based on examples
Validating the underlying software frequently using the tests
Evolving a documentation system from specifications with examples to support future development
Software teams that apply specification by example within a Scrum framework typically spend 5%-10% of their time in refining the product backlog, including specifying collaboratively, illustrating requirements using examples and refining examples.[3]

Example Mapping is a simple technique that can steer the conversation and derive Acceptance criteria in a short time. The process breaks stories into Rules and Examples documented in the form of specification by example, and is a widely used technique in the BDD sphere.[5]

Specification by example applies to projects with sufficient organisational and domain complexity to cause problems in understanding or communicating requirements from a business domain perspective. It does not apply to purely technical problems or where the key complexity is not in understanding or communicating knowledge. There are documented usages of this approach in domains including investment banking, financial trading, insurance, airline ticket reservation, online gaming and price comparison.[1] A similar approach is documented also in a nuclear-power plant simulation project.[3]

Tests based on shared examples fit best in the category of tests designed to support a team while delivering software from a business perspective (see Agile Testing Quadrants[6]) - ensuring that the right product is built. They do not replace tests that look at a software system from a purely technical perspective (those that evaluate whether a product is built the right way, such as unit tests, component or technical integration tests) or tests that evaluate a product after it was developed (such as security penetration tests).

The earliest documented usage of realistic examples as a single source of truth, requirements and automated tests, on software projects is the WyCash+ project, described by Ward Cunningham in the paper A Pattern Language of Competitive Development [7][8] in 1996. The name Specification by Example was coined by Martin Fowler in 2004.[9]

Specification by Example is an evolution of the Customer Test[10] practice of Extreme Programming proposed around 1997 and Ubiquitous Language[11] idea from Domain-driven design from 2004, using the idea of black-box tests as requirements described by Weinberg and Gause[12] in 1989.

Successful application of Specification by example on large scale projects requires frequent validation of software functionality against a large set of examples (tests). In practice, this requires tests based on examples to be automated. A common approach is to automate the tests but keep examples in a form readable and accessible to non-technical and technical team members, keeping the examples as a single source of truth. This process is supported by a class of test automation tools which work with tests divided into two aspects - the specification and the automation layer. The specification of a test which is often in a plain text or HTML form and contains the examples and auxiliary descriptions. The automation layer connects the example to a software system under test. Examples of such tools are:

Behat
Concordion
Cucumber
FitNesse
Framework for Integrated Test
Robot Framework
SpecFlow for .NET
Gauge (software)
Software development philosophiesSoftware testingBusiness analysis
CS1 maint: numeric names: authors listAll articles with unsourced statementsArticles with unsourced statements from May 2021




