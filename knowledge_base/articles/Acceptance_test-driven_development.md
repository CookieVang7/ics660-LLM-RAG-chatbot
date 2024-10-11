


(Top)





1
Overview




Toggle Overview subsection





1.1
Creation








1.2
Testing strategy










2
Acceptance criteria and tests




Toggle Acceptance criteria and tests subsection





2.1
Test format








2.2
Complete test








2.3
Test examination








2.4
Another test example








2.5
Project acceptance tests










3
See also








4
References








5
External links










1.1
Creation








1.2
Testing strategy














2.1
Test format








2.2
Complete test








2.3
Test examination








2.4
Another test example








2.5
Project acceptance tests






















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
Acceptance test–driven development (ATDD) is a development methodology based on communication between the business customers, the developers, and the testers.[1] ATDD encompasses many of the same practices as specification by example (SBE),[2][3] behavior-driven development (BDD),[4] example-driven development (EDD),[5] and support-driven development also called story test–driven development (SDD).[6] All these processes aid developers and testers in understanding the customer's needs prior to implementation and allow customers to be able to converse in their own domain language.

ATDD is closely related to test-driven development (TDD).[7] It differs by the emphasis on developer-tester-business customer collaboration. ATDD encompasses acceptance testing, but highlights writing acceptance tests before developers begin coding.

Acceptance tests are from the user's point of view – the external view of the system.[1] They examine externally visible effects, such as specifying the correct output of a system given a particular input. Acceptance tests can verify how the state of something changes, such as an order that goes from "paid" to "shipped". They also can check the interactions with interfaces of other systems, such as shared databases or web services. In general, they are implementation independent, although automation of them may not be.[8][9]

Acceptance tests are created when the requirements are analyzed and prior to coding.[1] They can be developed collaboratively by requirement requester (product owner, business analyst, customer representative, etc.), developer, and tester. Developers implement the system using the acceptance tests. Failing tests provide quick feedback that the requirements are not being met. The tests are specified in business domain terms. The terms then form a ubiquitous language that is shared between the customers, developers, and testers.[10] Tests and requirements are interrelated.[11] A requirement that lacks a test may not be implemented properly. A test that does not refer to a requirement is an unneeded test. An acceptance test that is developed after implementation begins represents a new requirement.[12]

Acceptance tests are a part of an overall testing strategy. They are the customer tests that demonstrate the business intent of a system. Component tests are technical acceptance tests developed by an architect that specify the behavior of large modules. Unit tests are created by the developer to drive easy-to-maintain code.[13] They are often derived from acceptance tests and unit tests. Cross-functional testing includes usability testing,[14] exploratory testing,[15] and property testing (scaling and security).[16]

Acceptance criteria are a description of what would be checked by a test. Given a requirement such as "As a user, I want to check out a book from the library", an acceptance criterion might be, "verify the book is marked as checked out". An acceptance test for this requirement gives the details so that the test can be run with the same effect each time.

Acceptance tests usually follow this form:[1]

Given (setup)

When (trigger)

Then (verification)

Also, it is possible to add Statements that start with AND in any of the sections below (Given, When, Then).


For the example requirement, the steps could be listed as:
The previous steps do not include any specific example data, so that is added to complete the test:

Given:


Books




Title
Checked out


Great book
No


Users


Name
Sam

When:


Checkout action


User
Sam
Checks out
Great book

Then:


Books


Title
Checked out
User


Great book
Yes
Sam

Examination of the test with specific data usually leads to many questions. For the sample, these might be:

What if the book is already checked out?
What if the book does not exist?
What if the user is not registered on the system?
Is there a date that the book is due to be checked-in?
How many books can a user check out?
These questions help illuminate missing or ambiguous requirements. Additional details such as a due-date can be added to the expected result. Other acceptance tests can check that conditions such as attempting to check out a book that is already checked out produces the expected error.

Suppose the business customer wanted a business rule that a user could only check out one book at a time. The following test would demonstrate that:

Scenario:
Check that checkout business rule is enforced

Given:


Books


Title
Checked out
User


Great book
Yes
Sam


Another great book
No


Users


Name


Sam

When:


Checkout action


User
Sam
Checks out
Another great book

Then:


Error occurred


Description


Violation of checkout business rule

In addition to acceptance tests for requirements, acceptance tests can be used on a project as a whole.[1] For example, if this requirement was part of a library book checkout project, there could be acceptance tests for the whole project. These are often termed SMART objectives. An example test is "When the new library system is in production, the users will be able to check books in and out three times as fast as they do today".

Concordion
FitNesse
Robot Framework
Gauge (software)
Cucumber (software)
Software development philosophiesSoftware testingBusiness analysis




