



From Wikipedia, the free encyclopedia


Restructuring existing computer code without changing its external behavior
"Refactoring" redirects here. For its use on Wikipedia, see [Wikipedia:Refactoring talk pages](/wiki/Wikipedia:Refactoring_talk_pages "Wikipedia:Refactoring talk pages").
This article is about a behaviour-preserving change. Not to be confused with [Rewrite (programming)](/wiki/Rewrite_(programming) "Rewrite (programming)").
In [computer programming](/wiki/Computer_programming "Computer programming") and [software design](/wiki/Software_design "Software design"), **code refactoring** is the process of restructuring existing [computer code](/wiki/Computer_code "Computer code")—changing the *[factoring](/wiki/Decomposition_(computer_science) "Decomposition (computer science)")*—without changing its external behavior. Refactoring is intended to improve the design, structure, and/or implementation of the [software](/wiki/Software "Software") (its *[non-functional](/wiki/Non-functional_requirement "Non-functional requirement")* attributes), while preserving its [functionality](/wiki/Functional_requirement "Functional requirement"). Potential advantages of refactoring may include improved code [readability](/wiki/Readability "Readability") and reduced [complexity](/wiki/Cyclomatic_complexity "Cyclomatic complexity"); these can improve the [source code](/wiki/Source_code "Source code")'s [maintainability](/wiki/Maintainability "Maintainability") and create a simpler, cleaner, or more expressive internal [architecture](/wiki/Software_architecture "Software architecture") or [object model](/wiki/Object_model "Object model") to improve [extensibility](/wiki/Extensibility "Extensibility"). Another potential goal for refactoring is improved performance; software engineers face an ongoing challenge to write programs that perform faster or use less memory.


Typically, refactoring applies a series of standardized basic *micro-refactorings*, each of which is (usually) a tiny change in a computer program's source code that either preserves the behavior of the software, or at least does not modify its conformance to functional requirements. Many [development environments](/wiki/Development_environment_(software_development_process) "Development environment (software development process)") provide automated support for performing the mechanical aspects of these basic refactorings. If done well, code refactoring may help software developers discover and fix hidden or dormant [bugs](/wiki/Software_bug "Software bug") or [vulnerabilities](/wiki/Vulnerability_(computing) "Vulnerability (computing)") in the system by simplifying the underlying logic and eliminating unnecessary levels of complexity. If done poorly, it may fail the requirement that external functionality not be changed, and may thus introduce new bugs.




> By continuously improving the design of code, we make it easier and easier to work with. This is in sharp contrast to what typically happens: little refactoring and a great deal of attention paid to expediently add new features. If you get into the hygienic habit of refactoring continuously, you'll find that it is easier to extend and maintain code.
> 
> — Joshua Kerievsky, *Refactoring to Patterns*[[1]](#cite_note-kerievsky-1)



Motivation[[edit](/w/index.php?title=Code_refactoring&action=edit&section=1 "Edit section: Motivation")]
--------------------------------------------------------------------------------------------------------


Refactoring is usually motivated by noticing a [code smell](/wiki/Code_smell "Code smell").[[2]](#cite_note-fowler-2) For example, the method at hand may be very long, or it may be a near [duplicate](/wiki/Duplicate_code "Duplicate code") of another nearby method. Once recognized, such problems can be addressed by *refactoring* the source code, or transforming it into a new form that behaves the same as before but that no longer "smells".


For a long routine, one or more smaller subroutines can be extracted; or for duplicate routines, the duplication can be removed and replaced with one shared function. Failure to perform refactoring can result in accumulating [technical debt](/wiki/Technical_debt "Technical debt"); on the other hand, refactoring is one of the primary means of repaying technical debt.[[3]](#cite_note-3)



Benefits[[edit](/w/index.php?title=Code_refactoring&action=edit&section=2 "Edit section: Benefits")]
----------------------------------------------------------------------------------------------------


There are two general categories of benefits to the activity of refactoring.



1. [Maintainability](/wiki/Maintainability "Maintainability"). It is easier to fix bugs because the source code is easy to read and the intent of its author is easy to grasp.[[4]](#cite_note-martin-4) This might be achieved by reducing large monolithic routines into a set of individually concise, well-named, single-purpose methods. It might be achieved by moving a method to a more appropriate class, or by removing misleading comments.
2. [Extensibility](/wiki/Extensibility "Extensibility"). It is easier to extend the capabilities of the application if it uses recognizable [design patterns](/wiki/Design_pattern_(computer_science) "Design pattern (computer science)"), and it provides some flexibility where none before may have existed.[[1]](#cite_note-kerievsky-1)


Performance engineering can remove inefficiencies in programs, known as software bloat, arising from traditional software-development strategies that aim to minimize an application's development time rather than the time it takes to run. Performance engineering can also tailor [software](/wiki/Software "Software") to the [hardware](/wiki/Hardware_security_module "Hardware security module") on which it runs, for example, to take advantage of parallel processors and vector units.[[5]](#cite_note-5)



Timing and responsibility[[edit](/w/index.php?title=Code_refactoring&action=edit&section=3 "Edit section: Timing and responsibility")]
--------------------------------------------------------------------------------------------------------------------------------------


There are two possible times for refactoring.



1. Preventive refactoring – the original developer of the code makes the code more robust when it is still free of [smells](/wiki/Code_smell "Code smell") to prevent the formation of smells in the future.[[6]](#cite_note-fraivert2022-6)
2. Corrective refactoring – a subsequent developer performs refactoring to correct [code smells](/wiki/Code_smell "Code smell") as they occur. [[6]](#cite_note-fraivert2022-6)


A method that balances preventive and corrective refactoring is "shared responsibility for refactoring".
This approach splits the refactoring action into two stages and two
roles. The original developer of the code just prepares the code for refactoring, and when the [code smells](/wiki/Code_smell "Code smell") form, a subsequent developer carries out the actual refactoring action. [[6]](#cite_note-fraivert2022-6)



Challenges[[edit](/w/index.php?title=Code_refactoring&action=edit&section=4 "Edit section: Challenges")]
--------------------------------------------------------------------------------------------------------


Refactoring requires extracting software system structure, data models, and intra-application dependencies to get back knowledge of an existing software system.[[7]](#cite_note-7)
The turnover of teams implies missing or inaccurate knowledge of the current state of a system and about design decisions made by departing developers. Further code refactoring activities may require additional effort to regain this knowledge.[[8]](#cite_note-8)
Refactoring activities generate architectural modifications that deteriorate the structural architecture of a software system. Such deterioration affects architectural properties such as maintainability and comprehensibility which can lead to a complete re-development of software systems.
[[9]](#cite_note-9)


Code refactoring activities are secured with [software intelligence](/wiki/Software_intelligence "Software intelligence") when using tools and techniques providing data about algorithms and sequences of code execution.[[10]](#cite_note-10) Providing a comprehensible format for the inner-state of software system structure, data models, and intra-components dependencies is a critical element to form a high-level understanding and then refined views of what needs to be modified, and how.[[11]](#cite_note-11)



Testing[[edit](/w/index.php?title=Code_refactoring&action=edit&section=5 "Edit section: Testing")]
--------------------------------------------------------------------------------------------------


Automatic [unit tests](/wiki/Unit_testing "Unit testing") should be set up before refactoring to ensure routines still behave as expected.[[12]](#cite_note-12) Unit tests can bring stability to even large refactors when performed with a single [atomic commit](/wiki/Atomic_commit#Revision_control "Atomic commit"). A common strategy to allow safe and atomic refactors spanning multiple projects is to store all projects in a single [repository](/wiki/Repository_(version_control) "Repository (version control)"), known as [monorepo](/wiki/Monorepo "Monorepo").[[13]](#cite_note-13)


With unit testing in place, refactoring is then an iterative cycle of making a small [program transformation](/wiki/Program_transformation "Program transformation"), testing it to ensure correctness, and making another small transformation. If at any point a test fails, the last small change is undone and repeated in a different way. Through many small steps the program moves from where it was to where you want it to be. For this very iterative process to be practical, the tests must run very quickly, or the programmer would have to spend a large fraction of their time waiting for the tests to finish. Proponents of [extreme programming](/wiki/Extreme_programming "Extreme programming") and other [agile software development](/wiki/Agile_software_development "Agile software development") describe this activity as an integral part of the [software development cycle](/wiki/Software_development_process "Software development process").



Techniques[[edit](/w/index.php?title=Code_refactoring&action=edit&section=6 "Edit section: Techniques")]
--------------------------------------------------------------------------------------------------------


Here are some examples of micro-refactorings; some of these may only apply to certain languages or language types. A longer list can be found in [Martin Fowler](/wiki/Martin_Fowler_(software_engineer) "Martin Fowler (software engineer)")'s refactoring book[[2]](#cite_note-fowler-2)[*[page needed](/wiki/Wikipedia:Citing_sources "Wikipedia:Citing sources")*] and website.[[14]](#cite_note-refactoring.com-14) Many development environments provide automated support for these micro-refactorings. For instance, a programmer could click on the name of a variable and then select the "Encapsulate field" refactoring from a [context menu](/wiki/Context_menu "Context menu"). The IDE would then prompt for additional details, typically with sensible defaults and a preview of the code changes. After confirmation by the programmer it would carry out the required changes throughout the code.



* Techniques that allow for more [understanding](/wiki/Application_discovery_and_understanding "Application discovery and understanding")
	+ [Program Dependence Graph](/wiki/Program_Dependence_Graph "Program Dependence Graph") - explicit representation of data and control dependencies [[15]](#cite_note-15)
	+ System Dependence Graph - representation of procedure calls between PDG [[16]](#cite_note-16)
	+ [Software intelligence](/wiki/Software_intelligence "Software intelligence") - reverse engineers the initial state to understand existing intra-application dependencies
* Techniques that allow for more [abstraction](/wiki/Abstraction_(computer_science) "Abstraction (computer science)")
	+ [Encapsulate field](/wiki/Field_encapsulation "Field encapsulation") – force code to access the field with getter and setter methods
	+ [Generalize type](/wiki/Type_generalization "Type generalization") – create more general types to allow for more code sharing
	+ Replace type-checking code with state/strategy[[17]](#cite_note-17)
	+ Replace conditional with [polymorphism](/wiki/Polymorphism_(computer_science) "Polymorphism (computer science)")[[18]](#cite_note-18)
* Techniques for breaking code apart into more logical pieces
	+ Componentization breaks code down into reusable semantic units that present clear, well-defined, simple-to-use interfaces.
	+ [Extract class](/wiki/Extract_class "Extract class") moves part of the code from an existing class into a new class.
	+ Extract method, to turn part of a larger [method](/wiki/Method_(computer_science) "Method (computer science)") into a new method. By breaking down code in smaller pieces, it is more easily understandable. This is also applicable to [functions](/wiki/Function_(programming) "Function (programming)").
* Techniques for improving names and location of code
	+ Move method or move field – move to a more appropriate [class](/wiki/Class_(computer_science) "Class (computer science)") or source file
	+ Rename method or rename field – changing the name into a new one that better reveals its purpose
	+ Pull up – in [object-oriented programming](/wiki/Object-oriented_programming "Object-oriented programming") (OOP), move to a [superclass](/wiki/Superclass_(computer_science) "Superclass (computer science)")
	+ Push down – in OOP, move to a [subclass](/wiki/Subclass_(computer_science) "Subclass (computer science)")[[14]](#cite_note-refactoring.com-14)
* Automatic [clone detection](/wiki/Clone_detection "Clone detection")[[19]](#cite_note-19)


Hardware refactoring[[edit](/w/index.php?title=Code_refactoring&action=edit&section=7 "Edit section: Hardware refactoring")]
----------------------------------------------------------------------------------------------------------------------------


While the term *refactoring* originally referred exclusively to refactoring of software code, in recent years code written in [hardware description languages](/wiki/Hardware_description_language "Hardware description language") has also been refactored. The term *hardware refactoring* is used as a shorthand term for refactoring of code in hardware description languages. Since hardware description languages are not considered to be [programming languages](/wiki/Programming_language "Programming language") by most hardware engineers,[[20]](#cite_note-20) hardware refactoring is to be considered a separate field from traditional code refactoring.


Automated refactoring of analog hardware descriptions (in [VHDL-AMS](/wiki/VHDL-AMS "VHDL-AMS")) has been proposed by Zeng and Huss.[[21]](#cite_note-21) In their approach, refactoring preserves the simulated behavior of a hardware design. The non-functional measurement that improves is that refactored code can be processed by standard synthesis tools, while the original code cannot. Refactoring of digital hardware description languages, albeit manual refactoring, has also been investigated by [Synopsys](/wiki/Synopsys "Synopsys") [fellow](/wiki/Fellow "Fellow") Mike Keating.[[22]](#cite_note-22)[[23]](#cite_note-23) His target is to make complex systems easier to understand, which increases the designers' productivity.



History[[edit](/w/index.php?title=Code_refactoring&action=edit&section=8 "Edit section: History")]
--------------------------------------------------------------------------------------------------


The first known use of the term "refactoring" in the published literature was in a September, 1990 article by [William Opdyke](/wiki/William_Opdyke "William Opdyke") and [Ralph Johnson](/wiki/Ralph_Johnson_(computer_scientist) "Ralph Johnson (computer scientist)").[[24]](#cite_note-opdyke90-24)
Although refactoring code has been done informally for decades, [William Griswold](/wiki/Bill_Griswold "Bill Griswold")'s 1991 Ph.D. dissertation[[25]](#cite_note-griswold-thesis-25)
is one of the first major academic works on refactoring functional and procedural programs, followed by [William Opdyke](/wiki/William_Opdyke "William Opdyke")'s 1992 dissertation[[26]](#cite_note-opdyke-thesis-26)
on the refactoring of object-oriented programs,[[27]](#cite_note-etymology-27) although all the theory and machinery have long been available as [program transformation](/wiki/Program_transformation "Program transformation") systems. All of these resources provide a catalog of common methods for refactoring; a refactoring method has a description of how to apply the [method](/wiki/Scientific_method "Scientific method") and indicators for when you should (or should not) apply the method.


[Martin Fowler](/wiki/Martin_Fowler_(software_engineer) "Martin Fowler (software engineer)")'s book *Refactoring: Improving the Design of Existing Code* is the canonical reference. [*[according to whom?](/wiki/Wikipedia:Manual_of_Style/Words_to_watch#Unsupported_attributions "Wikipedia:Manual of Style/Words to watch")*]


The terms "factoring" and "factoring out" have been used in this way in the [Forth](/wiki/Forth_(programming_language) "Forth (programming language)") community since at least the early 1980s. Chapter Six of [Leo Brodie](/w/index.php?title=Leo_Brodie_(programmer)&action=edit&redlink=1 "Leo Brodie (programmer) (page does not exist)")'s book *[Thinking Forth](/w/index.php?title=Thinking_Forth&action=edit&redlink=1 "Thinking Forth (page does not exist)")* (1984)[[28]](#cite_note-28) is dedicated to the subject.


In extreme programming, the Extract Method refactoring technique has essentially the same meaning as factoring in Forth; to break down a "word" (or [function](/wiki/Function_(programming) "Function (programming)")) into smaller, more easily maintained functions.


Refactorings can also be reconstructed[[29]](#cite_note-What-is-code-refactoring?-29) posthoc to produce concise descriptions of complex software changes recorded in software repositories like CVS or SVN.



Automated code refactoring[[edit](/w/index.php?title=Code_refactoring&action=edit&section=9 "Edit section: Automated code refactoring")]
----------------------------------------------------------------------------------------------------------------------------------------




|  | This section **needs additional citations for [verification](/wiki/Wikipedia:Verifiability "Wikipedia:Verifiability")**. Please help [improve this article](/wiki/Special:EditPage/Code_refactoring "Special:EditPage/Code refactoring") by [adding citations to reliable sources](/wiki/Help:Referencing_for_beginners "Help:Referencing for beginners") in this section. Unsourced material may be challenged and removed.*Find sources:* ["Code refactoring"](https://www.google.com/search?as_eq=wikipedia&q=%22Code+refactoring%22) – [news](https://www.google.com/search?tbm=nws&q=%22Code+refactoring%22+-wikipedia&tbs=ar:1) **·** [newspapers](https://www.google.com/search?&q=%22Code+refactoring%22&tbs=bkt:s&tbm=bks) **·** [books](https://www.google.com/search?tbs=bks:1&q=%22Code+refactoring%22+-wikipedia) **·** [scholar](https://scholar.google.com/scholar?q=%22Code+refactoring%22) **·** [JSTOR](https://www.jstor.org/action/doBasicSearch?Query=%22Code+refactoring%22&acc=on&wc=on) *(July 2018)* *([Learn how and when to remove this message](/wiki/Help:Maintenance_template_removal "Help:Maintenance template removal"))* |
| --- | --- |


Many software [editors](/wiki/Text_editor "Text editor") and [IDEs](/wiki/Integrated_development_environment "Integrated development environment") have automated refactoring support. Here is a list of a few of these editors, or so-called [refactoring browsers](/wiki/Refactoring_Browser "Refactoring Browser").



* [DMS Software Reengineering Toolkit](/wiki/DMS_Software_Reengineering_Toolkit "DMS Software Reengineering Toolkit") (Implements large-scale refactoring for C, C++, C#, COBOL, Java, PHP and other languages)
* Eclipse based:
	+ [Eclipse](/wiki/Eclipse_(software) "Eclipse (software)") (for [Java](/wiki/Java_(programming_language) "Java (programming language)"), and to a lesser extent, C++, PHP, Ruby and JavaScript)
	+ [PyDev](/wiki/PyDev "PyDev") (for [Python](/wiki/Python_(programming_language) "Python (programming language)"))
	+ [Photran](/w/index.php?title=Photran&action=edit&redlink=1 "Photran (page does not exist)") (a [Fortran](/wiki/Fortran "Fortran") plugin for the [Eclipse IDE](/wiki/Eclipse_(software) "Eclipse (software)"))
* [Embarcadero Delphi](/wiki/Embarcadero_Delphi "Embarcadero Delphi")
* IntelliJ based:
	+ [Resharper](/w/index.php?title=Resharper&action=edit&redlink=1 "Resharper (page does not exist)") (for [C#](/wiki/C_Sharp_(programming_language) "C Sharp (programming language)"))
	+ [AppCode](/wiki/AppCode "AppCode") (for [Objective-C](/wiki/Objective-C "Objective-C"), C and C++)
	+ [IntelliJ IDEA](/wiki/IntelliJ_IDEA "IntelliJ IDEA") (for [Java](/wiki/Java_(programming_language) "Java (programming language)"))
	+ [PyCharm](/wiki/PyCharm "PyCharm") (for [Python](/wiki/Python_(programming_language) "Python (programming language)"))
	+ [WebStorm](/wiki/WebStorm "WebStorm") (for [JavaScript](/wiki/JavaScript "JavaScript"))
	+ [PhpStorm](/wiki/PhpStorm "PhpStorm") (for [PHP](/wiki/PHP "PHP"))
	+ [Android Studio](/wiki/Android_Studio "Android Studio") (for [Java](/wiki/Java_(programming_language) "Java (programming language)") and C++)
* [JDeveloper](/wiki/JDeveloper "JDeveloper") (for [Java](/wiki/Java_(programming_language) "Java (programming language)"))
* [NetBeans](/wiki/NetBeans "NetBeans") (for [Java](/wiki/Java_(programming_language) "Java (programming language)"))
* [Smalltalk](/wiki/Smalltalk "Smalltalk"): Most dialects include powerful refactoring tools. Many use the original refactoring browser produced in the early '90s by [Ralph Johnson](/wiki/Ralph_Johnson_(computer_scientist) "Ralph Johnson (computer scientist)").
* Visual Studio based:
	+ [Visual Studio](/wiki/Visual_Studio "Visual Studio") (for .NET and C++)
	+ [Visual Assist](/wiki/Visual_Assist "Visual Assist") (addon for Visual Studio with refactoring support for C# and C++)
* [Wing IDE](/wiki/Wing_IDE "Wing IDE") (for [Python](/wiki/Python_(programming_language) "Python (programming language)"))
* [Xcode](/wiki/Xcode "Xcode") (for C, [Objective-C](/wiki/Objective-C "Objective-C"), and [Swift](/wiki/Swift_(programming_language) "Swift (programming language)"))[[30]](#cite_note-30)
* [Qt Creator](/wiki/Qt_Creator "Qt Creator") (for C++, Objective-C and QML)[[31]](#cite_note-31)


See also[[edit](/w/index.php?title=Code_refactoring&action=edit&section=10 "Edit section: See also")]
-----------------------------------------------------------------------------------------------------


* [Amelioration pattern](/wiki/Amelioration_pattern "Amelioration pattern")
* [Code review](/wiki/Code_review "Code review")
* [Database refactoring](/wiki/Database_refactoring "Database refactoring")
* [Decomposition (computer science)](/wiki/Decomposition_(computer_science) "Decomposition (computer science)")
* [Modular programming](/wiki/Modular_programming "Modular programming")
* [Obfuscated code](/wiki/Obfuscated_code "Obfuscated code")
* [Prefactoring](/wiki/Prefactoring "Prefactoring")
* [Rewrite (programming)](/wiki/Rewrite_(programming) "Rewrite (programming)")
* [Separation of concerns](/wiki/Separation_of_concerns "Separation of concerns")
* [Software peer review](/wiki/Software_peer_review "Software peer review")
* [Test-driven development](/wiki/Test-driven_development "Test-driven development")


References[[edit](/w/index.php?title=Code_refactoring&action=edit&section=11 "Edit section: References")]
---------------------------------------------------------------------------------------------------------



1. ^ [***a***](#cite_ref-kerievsky_1-0) [***b***](#cite_ref-kerievsky_1-1) Kerievsky, Joshua (2004). *Refactoring to Patterns*. Addison Wesley.
2. ^ [***a***](#cite_ref-fowler_2-0) [***b***](#cite_ref-fowler_2-1) [Fowler, Martin](/wiki/Martin_Fowler_(software_engineer) "Martin Fowler (software engineer)") (1999). [*Refactoring. Improving the Design of Existing Code*](https://archive.org/details/isbn_9780201485677/page/63). Addison-Wesley. pp. [63ff](https://archive.org/details/isbn_9780201485677/page/63). [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-0-201-48567-7](/wiki/Special:BookSources/978-0-201-48567-7 "Special:BookSources/978-0-201-48567-7").
3. **[^](#cite_ref-3)** Suryanarayana, Girish (November 2014). *Refactoring for Software Design Smells*. Morgan Kaufmann. p. 258. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-0128013977](/wiki/Special:BookSources/978-0128013977 "Special:BookSources/978-0128013977").
4. **[^](#cite_ref-martin_4-0)** Martin, Robert (2009). *Clean Code*. Prentice Hall.
5. **[^](#cite_ref-5)** Leiserson, Charles E.; Thompson, Neil C.; Emer, Joel S.; Kuszmaul, Bradley C.; Lampson, Butler W.; Sanchez, Daniel; Schardl, Tao B. (2020). ["There's plenty of room at the Top: What will drive computer performance after Moore's law?"](https://doi.org/10.1126%2Fscience.aam9744). *Science*. **368** (6495): eaam9744. [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.1126/science.aam9744](https://doi.org/10.1126%2Fscience.aam9744). [PMID](/wiki/PMID_(identifier) "PMID (identifier)") [32499413](https://pubmed.ncbi.nlm.nih.gov/32499413).
6. ^ [***a***](#cite_ref-fraivert2022_6-0) [***b***](#cite_ref-fraivert2022_6-1) [***c***](#cite_ref-fraivert2022_6-2) 
Fraivert, Dov; Lorenz, David H. (2022). "Language Support for Refactorability Decay Prevention". *Proceedings of the 21st ACM SIGPLAN International Conference on Generative Programming: Concepts and Experiences*: 122–134. [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.1145/3564719.3568688](https://doi.org/10.1145%2F3564719.3568688).
7. **[^](#cite_ref-7)** 
Haendler, Thorsten; Neumann, Gustaf (2019). "A Framework for the Assessment and Training of Software Refactoring Competences". *Proceedings of the 11th International Joint Conference on Knowledge Discovery, Knowledge Engineering and Knowledge Management*. pp. 307–316. [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.5220/0008350803070316](https://doi.org/10.5220%2F0008350803070316). [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-989-758-382-7](/wiki/Special:BookSources/978-989-758-382-7 "Special:BookSources/978-989-758-382-7"). [S2CID](/wiki/S2CID_(identifier) "S2CID (identifier)") [204754665](https://api.semanticscholar.org/CorpusID:204754665).
8. **[^](#cite_ref-8)** 
Nassif, Matthieu; Robillard, Martin P. (November 2017). "Revisiting Turnover-Induced Knowledge Loss in Software Projects". *2017 IEEE International Conference on Software Maintenance and Evolution (ICSME)*. pp. 261–272. [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.1109/ICSME.2017.64](https://doi.org/10.1109%2FICSME.2017.64). [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-1-5386-0992-7](/wiki/Special:BookSources/978-1-5386-0992-7 "Special:BookSources/978-1-5386-0992-7"). [S2CID](/wiki/S2CID_(identifier) "S2CID (identifier)") [13147063](https://api.semanticscholar.org/CorpusID:13147063).
9. **[^](#cite_ref-9)** 
van Gurp, Jilles; Bosch, Jan (March 2002). "Design erosion: problems and causes". *Journal of Systems and Software*. **61** (2): 105–119. [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.1016/S0164-1212(01)00152-2](https://doi.org/10.1016%2FS0164-1212%2801%2900152-2).
10. **[^](#cite_ref-10)** 
Hassan, Ahmed E.; Xie, Tao (November 2010). "Software intelligence: the future of mining software engineering data". *In Proceedings of the FSE/SDP Workshop on Future of Software Engineering Research (FoSER '10)*: 161–166. [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.1145/1882362.1882397](https://doi.org/10.1145%2F1882362.1882397). [S2CID](/wiki/S2CID_(identifier) "S2CID (identifier)") [3485526](https://api.semanticscholar.org/CorpusID:3485526).
11. **[^](#cite_ref-11)** 
Novais, Renato; Santos, José Amancio; Mendonça, Manoel (2017). "Experimentally assessing the combination of multiple visualization strategies for software evolution analysis". *Journal of Systems and Software*. **128**: 56–71. [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.1016/j.jss.2017.03.006](https://doi.org/10.1016%2Fj.jss.2017.03.006).
12. **[^](#cite_ref-12)** Fowler, Martin (1999). [*Refactoring : improving the design of existing code*](https://archive.org/details/isbn_9780201485677). Reading, MA: Addison-Wesley. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-0201485677](/wiki/Special:BookSources/978-0201485677 "Special:BookSources/978-0201485677"). [OCLC](/wiki/OCLC_(identifier) "OCLC (identifier)") [41017370](https://www.worldcat.org/oclc/41017370).
13. **[^](#cite_ref-13)** Smart, John Ferguson (2008). [*Java Power Tools*](https://books.google.com/books?id=kE0UDQAAQBAJ&q=visual+sourcesafe+atomic+commit&pg=PA301). "O'Reilly Media, Inc.". p. 301. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [9781491954546](/wiki/Special:BookSources/9781491954546 "Special:BookSources/9781491954546"). Retrieved 26 July 2018.
14. ^ [***a***](#cite_ref-refactoring.com_14-0) [***b***](#cite_ref-refactoring.com_14-1) (these are only about OOP however).[Refactoring techniques in Fowler's refactoring Website](http://refactoring.com/catalog/index.html)
15. **[^](#cite_ref-15)** 
Ferrante, Jeanne; Ottenstein, Karl J.; Warren, Joe D. (July 1987). ["The program dependence graph and its use in optimization"](https://doi.org/10.1145%2F24039.24041). *ACM Transactions on Programming Languages and Systems*. **9** (3). ACM: 319–349. [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.1145/24039.24041](https://doi.org/10.1145%2F24039.24041). [S2CID](/wiki/S2CID_(identifier) "S2CID (identifier)") [505075](https://api.semanticscholar.org/CorpusID:505075).
16. **[^](#cite_ref-16)** 
Donglin, Linag; Harrold, M. J. (November 2008). "Slicing objects using system dependence graphs". *Proceedings. International Conference on Software Maintenance (Cat. No. 98CB36272)*. IEEE. pp. 319–349. [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.1109/ICSM.1998.738527](https://doi.org/10.1109%2FICSM.1998.738527). [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-0-8186-8779-2](/wiki/Special:BookSources/978-0-8186-8779-2 "Special:BookSources/978-0-8186-8779-2"). [S2CID](/wiki/S2CID_(identifier) "S2CID (identifier)") [18160599](https://api.semanticscholar.org/CorpusID:18160599).
17. **[^](#cite_ref-17)** ["Replace type-checking code with State/Strategy"](http://refactoring.com/catalog/replaceTypeCodeWithStateStrategy.html).
18. **[^](#cite_ref-18)** ["Replace conditional with polymorphism"](http://refactoring.com/catalog/replaceConditionalWithPolymorphism.html).
19. **[^](#cite_ref-19)** Bruntink, Magiel, et al. "[An evaluation of clone detection techniques for crosscutting concerns](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.57.9709&rep=rep1&type=pdf)." Software Maintenance, 2004. Proceedings. 20th IEEE International Conference on. IEEE, 2004.
20. **[^](#cite_ref-20)** [Hardware description languages#HDL and programming languages](/wiki/Hardware_description_languages#HDL_and_programming_languages "Hardware description languages")
21. **[^](#cite_ref-21)** Kaiping Zeng, Sorin A. Huss, "Architecture refinements by code refactoring of behavioral VHDL-AMS models". ISCAS 2006
22. **[^](#cite_ref-22)** M. Keating :"Complexity, Abstraction, and the Challenges of Designing Complex Systems", in DAC'08 tutorial [[1]](http://www.dac.com/events/eventdetails.aspx?id=77-130) [Archived](https://web.archive.org/web/20160328163412/https://dac.com/events/eventdetails.aspx?id=77-130) 2016-03-28 at the [Wayback Machine](/wiki/Wayback_Machine "Wayback Machine")"Bridging a Verification Gap: C++ to RTL for Practical Design"
23. **[^](#cite_ref-23)** M. Keating, P. Bricaud: *Reuse Methodology Manual for System-on-a-Chip Designs*, Kluwer Academic Publishers, 1999.
24. **[^](#cite_ref-opdyke90_24-0)** [Opdyke, William F.](/wiki/William_Opdyke "William Opdyke"); Johnson, Ralph E. (September 1990). "Refactoring: An Aid in Designing Application Frameworks and Evolving Object-Oriented Systems". *Proceedings of the Symposium on Object Oriented Programming Emphasizing Practical Applications (SOOPPA)*. ACM.
25. **[^](#cite_ref-griswold-thesis_25-0)** [Griswold, William G](/wiki/Bill_Griswold "Bill Griswold") (July 1991). [*Program Restructuring as an Aid to Software Maintenance*](http://cseweb.ucsd.edu/~wgg/Abstracts/gristhesis.pdf) (PDF) (Ph.D. thesis). University of Washington. Retrieved 2011-12-24.
26. **[^](#cite_ref-opdyke-thesis_26-0)** [Opdyke, William F](/wiki/William_Opdyke "William Opdyke") (June 1992). [*Refactoring Object-Oriented Frameworks*](https://web.archive.org/web/20191216212919/https://dl.acm.org/citation.cfm?id=169783) (Ph.D. thesis). University of Illinois at Urbana-Champaign. Archived from the original on 2019-12-16. Retrieved 2008-02-12.`{{[cite thesis](/wiki/Template:Cite_thesis "Template:Cite thesis")}}`: CS1 maint: bot: original URL status unknown ([link](/wiki/Category:CS1_maint:_bot:_original_URL_status_unknown "Category:CS1 maint: bot: original URL status unknown"))
27. **[^](#cite_ref-etymology_27-0)** ["Martin Fowler, "MF Bliki: EtymologyOfRefactoring""](http://martinfowler.com/bliki/EtymologyOfRefactoring.html).
28. **[^](#cite_ref-28)** Brodie, Leo (2004). [*Thinking Forth*](https://web.archive.org/web/20051216163615/http://thinking-forth.sourceforge.net/). Fig Leaf Press, Forth Interest. pp. 171–196. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [0-9764587-0-5](/wiki/Special:BookSources/0-9764587-0-5 "Special:BookSources/0-9764587-0-5"). Archived from [the original](http://thinking-forth.sourceforge.net) on 16 December 2005. Retrieved 3 May 2020.
29. **[^](#cite_ref-What-is-code-refactoring?_29-0)** Sokolov, Andriy. ["What is code refactoring?"](https://duecode.io/blog/what-is-code-refactoring/).
30. **[^](#cite_ref-30)** ["What's new in Xcode 9"](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/WhatsNewXcode/xcode_9/xcode_9.html).
31. **[^](#cite_ref-31)** ["Refactoring in Qt Creator"](https://doc.qt.io/qtcreator/creator-editor-refactoring.html).

Further reading[[edit](/w/index.php?title=Code_refactoring&action=edit&section=12 "Edit section: Further reading")]
-------------------------------------------------------------------------------------------------------------------


* Wake, William C. (2003). *Refactoring Workbook*. Addison-Wesley. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-0-321-10929-3](/wiki/Special:BookSources/978-0-321-10929-3 "Special:BookSources/978-0-321-10929-3").
* Mens, T.; Tourwe, T. (February 2004). ["A survey of software refactoring"](https://zenodo.org/record/848931). *IEEE Transactions on Software Engineering*. **30** (2): 126–139. [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.1109/tse.2004.1265817](https://doi.org/10.1109%2Ftse.2004.1265817). [ISSN](/wiki/ISSN_(identifier) "ISSN (identifier)") [0098-5589](https://www.worldcat.org/issn/0098-5589). [S2CID](/wiki/S2CID_(identifier) "S2CID (identifier)") [206778272](https://api.semanticscholar.org/CorpusID:206778272).
* Feathers, Michael C (2004). *Working Effectively with Legacy Code*. Prentice Hall. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-0-13-117705-5](/wiki/Special:BookSources/978-0-13-117705-5 "Special:BookSources/978-0-13-117705-5").
* Kerievsky, Joshua (2004). *Refactoring To Patterns*. Addison-Wesley. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-0-321-21335-8](/wiki/Special:BookSources/978-0-321-21335-8 "Special:BookSources/978-0-321-21335-8").
* Arsenovski, Danijel (2008). *Professional Refactoring in Visual Basic*. Wrox. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-0-470-17979-6](/wiki/Special:BookSources/978-0-470-17979-6 "Special:BookSources/978-0-470-17979-6").
* Arsenovski, Danijel (2009). *Professional Refactoring in C# and ASP.NET*. Wrox. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-0-470-43452-9](/wiki/Special:BookSources/978-0-470-43452-9 "Special:BookSources/978-0-470-43452-9").
* Ritchie, Peter (2010). *Refactoring with Visual Studio 2010*. Packt. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-1-84968-010-3](/wiki/Special:BookSources/978-1-84968-010-3 "Special:BookSources/978-1-84968-010-3").


External links[[edit](/w/index.php?title=Code_refactoring&action=edit&section=13 "Edit section: External links")]
-----------------------------------------------------------------------------------------------------------------


* [What Is Refactoring?](http://c2.com/cgi/wiki?WhatIsRefactoring) (c2.com article)
* [Martin Fowler's homepage about refactoring](http://refactoring.com/)
* [Refactoring](https://curlie.org/Computers/Programming/Methodologies/Refactoring) at [Curlie](/wiki/Curlie "Curlie")




| [Authority control databases](/wiki/Help:Authority_control "Help:Authority control") [Edit this at Wikidata](https://www.wikidata.org/wiki/Q116877#identifiers "Edit this at Wikidata") | |
| --- | --- |
| International | * [FAST](http://id.worldcat.org/fast/1124216/) |
| National | * [Germany](https://d-nb.info/gnd/4784343-3) * [Israel](http://olduli.nli.org.il/F/?func=find-b&local_base=NLX10&find_code=UID&request=987007566125005171) * [United States](https://id.loc.gov/authorities/sh99002049) * [Japan](https://id.ndl.go.jp/auth/ndlna/01191220) * [Czech Republic](https://aleph.nkp.cz/F/?func=find-c&local_base=aut&ccl_term=ica=ph198771&CON_LNG=ENG) |





![](https://login.wikimedia.org/wiki/Special:CentralAutoLogin/start?type=1x1)
Retrieved from "<https://en.wikipedia.org/w/index.php?title=Code_refactoring&oldid=1227963239>"
[Categories](/wiki/Help:Category "Help:Category"): * [Code refactoring](/wiki/Category:Code_refactoring "Category:Code refactoring")
* [Extreme programming](/wiki/Category:Extreme_programming "Category:Extreme programming")
* [Technology neologisms](/wiki/Category:Technology_neologisms "Category:Technology neologisms")
Hidden categories: * [Webarchive template wayback links](/wiki/Category:Webarchive_template_wayback_links "Category:Webarchive template wayback links")
* [CS1 maint: bot: original URL status unknown](/wiki/Category:CS1_maint:_bot:_original_URL_status_unknown "Category:CS1 maint: bot: original URL status unknown")
* [Articles with short description](/wiki/Category:Articles_with_short_description "Category:Articles with short description")
* [Short description is different from Wikidata](/wiki/Category:Short_description_is_different_from_Wikidata "Category:Short description is different from Wikidata")
* [Wikipedia articles needing page number citations from July 2018](/wiki/Category:Wikipedia_articles_needing_page_number_citations_from_July_2018 "Category:Wikipedia articles needing page number citations from July 2018")
* [All articles with specifically marked weasel-worded phrases](/wiki/Category:All_articles_with_specifically_marked_weasel-worded_phrases "Category:All articles with specifically marked weasel-worded phrases")
* [Articles with specifically marked weasel-worded phrases from July 2018](/wiki/Category:Articles_with_specifically_marked_weasel-worded_phrases_from_July_2018 "Category:Articles with specifically marked weasel-worded phrases from July 2018")
* [Articles needing additional references from July 2018](/wiki/Category:Articles_needing_additional_references_from_July_2018 "Category:Articles needing additional references from July 2018")
* [All articles needing additional references](/wiki/Category:All_articles_needing_additional_references "Category:All articles needing additional references")
* [Articles with Curlie links](/wiki/Category:Articles_with_Curlie_links "Category:Articles with Curlie links")
* [Articles with FAST identifiers](/wiki/Category:Articles_with_FAST_identifiers "Category:Articles with FAST identifiers")
* [Articles with GND identifiers](/wiki/Category:Articles_with_GND_identifiers "Category:Articles with GND identifiers")
* [Articles with J9U identifiers](/wiki/Category:Articles_with_J9U_identifiers "Category:Articles with J9U identifiers")
* [Articles with LCCN identifiers](/wiki/Category:Articles_with_LCCN_identifiers "Category:Articles with LCCN identifiers")
* [Articles with NDL identifiers](/wiki/Category:Articles_with_NDL_identifiers "Category:Articles with NDL identifiers")
* [Articles with NKC identifiers](/wiki/Category:Articles_with_NKC_identifiers "Category:Articles with NKC identifiers")

