


(Top)





1
Motivation








2
Benefits








3
Timing and responsibility








4
Challenges








5
Testing








6
Techniques








7
Hardware refactoring








8
History








9
Automated code refactoring








10
See also








11
References








12
Further reading








13
External links
































In computer programming and software design, code refactoring is the process of restructuring existing source code—changing the factoring—without changing its external behavior. Refactoring is intended to improve the design, structure, and/or implementation of the software (its non-functional attributes), while preserving its functionality. Potential advantages of refactoring may include improved code readability and reduced complexity; these can improve the source code's maintainability and create a simpler, cleaner, or more expressive internal architecture or object model to improve extensibility. Another potential goal for refactoring is improved performance; software engineers face an ongoing challenge to write programs that perform faster or use less memory.

Typically, refactoring applies a series of standardized basic micro-refactorings, each of which is (usually) a tiny change in a computer program's source code that either preserves the behavior of the software, or at least does not modify its conformance to functional requirements. Many development environments provide automated support for performing the mechanical aspects of these basic refactorings. If done well, code refactoring may help software developers discover and fix hidden or dormant bugs or vulnerabilities in the system by simplifying the underlying logic and eliminating unnecessary levels of complexity. If done poorly, it may fail the requirement that external functionality not be changed, and may thus introduce new bugs.

By continuously improving the design of code, we make it easier and easier to work with. This is in sharp contrast to what typically happens: little refactoring and a great deal of attention paid to expediently add new features. If you get into the hygienic habit of refactoring continuously, you'll find that it is easier to extend and maintain code.
Refactoring is usually motivated by noticing a code smell.[2] For example, the method at hand may be very long, or it may be a near duplicate of another nearby method. Once recognized, such problems can be addressed by refactoring the source code, or transforming it into a new form that behaves the same as before but that no longer "smells".

For a long routine, one or more smaller subroutines can be extracted; or for duplicate routines, the duplication can be removed and replaced with one shared function. Failure to perform refactoring can result in accumulating technical debt; on the other hand, refactoring is one of the primary means of repaying technical debt.[3]

There are two general categories of benefits to the activity of refactoring.

Maintainability. It is easier to fix bugs because the source code is easy to read and the intent of its author is easy to grasp.[4] This might be achieved by reducing large monolithic routines into a set of individually concise, well-named, single-purpose methods. It might be achieved by moving a method to a more appropriate class, or by removing misleading comments.
Extensibility. It is easier to extend the capabilities of the application if it uses recognizable design patterns, and it provides some flexibility where none before may have existed.[1]
Performance engineering can remove inefficiencies in programs, known as software bloat, arising from traditional software-development strategies that aim to minimize an application's development time rather than the time it takes to run. Performance engineering can also tailor software to the hardware on which it runs, for example, to take advantage of parallel processors and vector units.[5]

There are two possible times for refactoring.

Preventive refactoring – the original developer of the code makes the code more robust when it is still free of smells to prevent the formation of smells in the future.[6]
Corrective refactoring – a subsequent developer performs refactoring to correct code smells as they occur. [6]
A method that balances preventive and corrective refactoring is "shared responsibility for refactoring".
This approach splits the refactoring action into two stages and two
roles. The original developer of the code just prepares the code for refactoring, and when the code smells form, a subsequent developer carries out the actual refactoring action. [6]

Refactoring requires extracting software system structure, data models, and intra-application dependencies to get back knowledge of an existing software system.[7]
The turnover of teams implies missing or inaccurate knowledge of the current state of a system and about design decisions made by departing developers. Further code refactoring activities may require additional effort to regain this knowledge.[8]
Refactoring activities generate architectural modifications that deteriorate the structural architecture of a software system. Such deterioration affects architectural properties such as maintainability and comprehensibility which can lead to a complete re-development of software systems.
[9]

Code refactoring activities are secured with software intelligence when using tools and techniques providing data about algorithms and sequences of code execution.[10] Providing a comprehensible format for the inner-state of software system structure, data models, and intra-components dependencies is a critical element to form a high-level understanding and then refined views of what needs to be modified, and how.[11]

Automatic unit tests should be set up before refactoring to ensure routines still behave as expected.[12] Unit tests can bring stability to even large refactors when performed with a single atomic commit. A common strategy to allow safe and atomic refactors spanning multiple projects is to store all projects in a single repository, known as monorepo.[13]

With unit testing in place, refactoring is then an iterative cycle of making a small program transformation, testing it to ensure correctness, and making another small transformation. If at any point a test fails, the last small change is undone and repeated in a different way. Through many small steps the program moves from where it was to where you want it to be. For this very iterative process to be practical, the tests must run very quickly, or the programmer would have to spend a large fraction of their time waiting for the tests to finish. Proponents of extreme programming and other agile software development describe this activity as an integral part of the software development cycle.

Here are some examples of micro-refactorings; some of these may only apply to certain languages or language types. A longer list can be found in Martin Fowler's refactoring book[2][page needed] and website.[14] Many development environments provide automated support for these micro-refactorings. For instance, a programmer could click on the name of a variable and then select the "Encapsulate field" refactoring from a context menu. The IDE would then prompt for additional details, typically with sensible defaults and a preview of the code changes. After confirmation by the programmer it would carry out the required changes throughout the code.

Techniques that allow for more understanding
Program Dependence Graph - explicit representation of data and control dependencies [15]
System Dependence Graph - representation of procedure calls between PDG [16]
Software intelligence - reverse engineers the initial state to understand existing intra-application dependencies
Techniques that allow for more abstraction
Encapsulate field – force code to access the field with getter and setter methods
Generalize type – create more general types to allow for more code sharing
Replace type-checking code with state/strategy[17]
Replace conditional with polymorphism[18]
Techniques for breaking code apart into more logical pieces
Componentization breaks code down into reusable semantic units that present clear, well-defined, simple-to-use interfaces.
Extract class moves part of the code from an existing class into a new class.
Extract method, to turn part of a larger method into a new method. By breaking down code in smaller pieces, it is more easily understandable. This is also applicable to functions.
Techniques for improving names and location of code
Move method or move field – move to a more appropriate class or source file
Rename method or rename field – changing the name into a new one that better reveals its purpose
Pull up – in object-oriented programming (OOP), move to a superclass
Push down – in OOP, move to a subclass[14]
Automatic clone detection[19]
Program Dependence Graph - explicit representation of data and control dependencies [15]
System Dependence Graph - representation of procedure calls between PDG [16]
Software intelligence - reverse engineers the initial state to understand existing intra-application dependencies
Encapsulate field – force code to access the field with getter and setter methods
Generalize type – create more general types to allow for more code sharing
Replace type-checking code with state/strategy[17]
Replace conditional with polymorphism[18]
Componentization breaks code down into reusable semantic units that present clear, well-defined, simple-to-use interfaces.
Extract class moves part of the code from an existing class into a new class.
Extract method, to turn part of a larger method into a new method. By breaking down code in smaller pieces, it is more easily understandable. This is also applicable to functions.
Move method or move field – move to a more appropriate class or source file
Rename method or rename field – changing the name into a new one that better reveals its purpose
Pull up – in object-oriented programming (OOP), move to a superclass
Push down – in OOP, move to a subclass[14]
While the term refactoring originally referred exclusively to refactoring of software code, in recent years code written in hardware description languages has also been refactored. The term hardware refactoring is used as a shorthand term for refactoring of code in hardware description languages. Since hardware description languages are not considered to be programming languages by most hardware engineers,[20] hardware refactoring is to be considered a separate field from traditional code refactoring.

Automated refactoring of analog hardware descriptions (in VHDL-AMS) has been proposed by Zeng and Huss.[21] In their approach, refactoring preserves the simulated behavior of a hardware design. The non-functional measurement that improves is that refactored code can be processed by standard synthesis tools, while the original code cannot. Refactoring of digital hardware description languages, albeit manual refactoring, has also been investigated by Synopsys fellow Mike Keating.[22][23] His target is to make complex systems easier to understand, which increases the designers' productivity.

The first known use of the term "refactoring" in the published literature was in a September, 1990 article by William Opdyke and Ralph Johnson.[24]
Although refactoring code has been done informally for decades, William Griswold's 1991 Ph.D. dissertation[25]
is one of the first major academic works on refactoring functional and procedural programs, followed by William Opdyke's 1992 dissertation[26]
on the refactoring of object-oriented programs,[27] although all the theory and machinery have long been available as program transformation systems. All of these resources provide a catalog of common methods for refactoring; a refactoring method has a description of how to apply the method and indicators for when you should (or should not) apply the method.

Martin Fowler's book Refactoring: Improving the Design of Existing Code is the canonical reference. [according to whom?]

The terms "factoring" and "factoring out" have been used in this way in the Forth community since at least the early 1980s. Chapter Six of Leo Brodie's book Thinking Forth (1984)[28] is dedicated to the subject.

In extreme programming, the Extract Method refactoring technique has essentially the same meaning as factoring in Forth; to break down a "word" (or function) into smaller, more easily maintained functions.

Refactorings can also be reconstructed[29] posthoc to produce concise descriptions of complex software changes recorded in software repositories like CVS or SVN.

This section needs additional citations for verification. Please help improve this article by adding citations to reliable sources in this section. Unsourced material may be challenged and removed.Find sources: "Code refactoring" – news · newspapers · books · scholar · JSTOR (July 2018) (Learn how and when to remove this message)
Many software editors and IDEs have automated refactoring support. Here is a list of a few of these editors, or so-called refactoring browsers.

DMS Software Reengineering Toolkit (Implements large-scale refactoring for C, C++, C#, COBOL, Java, PHP and other languages)
Eclipse based:
Eclipse (for Java, and to a lesser extent, C++, PHP, Ruby and JavaScript)
PyDev (for Python)
Photran (a Fortran plugin for the Eclipse IDE)
Embarcadero Delphi
IntelliJ based:
Resharper (for C#)
AppCode (for Objective-C, C and C++)
IntelliJ IDEA (for Java)
PyCharm (for Python)
WebStorm (for JavaScript)
PhpStorm (for PHP)
Android Studio (for Java and C++)
JDeveloper (for Java)
NetBeans (for Java)
Smalltalk: Most dialects include powerful refactoring tools. Many use the original refactoring browser produced in the early '90s by Ralph Johnson.
Visual Studio based:
Visual Studio (for .NET and C++)
Visual Assist (addon for Visual Studio with refactoring support for C# and C++)
Wing IDE (for Python)
Xcode (for C, Objective-C, and Swift)[30]
Qt Creator (for C++, Objective-C and QML)[31]
Eclipse (for Java, and to a lesser extent, C++, PHP, Ruby and JavaScript)
PyDev (for Python)
Photran (a Fortran plugin for the Eclipse IDE)
Resharper (for C#)
AppCode (for Objective-C, C and C++)
IntelliJ IDEA (for Java)
PyCharm (for Python)
WebStorm (for JavaScript)
PhpStorm (for PHP)
Android Studio (for Java and C++)
Visual Studio (for .NET and C++)
Visual Assist (addon for Visual Studio with refactoring support for C# and C++)
Amelioration pattern
Code review
Database refactoring
Decomposition (computer science)
Modular programming
Obfuscated code
Prefactoring
Rewrite (programming)
Separation of concerns
Software peer review
Test-driven development
Code refactoringExtreme programmingTechnology neologisms
Webarchive template wayback linksCS1 maint: bot: original URL status unknownArticles with short descriptionShort description is different from WikidataWikipedia articles needing page number citations from July 2018All articles with specifically marked weasel-worded phrasesArticles with specifically marked weasel-worded phrases from July 2018Articles needing additional references from July 2018All articles needing additional referencesArticles with Curlie linksArticles with FAST identifiersArticles with GND identifiersArticles with J9U identifiersArticles with LCCN identifiersArticles with NDL identifiersArticles with NKC identifiers




