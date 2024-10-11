


(Top)





1
Overview








2
History








3
Principles




Toggle Principles subsection





3.1
Behavioral specifications








3.2
Specification as a ubiquitous language










4
Specialized tooling




Toggle Specialized tooling subsection





4.1
Tooling principles








4.2
Tooling examples










5
Story versus specification








6
The three amigos








7
See also








8
References














3.1
Behavioral specifications








3.2
Specification as a ubiquitous language














4.1
Tooling principles








4.2
Tooling examples


















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
Behavior-driven development (BDD) involves naming software tests using domain language to describe the behavior of the code.

BDD involves use of a domain-specific language (DSL) using natural-language constructs (e.g., English-like sentences) that can express the behavior and the expected outcomes.

Proponents claim it encourages collaboration among developers, quality assurance experts, and customer representatives in a software project.[1][2][3] It encourages teams to use conversation and concrete examples to formalize a shared understanding of how the application should behave.[4] BDD is considered an effective practice especially when the problem space is complex.[5]

BDD is considered a refinement of test-driven development (TDD).[1][2][6][7][vague][8] [9] BDD combines the techniques of TDD with ideas from domain-driven design and object-oriented analysis and design to provide software development and management teams with shared tools and a shared process to collaborate on software development.[2][8]

At a high level, BDD is an idea about how software development should be managed by both business interests and technical insight. Its practice involves use of specialized tools.[6] Some tools specifically for BDD can be used for TDD. The tools automate the ubiquitous language.

BDD is a process by which DSL structured natural language statements are converted to executable tests. The result are tests that read like acceptance criteria for a given function. 

As such BDD is an extension of TDD.

BDD focuses on:

Where to start in the process
What to test and what not to test
How much to test in one go
What to call the tests
How to understand why a test fails
At its heart, BDD is about rethinking the approach to automated testing (including unit testing and acceptance testing) in order to avoid issues that naturally arise. For example, BDD suggests that unit test names be whole sentences starting with a conditional verb ("should" in English for example) and should be written in order of business value. Acceptance tests should be written using the standard agile framework of a user story: "Being a [role/actor/stakeholder] I want a [feature/capability] yielding a [benefit]". Acceptance criteria should be written in terms of scenarios and implemented in classes: Given [initial context], when [event occurs], then [ensure some outcomes] .

Starting from this point, many people developed BDD frameworks over a period of years, finally framing it in terms of a communication and collaboration framework for developers, QA and non-technical or business participants in a software project.[10] During the "Agile specifications, BDD and Testing eXchange" in November 2009 in London, Dan North[11] gave the following description of BDD:


BDD is a second-generation, outside-in, pull-based, multiple-stakeholder, multiple-scale, high-automation, agile methodology. It describes a cycle of interactions with well-defined outputs, resulting in the delivery of working, tested software that matters.
During an interview with Dan North at GOTO Conference in 2013, Liz Keogh[12] defined BDD as:

It's using examples to talk through how an application behaves... And having conversations about those examples.
[13]
Dan North created a BDD framework, JBehave, followed by a story-level BDD framework for Ruby called RBehave[14] which was later integrated into the RSpec project.[15] He also worked with David Chelimsky, Aslak Hellesøy and others to develop RSpec and also to write "The RSpec Book: Behaviour Driven Development with RSpec, Cucumber, and Friends". The first story-based framework in RSpec was later replaced by Cucumber mainly developed by Aslak Hellesøy. Capybara, which is a part of the Cucumber testing framework is one such web-based test automation software.

BDD suggests that software tests should be named in terms of desired behavior.[6][8][1] Borrowing from agile software development the "desired behavior" in this case consists of the requirements set by the business — that is, the desired behavior that has business value for whatever entity commissioned the software unit under construction.[6][1] Within BDD practice, this is referred to as BDD being an "outside-in" activity.[16]

TDD does not differentiate tests in terms of high-level software requirements, low-level technical details or anything in between. One way of looking at BDD therefore, is that it is an evolution of TDD which makes more specific choices.

Another BDD suggestion relates to how the desired behavior should be specified. BDD suggests using a semi-formal format for behavioral specification which is borrowed from user story specifications from the field of object-oriented analysis and design. The scenario aspect of this format may be regarded as an application of Hoare logic to behavioral specification of software using the domain-specific language.

BDD suggests that business analysts and software developers should collaborate in this area and should specify behavior in terms of user stories, which are each explicitly documented.[1][16] Each user story should, to some extent, follow the structure:[6][16]

As a: the person or role who will benefit from the feature;
I want: the feature;
so that: the benefit or value of the feature.
Given: the initial context at the beginning of the scenario, in one or more clauses;
When: the event that triggers the scenario;
Then: the expected outcome, in one or more clauses.
BDD does not require how this information is formatted, but it does suggest that a team should decide on a relatively simple, standardized format with the above elements.[6][16] In 2007, Dan North suggested a template for a textual format which is used in multiple BDD tools.[16] For example:


BDD suggested that the scenarios should be phrased declaratively rather than imperatively — in the business language, with no reference to elements of the UI through which the interactions take place.[17]

This format is referred to as the Gherkin language. The term Gherkin, however, is specific to the Cucumber, JBehave, Lettuce,[18] behave and Behat software tools.[19][20][21][22]

BDD borrows the concept of the ubiquitous language from domain driven design.[6][8] A ubiquitous language is a (semi-)formal language that is shared by all members of a software development team — both software developers and non-technical personnel.[23] The language in question is both used and developed by all team members as a common means of discussing the domain of the software in question.[23] In this way BDD becomes a vehicle for communication between all the different roles in a software project.[6][24]

A common risk with software development includes communication breakdowns between Developers and Business Stakeholders.[25] BDD uses the specification of desired behavior as a ubiquitous language for the project Team members. This is the reason that BDD insists on a semi-formal language for behavioral specification: some formality is a requirement for being a ubiquitous language.[6] In addition, having such a ubiquitous language creates a domain model of specifications, so that specifications may be reasoned about formally.[26] This model is also the basis for the different BDD-supporting software tools that are available.

The example given above establishes a user story for a software system under development. This user story identifies a stakeholder, a business effect and a business value. It also describes several scenarios, each with a precondition, trigger and expected outcome. Each of these parts is exactly identified by the more formal part of the language (the term Given might be considered a keyword, for example) and may therefore be processed in some way by a tool that understands the formal parts of the ubiquitous language.

Most BDD applications use text-based DSLs and specification approaches. However, graphical modeling of integration scenarios has also been applied successfully in practice, e.g., for testing purposes. [27]

Much like TDD, BDD may involve using specialized tooling. 

BDD requires not only test code as does TDD, but also a document that describes behavior in a more human-readable language. This requires a two-step process for executing the tests, reading and parsing the descriptions, and reading the test code and finding the corresponding test implementation to execute. This process makes BDD more laborious for developers. Proponents suggest that due to its human-readable nature the value of those documents extends to a relatively non-technical audience, and can hence serve as a communication means for describing requirements ("features").

In principle, a BDD support tool is a testing framework for software, much like the tools that support TDD. However, where TDD tools tend to be quite free-format in what is allowed for specifying tests, BDD tools are linked to the definition of the ubiquitous language.

The ubiquitous language allows business analysts to document behavioral requirements in a way that will also be understood by developers. The principle of BDD support tooling is to make these same requirements documents directly executable as a collection of tests. If this cannot be achieved because of reasons related to the technical tool that enables the execution of the specifications, then either the style of writing the behavioral requirements must be altered or the tool must be changed.[28] The exact implementation of behavioral requirements varies per tool, but agile practice has come up with the following general process:

The tooling reads a specification document.
The tooling directly understands completely formal parts of the ubiquitous language (such as the Given keyword in the example above). Based on this, the tool breaks each scenario up into meaningful clauses.
Each individual clause in a scenario is transformed into some sort of parameter for a test for the user story. This part requires project-specific work by the software developers.
The framework then executes the test for each scenario, with the parameters from that scenario.
Dan North has developed a number of frameworks that support BDD (including JBehave and RBehave), whose operation is based on the template that he suggested for recording user stories.[6] These tools use a textual description for use cases and several other tools (such as CBehave) have followed suit. However, this format is not required and so there are other tools that use other formats as well. For example, Fitnesse (which is built around decision tables), has also been used to roll out BDD.[29]

There are several different examples of BDD software tools in use in projects today, for different platforms and programming languages.

Possibly the most well-known is JBehave, which was developed by Dan North, Elizabeth Keogh and several others.[30] The following is an example taken from that project:[20]

Consider an implementation of the Game of Life. A domain expert (or business analyst) might want to specify what should happen when someone is setting up a starting configuration of the game grid. To do this, he might want to give an example of a number of steps taken by a person who is toggling cells. Skipping over the narrative part, he might do this by writing up the following scenario into a plain text document (which is the type of input document that JBehave reads):

The bold print is not part of the input; it is included here to show which words are recognized as formal language. JBehave recognizes the terms Given (as a precondition which defines the start of a scenario), When (as an event trigger) and Then (as a postcondition which must be verified as the outcome of the action that follows the trigger). Based on this, JBehave is capable of reading the text file containing the scenario and parsing it into clauses (a set-up clause and then three event triggers with verifiable conditions). JBehave then takes these clauses and passes them on to code that is capable of setting a test, responding to the event triggers and verifying the outcome. This code must be written by the developers in the project team (in Java, because that is the platform JBehave is based on). In this case, the code might look like this:

The code has a method for every type of clause in a scenario. JBehave will identify which method goes with which clause through the use of annotations and will call each method in order while running through the scenario. The text in each clause in the scenario is expected to match the template text given in the code for that clause (for example, a Given in a scenario is expected to be followed by a clause of the form "a X by Y game"). JBehave supports the matching of clauses to templates and has built-in support for picking terms out of the template and passing them to methods in the test code as parameters. The test code provides an implementation for each clause type in a scenario which interacts with the code that is being tested and performs a test based on the scenario. In this case:

The theGameIsRunning method reacts to a Given clause by setting up the initial game grid.
The iToggleTheCellAt method reacts to a When clause by firing off the toggle event described in the clause.
The theGridShouldLookLike method reacts to a Then clause by comparing the state of the game grid to the expected state from the scenario.
The primary function of this code is to be a bridge between a text file with a story and the code being tested. Note that the test code has access to the code being tested (in this case an instance of Game) and is very simple in nature. The test code has to be simple, otherwise a developer would end up having to write tests for his tests.

Finally, in order to run the tests, JBehave requires some plumbing code that identifies the text files which contain scenarios and which inject dependencies (like instances of Game) into the test code. This plumbing code is not illustrated here, since it is a technical requirement of JBehave and does not relate directly to the principle of BDD-style testing.

A separate subcategory of behavior-driven development is formed by tools that use specifications as an input language rather than user stories. An example of this style is the RSpec tool that was also originally developed by Dan North. Specification tools don't use user stories as an input format for test scenarios but rather use functional specifications for units that are being tested. These specifications often have a more technical nature than user stories and are usually less convenient for communication with business personnel than are user stories.[6][31] An example of a specification for a stack might look like this:

Such a specification may exactly specify the behavior of the component being tested, but is less meaningful to a business user. As a result, specification-based testing is seen in BDD practice as a complement to story-based testing and operates at a lower level. Specification testing is often seen as a replacement for free-format unit testing.[31]

Specification testing tools like RSpec and JDave are somewhat different in nature from tools like JBehave. Since they are seen as alternatives to basic unit testing tools like JUnit, these tools tend to favor forgoing the separation of story and testing code and prefer embedding the specification directly in the test code instead. For example, an RSpec test for a hashtable might look like this:[32]

This example shows a specification in readable language embedded in executable code. In this case a choice of the tool is to formalize the specification language into the language of the test code by adding methods named it and should. Also there is the concept of a specification precondition – the before section establishes the preconditions that the specification is based on.

The result of test will be:

The three amigos, also referred to as a "Specification Workshop", is a meeting where the product owner discusses the requirement in the form of specification by example with different stakeholders like the QA and development team. The key goal for this discussion is to trigger conversation and identify any missing specifications. The discussion also gives a platform for QA, development team and product owner to converge and hear out each other's perspective to enrich the requirement and also make sure if they are building the right product.[33]

The three amigos are:

Business - Role of the business user is to define the problem only and not venture into suggesting a solution
Development - Role of the developers involve suggesting ways to fix the problem
Testing - Role of testers is to question the solution, bring up as many as different possibilities for brain storming through what-if scenarios and help make the solution more precise to fix the problem.
Specification by example
Behat (PHP framework)
Cynefin framework
Concordion (Java framework)
Gauge (software)
Jasmine (JavaScript testing framework)
Squish GUI Tester (BDD GUI Testing Tool for JavaScript, Python, Perl, Ruby and Tcl)
Use case
Software designSoftware development philosophiesSoftware testing
CS1 Dutch-language sources (nl)Webarchive template wayback linksArticles with short descriptionShort description is different from WikidataAll Wikipedia articles needing clarificationWikipedia articles needing clarification from May 2015Articles with example Java code




