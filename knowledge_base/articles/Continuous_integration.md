


(Top)





1
History








2
Practices








3
Related practices




Toggle Related practices subsection





3.1
Build automation








3.2
Atomic commits








3.3
Committing changes








3.4
Testing locally








3.5
Continuous delivery and continuous deployment








3.6
Version control








3.7
Automate the build








3.8
Commit frequently








3.9
Daily build








3.10
Every commit should be built








3.11
Every bug-fix commit should come with a test case








3.12
Keep the build fast








3.13
Test in a clone of the production environment








3.14
Make it easy to get the latest deliverables








3.15
Everyone can see the results of the latest build








3.16
Automate deployment










4
Benefits








5
Risks








6
See also








7
References








8
External links














3.1
Build automation








3.2
Atomic commits








3.3
Committing changes








3.4
Testing locally








3.5
Continuous delivery and continuous deployment








3.6
Version control








3.7
Automate the build








3.8
Commit frequently








3.9
Daily build








3.10
Every commit should be built








3.11
Every bug-fix commit should come with a test case








3.12
Keep the build fast








3.13
Test in a clone of the production environment








3.14
Make it easy to get the latest deliverables








3.15
Everyone can see the results of the latest build








3.16
Automate deployment
















































This article includes a list of general references, but it lacks sufficient corresponding inline citations. Please help to improve this article by introducing more precise citations. (July 2016) (Learn how and when to remove this message)


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
Continuous integration (CI) is the practice of integrating source code changes frequently and ensuring that the integrated codebase is in a workable state.

Typically, developers merge changes to an integration branch, and an automated system builds and tests the software system.[1] 
Often, the automated process runs on each commit or runs on a schedule such as once a day. 

Grady Booch first proposed the term CI in 1991,[2] although he did not advocate integrating multiple times a day, but later, CI came to include that aspect.[3]

This section needs expansion. You can help by adding to it. (August 2014)
The earliest known work on continuous integration was the Infuse environment developed by G. E. Kaiser, D. E. Perry, and W. M. Schell.[4]

In 1994, Grady Booch used the phrase continuous integration in Object-Oriented Analysis and Design with Applications (2nd edition)[5] to explain how, when developing using micro processes, "internal releases represent a sort of continuous integration of the system, and exist to force closure of the micro process".

In 1997, Kent Beck and Ron Jeffries invented extreme programming (XP) while on the Chrysler Comprehensive Compensation System project, including continuous integration.[1][self-published source] Beck published about continuous integration in 1998, emphasising the importance of face-to-face communication over technological support.[6] In 1999, Beck elaborated more in his first full book on Extreme Programming.[7] CruiseControl, one of the first open-source CI tools,[8][self-published source] was released in 2001.

In 2010, Timothy Fitz published an article detailing how IMVU's engineering team had built and been using the first practical CI system. While his post was originally met with skepticism, it quickly caught on and found widespread adoption[9] as part of the lean software development methodology, also based on IMVU.

The core activities of CI are developers co-locate code changes in a shared, integration area frequently and that the resulting integrated codebase is verified for correctness. The first part generally involves merging changes to a common version control branch. The second part generally involves automated processes including: building, testing and many other processes.

Typically, a server builds from the integration area frequently; i.e. after each commit or periodically like once a day. The server may perform quality control checks such as running unit tests[10] and collect software quality metrics via processes such as static analysis and performance testing.

This section contains instructions, advice, or how-to content. Please help rewrite the content so that it is more encyclopedic or move it to Wikiversity, Wikibooks, or Wikivoyage. (May 2015)
This section lists best practices from practitioners for other practices that enhance CI.

Build automation is a best practice.[11][12]

CI requires the version control system to support atomic commits; i.e., all of a developer's changes are handled as a single commit.

When making a code change, a developer creates a branch that is a copy of the current codebase. As other changes are committed to the repository, this copy diverges from the latest version.

The longer development continues on a branch without merging to the integration branch, the greater the risk of multiple integration conflicts[13] and failures when the developer branch is eventually merged back. When developers submit code to the repository they must first update their code to reflect the changes in the repository since they took their copy. The more changes the repository contains, the more work developers must do before submitting their own changes.

Eventually, the repository may become so different from the developers' baselines that they enter what is sometimes referred to as "merge hell", or "integration hell",[14] where the time it takes to integrate exceeds the time it took to make their original changes.[15]

Proponents of CI suggest that developers should 
use test-driven development and to
ensure that all unit tests pass locally before committing to the integration branch so that one developer's work does not break another developer's copy. 

Incomplete features can be disabled before committing, using feature toggles.

Continuous delivery ensures the software checked in on an integration branch is always in a state that can be deployed to users, and continuous deployment automates the deployment process.

Continuous delivery and continuous deployment are often performed in conjunction with CI and together form a CI/CD pipeline. 

Proponents of CI recommend storing all files and information needed for building in version control, (for git a repository); that the system should be buildable from a fresh checkout and not require additional dependencies. 

Martin Fowler recommends that all developers commit to the same integration branch.[16]

Build automation tools automate building. 

Proponents of CI recommend that a single command should have the capability of building the system. 

Automation often includes automating the integration, which often includes deployment into a production-like environment. In many cases, the build script not only compiles binaries but also generates documentation, website pages, statistics and distribution media (such as Debian DEB, Red Hat RPM or Windows MSI files).

Developers can reduce the effort of resolving conflicting changes by synchronizing changes with each other frequently; at least daily. Checking in a week's worth of work risks conflict both in likelihood of occurrence and complexity to resolve. Relatively small conflicts are significantly easier to resolve than larger ones. Integrating (committing) changes at least once a day is considered good practice, and more often better.[17]

Building daily, if not more often, is generally recommended.[citation needed]

The system should build commits to the current working version to verify that they integrate correctly. A common practice is to use Automated Continuous Integration, although this may be done manually. Automated Continuous Integration employs a continuous integration server or daemon to monitor the revision control system for changes, then automatically run the build process.

When fixing a bug, it is a good practice to push a test case that reproduces the bug. This avoids the fix to be reverted, and the bug to reappear, which is known as a regression.

The build needs to complete rapidly so that if there is a problem with integration, it is quickly identified.

Having a test environment can lead to failures in tested systems when they deploy in the production environment because the production environment may differ from the test environment in a significant way. However, building a replica of a production environment is cost-prohibitive. Instead, the test environment or a separate pre-production environment ("staging") should be built to be a scalable version of the production environment to alleviate costs while maintaining technology stack composition and nuances. Within these test environments, service virtualisation is commonly used to obtain on-demand access to dependencies (e.g., APIs, third-party applications, services, mainframes, etc.) that are beyond the team's control, still evolving, or too complex to configure in a virtual test lab.

Making builds readily available to stakeholders and testers can reduce the amount of rework necessary when rebuilding a feature that doesn't meet requirements. Additionally, early testing reduces the chances that defects survive until deployment. Finding errors earlier can reduce the amount of work necessary to resolve them.

All programmers should start the day by updating the project from the repository. That way, they will all stay up to date.

It should be easy to find out whether the build breaks and, if so, who made the relevant change and what that change was.

Most CI systems allow the running of scripts after a build finishes. In most situations, it is possible to write a script to deploy the application to a live test server that everyone can look at. A further advance in this way of thinking is continuous deployment, which calls for the software to be deployed directly into production, often with additional automation to prevent defects or regressions.[18][19]

The neutrality of this section is disputed. Relevant discussion may be found on the talk page. Please do not remove this message until conditions to do so are met. (May 2016) (Learn how and when to remove this message)
This section needs additional citations for verification. Please help improve this article by adding citations to reliable sources in this section. Unsourced material may be challenged and removed. (May 2016) (Learn how and when to remove this message)
CI benefits include:

Facilitates detecting bugs earlier
Reduces effort to find cause of bugs; if a CI test fails then changes since last good build contain causing change; if build after each change then exactly one change is the cause[1]
Avoids the chaos of integrating many changes
When a test fails or a bug is found, reverting the codebase to a good state results in fewer lost changes
Frequent availability of a known-good build for testing, demo, and release
Frequent code commit encourages modular, less complex code[20]
Quick feedback on system-wide impact of code changes
Supports collection of software metrics such as code coverage, code complexity
Risks of CI include:

Build system setup requires effort[21]
Writing and maintaining an automated test suite requires effort
Value added depends on the quality of tests[22]
High build latency (sitting in queue) limits value[22]
Implies that incomplete code should not be integrated which is counter to some developer's preferred practice[22]
Safety and mission-critical development assurance (e.g., DO-178C, ISO 26262) require documentation and review which may be difficult to achieve
Application release automation – Process of packaging and deploymentPages displaying short descriptions of redirect targets
Build light indicator – visual device used in agile software development to inform the team on the build progressPages displaying wikidata descriptions as a fallback
Comparison of continuous integration software
Continuous design – modular design process in which components can be freely substituted to improve the design, modify performance or change another feature at a later timePages displaying wikidata descriptions as a fallback
Continuous testing – process of executing automated tests as part of the software delivery pipeline to obtain immediate feedback on the business risks associated with a release candidatePages displaying wikidata descriptions as a fallback
Multi-stage continuous integration – Software development technique
Rapid application development – Concept of software development
Continuous integrationAgile software developmentExtreme programmingSoftware development process
Articles with short descriptionShort description is different from WikidataArticles lacking in-text citations from July 2016All articles lacking in-text citationsUse dmy dates from April 2022EngvarB from April 2022Articles to be expanded from August 2014All articles to be expandedArticles using small message boxesAll accuracy disputesAccuracy disputes from May 2020Articles needing cleanup from May 2015All pages needing cleanupArticles containing how-to sectionsAll articles with unsourced statementsArticles with unsourced statements from April 2012Wikipedia neutral point of view disputes from May 2016All Wikipedia neutral point of view disputesArticles needing additional references from May 2016All articles needing additional referencesPages displaying short descriptions of redirect targets via Module:Annotated linkPages displaying wikidata descriptions as a fallback via Module:Annotated linkCS1 errors: missing periodical




