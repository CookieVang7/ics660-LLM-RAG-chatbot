


(Top)





1
History








2
Model








3
Supporting arguments








4
Criticism








5
Modified waterfall models








6
Royce's final model








7
See also








8
References








9
External links


























This article needs to be updated. Please help update this article to reflect recent events or newly available information. (October 2021)
The waterfall model is a breakdown of development activities into linear sequential phases, meaning they are passed down onto each other, where each phase depends on the deliverables of the previous one and corresponds to a specialization of tasks.[1]
The approach is typical for certain areas of engineering design. In software development,[1]
it tends to be among the less iterative and flexible approaches, as progress flows in largely one direction (downwards like a waterfall) through the phases of conception, initiation, analysis, design, construction, testing, deployment and maintenance.[2]
The waterfall model is the earliest SDLC approach that was used in software development.[3]

The waterfall development model originated in the manufacturing and construction industries,[citation needed] where the highly structured physical environments meant that design changes became prohibitively expensive much sooner in the development process.[citation needed]
When first adopted for software development, there were no recognized alternatives for knowledge-based creative work.[4]

The first known presentation describing use of such phases in software engineering was held by Herbert D. Benington at the Symposium on Advanced Programming Methods for Digital Computers on 29 June 1956.[5]
This presentation was about the development of software for SAGE. In 1983 the paper was republished with a foreword by Benington explaining that the phases were on purpose organized according to the specialization of tasks, and pointing out that the process was not in fact performed in a strict top-down fashion, but depended on a prototype.[6][better source needed]

Although the term "waterfall" is not used in the paper, the first formal detailed diagram of the process later known as the "waterfall model" is often[7] cited as a 1970 article by Winston W. Royce.[8][9][10] However, he also felt it had major flaws stemming from the fact that testing only happened at the end of the process, which he described as being "risky and invites failure".[8] The rest of his paper introduced five steps which he felt were necessary to "eliminate most of the development risks" associated with the unaltered waterfall approach.[8]

Royce's five additional steps (which included writing complete documentation at various stages of development) never took mainstream hold, but his diagram of what he considered a flawed process became the starting point when describing a "waterfall" approach.[11]
[12]

The earliest use of the term "waterfall" may have been in a 1976 paper by Bell and Thayer.[13][better source needed]

In 1985, the United States Department of Defense adopted the waterfall model in the DOD-STD-2167 standard for working with software development contractors. This standard referred for iterations of a software development[14] to "the sequential phases of a software development cycle" and stated that "the contractor shall implement a software development cycle that includes the following six phases: Software Requirement Analysis, Preliminary Design, Detailed Design, Coding and Unit Testing, Integration, and Testing".[14][15]

Although Royce never recommended nor described a waterfall model,[16] rigid adherence to the following phases are criticized by him:

System and software requirements: captured in a product requirements document
Analysis: resulting in models, schema, and business rules
Design: resulting in the software architecture
Coding: the development, proving, and integration of software
Testing: the systematic discovery and debugging of defects
Operations: the installation, migration, support, and maintenance of complete systems
Thus the waterfall model maintains that one should move to a phase only when its preceding phase is reviewed and verified.

Various modified waterfall models (including Royce's final model), however, can include slight or major variations on this process.[8] These variations included returning to the previous cycle after flaws were found downstream, or returning all the way to the design phase if downstream phases deemed insufficient.

Time spent early in the software production cycle can reduce costs at later stages. For example, a problem found in the early stages (such as requirements specification) is cheaper to fix than the same bug found later on in the process (by a factor of 50 to 200).[17]

In common practice, waterfall methodologies result in a project schedule with 20–40% of the time invested for the first two phases, 30–40% of the time to coding, and the rest dedicated to testing and implementation. The actual project organization needs to be highly structured. Most medium and large projects will include a detailed set of procedures and controls, which regulate every process on the project.[18][failed verification]

A further argument for the waterfall model is that it places emphasis on documentation (such as requirements documents and design documents) as well as source code.[citation needed] In less thoroughly designed and documented methodologies, knowledge is lost if team members leave before the project is completed, and it may be difficult for a project to recover from the loss. If a fully working design document is present (as is the intent of big design up front and the waterfall model), new team members or even entirely new teams should be able to familiarise themselves by reading the documents.[19]

The waterfall model provides a structured approach; the model itself progresses linearly through discrete, easily understandable and explainable phases and thus is easy to understand; it also provides easily identifiable milestones in the development process. It is perhaps for this reason that the waterfall model is used as a beginning example of a development model in many software engineering texts and courses.[20]

Simulation can play a valuable role within the waterfall model. By creating computerized or mathematical simulations of the system being developed, teams can gain insights into how the system will perform before proceeding to the next phase. Simulations allow for testing and refining the design, identifying potential issues or bottlenecks, and making informed decisions about the system's functionality and performance.

Clients may not know exactly what their requirements are before they see working software and so change their requirements, leading to redesign, redevelopment, and retesting, and increased costs.[21]

Designers may not be aware of future difficulties when designing a new software product or feature, in which case it is better to revise the design than persist in a design that does not account for any newly discovered constraints, requirements, or problems.[22]

Organisations may attempt to deal with a lack of concrete requirements from clients by employing systems analysts to examine existing manual systems and analyse what they do and how they might be replaced. However, in practice, it is difficult to sustain a strict separation between systems analysis and programming.[23] This is because implementing any non-trivial system will almost inevitably expose issues and edge cases that the systems analyst did not consider.

In response to the perceived problems with the pure waterfall model, modified waterfall models were introduced, such as "Sashimi (Waterfall with Overlapping Phases), Waterfall with Subprojects, and Waterfall with Risk Reduction."[17]

Some organisations, such as the United States Department of Defense, now have a stated preference against waterfall-type methodologies, starting with MIL-STD-498 released in 1994, which encourages evolutionary acquisition and Iterative and Incremental Development.[24]

In response to the perceived problems with the "pure" waterfall model, many 'modified waterfall models' have been introduced. These models may address some or all of the criticisms of the "pure" waterfall model.

These include the Rapid Development models that Steve McConnell calls "modified waterfalls":[17] Peter DeGrace's "sashimi model" (waterfall with overlapping phases), waterfall with subprojects, and waterfall with risk reduction. Other software development model combinations such as "incremental waterfall model" also exist.[25]

Winston W. Royce's final model, his intended improvement upon his initial "waterfall model", illustrated that feedback could (should, and often would) lead from code testing to design (as testing of code uncovered flaws in the design) and from design back to requirements specification (as design problems may necessitate the removal of conflicting or otherwise unsatisfiable/undesignable requirements). In the same paper Royce also advocated large quantities of documentation, doing the job "twice if possible" (a sentiment similar to that of Fred Brooks, famous for writing the Mythical Man Month, an influential book in software project management, who advocated planning to "throw one away"), and involving the customer as much as possible (a sentiment similar to that of extreme programming).

Royce notes on the final model are:

Complete program design before analysis and coding begins
Documentation must be current and complete
Do the job twice if possible
Testing must be planned, controlled, and monitored
Involve the customer
List of software development philosophies
Agile software development
Big design up front
Chaos model
DevOps
Iterative and incremental development
Monitoring Maintenance Lifecycle
Object-oriented analysis and design
Rapid application development
Software development process
Spiral model
Structured Systems Analysis and Design Method (SSADM)
System development methodology
Traditional engineering
V-model
Software development philosophiesProject managementDesign
Webarchive template wayback linksArticles with short descriptionShort description is different from WikidataEngvarB from January 2023Wikipedia articles in need of updating from October 2021All Wikipedia articles in need of updatingAll articles with unsourced statementsArticles with unsourced statements from October 2021Articles with unsourced statements from February 2021All articles lacking reliable referencesArticles lacking reliable references from March 2021All articles with failed verificationArticles with failed verification from March 2021Articles with unsourced statements from March 2021Commons category link is on Wikidata




