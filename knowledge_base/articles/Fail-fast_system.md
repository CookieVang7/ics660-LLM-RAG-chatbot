



From Wikipedia, the free encyclopedia


System which reports likely failures


|  | This article includes a list of general [references](/wiki/Wikipedia:Citing_sources "Wikipedia:Citing sources"), but **it lacks sufficient corresponding [inline citations](/wiki/Wikipedia:Citing_sources#Inline_citations "Wikipedia:Citing sources")**. Please help to [improve](/wiki/Wikipedia:WikiProject_Reliability "Wikipedia:WikiProject Reliability") this article by [introducing](/wiki/Wikipedia:When_to_cite "Wikipedia:When to cite") more precise citations. *(June 2016)* *([Learn how and when to remove this message](/wiki/Help:Maintenance_template_removal "Help:Maintenance template removal"))* |
| --- | --- |


In [systems design](/wiki/Systems_design "Systems design"), a **fail-fast system** is one that immediately reports at its interface any condition that is likely to indicate a failure. Fail-fast systems are usually designed to stop normal operation rather than attempt to continue a possibly flawed process. Such designs often check the system's state at several points in an operation, so that any failures can be detected early. The responsibility of a fail-fast module is detecting errors, and then letting the next-highest level of the system handle them.




Hardware and software[[edit](/w/index.php?title=Fail-fast_system&action=edit&section=1 "Edit section: Hardware and software")]
------------------------------------------------------------------------------------------------------------------------------


Fail-fast systems or modules are desirable in several circumstances:



* Fail-fast architectures are based on an error handling policy where any detected error or non-contemplated state makes the system fail (fast). In some sense, the error-handling policy is the opposite of that used in a [fault-tolerant system](/wiki/Fault-tolerant_system "Fault-tolerant system"). In a fault-tolerant system, an error handling policy is established to have redundant components and move computation requests to alive components when some component fails. Paradoxically fail-fast systems make fault-tolerant systems more resilient. We can have 10 redundant servers for a given database, but if the shared configuration for the 10 servers is updated with wrong authentication data for clients, all of them will "redundantly fail". In that sense, a fail-fast system will make sure that all the 10 redundant servers fail as soon as possible to make the DevOps react fast.
* Fail-fast components are often used in situations where failure in one component might not be visible until it leads to failure in another component as a consequence of lazy initialization. e.g. "The system that is "doomed" to fail because a file-system path is wrongly set up, does it not fail at startup because the file-system path is not checked at startup. Only when a client-request arrives the system fails, at random, later on.
* Finding the cause of a failure is easier in a fail-fast system because the system reports the failure with as much information as possible as close to the time of failure as possible. In a fault-tolerant system, the failure might go undetected, whereas in a system that is neither fault-tolerant nor fail-fast, the failure might be temporarily hidden until it causes some seemingly unrelated problem later.
* A fail-fast system that is designed to halt as well as report the error on failure is less likely to erroneously perform an irreversible or costly operation.


Developers also refer to code as fail-fast if it tries to fail as soon as possible at a variable or object initialization. In [object-oriented programming](/wiki/Object-oriented_programming "Object-oriented programming"), a fail-fast-designed object initializes the internal state of the object in the constructor, launching an exception if something is wrong (rather than allowing non-initialized or partially initialized objects that will fail later due to a wrong "setter"). The object can then be made [immutable](/wiki/Immutable_object "Immutable object") if no more changes to the internal state are expected. In functions, fail-fast code will check input parameters in the [precondition](/wiki/Precondition "Precondition"). In client-server architectures, fail-fast will check the client request just upon arrival, before processing or redirecting it to other internal components, returning an error if the request fails (incorrect parameters, ...). Fail-fast-designed code decreases the internal [software entropy](/wiki/Software_entropy "Software entropy") and reduces debugging effort.



### Examples[[edit](/w/index.php?title=Fail-fast_system&action=edit&section=2 "Edit section: Examples")]


* A fail-fast application/system checks that all input/output resources needed for future computations are ready before any computation request arrives.
* A fail-fast application/system checks that all immutable initial configurations are correct at startup.
* A fail-fast function is a function that checks all input to the function in a [Precondition](/wiki/Precondition "Precondition") before proceeding with any computation or business logic in such function.
* A fail-fast function will normally throw a runtime exception, when some abnormal computation, is found making the system fail if no "catch" has been contemplated by any other, versus returning some error value without making any (optimistic) assumption about the correct management of the raised error.
* From the field of [software engineering](/wiki/Software_engineering "Software engineering"), a *fail-fast iterator* is an [iterator](/wiki/Iterator "Iterator") that attempts to raise an error if the sequence of elements processed by the iterator is changed during [iteration](/wiki/Iteration "Iteration").
* Given an initial state in a state machine, a fail-fast system will check such a state and fail fast.
* Given a state-change in a state machine, the fail-fast system will halt the machine if the state-change is forbidden. It could be the case that the forbidden state-change is due to a wrong external input. In that case, the fail-fast system will stop processing the request as soon as the wrong input is detected (vs. delegating to the state-machine implementation).


Business[[edit](/w/index.php?title=Fail-fast_system&action=edit&section=3 "Edit section: Business")]
----------------------------------------------------------------------------------------------------


Main article: [Fail fast (business)](/wiki/Fail_fast_(business) "Fail fast (business)")
The term has been widely employed as a metaphor in business, dating back to at least 2001,[[1]](#cite_note-1) meaning that businesses should undertake bold experiments to determine the long-term viability of a product or strategy, rather than proceeding cautiously and investing years in a doomed approach. It became adopted as a kind of "mantra" within [startup](/wiki/Startup_company "Startup company") culture, i.e. "Fail fast, fail often."[[2]](#cite_note-2)



See also[[edit](/w/index.php?title=Fail-fast_system&action=edit&section=4 "Edit section: See also")]
----------------------------------------------------------------------------------------------------


* [Crash-only software](/wiki/Crash-only_software "Crash-only software")
* [Design by contract](/wiki/Design_by_contract "Design by contract")
* [Failing badly](/wiki/Failing_badly "Failing badly") vs. failing well
* [Fail-safe](/wiki/Fail-safe "Fail-safe")
* [Fail-stop](/wiki/Fail-stop "Fail-stop")
* [Fail-silent system](/wiki/Fail-silent_system "Fail-silent system")


References[[edit](/w/index.php?title=Fail-fast_system&action=edit&section=5 "Edit section: References")]
--------------------------------------------------------------------------------------------------------


1. **[^](#cite_ref-1)** Khanna, Rajat; Guler, Isin; Nerkar, Atul (2016-04-01). "Fail Often, Fail Big, and Fail Fast? Learning from Small Failures and R&D Performance in the Pharmaceutical Industry". *Academy of Management Journal*. **59** (2): 436–459. [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.5465/amj.2013.1109](https://doi.org/10.5465%2Famj.2013.1109). [ISSN](/wiki/ISSN_(identifier) "ISSN (identifier)") [0001-4273](https://www.worldcat.org/issn/0001-4273).
2. **[^](#cite_ref-2)** Surowiecki, James. ["Epic Fails of the Startup World"](http://www.newyorker.com/magazine/2014/05/19/epic-fails-of-the-startup-world). *The New Yorker*. Retrieved 2017-08-14.

External links[[edit](/w/index.php?title=Fail-fast_system&action=edit&section=6 "Edit section: External links")]
----------------------------------------------------------------------------------------------------------------


* [Gray, Jim](/wiki/Jim_Gray_(computer_scientist) "Jim Gray (computer scientist)") (1985). ["Why Do Computers Stop and What Can Be Done About It?"](https://citeseerx.ist.psu.edu/doc/10.1.1.110.9127). [CiteSeerX](/wiki/CiteSeerX_(identifier) "CiteSeerX (identifier)") [10.1.1.110.9127](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.110.9127), introducing 'Fail Fast'
* ["Fail Fast" Article by Jim Shore explaining using 'Fail Fast' concept in software development](http://www.martinfowler.com/ieeeSoftware/failFast.pdf) (from 'columns for IEEE software' edited by [Martin Fowler](/wiki/Martin_Fowler_(software_engineer) "Martin Fowler (software engineer)"))





![](https://login.wikimedia.org/wiki/Special:CentralAutoLogin/start?type=1x1)
Retrieved from "<https://en.wikipedia.org/w/index.php?title=Fail-fast_system&oldid=1220870627>"
[Categories](/wiki/Help:Category "Help:Category"): * [Engineering failures](/wiki/Category:Engineering_failures "Category:Engineering failures")
* [Programming principles](/wiki/Category:Programming_principles "Category:Programming principles")
Hidden categories: * [Articles with short description](/wiki/Category:Articles_with_short_description "Category:Articles with short description")
* [Short description is different from Wikidata](/wiki/Category:Short_description_is_different_from_Wikidata "Category:Short description is different from Wikidata")
* [Articles lacking in-text citations from June 2016](/wiki/Category:Articles_lacking_in-text_citations_from_June_2016 "Category:Articles lacking in-text citations from June 2016")
* [All articles lacking in-text citations](/wiki/Category:All_articles_lacking_in-text_citations "Category:All articles lacking in-text citations")

