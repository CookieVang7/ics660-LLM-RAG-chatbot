



From Wikipedia, the free encyclopedia


Software development concept
In [software development](/wiki/Software_development "Software development") and other [information technology](/wiki/Information_technology "Information technology") fields, **technical debt** (also known as **design debt**[[1]](#cite_note-Girish_2014-1) or **code debt**) is the implied cost of future reworking required when choosing an easy but limited solution instead of a better approach that could take more time.[[2]](#cite_note-2)


Analogous with monetary [debt](/wiki/Debt "Debt"),[[3]](#cite_note-Managing_Technical_Debt-3) if technical debt is not repaid, it can accumulate "interest", making it harder to implement changes. Unaddressed technical debt increases [software entropy](/wiki/Software_entropy "Software entropy") and cost of further rework. Similarly to monetary debt, technical debt is not necessarily a bad thing, and sometimes (e.g. as a [proof-of-concept](/wiki/Proof_of_concept "Proof of concept")) is required to move projects forward. On the other hand, some experts claim that the "technical debt" metaphor tends to minimize the ramifications, which results in insufficient prioritization of the necessary work to correct it.[[4]](#cite_note-Jeffries_2015-4)[[5]](#cite_note-Knesek_2016-5)


As a change is started on a codebase, there is often the need to make other coordinated changes in other parts of the codebase or documentation. Changes required that are not completed are considered debt, and until paid, will incur interest on top of interest, making it cumbersome to build a project. Although the term is primarily used in software development, it can also be applied to other professions.


In a [Dagstuhl seminar](/wiki/Dagstuhl#Seminar_series "Dagstuhl") held in 2016, technical debt was defined by academic and industrial experts of the topic as follows: "In software-intensive systems, technical debt is a collection of design or implementation constructs that are expedient in the short term, but set up a technical context that can make future changes more costly or impossible. Technical debt presents an actual or contingent liability whose impact is limited to internal system qualities, primarily maintainability and evolvability."[[6]](#cite_note-6)




Causes[[edit](/w/index.php?title=Technical_debt&action=edit&section=1 "Edit section: Causes")]
----------------------------------------------------------------------------------------------




|  | This section **needs additional citations for [verification](/wiki/Wikipedia:Verifiability "Wikipedia:Verifiability")**. Please help [improve this article](/wiki/Special:EditPage/Technical_debt "Special:EditPage/Technical debt") by [adding citations to reliable sources](/wiki/Help:Referencing_for_beginners "Help:Referencing for beginners") in this section. Unsourced material may be challenged and removed. *(October 2022)* *([Learn how and when to remove this message](/wiki/Help:Maintenance_template_removal "Help:Maintenance template removal"))* |
| --- | --- |


Common causes of technical debt include:



* Ongoing development, long series of project enhancements over time renders old solutions sub-optimal.
* Insufficient up-front definition, where [requirements](/wiki/Requirements_analysis "Requirements analysis") are still being defined during development, development starts before any design takes place. This is done to save time but often has to be reworked later.[[7]](#cite_note-:0-7)
* Business pressures, where the business considers getting something released sooner before the necessary changes are completed, hence builds up technical debt involving those uncompleted changes.[[8]](#cite_note-SuryanarayanaSamarthyam2014-8): 4[[9]](#cite_note-Sterling2010-9): 22
* Lack of process or understanding, where businesses are blind to the concept of technical debt, and make decisions without considering the implications.
* [Tightly coupled components](/wiki/Coupling_(computer_programming) "Coupling (computer programming)"), where functions are not [modular](/wiki/Modular_programming "Modular programming"), the software is not flexible enough to adapt to changes in business needs.
* Lack of a [test suite](/wiki/Test_suite "Test suite"), which encourages quick and risky [band-aid](/wiki/Band-aid_(Computing) "Band-aid (Computing)") bug fixes.
* Lack of [software documentation](/wiki/Software_documentation "Software documentation"), where code is created without supporting documentation. The work to create documentation represents debt.[[8]](#cite_note-SuryanarayanaSamarthyam2014-8)
* Lack of collaboration, where knowledge isn't shared around the organization and business efficiency suffers, or junior developers are not properly mentored.
* Parallel development on multiple branches accrues technical debt because of the work required to merge the changes into a single source base. The more changes done in isolation, the more debt.
* Deferred [refactoring](/wiki/Code_refactoring "Code refactoring"); As the requirements for a project evolve, it may become clear that parts of the code have become inefficient or difficult to edit and must be refactored in order to support future requirements. The longer refactoring is delayed, and the more code is added, the bigger the debt.[[9]](#cite_note-Sterling2010-9): 29
* Lack of alignment to standards, where industry standard features, [frameworks](/wiki/Software_framework "Software framework"), and technologies are ignored. Eventually integration with standards will come and doing so sooner will cost less (similar to "delayed refactoring").[[8]](#cite_note-SuryanarayanaSamarthyam2014-8): 7
* Lack of knowledge, when the developer doesn't know how to write elegant code.[[9]](#cite_note-Sterling2010-9)
* Lack of ownership, when outsourced software efforts result in in-house engineering being required to [refactor](/wiki/Code_refactoring "Code refactoring") or [rewrite](/wiki/Code_rewriting "Code rewriting") outsourced code.
* Poor technological leadership, where poorly thought out commands are handed down the chain of command.
* Last minute specification changes. These have potential to percolate throughout a project, but there is insufficient time or budget to document and test the changes.[[7]](#cite_note-:0-7)


Service or repay the technical debt[[edit](/w/index.php?title=Technical_debt&action=edit&section=2 "Edit section: Service or repay the technical debt")]
--------------------------------------------------------------------------------------------------------------------------------------------------------


Kenny Rubin uses the following status categories:[[10]](#cite_note-Essential_Scrum:_Velocity-10)



* Happened-upon technical debt—debt that the development team was unaware existed until it was exposed during the normal course of performing work on the product. For example, the team is adding a new feature to the product and in doing so it realizes that a work-around had been built into the code years before by someone who has long since departed.
* Known technical debt—debt that is known to the development team and has been made visible using one of many approaches.
* Targeted technical debt—debt that is known and has been targeted for servicing by the development team.


Consequences[[edit](/w/index.php?title=Technical_debt&action=edit&section=3 "Edit section: Consequences")]
----------------------------------------------------------------------------------------------------------


"Interest payments" are caused by both the necessary local maintenance and the absence of maintenance by other users of the project. Ongoing development in the [upstream](/wiki/Upstream_(software_development) "Upstream (software development)") project can increase the cost of "paying off the debt" in the future.[*[clarification needed](/wiki/Wikipedia:Please_clarify "Wikipedia:Please clarify")*] One pays off the debt by simply completing the uncompleted work.[*[citation needed](/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")*]


The buildup of technical debt is a major cause for projects to miss deadlines.[*[citation needed](/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")*] It is difficult to [estimate](/wiki/Estimation_(project_management) "Estimation (project management)") exactly how much work is necessary to pay off the debt. For each change that is initiated, an uncertain amount of uncompleted work is committed to the project. The deadline is missed when the project realizes that there is more uncompleted work (debt) than there is time to complete it in. To have predictable release schedules, a development team should limit the amount of work in progress in order to keep the amount of uncompleted work (or debt) small at all times.[*[citation needed](/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")*]


If enough work is completed on a project to not present a barrier to submission, then a project will be released which still carries a substantial amount of technical debt. If this software reaches production, then the risks of implementing any future refactors which might address the technical debt increase dramatically. Modifying production code carries the risk of outages, actual financial losses and possibly legal repercussions if contracts involve [service-level agreements](/wiki/Service-level_agreements "Service-level agreements") (SLA). For this reason we can view the carrying of technical debt to production almost as if it were an *increase in interest rate* and the only time this decreases is when deployments are turned down and retired.




> "As an evolving program is continually changed, its complexity, reflecting deteriorating structure, increases unless work is done to maintain or reduce it."[[11]](#cite_note-11) 
> 
> — [Meir Manny Lehman](/wiki/Meir_Manny_Lehman "Meir Manny Lehman"), 1980


While [Manny Lehman](/wiki/Meir_Manny_Lehman "Meir Manny Lehman")'s Law already indicated that evolving programs continually add to their complexity and deteriorating structure unless work is done to maintain them, [Ward Cunningham](/wiki/Ward_Cunningham "Ward Cunningham") first drew the comparison between technical complexity and [debt](/wiki/Debt "Debt") in a 1992 experience report:




> "Shipping first time code is like going into debt. A little debt speeds development so long as it is paid back promptly with a rewrite... The danger occurs when the debt is not repaid. Every minute spent on not-quite-right code counts as [interest](/wiki/Interest "Interest") on that debt. Entire engineering organizations can be brought to a stand-still under the debt load of an unconsolidated implementation, [object-oriented](/wiki/Object-oriented_programming "Object-oriented programming") or otherwise."[[12]](#cite_note-oopsla92-12) 
> 
> — [Ward Cunningham](/wiki/Ward_Cunningham "Ward Cunningham"), 1992


In his 2004 text, *Refactoring to Patterns*, [Joshua Kerievsky](/w/index.php?title=Joshua_Kerievsky&action=edit&redlink=1 "Joshua Kerievsky (page does not exist)") presents a comparable argument concerning the costs associated with architectural negligence, which he describes as "design debt".[[13]](#cite_note-rtp-13)


Activities that might be postponed include [documentation](/wiki/Documentation "Documentation"), writing [tests](/wiki/Test_automation "Test automation"), attending to [TODO comments](/wiki/Comment_(computer_programming)#Tags "Comment (computer programming)") and tackling compiler and [static code analysis](/wiki/Static_code_analysis "Static code analysis") warnings. Other instances of technical debt include knowledge that isn't shared around the organization and code that is too confusing to be modified easily.[*[citation needed](/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")*]


Writing about PHP development in 2014, [Junade Ali](/wiki/Junade_Ali "Junade Ali") said:




> The cost of never paying down this technical debt is clear; eventually the cost to deliver functionality will become so slow that it is easy for a well-designed competitive software product to overtake the badly-designed software in terms of features. In my experience, badly designed software can also lead to a more stressed engineering workforce, in turn leading higher staff churn (which in turn affects costs and productivity when delivering features). Additionally, due to the complexity in a given codebase, the ability to accurately estimate work will also disappear. In cases where development agencies charge on a feature-to-feature basis, the profit margin for delivering code will eventually deteriorate.
> 
> — [Junade Ali](/wiki/Junade_Ali "Junade Ali") writes in *Mastering PHP Design Patterns*[[14]](#cite_note-14)


[Grady Booch](/wiki/Grady_Booch "Grady Booch") compares how evolving cities is similar to evolving software-intensive systems and how lack of refactoring can lead to technical debt.




> "The concept of technical debt is central to understanding the forces that weigh upon systems, for it often explains where, how, and why a system is stressed. In cities, repairs on infrastructure are often delayed and incremental changes are made rather than bold ones. So it is again in software-intensive systems. Users suffer the consequences of capricious complexity, delayed improvements, and insufficient incremental change; the developers who evolve such systems suffer the slings and arrows of never being able to write quality code because they are always trying to catch up."[[1]](#cite_note-Girish_2014-1) 
> 
> — [Grady Booch](/wiki/Grady_Booch "Grady Booch"), 2014


In [open source software](/wiki/Open_source_software "Open source software"), postponing sending local changes to the upstream project is a form of technical debt.[*[citation needed](/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")*]



See also[[edit](/w/index.php?title=Technical_debt&action=edit&section=4 "Edit section: See also")]
--------------------------------------------------------------------------------------------------


* [Code smell](/wiki/Code_smell "Code smell") (symptoms of inferior code quality that can contribute to technical debt)
* [Big ball of mud](/wiki/Big_ball_of_mud "Big ball of mud")
* [Bus factor](/wiki/Bus_factor "Bus factor")
* [Escalation of commitment](/wiki/Escalation_of_commitment "Escalation of commitment")
* [Manumation](/wiki/Manumation "Manumation")
* [Overengineering](/wiki/Overengineering "Overengineering")
* [Shotgun surgery](/wiki/Shotgun_surgery "Shotgun surgery")
* [Software entropy](/wiki/Software_entropy "Software entropy")
* [Software rot](/wiki/Software_rot "Software rot")
* [Spaghetti code](/wiki/Spaghetti_code "Spaghetti code")
* [SQALE](/wiki/SQALE "SQALE")
* [Sunk cost](/wiki/Sunk_cost "Sunk cost")
* [TODO, FIXME, XXX](/wiki/Comment_(computer_programming)#Tags "Comment (computer programming)")


References[[edit](/w/index.php?title=Technical_debt&action=edit&section=5 "Edit section: References")]
------------------------------------------------------------------------------------------------------


1. ^ [***a***](#cite_ref-Girish_2014_1-0) [***b***](#cite_ref-Girish_2014_1-1) Suryanarayana, Girish (November 2014). *Refactoring for Software Design Smells* (1st ed.). Morgan Kaufmann. p. 258. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-0128013977](/wiki/Special:BookSources/978-0128013977 "Special:BookSources/978-0128013977").
2. **[^](#cite_ref-2)** ["Definition of the term "Technical Debt" (plus, some background information and an "explanation")"](https://www.techopedia.com/definition/27913/technical-debt). *Techopedia*. Retrieved August 11, 2016.
3. **[^](#cite_ref-Managing_Technical_Debt_3-0)** Allman, Eric (May 2012). "Managing Technical Debt". *Communications of the ACM*. **55** (5): 50–55. [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.1145/2160718.2160733](https://doi.org/10.1145%2F2160718.2160733). [S2CID](/wiki/S2CID_(identifier) "S2CID (identifier)") [53246391](https://api.semanticscholar.org/CorpusID:53246391).
4. **[^](#cite_ref-Jeffries_2015_4-0)** Jeffries, Ron. ["Technical Debt – Bad metaphor or worst metaphor?"](https://web.archive.org/web/20151111011323/http://ronjeffries.com/articles/015-11/tech-debt/). Archived from [the original](http://ronjeffries.com/articles/015-11/tech-debt/) on November 11, 2015. Retrieved November 10, 2015.
5. **[^](#cite_ref-Knesek_2016_5-0)** Knesek, Doug. ["Averting a 'Technical Debt' Crisis"](https://www.linkedin.com/pulse/averting-technical-debt-crisis-part-1-doug-knesek). Retrieved April 7, 2016.
6. **[^](#cite_ref-6)** Avgeriou, Paris; Kruchten, Philippe; Ozkaya, Ipek; Carolyn, Seaman (2016). ["Managing technical debt in software engineering (dagstuhl seminar 16162)"](https://drops.dagstuhl.de/opus/volltexte/2016/6693/pdf/dagrep_v006_i004_p110_s16162.pdf#page=3) (PDF). *Dagstuhl Reports*. **6** (4).
7. ^ [***a***](#cite_ref-:0_7-0) [***b***](#cite_ref-:0_7-1) Rios, Nicolli; Spínola, Rodrigo Oliveira; Mendonça, Manoel; Seaman, Carolyn (2018-10-11). ["The most common causes and effects of technical debt: First results from a global family of industrial surveys"](https://doi.org/10.1145/3239235.3268917). *Proceedings of the 12th ACM/IEEE International Symposium on Empirical Software Engineering and Measurement*. ESEM '18. New York, NY, USA: Association for Computing Machinery. pp. 1–10. [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.1145/3239235.3268917](https://doi.org/10.1145%2F3239235.3268917). [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-1-4503-5823-1](/wiki/Special:BookSources/978-1-4503-5823-1 "Special:BookSources/978-1-4503-5823-1").
8. ^ [***a***](#cite_ref-SuryanarayanaSamarthyam2014_8-0) [***b***](#cite_ref-SuryanarayanaSamarthyam2014_8-1) [***c***](#cite_ref-SuryanarayanaSamarthyam2014_8-2) Girish Suryanarayana; Ganesh Samarthyam; Tushar Sharma (11 November 2014). [*Refactoring for Software Design Smells: Managing Technical Debt*](https://books.google.com/books?id=1SaOAwAAQBAJ&pg=PA3). Elsevier Science. p. 3. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-0-12-801646-6](/wiki/Special:BookSources/978-0-12-801646-6 "Special:BookSources/978-0-12-801646-6").
9. ^ [***a***](#cite_ref-Sterling2010_9-0) [***b***](#cite_ref-Sterling2010_9-1) [***c***](#cite_ref-Sterling2010_9-2) Chris Sterling (10 December 2010). [*Managing Software Debt: Building for Inevitable Change (Adobe Reader)*](https://books.google.com/books?id=LYQlOaRwpnEC&pg=PA17). Addison-Wesley Professional. p. 17. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-0-321-70055-1](/wiki/Special:BookSources/978-0-321-70055-1 "Special:BookSources/978-0-321-70055-1").
10. **[^](#cite_ref-Essential_Scrum:_Velocity_10-0)** Rubin, Kenneth (2013), *Essential Scrum. A Practical Guide to the Most Popular Agile Process*, Addison-Wesley, p. 155, [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-0-13-704329-3](/wiki/Special:BookSources/978-0-13-704329-3 "Special:BookSources/978-0-13-704329-3")
11. **[^](#cite_ref-11)** Lehman, MM (1996). ["Laws of Software Evolution Revisited"](http://dl.acm.org/citation.cfm?id=681473). *EWSPT '96 Proceedings of the 5th European Workshop on Software Process Technology*: 108–124. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [9783540617716](/wiki/Special:BookSources/9783540617716 "Special:BookSources/9783540617716"). Retrieved 19 November 2014.
12. **[^](#cite_ref-oopsla92_12-0)** [Ward Cunningham](/wiki/Ward_Cunningham "Ward Cunningham") (1992-03-26). ["The WyCash Portfolio Management System"](http://c2.com/doc/oopsla92.html). Retrieved 2008-09-26.
13. **[^](#cite_ref-rtp_13-0)** Kerievsky, Joshua (2004). *Refactoring to Patterns*. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-0-321-21335-8](/wiki/Special:BookSources/978-0-321-21335-8 "Special:BookSources/978-0-321-21335-8").
14. **[^](#cite_ref-14)** Ali, Junade (September 2016). [*Mastering PHP Design Patterns | PACKT Books*](https://www.packtpub.com/application-development/mastering-php-design-patterns) (1 ed.). Birmingham, England, UK: Packt Publishing Limited. p. 11. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-1-78588-713-0](/wiki/Special:BookSources/978-1-78588-713-0 "Special:BookSources/978-1-78588-713-0"). Retrieved 11 December 2017.

External links[[edit](/w/index.php?title=Technical_debt&action=edit&section=6 "Edit section: External links")]
--------------------------------------------------------------------------------------------------------------


* [*Ward Explains Debt Metaphor*](http://c2.com/cgi/wiki?WardExplainsDebtMetaphor), video from Ward Cunningham
* [OnTechnicalDebt](http://www.ontechnicaldebt.com) The online community for discussing technical debt
* Experts interviews on Technical Debt: [Ward Cunningham](https://web.archive.org/web/20120621171342/http://blog.techdebt.org/resources-links/67/ward-cunningham-interview-about-technical-debt-sqale-agile), [Philippe KRUCHTEN](https://web.archive.org/web/20120717083235/http://blog.techdebt.org/interviews/156/interview-with-philippe-kruchten-on-technical-debt-rup-ubc-decision-process-architecture), [Ipek OZKAYA](https://web.archive.org/web/20121129073247/http://blog.techdebt.org/interviews/189/technical-debt-interview-with-ipek-ozkaya-on-technical-debt-sei-ieee-software-architecture-agile), [Jean-Louis LETOUZEY](https://web.archive.org/web/20120714053317/http://blog.techdebt.org/interviews/118/interview-with-jean-louis-letouzey-on-technical-debt-and-sqale)
* [Steve McConnell discusses technical debt](http://www.construx.com/10x_Software_Development/Technical_Debt/)
* [TechnicalDebt](http://www.martinfowler.com/bliki/TechnicalDebt.html) from Martin Fowler Bliki
* [Averting a "Technical Debt" Crisis](https://www.linkedin.com/pulse/averting-technical-debt-crisis-part-1-doug-knesek) by Doug Knesek
* ["Get out of Technical Debt Now!"](http://www.media-landscape.com/yapc/2006-06-26.AndyLester/), a talk by Andy Lester
* [Lehman's Law](http://www.inf.ed.ac.uk/teaching/courses/rtse/Lectures/lehmanslaws.pdf)
* [Managing Technical Debt Webinar by Steve McConnell](https://www.youtube.com/watch?v=lEKvzEyNtbk)
* [Boundy, David](/w/index.php?title=David_E._Boundy&action=edit&redlink=1 "David E. Boundy (page does not exist)"), [Software cancer: the seven early warning signs](http://dl.acm.org/citation.cfm?id=156632) or [here](https://www.academia.edu/2303865/Software_cancer_the_seven_early_warning_signs), ACM SIGSOFT Software Engineering Notes, Vol. 18 No. 2 (April 1993), Association for Computing Machinery, New York, New York, US
* [Technical debt: investeer en voorkom faillissement](http://www.emerce.nl/opinie/hoge-ontwikkelkosten-eigen-schuld) by Colin Spoel
* [Technical debts: Everything you need to know](https://gauravtiwari.org/2016/12/10/technical-debts-basics/)
* [What is technical debt?](https://deepsource.io/blog/what-is-technical-debt/) from DeepSource blog





![](https://login.wikimedia.org/wiki/Special:CentralAutoLogin/start?type=1x1)
Retrieved from "<https://en.wikipedia.org/w/index.php?title=Technical_debt&oldid=1220717363>"
[Categories](/wiki/Help:Category "Help:Category"): * [Metaphors](/wiki/Category:Metaphors "Category:Metaphors")
* [Software architecture](/wiki/Category:Software_architecture "Category:Software architecture")
* [Software engineering terminology](/wiki/Category:Software_engineering_terminology "Category:Software engineering terminology")
* [Software maintenance](/wiki/Category:Software_maintenance "Category:Software maintenance")
Hidden categories: * [Articles with short description](/wiki/Category:Articles_with_short_description "Category:Articles with short description")
* [Short description is different from Wikidata](/wiki/Category:Short_description_is_different_from_Wikidata "Category:Short description is different from Wikidata")
* [Articles needing additional references from October 2022](/wiki/Category:Articles_needing_additional_references_from_October_2022 "Category:Articles needing additional references from October 2022")
* [All articles needing additional references](/wiki/Category:All_articles_needing_additional_references "Category:All articles needing additional references")
* [Wikipedia articles needing clarification from October 2013](/wiki/Category:Wikipedia_articles_needing_clarification_from_October_2013 "Category:Wikipedia articles needing clarification from October 2013")
* [All articles with unsourced statements](/wiki/Category:All_articles_with_unsourced_statements "Category:All articles with unsourced statements")
* [Articles with unsourced statements from May 2018](/wiki/Category:Articles_with_unsourced_statements_from_May_2018 "Category:Articles with unsourced statements from May 2018")
* [Articles with unsourced statements from April 2013](/wiki/Category:Articles_with_unsourced_statements_from_April_2013 "Category:Articles with unsourced statements from April 2013")

