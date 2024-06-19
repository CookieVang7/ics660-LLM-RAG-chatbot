



From Wikipedia, the free encyclopedia


Collaborative technique for software development
[![](//upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Wocintech_%28microsoft%29_-_61_%2825926639341%29.jpg/220px-Wocintech_%28microsoft%29_-_61_%2825926639341%29.jpg)](/wiki/File:Wocintech_(microsoft)_-_61_(25926639341).jpg)

Pair programming


**Pair programming** is a [software development](/wiki/Software_development "Software development") technique in which two [programmers](/wiki/Computer_programmer "Computer programmer") work together at one workstation. One, the *driver*, writes [code](/wiki/Source_code "Source code") while the other, the *observer* or *navigator*,[[1]](#cite_note-1) [reviews](/wiki/Code_review "Code review") each line of code as it is typed in. The two programmers switch roles frequently.


While reviewing, the observer also considers the "strategic" direction of the work, coming up with ideas for improvements and likely future problems to address. This is intended to free the driver to focus all of their attention on the "tactical" aspects of completing the current task, using the observer as a safety net and guide.




Economics[[edit](/w/index.php?title=Pair_programming&action=edit&section=1 "Edit section: Economics")]
------------------------------------------------------------------------------------------------------


Pair programming increases the [man-hours](/wiki/Man-hour "Man-hour") required to deliver code compared to programmers working individually.[[2]](#cite_note-ijhcs-2) However, the resulting code has fewer defects.[[3]](#cite_note-costs-benefits-3) Along with code development time, other factors like field support costs and quality assurance also figure into the return on investment. Pair programming might theoretically offset these expenses by reducing defects in the programs.[[3]](#cite_note-costs-benefits-3)


In addition to preventing mistakes as they are made, other intangible benefits may exist. For example, the courtesy of rejecting phone calls or other distractions while working together, taking fewer breaks at agreed-upon intervals or sharing breaks to return phone calls (but returning to work quickly since someone is waiting). One member of the team might have more focus and help drive or awaken the other if they lose focus, and that role might periodically change. One member might know about a topic or technique that the other does not, which might eliminate delays to finding or testing a solution, or allow for a better solution, thus effectively expanding the skill set, knowledge, and experience of a programmer as compared to working alone. Each of these intangible benefits, and many more, may be challenging to accurately measure but can contribute to more efficient working hours.[*[citation needed](/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")*]



Design quality[[edit](/w/index.php?title=Pair_programming&action=edit&section=2 "Edit section: Design quality")]
----------------------------------------------------------------------------------------------------------------


A system with two programmers possesses greater potential for the generation of more diverse solutions to problems for three reasons:



1. the programmers bring different prior experiences to the task;
2. they may assess information relevant to the task in different ways;
3. they stand in different relationships to the problem by their functional roles.


In an attempt to share goals and plans, the programmers must overtly negotiate a shared course of action when a conflict arises between them. In doing so, they consider a larger number of ways of solving the problem than a single programmer alone might do. This significantly improves the design quality of the program as it reduces the chances of selecting a poor method.[[4]](#cite_note-4)



Satisfaction[[edit](/w/index.php?title=Pair_programming&action=edit&section=3 "Edit section: Satisfaction")]
------------------------------------------------------------------------------------------------------------


In an online survey of pair programmers from 2000, 96% of programmers stated that they enjoyed working more while pair programming than programming alone. Furthermore, 95% said that they were more confident in their work when they pair programmed. However, as the survey was among self-selected pair programmers, it did not account for programmers who were forced to pair program.[[5]](#cite_note-strengthening-5)



Learning[[edit](/w/index.php?title=Pair_programming&action=edit&section=4 "Edit section: Learning")]
----------------------------------------------------------------------------------------------------


Knowledge is constantly shared between pair programmers, whether in the industry or in a classroom. Many sources suggest that students show higher confidence when programming in pairs,[[5]](#cite_note-strengthening-5) and many learn whether it be from tips on programming language rules to overall design skills.[[6]](#cite_note-support-6) In "promiscuous pairing", each programmer communicates and works with all the other programmers on the team rather than pairing only with one partner, which causes knowledge of the system to spread throughout the whole team.[[3]](#cite_note-costs-benefits-3) Pair programming allows programmers to examine their partner's code and provide feedback, which is necessary to increase their own ability to develop monitoring mechanisms for their own learning activities.[[6]](#cite_note-support-6)



Team-building and communication[[edit](/w/index.php?title=Pair_programming&action=edit&section=5 "Edit section: Team-building and communication")]
--------------------------------------------------------------------------------------------------------------------------------------------------


[![](//upload.wikimedia.org/wikipedia/commons/thumb/a/af/Pair_programming_1.jpg/220px-Pair_programming_1.jpg)](/wiki/File:Pair_programming_1.jpg)

Two co-workers pair programming, 2007


Pair programming allows team members to share quickly, making them less likely to have agendas hidden from each other. This helps pair programmers learn to communicate more easily. "This raises the communication bandwidth and frequency within the project, increasing overall information flow within the team."[[3]](#cite_note-costs-benefits-3)



Studies[[edit](/w/index.php?title=Pair_programming&action=edit&section=6 "Edit section: Studies")]
--------------------------------------------------------------------------------------------------


There are both empirical studies and meta-analyses of pair programming. The empirical studies tend to examine the level of productivity and the quality of the code, while meta-analyses may focus on biases introduced by the process of testing and publishing.


A [meta-analysis](/wiki/Meta-analysis "Meta-analysis") found pairs typically consider more design alternatives than programmers working alone, arrive at simpler, more maintainable designs, and catch design defects earlier. However, it raised concerns that its findings may have been influenced by "signs of [publication bias](/wiki/Publication_bias "Publication bias") among published studies on pair programming." It concluded that "pair programming is not uniformly beneficial or effective."[[7]](#cite_note-hannay-meta-7)


Although pair programmers may complete a task faster than a solo programmer, the total number of [man-hours](/wiki/Man-hour "Man-hour") increases.[[2]](#cite_note-ijhcs-2) A manager would have to balance faster completion of the work and reduced testing and debugging time against the higher cost of coding. The relative weight of these factors can vary by project and task.


The benefit of pairing is greatest on tasks that the programmers do not fully understand before they begin: that is, challenging tasks that call for creativity and sophistication, and for novices as compared to experts.[[2]](#cite_note-ijhcs-2) Pair programming could be helpful for attaining high quality and correctness on complex programming tasks, but it would also increase the development effort (cost) significantly.[[7]](#cite_note-hannay-meta-7)


On simple tasks, which the pair already fully understands, pairing results in a net drop in productivity.[[2]](#cite_note-ijhcs-2)[[8]](#cite_note-Arisholm_2007_65–86-8) It may reduce the code development time but also risks reducing the quality of the program.[[7]](#cite_note-hannay-meta-7) Productivity can also drop when novice–novice pairing is used without sufficient availability of a mentor to coach them.[[9]](#cite_note-9)


A study of programmers using AI assistance tools such as [GitHub Copilot](/wiki/GitHub_Copilot "GitHub Copilot") found that while some programmers conceived of AI assistance as similar to pair programming, in practice the use of such tools is very different in terms of the programmer experience, with the human programmer having to transition repeatedly between driver and navigator roles.[[10]](#cite_note-10)



Indicators of non-performance[[edit](/w/index.php?title=Pair_programming&action=edit&section=7 "Edit section: Indicators of non-performance")]
----------------------------------------------------------------------------------------------------------------------------------------------


There are indicators that a pair is not performing well: [*[opinion](/wiki/Wikipedia:Neutral_point_of_view/FAQ#Assert_facts,_not_opinions "Wikipedia:Neutral point of view/FAQ")*]



* *Disengagement* may present as one of the members physically withdraws away from the keyboard, accesses email, or even falls asleep.
* The *"Watch the Master"* phenomenon can arise if one member is more experienced than the other. In this situation, the junior member may take the observer role, deferring to the senior member of the pair for the majority of coding activity. This can easily lead to disengagement.


Pairing variations[[edit](/w/index.php?title=Pair_programming&action=edit&section=8 "Edit section: Pairing variations")]
------------------------------------------------------------------------------------------------------------------------


Expert–expert
Expert–expert pairing may seem to be the obvious choice for the highest productivity and can produce great results, but it often yields little insight into new ways to solve problems, as both parties are unlikely to question established practices.[[2]](#cite_note-ijhcs-2)
Expert–novice
Expert–novice pairing creates many opportunities for the expert to mentor the novice. This pairing can also introduce new ideas, as the novice is more likely to question established practices. The expert, now required to explain established practices, is also more likely to question them. However, in this pairing, an intimidated novice may passively "watch the master" and hesitate to participate meaningfully. Also, some experts may not have the patience needed to allow constructive novice participation.[[11]](#cite_note-11)
Novice–novice
Novice–novice pairing can produce results significantly better than two novices working independently, although this practice is generally discouraged because it is harder for novices to develop good habits without a proper role model.[[3]](#cite_note-costs-benefits-3)
Remote pair programming[[edit](/w/index.php?title=Pair_programming&action=edit&section=9 "Edit section: Remote pair programming")]
----------------------------------------------------------------------------------------------------------------------------------


**Remote pair programming**, also known as **virtual pair programming** or **distributed pair programming**, is pair programming in which the two programmers are in different locations,[[12]](#cite_note-12) working via a [collaborative real-time editor](/wiki/Collaborative_real-time_editor "Collaborative real-time editor"), shared desktop, or a remote pair programming [IDE](/wiki/Integrated_development_environment "Integrated development environment") plugin. Remote pairing introduces difficulties not present in face-to-face pairing, such as extra delays for coordination, depending more on "heavyweight" task-tracking tools instead of "lightweight" ones like index cards, and loss of verbal communication resulting in confusion and conflicts over such things as who "has the keyboard".[[13]](#cite_note-jucs-13)


Tool support could be provided by:



* Whole-screen sharing software[[14]](#cite_note-14)[[15]](#cite_note-15)[*[self-published source?](/wiki/Wikipedia:Verifiability#Self-published_sources "Wikipedia:Verifiability")*]
* [Terminal multiplexers](/wiki/Terminal_multiplexer "Terminal multiplexer")
* Specialized distributed editing tools
* Audio chat programs or VoIP software could be helpful when the screen sharing software does not provide two-way audio capability. Use of headsets keep the programmers' hands free
* Cloud development environments
* Collaborative pair programming services


See also[[edit](/w/index.php?title=Pair_programming&action=edit&section=10 "Edit section: See also")]
-----------------------------------------------------------------------------------------------------


* [Extreme programming](/wiki/Extreme_programming "Extreme programming")
* [Joint attention](/wiki/Joint_attention "Joint attention")
* [Mob programming](/wiki/Mob_programming "Mob programming")
* [Team programming](/wiki/Team_programming "Team programming")


References[[edit](/w/index.php?title=Pair_programming&action=edit&section=11 "Edit section: References")]
---------------------------------------------------------------------------------------------------------



1. **[^](#cite_ref-1)** [Williams, Laurie](/wiki/Laurie_Williams_(software_engineer) "Laurie Williams (software engineer)") (February 19–20, 2001). *Integrating pair programming into a software development process*. 14th Conference on Software Engineering Education and Training. Charlotte. pp. 27–36. [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.1109/CSEE.2001.913816](https://doi.org/10.1109%2FCSEE.2001.913816). [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [0-7695-1059-0](/wiki/Special:BookSources/0-7695-1059-0 "Special:BookSources/0-7695-1059-0"). One of the programmers, the driver, has control of the keyboard/mouse and actively implements the program. The other programmer, the observer, continuously observes the work of the driver to identify tactical (syntactic, spelling, etc.) defects, and also thinks strategically about the direction of the work.
2. ^ [***a***](#cite_ref-ijhcs_2-0) [***b***](#cite_ref-ijhcs_2-1) [***c***](#cite_ref-ijhcs_2-2) [***d***](#cite_ref-ijhcs_2-3) [***e***](#cite_ref-ijhcs_2-4) Lui, Kim Man (September 2006). ["Pair programming productivity: Novice–novice vs. expert–expert"](https://web.archive.org/web/20110720105133/http://www.cs.utexas.edu/users/mckinley/305j/pair-hcs-2006.pdf) (PDF). *International Journal of Human–Computer Studies*. **64** (9): 915–925. [CiteSeerX](/wiki/CiteSeerX_(identifier) "CiteSeerX (identifier)") [10.1.1.364.2159](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.364.2159). [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.1016/j.ijhcs.2006.04.010](https://doi.org/10.1016%2Fj.ijhcs.2006.04.010). Archived from [the original](http://www.cs.utexas.edu/users/mckinley/305j/pair-hcs-2006.pdf) (PDF) on 2011-07-20. Retrieved 2012-11-18.
3. ^ [***a***](#cite_ref-costs-benefits_3-0) [***b***](#cite_ref-costs-benefits_3-1) [***c***](#cite_ref-costs-benefits_3-2) [***d***](#cite_ref-costs-benefits_3-3) [***e***](#cite_ref-costs-benefits_3-4) [Cockburn, Alistair](/wiki/Alistair_Cockburn "Alistair Cockburn"); [Williams, Laurie](/wiki/Laurie_Williams_(software_engineer) "Laurie Williams (software engineer)") (2000). ["The Costs and Benefits of Pair Programming"](http://collaboration.csc.ncsu.edu/laurie/Papers/XPSardinia.PDF) (PDF). *Proceedings of the First International Conference on Extreme Programming and Flexible Processes in Software Engineering (XP2000)*.
4. **[^](#cite_ref-4)** Flor, Nick V.; Hutchins, Edwin L. (1991). ["Analyzing Distributed Cognition in Software Teams: A Case Study of Team Programming During Perfective Software Maintenance"](https://books.google.com/books?id=KT_bpSSJBgcC&pg=PA36). In Koenemann-Belliveau, Jürgen; Moher, Thomas G.; Robertson, Scott P. (eds.). *Empirical Studies of Programmers: Fourth Workshop*. Ablex. pp. 36–64. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-0-89391-856-9](/wiki/Special:BookSources/978-0-89391-856-9 "Special:BookSources/978-0-89391-856-9").
5. ^ [***a***](#cite_ref-strengthening_5-0) [***b***](#cite_ref-strengthening_5-1) [Williams, Laurie](/wiki/Laurie_Williams_(software_engineer) "Laurie Williams (software engineer)"); Kessler, Robert R.; Cunningham, Ward; Jeffries, Ron (2000). ["Strengthening the case for pair programming"](http://sunnyday.mit.edu/16.355/williams.pdf) (PDF). *IEEE Software*. **17** (4): 19–25. [CiteSeerX](/wiki/CiteSeerX_(identifier) "CiteSeerX (identifier)") [10.1.1.33.5248](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.33.5248). [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.1109/52.854064](https://doi.org/10.1109%2F52.854064).
6. ^ [***a***](#cite_ref-support_6-0) [***b***](#cite_ref-support_6-1) [Williams, Laurie](/wiki/Laurie_Williams_(software_engineer) "Laurie Williams (software engineer)"); Upchurch, Richard L. (2001). ["In support of student pair programming"](https://doi.org/10.1145%2F366413.364614). *ACM SIGCSE Bulletin*. **33** (1): 327–31. [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.1145/366413.364614](https://doi.org/10.1145%2F366413.364614).
7. ^ [***a***](#cite_ref-hannay-meta_7-0) [***b***](#cite_ref-hannay-meta_7-1) [***c***](#cite_ref-hannay-meta_7-2) Hannay, Jo E.; Tore Dybå; Erik Arisholm; Dag I.K. Sjøberg (July 2009). "The Effectiveness of Pair Programming: A Meta-Analysis". *Information and Software Technology*. **51** (7): 1110–1122. [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.1016/j.infsof.2009.02.001](https://doi.org/10.1016%2Fj.infsof.2009.02.001).
8. **[^](#cite_ref-Arisholm_2007_65–86_8-0)** Arisholm, Erik; Hans Gallis; Tore Dybå; Dag I.K. Sjøberg (February 2007). ["Evaluating Pair Programming with Respect to System Complexity and Programmer Expertise"](https://web.archive.org/web/20101029033020/http://simula.no/research/se/publications/Arisholm.2006.2/simula_pdf_file). *IEEE Transactions on Software Engineering*. **33** (2): 65–86. [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.1109/TSE.2007.17](https://doi.org/10.1109%2FTSE.2007.17). [S2CID](/wiki/S2CID_(identifier) "S2CID (identifier)") [9889035](https://api.semanticscholar.org/CorpusID:9889035). Archived from [the original](http://simula.no/research/se/publications/Arisholm.2006.2/simula_pdf_file) on 2010-10-29. Retrieved 2008-07-21.
9. **[^](#cite_ref-9)** Stephens, Matt; Doug Rosenberg. ["Will Pair Programming Really Improve Your Project?"](http://www.methodsandtools.com/archive/archive.php?id=10). Retrieved 28 May 2011.
10. **[^](#cite_ref-10)** Sarkar, Advait; Gordon, Andrew D.; Negreanu, Carina; Poelitz, Christian; Ragavan, Sruti S.; Zorn, Ben (2022). ["What is it like to program with artificial intelligence?"](https://www.ppig.org/papers/2022-ppig-33rd-sarkar/). *Psychology of Programming Interest Group*. Retrieved 27 March 2023.
11. **[^](#cite_ref-11)** [Williams, L.](/wiki/Laurie_Williams_(software_engineer) "Laurie Williams (software engineer)") & Kessler, R. (2003). [*Pair Programming Illuminated*](https://books.google.com/books?id=LRQhdlrKNE8C). Boston: Addison-Wesley Professional. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [9780201745764](/wiki/Special:BookSources/9780201745764 "Special:BookSources/9780201745764").
12. **[^](#cite_ref-12)** Flor, Nick V. (2006). "Globally distributed software development and pair programming". *Communications of the ACM*. **49** (10): 57–8. [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.1145/1164394.1164421](https://doi.org/10.1145%2F1164394.1164421). [S2CID](/wiki/S2CID_(identifier) "S2CID (identifier)") [8963421](https://api.semanticscholar.org/CorpusID:8963421).
13. **[^](#cite_ref-jucs_13-0)** Schümmer, Till; Stephan Lukosch (September 2009). ["Understanding Tools and Practices for Distributed Pair Programming"](http://www.jucs.org/jucs_15_16/understanding_tools_and_practices/jucs_15_16_3101_3125_schuemmer.pdf) (PDF). *[Journal of Universal Computer Science](/wiki/Journal_of_Universal_Computer_Science "Journal of Universal Computer Science")*. **15** (16): 3101–3125. Retrieved 2010-04-30.
14. **[^](#cite_ref-14)** [Agile Ajax: Pair Programming with VNC](http://blogs.pathf.com/agileajax/2007/09/pair-programmin.html) [Archived](https://web.archive.org/web/20080402003711/http://blogs.pathf.com/agileajax/2007/09/pair-programmin.html) 2008-04-02 at the [Wayback Machine](/wiki/Wayback_Machine "Wayback Machine")[*[self-published source](/wiki/Wikipedia:Verifiability#Self-published_sources "Wikipedia:Verifiability")*]
15. **[^](#cite_ref-15)** [Pair Programming – The Ultimate Setup and the other options we tried. – Jonathan Cogley's Blog](https://weblogs.asp.net/jcogley/archive/2004/10/13/242117.aspx)

External links[[edit](/w/index.php?title=Pair_programming&action=edit&section=12 "Edit section: External links")]
-----------------------------------------------------------------------------------------------------------------


* [wikiHow: How to Pair Program](https://www.wikihow.com/Pair-Program)  How-to guide; contains common wisdom on how to make pair programming work.
* [Tuple:Pair Programming Guide](https://tuple.app/pair-programming-guide) Pair programming guide that covers paring styles, antipatterns, and more. Includes example paring videos.
* [c2:PairProgramming](https://wiki.c2.com/?PairProgramming "c2:PairProgramming")
* [c2:PairProgrammingPattern](https://wiki.c2.com/?PairProgrammingPattern "c2:PairProgrammingPattern")
* [c2:PairRotationFrequency](https://wiki.c2.com/?PairRotationFrequency "c2:PairRotationFrequency")





![](https://login.wikimedia.org/wiki/Special:CentralAutoLogin/start?type=1x1)
Retrieved from "<https://en.wikipedia.org/w/index.php?title=Pair_programming&oldid=1220523497>"
[Categories](/wiki/Help:Category "Help:Category"): * [Agile software development](/wiki/Category:Agile_software_development "Category:Agile software development")
* [Extreme programming](/wiki/Category:Extreme_programming "Category:Extreme programming")
* [Software review](/wiki/Category:Software_review "Category:Software review")
Hidden categories: * [Webarchive template wayback links](/wiki/Category:Webarchive_template_wayback_links "Category:Webarchive template wayback links")
* [All accuracy disputes](/wiki/Category:All_accuracy_disputes "Category:All accuracy disputes")
* [Accuracy disputes from April 2016](/wiki/Category:Accuracy_disputes_from_April_2016 "Category:Accuracy disputes from April 2016")
* [Articles with short description](/wiki/Category:Articles_with_short_description "Category:Articles with short description")
* [Short description matches Wikidata](/wiki/Category:Short_description_matches_Wikidata "Category:Short description matches Wikidata")
* [All articles with unsourced statements](/wiki/Category:All_articles_with_unsourced_statements "Category:All articles with unsourced statements")
* [Articles with unsourced statements from April 2022](/wiki/Category:Articles_with_unsourced_statements_from_April_2022 "Category:Articles with unsourced statements from April 2022")
* [All articles with minor POV problems](/wiki/Category:All_articles_with_minor_POV_problems "Category:All articles with minor POV problems")
* [Articles with minor POV problems from May 2021](/wiki/Category:Articles_with_minor_POV_problems_from_May_2021 "Category:Articles with minor POV problems from May 2021")
* [All articles with self-published sources](/wiki/Category:All_articles_with_self-published_sources "Category:All articles with self-published sources")
* [Articles with self-published sources from April 2016](/wiki/Category:Articles_with_self-published_sources_from_April_2016 "Category:Articles with self-published sources from April 2016")

