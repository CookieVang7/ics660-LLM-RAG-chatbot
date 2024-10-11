


(Top)





1
History








2
Principle




Toggle Principle subsection





2.1
Common templates










3
Examples








4
Usage




Toggle Usage subsection





4.1
Acceptance criteria










5
Benefits








6
Limitations








7
Relationship to epics, themes and initiatives/programs




Toggle Relationship to epics, themes and initiatives/programs subsection





7.1
Theme








7.2
Initiative








7.3
Epic










8
Story map








9
User journey map








10
Comparing with use cases








11
See also








12
References








13
Further reading












2.1
Common templates














4.1
Acceptance criteria
















7.1
Theme








7.2
Initiative








7.3
Epic
























Some of this article's listed sources may not be reliable. Please help improve this article by looking for better, more reliable sources. Unreliable citations may be challenged and removed. (August 2017) (Learn how and when to remove this message)


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
In software development and product management, a user story is an informal, natural language description of features of a software system. They are written from the perspective of an end user or user of a system, and may be recorded on index cards, Post-it notes, or digitally in specific management software.[1] Depending on the product, user stories may be written by different stakeholders like client, user, manager, or development team.

User stories are a type of boundary object. They facilitate sensemaking and communication; and may help software teams document their understanding of the system and its context.[2]

1997: Kent Beck introduces user stories at the Chrysler C3 project in Detroit.
1998: Alistair Cockburn visited the C3 project and coined the phrase "A user story is a promise for a conversation."[3]
1999: Kent Beck published the first edition of the book Extreme Programming Explained, introducing Extreme Programming (XP),[4] and the usage of user stories in the planning game.
2001: Ron Jeffries proposed a "Three Cs" formula for user story creation:[5]
The Card (or often a post-it note) is a tangible physical token to hold the concepts;
The Conversation is between the stakeholders (customers, users, developers, testers, etc.). It is verbal and often supplemented by documentation;
The Confirmation ensures that the objectives of the conversation have been reached.
2001: The XP team at Connextra[6] in London devised the user story format and shared examples with others.
2004: Mike Cohn generalized the principles of user stories beyond the usage of cards in his book User Stories Applied: For Agile Software Development[7] that is now considered the standard reference for the topic according to Martin Fowler.[8] Cohn names Rachel Davies as the inventor of user stories.[citation needed] While Davies was a team member at Connextra she credits the team as a whole with the invention.[citation needed]
2014: After a first article in 2005[9] and a blog post in 2008,[10] in 2014 Jeff Patton published the user-story mapping technique, which intends to improve with a systematic approach the identification of user stories and to structure the stories to give better visibility to their interdependence.[11]
The Card (or often a post-it note) is a tangible physical token to hold the concepts;
The Conversation is between the stakeholders (customers, users, developers, testers, etc.). It is verbal and often supplemented by documentation;
The Confirmation ensures that the objectives of the conversation have been reached.
User stories are written by or for users or customers to influence the functionality of the system being developed. In some teams, the product manager (or product owner in Scrum), is primarily responsible for formulating user stories and organizing them into a product backlog. In other teams, anyone can write a user story. User stories can be developed through discussion with stakeholders, based on personas or are simply made up.

User stories may follow one of several formats or templates.

The most common is the Connextra template, stated below.[12][7][13] Mike Cohn suggested the "so that" clause is optional although still often helpful.[14]

Chris Matts suggested that "hunting the value" was the first step in successfully delivering software, and proposed this alternative:[15]

Another template based on the Five Ws specifies:[16]

A template that's commonly used to improve security is called the "Evil User Story" or "Abuse User Story" and is used as a way to think like a hacker in order to consider scenarios that might occur in a cyber-attack. These stories are written from the perspective of an attacker attempting to compromise or damage the application, rather the typical personae found in a user story:[17]

A central part of many agile development methodologies, such as in extreme programming's planning game, user stories describe what may be built in the software product. User stories are prioritized by the customer (or the product owner in Scrum) to indicate which are most important for the system and will be broken down into tasks and estimated by the developers. One way of estimating is via a Fibonacci scale.

When user stories are about to be implemented, the developers should have the possibility to talk to the customer about it. The short stories may be
difficult to interpret, may require some background knowledge or the requirements may have changed since the story was written.

User stories can be expanded to add detail based on these conversations. This can include notes, attachments and acceptance criteria.

Mike Cohn defines acceptance criteria as "notes about what the story must do in order for the product owner to accept it as complete."[20] They define the boundaries of a user story and are used to confirm when a story is completed and working as intended.

The appropriate amount of information to be included in the acceptance criteria varies by team, program and project. Some may include 'predecessor criteria', "The user has already logged in and has already edited his information once".[This quote needs a citation] Some may write the acceptance criteria in typical agile format, Given-When-Then. Others may simply use bullet points taken from original requirements gathered from customers or stakeholders.[20]
In order for a story to be considered done or complete, all acceptance criteria must be met.

There is no good evidence that using user stories increases software success or developer productivity. However, user stories facilitate sensemaking without undue problem structuring, which is linked to success.[21]

Limitations of user stories include:

Scale-up problem: User stories written on small physical cards are hard to maintain, difficult to scale to large projects and troublesome for geographically distributed teams.
Vague, informal and incomplete: User story cards are regarded as conversation starters. Being informal, they are open to many interpretations. Being brief, they do not state all of the details necessary to implement a feature. Stories are therefore inappropriate for reaching formal agreements or writing legal contracts.[22]
Lack of non-functional requirements: User stories rarely include performance or non-functional requirement details, so non-functional tests (e.g. response time) may be overlooked.
Don't necessarily represent how technology has to be built: Since user stories are often written from the business perspective, once a technical team begins to implement, it may find that technical constraints require effort which may be broader than the scope of an individual story. Sometimes splitting stories into smaller ones can help resolve this. Other times, 'technical-only' stories are most appropriate. These 'technical-only' stories may be challenged by the business stakeholders as not delivering value that can be demonstrated to customers/stakeholders.
In many contexts, user stories are used and also summarized in groups for ontological, semantic and organizational reasons. Initiative is also referred to as Program in certain scaled agile frameworks. The different usages depend on the point-of-view, e.g. either looking from a user perspective as product owner in relation to features or a company perspective in relation to task organization.

While some suggest to use 'epic' and 'theme' as labels for any thinkable kind of grouping of user stories, organization management tends to use it for strong structuring and uniting work loads. For instance, Jira seems to use a hierarchically organized to-do-list, in which they named the first level of to-do-tasks 'user-story', the second level 'epics' (grouping of user stories) and the third level 'initiatives' (grouping of epics). However, initiatives are not always present in product management development and just add another level of granularity. In Jira, 'themes' exist (for tracking purposes) that allow to cross-relate and group items of different parts of the fixed hierarchy.[23][24]

In this usage, Jira shifts the meaning of themes in an organization perspective: e.g how much time did we spent on developing theme "xyz". But another definition of themes is: a set of stories, epics, features etc for a user that forms a common semantic unit or goal. There is probably not a common definition because different approaches exist for different styles of product design and development. In this sense, some also suggest to not use any kind of hard groups and hierarchies.[25][26][27][28][29][30]

Multiple epics or many very large stories that are closely related are summarized as themes. A common explanation of epics is also: so much work that requires many sprints, or in scaled frameworks -- a Release Train or Solution Train.

Multiple themes, epics, or stories grouped together hierarchically.[31]

Multiple themes or stories grouped together by ontology and/or semantic relationship.

A story map[32] organises user stories according to a narrative flow that presents the big picture of the product. The technique was developed by Jeff Patton from 2005 to 2014 to address the risk of projects flooded with very detailed user stories that distract from realizing the product's main objectives.[citation needed]

User story mapping[33] uses workshops with users to identify first the main business activities. Each of these main activities may involve several kind of users or personas.

The horizontal cross-cutting narrative line is then drawn by identifying the main tasks of the individual user involved in these business activities. The line is kept throughout the project. More detailed user stories are gathered and collected as usual with the user story practice. But each new user story is either inserted into the narrative flow or related vertically to a main tasks.

The horizontal axis corresponds to the coverage of the product objectives, and the vertical axis to the needs of the individual users.

In this way it becomes possible to describe even large systems without losing the big picture.

Story maps can easily provide a two-dimensional graphical visualization of the product backlog: At the top of the map are the headings under which stories are grouped, usually referred to as 'epics' (big coarse-grained user stories), 'themes' (collections of related user stories[34]) or 'activities'. These are identified by orienting at the user’s workflow or "the order you'd explain the behavior of the system". Vertically, below the epics, the actual story cards are allocated and ordered by priority. The first horizontal row is a "walking skeleton"[35] and below that represents increasing sophistication.[36][clarification needed]

A user journey map[37] intends to show the big picture but for a single user category. Its narrative line focuses on the chronology of phases and actions that a single user has to perform in order to achieve his or her objectives.

This allows to map the user experience beyond a set of user stories. Based on user feedback, the positive and negative emotions can be identified across the journey. Points of friction or unfulfilled needs can be identified on the map. This technique is used to improve the design of a product,[38] allowing to engage users in participatory approaches.[39]

A use case has been described as "a generalized description of a set of interactions between the system and one or more actors, where an actor is either a user or another system."[40] While user stories and use cases have some similarities, there are several differences between them.




User Stories

Use Cases


Similarities


Generally formulated in users' everyday language. They should help the reader understand what the software should accomplish.


Written in users' everyday business language, to facilitate stakeholder communications.


Differences


Provide a small-scale and easy-to-use presentation of information, with little detail, thus remaining open to interpretation, through conversations with on-site customers.


Use cases organize requirements to form a narrative of how users relate to and use a system. Hence they focus on user goals and how interacting with a system satisfies the goals.[41]
Use case flows describe sequences of interactions, and may be worded in terms of a formal model. A use case is intended to provide sufficient detail for it to be understood on its own.


Template

As a , I can  so that .[19]


Title: "goal the use case is trying to satisfy"
Main Success Scenario: numbered list of steps
Step: "a simple statement of the interaction between the actor and a system"
Extensions: separately numbered lists, one per Extension
Extension: "a condition that results in different interactions from .. the main success scenario". An extension from main step 3 is numbered 3a, etc.

Generally formulated in users' everyday language. They should help the reader understand what the software should accomplish.
Written in users' everyday business language, to facilitate stakeholder communications.
Provide a small-scale and easy-to-use presentation of information, with little detail, thus remaining open to interpretation, through conversations with on-site customers.
Use cases organize requirements to form a narrative of how users relate to and use a system. Hence they focus on user goals and how interacting with a system satisfies the goals.[41]
Use case flows describe sequences of interactions, and may be worded in terms of a formal model. A use case is intended to provide sufficient detail for it to be understood on its own.
Title: "goal the use case is trying to satisfy"
Main Success Scenario: numbered list of steps
Step: "a simple statement of the interaction between the actor and a system"
Extensions: separately numbered lists, one per Extension
Extension: "a condition that results in different interactions from .. the main success scenario". An extension from main step 3 is numbered 3a, etc.
Step: "a simple statement of the interaction between the actor and a system"
Extension: "a condition that results in different interactions from .. the main success scenario". An extension from main step 3 is numbered 3a, etc.
Kent Beck, Alistair Cockburn, Martin Fowler and others discussed this topic further on the c2.com wiki (the home of extreme programming).[42]

Kanban board
Persona (user experience)
Scenario (computing)
Use case
Software requirementsExtreme programmingAgile software development
CS1 maint: location missing publisherCS1 errors: generic nameCS1 errors: missing periodicalArticles with short descriptionShort description is different from WikidataArticles lacking reliable references from August 2017All articles lacking reliable referencesUse dmy dates from May 2021All articles with unsourced statementsArticles with unsourced statements from April 2020Articles with unsourced quotesArticles with unsourced statements from August 2020Wikipedia articles needing clarification from April 2014




