



From Wikipedia, the free encyclopedia




|  | **This article has multiple issues.** Please help **[improve it](/wiki/Special:EditPage/Story-driven_modeling "Special:EditPage/Story-driven modeling")** or discuss these issues on the **[talk page](/wiki/Talk:Story-driven_modeling "Talk:Story-driven modeling")**. *([Learn how and when to remove these template messages](/wiki/Help:Maintenance_template_removal "Help:Maintenance template removal"))*    |  | This article includes a list of general [references](/wiki/Wikipedia:Citing_sources "Wikipedia:Citing sources"), but **it lacks sufficient corresponding [inline citations](/wiki/Wikipedia:Citing_sources#Inline_citations "Wikipedia:Citing sources")**. Please help to [improve](/wiki/Wikipedia:WikiProject_Reliability "Wikipedia:WikiProject Reliability") this article by [introducing](/wiki/Wikipedia:When_to_cite "Wikipedia:When to cite") more precise citations. *(February 2014)* *([Learn how and when to remove this message](/wiki/Help:Maintenance_template_removal "Help:Maintenance template removal"))* | | --- | --- |    |  | This article **is written like a [personal reflection, personal essay, or argumentative essay](/wiki/Wikipedia:What_Wikipedia_is_not#Wikipedia_is_not_a_publisher_of_original_thought "Wikipedia:What Wikipedia is not")** that states a Wikipedia editor's personal feelings or presents an original argument about a topic. Please [help improve it](https://en.wikipedia.org/w/index.php?title=Story-driven_modeling&action=edit) by rewriting it in an [encyclopedic style](/wiki/Wikipedia:Writing_better_articles#Information_style_and_tone "Wikipedia:Writing better articles"). *(February 2014)* *([Learn how and when to remove this message](/wiki/Help:Maintenance_template_removal "Help:Maintenance template removal"))* | | --- | --- |     *([Learn how and when to remove this message](/wiki/Help:Maintenance_template_removal "Help:Maintenance template removal"))* |
| --- | --- | --- | --- | --- | --- |


**Story-driven modeling**[[1]](#cite_note-SDMBook-1)[[2]](#cite_note-ZSW99-2)[[3]](#cite_note-DGZ04-3) is an [object-oriented modeling](/wiki/Object-oriented_modeling "Object-oriented modeling") technique.[[4]](#cite_note-4)[[5]](#cite_note-EGHZ12-5) Other forms of object-oriented modeling focus on [class diagrams](/wiki/Class_diagram "Class diagram"). 
Class diagrams describe the static structure of a program, i.e. the building blocks of a program and how they relate to each other. 
Class diagrams also model data structures, but with an emphasis on rather abstract concepts like types and type features.


Instead of abstract static structures, story-driven modeling focuses on concrete example scenarios[[6]](#cite_note-6) and on how the steps of the example scenarios 
may be represented as [object diagrams](/wiki/Object_diagram "Object diagram") and how these object diagrams evolve during scenario execution.




Software development approach[[edit](/w/index.php?title=Story-driven_modeling&action=edit&section=1 "Edit section: Software development approach")]
---------------------------------------------------------------------------------------------------------------------------------------------------


Story-driven modeling proposes the following software development approach:



1. **Textual scenarios**: For the feature you want to implement, develop a textual scenario description for the most common case. Look on only one example at a time. Try to use specific terms and individual names instead of general terms and e.g. role names:
Scenario Go-Dutch barbecue
	* Start: This Sunday Peter, Putri, and Peng meet at the park for a go-Dutch barbecue. They use the Group Account app to do the accounting.
	* Step 1: Peter brings the meat for $12. Peter adds this item to the Group Account app.
	* Step 2: Putri brings salad for $9. Peter adds this item, too. The app shows that by now the average share is $7 and that Peng still have to bring these $7 while Peter gets $5 out and Putri gets $2 out.
	* Step 3: ...
2. **GUI mock-ups**: To illustrate the [graphical user interface](/wiki/Graphical_user_interface "Graphical user interface") (GUI) for the desired feature, you may add some wireframe models or GUI mock-ups to your scenario:
Scenario Go-Dutch barbecue
	* Start: This Sunday Peter, Putri, and Peng meet at the park for a go-Dutch barbecue. They use the Group Account app to do the accounting.
	* Step 1: Peter brings the meat for $12. Peter adds this item to the Group Account app.
	* Step 2: Putri brings salad for $9. Peter adds this item, too. The app shows that by now the average share is $7 and that Peng still have to bring these $7 while Peter gets $5 out and Putri gets $2 out:   
	[![WikipediaGoDutchMockup](//upload.wikimedia.org/wikipedia/commons/e/e3/WikipediaGoDutchMockup.png)](/wiki/File:WikipediaGoDutchMockup.png "WikipediaGoDutchMockup")
	* Step 3: ...
3. **Storyboarding**: Next, you think about how a certain situation, i.e. a certain step of a scenario may be represented within a computer by a runtime object structure. This is done by adding [object diagrams](/wiki/Object_diagram "Object diagram") to the scenario. In story driven modeling, a scenario with object diagrams is also called a storyboard.
Scenario Go-Dutch barbecue
	* Start: This Sunday Peter, Putri, and Peng meet at the park for a go-Dutch barbecue. They use the Group Account app to do the accounting.
	* Step 1: Peter brings the meat for $12. Peter adds this item to the Group Account app.
	* Step 2: Putri brings salad for $9. Peter adds this item, too. The app shows that by now the average share is $7 and that Peng still have to bring these $7 while Peter gets $5 out and Putri gets $2 out:   
	[![WikipediaGoDutchMockup](//upload.wikimedia.org/wikipedia/commons/e/e3/WikipediaGoDutchMockup.png)](/wiki/File:WikipediaGoDutchMockup.png "WikipediaGoDutchMockup")[![Object diagram modeling a go-Dutch barbecue](//upload.wikimedia.org/wikipedia/commons/2/22/WikepediaObjectDiagramGoDutchBarbeque.png)](/wiki/File:WikepediaObjectDiagramGoDutchBarbeque.png "Object diagram modeling a go-Dutch barbecue")
	* Step 3: ...
4. **Class diagram derivation**: Now it is fairly straightforward to derive a [class diagram](/wiki/Class_diagram "Class diagram") from the object diagrams used in the storyboards.  
[![Class diagram for a go-Dutch barbecue](//upload.wikimedia.org/wikipedia/commons/6/64/WikipediaGoDutchClassDiag.png)](/wiki/File:WikipediaGoDutchClassDiag.png "Class diagram for a go-Dutch barbecue")  
Note, the class diagram serves as a common reference for all object diagrams. This ensures that overall the same types and attributes are used. Using a [UML](/wiki/Unified_Modeling_Language "Unified Modeling Language") tool, you may generate a first implementation from this class diagram.
5. **Algorithm design**: So far you have modeled and implemented that object structures that are deployed in your application. Now you need to add behavior, i.e. algorithms and method bodies. Programming the behavior of an application is a demanding task. To facilitate it, you should first outline the behavior in [pseudocode](/wiki/Pseudocode "Pseudocode") notation. You might do this, e.g. with an object game. For example, to update the saldo attributes of all persons you look at our object structure and from the point of view of the GroupAccount object you do the following:
Update the saldo of all persons:
	* visit each item
		+ for each item add the value to the total value and add 1 to the number of items
	* compute the average share of each person by dividing the total value by the number of persons
	* visit each person
		+ for each person reset the saldo
		+ for each person visit each item bought by this person
			- for each item add the value to the saldo of the current person
		+ for each person subtract the share from the saldo
6. **Behavior implementation**: Once you have refined your algorithm [pseudocode](/wiki/Pseudocode "Pseudocode") down to the level of operations on object structures it is straightforward to derive source code that executes the same operations on your object model implementation.
7. **Testing**: Finally, the scenarios may be used to derive automatic [JUnit](/wiki/JUnit "JUnit") tests. The pseudocode for a test for our example might look like:
Test update the saldo of all persons:
	* create a group account object
	* add a person object with name Peter and a person object with name Putri and a person object with name Peng to the group account object
	* add an item object with buyer Peter, description Meat, and value $12 to the group account object
	* add an item object with buyer Putri, description Salad, and value $9 to the group account object
	* call method update the saldo of all persons on the group account object
	* ensure that the saldo of the Peter object is $5
	* ensure that the saldo of the Putri object is $2
	* ensure that the saldo of the Peter object is -$7
	* ensure that the sum of all saldos is $0


Such automatic tests ensure that in the example situation the behavior implementation actually does what is outlined in the storyboard. While these tests are pretty simple and may not identify all kinds of bugs, these tests are very useful to document the desired behavior and the usage of the new features and these tests ensure that the corresponding functionality is not lost due to future changes.
Summary[[edit](/w/index.php?title=Story-driven_modeling&action=edit&section=2 "Edit section: Summary")]
-------------------------------------------------------------------------------------------------------


Story driven modeling has proven to work very well for the cooperation with non IT experts.[[7]](#cite_note-7) People from other domains usually have difficulties to describe their needs in general terms (i.e. classes) and general rules (pseudocode). Similarly, normal people have problems to understand pseudocode or to judge, whether their needs are properly addressed or not. However, these people know their business very well and with the help of concrete examples and scenarios it is very easy for normal people to spot problematic cases and to judge whether their needs have been addressed properly.


Story Driven Modeling has matured since its beginning in 1997. In 2013 it is used for teaching e.g. in Kassel University, Paderborn University, Tartu University, Antwerp University, Nazarbayev University Astana, Hasso Platner Institute Potsdam, University of Victoria, ...



See also[[edit](/w/index.php?title=Story-driven_modeling&action=edit&section=3 "Edit section: See also")]
---------------------------------------------------------------------------------------------------------


* [Agile modeling](/wiki/Agile_modeling "Agile modeling")
* [Entity-control-boundary](/wiki/Entity-control-boundary "Entity-control-boundary")
* [Agile software development](/wiki/Agile_software_development "Agile software development")
* [Class-responsibility-collaboration card](/wiki/Class-responsibility-collaboration_card "Class-responsibility-collaboration card")
* [Object-oriented analysis and design](/wiki/Object-oriented_analysis_and_design "Object-oriented analysis and design")
* [Object-oriented modeling](/wiki/Object-oriented_modeling "Object-oriented modeling")
* [Test-driven development](/wiki/Test-driven_development "Test-driven development")
* [Unified Modeling Language](/wiki/Unified_Modeling_Language "Unified Modeling Language")


References[[edit](/w/index.php?title=Story-driven_modeling&action=edit&section=4 "Edit section: References")]
-------------------------------------------------------------------------------------------------------------



1. **[^](#cite_ref-SDMBook_1-0)** Norbisrath, Ulrich; Zündorf, Albert; Jubeh, Ruben (2013). *Story Driven Modeling*. p. 333. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [9781483949253](/wiki/Special:BookSources/9781483949253 "Special:BookSources/9781483949253").
2. **[^](#cite_ref-ZSW99_2-0)** Zündorf, Albert; Schürr, A.; Winter, A. J. (1999). "Story Driven Modeling". *University of Paderborn*. Technical Report (tr-ri-99-211).
3. **[^](#cite_ref-DGZ04_3-0)** Diethelm, Ira; Geiger, L.; Zündorf, A. (January 2004). "Systematic story driven modeling: a case study". *Third International Workshop on Scenarios and State Machines*: 65–70.
4. **[^](#cite_ref-4)** van Gorp, Pieter (2008). "Evaluation of the Story Driven Modeling Methodology: From Towers to Models". *Technical Report University of Antwerp*.
5. **[^](#cite_ref-EGHZ12_5-0)** Eickhoff, Christoph; Geiger, N.; Hahn, M.; Zündorf, A. (2012). ["Developing Enterprise Web Applications Using the Story Driven Modeling Approach"](https://doi.org/10.1007%2F978-3-642-27997-3_21). *Current Trends in Web Engineering*. LNCS. **7059** (7059): 196–210. [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.1007/978-3-642-27997-3\_21](https://doi.org/10.1007%2F978-3-642-27997-3_21). [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-3-642-27996-6](/wiki/Special:BookSources/978-3-642-27996-6 "Special:BookSources/978-3-642-27996-6").
6. **[^](#cite_ref-6)** Ryser, J.; Glinz, M. (2000). "Improving the Quality of Requirements with Scenarios". *Proceedings of the Second World Congress on Software Quality. Yokohama*: 55–60.
7. **[^](#cite_ref-7)** Zündorf, Albert; Leohold, J.; Müller, D.; Gemmerich, R.; Reckord, C.; Schneider, C.; Semmelroth, S. (2006). "Using object scenarios for requirements analysis - an experience report". *Modellierung 2006*: 269–278.




![](https://login.wikimedia.org/wiki/Special:CentralAutoLogin/start?type=1x1)
Retrieved from "<https://en.wikipedia.org/w/index.php?title=Story-driven_modeling&oldid=1170212588>"
[Categories](/wiki/Help:Category "Help:Category"): * [Object-oriented programming](/wiki/Category:Object-oriented_programming "Category:Object-oriented programming")
* [Software design](/wiki/Category:Software_design "Category:Software design")
Hidden categories: * [CS1: long volume value](/wiki/Category:CS1:_long_volume_value "Category:CS1: long volume value")
* [Articles lacking in-text citations from February 2014](/wiki/Category:Articles_lacking_in-text_citations_from_February_2014 "Category:Articles lacking in-text citations from February 2014")
* [All articles lacking in-text citations](/wiki/Category:All_articles_lacking_in-text_citations "Category:All articles lacking in-text citations")
* [Wikipedia articles with style issues from February 2014](/wiki/Category:Wikipedia_articles_with_style_issues_from_February_2014 "Category:Wikipedia articles with style issues from February 2014")
* [All articles with style issues](/wiki/Category:All_articles_with_style_issues "Category:All articles with style issues")
* [Articles with multiple maintenance issues](/wiki/Category:Articles_with_multiple_maintenance_issues "Category:Articles with multiple maintenance issues")

