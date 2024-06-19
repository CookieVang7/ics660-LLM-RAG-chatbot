



From Wikipedia, the free encyclopedia


Technique for estimating


|  | This article **needs additional citations for [verification](/wiki/Wikipedia:Verifiability "Wikipedia:Verifiability")**. Please help [improve this article](/wiki/Special:EditPage/Planning_poker "Special:EditPage/Planning poker") by [adding citations to reliable sources](/wiki/Help:Referencing_for_beginners "Help:Referencing for beginners"). Unsourced material may be challenged and removed.*Find sources:* ["Planning poker"](https://www.google.com/search?as_eq=wikipedia&q=%22Planning+poker%22) – [news](https://www.google.com/search?tbm=nws&q=%22Planning+poker%22+-wikipedia&tbs=ar:1) **·** [newspapers](https://www.google.com/search?&q=%22Planning+poker%22&tbs=bkt:s&tbm=bks) **·** [books](https://www.google.com/search?tbs=bks:1&q=%22Planning+poker%22+-wikipedia) **·** [scholar](https://scholar.google.com/scholar?q=%22Planning+poker%22) **·** [JSTOR](https://www.jstor.org/action/doBasicSearch?Query=%22Planning+poker%22&acc=on&wc=on) *(February 2012)* *([Learn how and when to remove this message](/wiki/Help:Maintenance_template_removal "Help:Maintenance template removal"))* |
| --- | --- |






[![](//upload.wikimedia.org/wikipedia/commons/thumb/e/eb/CrispPlanningPokerDeck.jpg/250px-CrispPlanningPokerDeck.jpg)](/wiki/File:CrispPlanningPokerDeck.jpg)[![](//upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Planning_poker_deck_Serpro.jpg/250px-Planning_poker_deck_Serpro.jpg)](/wiki/File:Planning_poker_deck_Serpro.jpg)Planning poker decks
**Planning poker**, also called **Scrum poker**, is a consensus-based, [gamified](/wiki/Gamification "Gamification") technique for estimating, mostly used for [timeboxing](/wiki/Timeboxing "Timeboxing") in *[Agile principles](/wiki/Agile_software_development#Agile_principles "Agile software development")*. In planning poker, members of the group make estimates by playing numbered cards face-down to the table, instead of speaking them aloud. The cards are revealed, and the estimates are then discussed. By hiding the figures in this way, the group can avoid the cognitive bias of [anchoring](/wiki/Anchoring_(cognitive_bias) "Anchoring (cognitive bias)"), where the first number spoken aloud sets a precedent for subsequent estimates.


Planning poker is a variation of the [Wideband delphi](/wiki/Wideband_delphi "Wideband delphi") method. It is most commonly used in [agile software development](/wiki/Agile_software_development "Agile software development"), in particular in [Scrum](/wiki/Scrum_(development) "Scrum (development)") and [Extreme Programming](/wiki/Extreme_Programming "Extreme Programming").


The method was first defined and named by James Grenning in 2002[[1]](#cite_note-1) and later popularized by [Mike Cohn](/wiki/Mike_Cohn "Mike Cohn") in the book *Agile Estimating and Planning*,[[2]](#cite_note-2) whose company [trade marked](/wiki/Trade_mark "Trade mark") the term[[3]](#cite_note-3) and a digital online tool.[[4]](#cite_note-4)




Process[[edit](/w/index.php?title=Planning_poker&action=edit&section=1 "Edit section: Process")]
------------------------------------------------------------------------------------------------


### Rationale[[edit](/w/index.php?title=Planning_poker&action=edit&section=2 "Edit section: Rationale")]


The reason to use planning poker is to avoid the influence of the other participants. If a number is spoken, it can sound like a suggestion and influence the other participants' sizing. Planning poker should force people to think independently and propose their numbers simultaneously. This is accomplished by requiring that all participants show their cards at the same time.



### Equipment[[edit](/w/index.php?title=Planning_poker&action=edit&section=3 "Edit section: Equipment")]


Planning poker is based on a list of features to be delivered, several copies of a deck of cards, and optionally, an [egg timer](/wiki/Egg_timer "Egg timer") that can be used to limit time spent in discussion of each item.


The feature list, often a list of [user stories](/wiki/User_story "User story"), describes some software that needs to be developed.


The cards in the deck have numbers on them. A typical deck has cards showing the [Fibonacci sequence](/wiki/Fibonacci_sequence "Fibonacci sequence") including a zero: 0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89; other decks use similar progressions with a fixed ratio between each value such as 1, 2, 4, 8, etc.


The reason for using the Fibonacci sequence instead of simply doubling each subsequent value is because estimating a task as exactly double the effort as another task is misleadingly precise. A task that is about twice as much effort as a 5, has to be evaluated as either a bit less than double (8) or a bit more than double (13).


Several commercially available decks use the sequence: 0, ½, 1, 2, 3, 5, 8, 13, 20, 40, 100, and optionally a ? (unsure), an infinity symbol (this task cannot be completed), and a coffee cup (I need a break, and I will make the rest of the team coffee). The reason for not exactly following the Fibonacci sequence after 13 is because someone once said to Mike Cohn "You must be very certain to have estimated that task as 21 instead of 20." Using numbers with only a single digit of precision (except for 13) indicates the [uncertainty](/wiki/Software_development_effort_estimation#Uncertainty_assessment_approaches "Software development effort estimation") in the estimation. Alternatively standard playing cards of Ace, 2, 3, 5, 8, and king can be used. Where king means: "this item is too big or too complicated to estimate". "Throwing a king" ends the discussion of the item for the current sprint.


When [teams are not in the same geographical locations](/wiki/Virtual_team "Virtual team"), [collaborative software](/wiki/Collaborative_software "Collaborative software") over the internet can be used as replacement for physical cards. Several [web applications](/wiki/Web_applications "Web applications") and [mobile applications](/wiki/Mobile_applications "Mobile applications") exist for the purpose.



### Procedure[[edit](/w/index.php?title=Planning_poker&action=edit&section=4 "Edit section: Procedure")]


At the estimation meeting, each estimator is given one deck of the cards. All decks have identical sets of cards in them.


The meeting proceeds as follows:



* A Moderator, who will not play, chairs the meeting.
* The Product Owner provides a short overview of one user story to be estimated. The team is given an opportunity to ask questions and discuss to clarify assumptions and risks. A summary of the discussion is recorded, e.g. by the Moderator.
* Each individual lays a card face down representing their estimate for the story. Units used vary - they can be days duration, ideal days, t-shirt sizes[[5]](#cite_note-5) or [story points](/wiki/Story_point "Story point"). During the discussion, estimations must not be mentioned at all in relation to feature size to avoid [anchoring](/wiki/Anchoring_(cognitive_bias) "Anchoring (cognitive bias)").
* Everyone calls their cards simultaneously by turning them over.
* People with high estimates and low estimates are given a [soap box](/wiki/Soapbox "Soapbox") to offer their justification for their estimate and then the discussion continues.
* Repeat the estimation process until a consensus is reached. The developer who was likely to own the deliverable has a large portion of the "consensus vote", although the Moderator can negotiate the consensus.
* To ensure that discussion is structured; the Moderator or the Product Owner may at any point turn over the egg timer and when it runs out all discussion must cease and another round of poker is played. The structure in the conversation is re-introduced by the soapboxes.


The cards are numbered as they are to account for the fact that the longer an estimate is, the more uncertainty it contains. Thus, if a developer wants to play a 6 he is forced to reconsider and either work through that some of the perceived uncertainty does not exist and play a 5, or accept a conservative estimate accounting for the uncertainty and play an 8.



See also[[edit](/w/index.php?title=Planning_poker&action=edit&section=5 "Edit section: See also")]
--------------------------------------------------------------------------------------------------


* [Comparison of scrum software](/wiki/Comparison_of_scrum_software "Comparison of scrum software"), which generally has support for planning poker, either included or as an optional add-on.


References[[edit](/w/index.php?title=Planning_poker&action=edit&section=6 "Edit section: References")]
------------------------------------------------------------------------------------------------------



1. **[^](#cite_ref-1)** ["Wingman Software | Planning Poker - The Original Paper"](https://wingman-sw.com/articles/planning-poker). *wingman-sw.com*. Retrieved 5 July 2017.
2. **[^](#cite_ref-2)** Cohn, Mike (November 2005). ["Agile Estimating and Planning"](http://www.mountaingoatsoftware.com/book/1). Mountain Goat Software. Retrieved 1 February 2008.
3. **[^](#cite_ref-3)** ["Planning Poker - Trademark, Service Mark #3473287"](http://tsdr.uspto.gov/#caseNumber=3473287&caseType=US_REGISTRATION_NO&searchType=statusSearch). Trademark Status & Document Retrieval (TSDR). 15 January 2008. Retrieved 26 May 2014.
4. **[^](#cite_ref-4)** Cohn, Mike. ["Planning Poker Cards: Effective Agile Planning and Estimation"](https://www.mountaingoatsoftware.com/tools/planning-poker). *Mountain Goat Software*. Mountain Goat Software. Retrieved 30 March 2016.
5. **[^](#cite_ref-5)** ["How I use T-Shirt sizing as a Product Owner to estimate delivery"](https://medium.com/serious-scrum/how-i-use-t-shirt-sizing-as-a-product-owner-to-estimate-delivery-4b24634d22a6). Medium. 7 February 2020. Retrieved 22 October 2022.




![](https://login.wikimedia.org/wiki/Special:CentralAutoLogin/start?type=1x1)
Retrieved from "<https://en.wikipedia.org/w/index.php?title=Planning_poker&oldid=1228658846>"
[Categories](/wiki/Help:Category "Help:Category"): * [Agile software development](/wiki/Category:Agile_software_development "Category:Agile software development")
* [Software project management](/wiki/Category:Software_project_management "Category:Software project management")
* [Software development philosophies](/wiki/Category:Software_development_philosophies "Category:Software development philosophies")
Hidden categories: * [Articles with short description](/wiki/Category:Articles_with_short_description "Category:Articles with short description")
* [Short description matches Wikidata](/wiki/Category:Short_description_matches_Wikidata "Category:Short description matches Wikidata")
* [Articles needing additional references from February 2012](/wiki/Category:Articles_needing_additional_references_from_February_2012 "Category:Articles needing additional references from February 2012")
* [All articles needing additional references](/wiki/Category:All_articles_needing_additional_references "Category:All articles needing additional references")
* [Use American English from February 2022](/wiki/Category:Use_American_English_from_February_2022 "Category:Use American English from February 2022")
* [All Wikipedia articles written in American English](/wiki/Category:All_Wikipedia_articles_written_in_American_English "Category:All Wikipedia articles written in American English")
* [Use dmy dates from January 2020](/wiki/Category:Use_dmy_dates_from_January_2020 "Category:Use dmy dates from January 2020")

