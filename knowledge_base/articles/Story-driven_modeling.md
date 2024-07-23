


(Top)





1
Software development approach








2
Summary








3
See also








4
References














This article has multiple issues. Please help improve it or discuss these issues on the talk page. (Learn how and when to remove these template messages)

This article includes a list of general references, but it lacks sufficient corresponding inline citations. Please help to improve this article by introducing more precise citations. (February 2014) (Learn how and when to remove this message)This article is written like a personal reflection, personal essay, or argumentative essay that states a Wikipedia editor's personal feelings or presents an original argument about a topic. Please help improve it by rewriting it in an encyclopedic style. (February 2014) (Learn how and when to remove this message)

 (Learn how and when to remove this message)
This article includes a list of general references, but it lacks sufficient corresponding inline citations. Please help to improve this article by introducing more precise citations. (February 2014) (Learn how and when to remove this message)
This article is written like a personal reflection, personal essay, or argumentative essay that states a Wikipedia editor's personal feelings or presents an original argument about a topic. Please help improve it by rewriting it in an encyclopedic style. (February 2014) (Learn how and when to remove this message)
Story-driven modeling[1][2][3] is an object-oriented modeling technique.[4][5] Other forms of object-oriented modeling focus on class diagrams. 
Class diagrams describe the static structure of a program, i.e. the building blocks of a program and how they relate to each other. 
Class diagrams also model data structures, but with an emphasis on rather abstract concepts like types and type features.

Instead of abstract static structures, story-driven modeling focuses on concrete example scenarios[6] and on how the steps of the example scenarios 
may be represented as object diagrams and how these object diagrams evolve during scenario execution.

Story-driven modeling proposes the following software development approach:

Textual scenarios: For the feature you want to implement, develop a textual scenario description for the most common case. Look on only one example at a time. Try to use specific terms and individual names instead of general terms and e.g. role names:
Scenario Go-Dutch barbecue
Start: This Sunday Peter, Putri, and Peng meet at the park for a go-Dutch barbecue. They use the Group Account app to do the accounting.
Step 1: Peter brings the meat for $12. Peter adds this item to the Group Account app.
Step 2: Putri brings salad for $9. Peter adds this item, too. The app shows that by now the average share is $7 and that Peng still have to bring these $7 while Peter gets $5 out and Putri gets $2 out.
Step 3: ...
GUI mock-ups: To illustrate the graphical user interface (GUI) for the desired feature, you may add some wireframe models or GUI mock-ups to your scenario:
Scenario Go-Dutch barbecue
Start: This Sunday Peter, Putri, and Peng meet at the park for a go-Dutch barbecue. They use the Group Account app to do the accounting.
Step 1: Peter brings the meat for $12. Peter adds this item to the Group Account app.
Step 2: Putri brings salad for $9. Peter adds this item, too. The app shows that by now the average share is $7 and that Peng still have to bring these $7 while Peter gets $5 out and Putri gets $2 out: 
Step 3: ...
Storyboarding: Next, you think about how a certain situation, i.e. a certain step of a scenario may be represented within a computer by a runtime object structure. This is done by adding object diagrams to the scenario. In story driven modeling, a scenario with object diagrams is also called a storyboard.
Scenario Go-Dutch barbecue
Start: This Sunday Peter, Putri, and Peng meet at the park for a go-Dutch barbecue. They use the Group Account app to do the accounting.
Step 1: Peter brings the meat for $12. Peter adds this item to the Group Account app.
Step 2: Putri brings salad for $9. Peter adds this item, too. The app shows that by now the average share is $7 and that Peng still have to bring these $7 while Peter gets $5 out and Putri gets $2 out: 
Step 3: ...
Class diagram derivation: Now it is fairly straightforward to derive a class diagram from the object diagrams used in the storyboards.Note, the class diagram serves as a common reference for all object diagrams. This ensures that overall the same types and attributes are used. Using a UML tool, you may generate a first implementation from this class diagram.
Algorithm design: So far you have modeled and implemented that object structures that are deployed in your application. Now you need to add behavior, i.e. algorithms and method bodies. Programming the behavior of an application is a demanding task. To facilitate it, you should first outline the behavior in pseudocode notation. You might do this, e.g. with an object game. For example, to update the saldo attributes of all persons you look at our object structure and from the point of view of the GroupAccount object you do the following:
Update the saldo of all persons:
visit each item
for each item add the value to the total value and add 1 to the number of items
compute the average share of each person by dividing the total value by the number of persons
visit each person
for each person reset the saldo
for each person visit each item bought by this person
for each item add the value to the saldo of the current person
for each person subtract the share from the saldo
Behavior implementation: Once you have refined your algorithm pseudocode down to the level of operations on object structures it is straightforward to derive source code that executes the same operations on your object model implementation.
Testing: Finally, the scenarios may be used to derive automatic JUnit tests. The pseudocode for a test for our example might look like:
Test update the saldo of all persons:
create a group account object
add a person object with name Peter and a person object with name Putri and a person object with name Peng to the group account object
add an item object with buyer Peter, description Meat, and value $12 to the group account object
add an item object with buyer Putri, description Salad, and value $9 to the group account object
call method update the saldo of all persons on the group account object
ensure that the saldo of the Peter object is $5
ensure that the saldo of the Putri object is $2
ensure that the saldo of the Peter object is -$7
ensure that the sum of all saldos is $0
Start: This Sunday Peter, Putri, and Peng meet at the park for a go-Dutch barbecue. They use the Group Account app to do the accounting.
Step 1: Peter brings the meat for $12. Peter adds this item to the Group Account app.
Step 2: Putri brings salad for $9. Peter adds this item, too. The app shows that by now the average share is $7 and that Peng still have to bring these $7 while Peter gets $5 out and Putri gets $2 out.
Step 3: ...
Start: This Sunday Peter, Putri, and Peng meet at the park for a go-Dutch barbecue. They use the Group Account app to do the accounting.
Step 1: Peter brings the meat for $12. Peter adds this item to the Group Account app.
Step 2: Putri brings salad for $9. Peter adds this item, too. The app shows that by now the average share is $7 and that Peng still have to bring these $7 while Peter gets $5 out and Putri gets $2 out: 
Step 3: ...
Start: This Sunday Peter, Putri, and Peng meet at the park for a go-Dutch barbecue. They use the Group Account app to do the accounting.
Step 1: Peter brings the meat for $12. Peter adds this item to the Group Account app.
Step 2: Putri brings salad for $9. Peter adds this item, too. The app shows that by now the average share is $7 and that Peng still have to bring these $7 while Peter gets $5 out and Putri gets $2 out: 
Step 3: ...
visit each item
for each item add the value to the total value and add 1 to the number of items
compute the average share of each person by dividing the total value by the number of persons
visit each person
for each person reset the saldo
for each person visit each item bought by this person
for each item add the value to the saldo of the current person
for each person subtract the share from the saldo
for each item add the value to the total value and add 1 to the number of items
for each person reset the saldo
for each person visit each item bought by this person
for each item add the value to the saldo of the current person
for each person subtract the share from the saldo
for each item add the value to the saldo of the current person
create a group account object
add a person object with name Peter and a person object with name Putri and a person object with name Peng to the group account object
add an item object with buyer Peter, description Meat, and value $12 to the group account object
add an item object with buyer Putri, description Salad, and value $9 to the group account object
call method update the saldo of all persons on the group account object
ensure that the saldo of the Peter object is $5
ensure that the saldo of the Putri object is $2
ensure that the saldo of the Peter object is -$7
ensure that the sum of all saldos is $0
Story driven modeling has proven to work very well for the cooperation with non IT experts.[7] People from other domains usually have difficulties to describe their needs in general terms (i.e. classes) and general rules (pseudocode). Similarly, normal people have problems to understand pseudocode or to judge, whether their needs are properly addressed or not. However, these people know their business very well and with the help of concrete examples and scenarios it is very easy for normal people to spot problematic cases and to judge whether their needs have been addressed properly.

Story Driven Modeling has matured since its beginning in 1997. In 2013 it is used for teaching e.g. in Kassel University, Paderborn University, Tartu University, Antwerp University, Nazarbayev University Astana, Hasso Platner Institute Potsdam, University of Victoria, ...

Agile modeling
Entity-control-boundary
Agile software development
Class-responsibility-collaboration card
Object-oriented analysis and design
Object-oriented modeling
Test-driven development
Unified Modeling Language
Object-oriented programmingSoftware design
CS1: long volume valueArticles lacking in-text citations from February 2014All articles lacking in-text citationsWikipedia articles with style issues from February 2014All articles with style issuesArticles with multiple maintenance issues




