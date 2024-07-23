


(Top)





1
Causes








2
Service or repay the technical debt








3
Consequences








4
See also








5
References








6
External links


















This article has multiple issues. Please help improve it or discuss these issues on the talk page. (Learn how and when to remove these template messages)

This article may need to be rewritten to comply with Wikipedia's quality standards. You can help. The talk page may contain suggestions. (July 2024)
This article may be in need of reorganization to comply with Wikipedia's layout guidelines. Please help by editing the article to make improvements to the overall structure. (July 2024) (Learn how and when to remove this message)

 (Learn how and when to remove this message)
This article may need to be rewritten to comply with Wikipedia's quality standards. You can help. The talk page may contain suggestions. (July 2024)
This article may be in need of reorganization to comply with Wikipedia's layout guidelines. Please help by editing the article to make improvements to the overall structure. (July 2024) (Learn how and when to remove this message)
In software development and other information technology fields, technical debt (also known as design debt[1] or code debt) is the implied cost of future reworking required when choosing an easy but limited solution instead of a better approach that could take more time.[2]

Analogous with monetary debt,[3] if technical debt is not repaid, it can accumulate "interest", making it harder to implement changes. Unaddressed technical debt increases software entropy and cost of further rework. Similarly to monetary debt, technical debt is not necessarily a bad thing, and sometimes (e.g. as a proof-of-concept) is required to move projects forward. On the other hand, some experts claim that the "technical debt" metaphor tends to minimize the ramifications, which results in insufficient prioritization of the necessary work to correct it.[4][5]

As a change is started on a codebase, there is often the need to make other coordinated changes in other parts of the codebase or documentation. Changes required that are not completed are considered debt, and until paid, will incur interest on top of interest, making it cumbersome to build a project. Although the term is primarily used in software development, it can also be applied to other professions.

In a Dagstuhl seminar held in 2016, technical debt was defined by academic and industrial experts of the topic as follows: "In software-intensive systems, technical debt is a collection of design or implementation constructs that are expedient in the short term, but set up a technical context that can make future changes more costly or impossible. Technical debt presents an actual or contingent liability whose impact is limited to internal system qualities, primarily maintainability and evolvability."[6]

This section needs additional citations for verification. Please help improve this article by adding citations to reliable sources in this section. Unsourced material may be challenged and removed. (October 2022) (Learn how and when to remove this message)
Common causes of technical debt include:

Ongoing development, long series of project enhancements over time renders old solutions sub-optimal.
Insufficient up-front definition, where requirements are still being defined during development, development starts before any design takes place. This is done to save time but often has to be reworked later.[7]
Business pressures, where the business considers getting something released sooner before the necessary changes are completed, hence builds up technical debt involving those uncompleted changes.[8]: 4 [9]: 22 
Lack of process or understanding, where businesses are blind to the concept of technical debt, and make decisions without considering the implications.
Tightly coupled components, where functions are not modular, the software is not flexible enough to adapt to changes in business needs.
Lack of a test suite, which encourages quick and risky band-aid bug fixes.
Lack of software documentation, where code is created without supporting documentation. The work to create documentation represents debt.[8]
Lack of collaboration, where knowledge isn't shared around the organization and business efficiency suffers, or junior developers are not properly mentored.
Parallel development on multiple branches accrues technical debt because of the work required to merge the changes into a single source base. The more changes done in isolation, the more debt.
Deferred refactoring; As the requirements for a project evolve, it may become clear that parts of the code have become inefficient or difficult to edit and must be refactored in order to support future requirements. The longer refactoring is delayed, and the more code is added, the bigger the debt.[9]: 29 
Lack of alignment to standards, where industry standard features, frameworks, and technologies are ignored. Eventually integration with standards will come and doing so sooner will cost less (similar to "delayed refactoring").[8]: 7 
Lack of knowledge, when the developer doesn't know how to write elegant code.[9]
Lack of ownership, when outsourced software efforts result in in-house engineering being required to refactor or rewrite outsourced code.
Poor technological leadership, where poorly thought out commands are handed down the chain of command.
Last minute specification changes. These have potential to percolate throughout a project, but there is insufficient time or budget to document and test the changes.[7]
Kenny Rubin uses the following status categories:[10]

Happened-upon technical debt—debt that the development team was unaware existed until it was exposed during the normal course of performing work on the product. For example, the team is adding a new feature to the product and in doing so it realizes that a work-around had been built into the code years before by someone who has long since departed.
Known technical debt—debt that is known to the development team and has been made visible using one of many approaches.
Targeted technical debt—debt that is known and has been targeted for servicing by the development team.
"Interest payments" are caused by both the necessary local maintenance and the absence of maintenance by other users of the project. Ongoing development in the upstream project can increase the cost of "paying off the debt" in the future.[clarification needed] One pays off the debt by simply completing the uncompleted work.[citation needed]

The buildup of technical debt is a major cause for projects to miss deadlines.[citation needed] It is difficult to estimate exactly how much work is necessary to pay off the debt. For each change that is initiated, an uncertain amount of uncompleted work is committed to the project. The deadline is missed when the project realizes that there is more uncompleted work (debt) than there is time to complete it in. To have predictable release schedules, a development team should limit the amount of work in progress in order to keep the amount of uncompleted work (or debt) small at all times.[citation needed]

If enough work is completed on a project to not present a barrier to submission, then a project will be released which still carries a substantial amount of technical debt. If this software reaches production, then the risks of implementing any future refactors which might address the technical debt increase dramatically. Modifying production code carries the risk of outages, actual financial losses and possibly legal repercussions if contracts involve service-level agreements (SLA). For this reason we can view the carrying of technical debt to production almost as if it were an increase in interest rate and the only time this decreases is when deployments are turned down and retired.

"As an evolving program is continually changed, its complexity, reflecting deteriorating structure, increases unless work is done to maintain or reduce it."[11] 
While Manny Lehman's Law already indicated that evolving programs continually add to their complexity and deteriorating structure unless work is done to maintain them, Ward Cunningham first drew the comparison between technical complexity and debt in a 1992 experience report:

"Shipping first time code is like going into debt. A little debt speeds development so long as it is paid back promptly with a rewrite... The danger occurs when the debt is not repaid. Every minute spent on not-quite-right code counts as interest on that debt. Entire engineering organizations can be brought to a stand-still under the debt load of an unconsolidated implementation, object-oriented or otherwise."[12] 
In his 2004 text, Refactoring to Patterns, Joshua Kerievsky presents a comparable argument concerning the costs associated with architectural negligence, which he describes as "design debt".[13]

Activities that might be postponed include documentation, writing tests, attending to TODO comments and tackling compiler and static code analysis warnings. Other instances of technical debt include knowledge that isn't shared around the organization and code that is too confusing to be modified easily.[citation needed]

Writing about PHP development in 2014, Junade Ali said:

The cost of never paying down this technical debt is clear; eventually the cost to deliver functionality will become so slow that it is easy for a well-designed competitive software product to overtake the badly-designed software in terms of features. In my experience, badly designed software can also lead to a more stressed engineering workforce, in turn leading higher staff churn (which in turn affects costs and productivity when delivering features). Additionally, due to the complexity in a given codebase, the ability to accurately estimate work will also disappear. In cases where development agencies charge on a feature-to-feature basis, the profit margin for delivering code will eventually deteriorate.
Grady Booch compares how evolving cities is similar to evolving software-intensive systems and how lack of refactoring can lead to technical debt.

"The concept of technical debt is central to understanding the forces that weigh upon systems, for it often explains where, how, and why a system is stressed. In cities, repairs on infrastructure are often delayed and incremental changes are made rather than bold ones. So it is again in software-intensive systems. Users suffer the consequences of capricious complexity, delayed improvements, and insufficient incremental change; the developers who evolve such systems suffer the slings and arrows of never being able to write quality code because they are always trying to catch up."[1] 
In open source software, postponing sending local changes to the upstream project is a form of technical debt.[citation needed]

Code smell (symptoms of inferior code quality that can contribute to technical debt)
Big ball of mud
Bus factor
Escalation of commitment
Manumation
Overengineering
Shotgun surgery
Software entropy
Software rot
Spaghetti code
SQALE
Sunk cost
TODO, FIXME, XXX
MetaphorsSoftware architectureSoftware engineering terminologySoftware maintenance
Articles with short descriptionShort description is different from WikidataWikipedia articles needing rewrite from July 2024All articles needing rewriteWikipedia articles needing reorganization from July 2024Articles with multiple maintenance issuesArticles needing additional references from October 2022All articles needing additional referencesWikipedia articles needing clarification from October 2013All articles with unsourced statementsArticles with unsourced statements from May 2018Articles with unsourced statements from April 2013




