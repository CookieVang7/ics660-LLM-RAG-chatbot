


(Top)





1
Hardware and software




Toggle Hardware and software subsection





1.1
Examples










2
Business








3
See also








4
References








5
External links










1.1
Examples
















This article includes a list of general references, but it lacks sufficient corresponding inline citations. Please help to improve this article by introducing more precise citations. (June 2016) (Learn how and when to remove this message)
In systems design, a fail-fast system is one that immediately reports at its interface any condition that is likely to indicate a failure. Fail-fast systems are usually designed to stop normal operation rather than attempt to continue a possibly flawed process. Such designs often check the system's state at several points in an operation, so that any failures can be detected early. The responsibility of a fail-fast module is detecting errors, and then letting the next-highest level of the system handle them.

Fail-fast systems or modules are desirable in several circumstances:

Fail-fast architectures are based on an error handling policy where any detected error or non-contemplated state makes the system fail (fast). In some sense, the error-handling policy is the opposite of that used in a fault-tolerant system. In a fault-tolerant system, an error handling policy is established to have redundant components and move computation requests to alive components when some component fails. Paradoxically fail-fast systems make fault-tolerant systems more resilient. We can have 10 redundant servers for a given database, but if the shared configuration for the 10 servers is updated with wrong authentication data for clients, all of them will "redundantly fail". In that sense, a fail-fast system will make sure that all the 10 redundant servers fail as soon as possible to make the DevOps react fast.
Fail-fast components are often used in situations where failure in one component might not be visible until it leads to failure in another component as a consequence of lazy initialization. e.g. "The system that is "doomed" to fail because a file-system path is wrongly set up, does it not fail at startup because the file-system path is not checked at startup. Only when a client-request arrives the system fails, at random, later on.
Finding the cause of a failure is easier in a fail-fast system because the system reports the failure with as much information as possible as close to the time of failure as possible. In a fault-tolerant system, the failure might go undetected, whereas in a system that is neither fault-tolerant nor fail-fast, the failure might be temporarily hidden until it causes some seemingly unrelated problem later.
A fail-fast system that is designed to halt as well as report the error on failure is less likely to erroneously perform an irreversible or costly operation.
Developers also refer to code as fail-fast if it tries to fail as soon as possible at a variable or object initialization. In object-oriented programming, a fail-fast-designed object initializes the internal state of the object in the constructor, launching an exception if something is wrong (rather than allowing non-initialized or partially initialized objects that will fail later due to a wrong "setter"). The object can then be made immutable if no more changes to the internal state are expected. In functions, fail-fast code will check input parameters in the precondition. In client-server architectures, fail-fast will check the client request just upon arrival, before processing or redirecting it to other internal components, returning an error if the request fails (incorrect parameters, ...). Fail-fast-designed code decreases the internal software entropy and reduces debugging effort.

A fail-fast application/system checks that all input/output resources needed for future computations are ready before any computation request arrives.
A fail-fast application/system checks that all immutable initial configurations are correct at startup.
A fail-fast function is a function that checks all input to the function in a Precondition before proceeding with any computation or business logic in such function.
A fail-fast function will normally throw a runtime exception, when some abnormal computation, is found making the system fail if no "catch" has been contemplated by any other, versus returning some error value without making any (optimistic) assumption about the correct management of the raised error.
From the field of software engineering, a fail-fast iterator is an iterator that attempts to raise an error if the sequence of elements processed by the iterator is changed during iteration.
Given an initial state in a state machine, a fail-fast system will check such a state and fail fast.
Given a state-change in a state machine, the fail-fast system will halt the machine if the state-change is forbidden. It could be the case that the forbidden state-change is due to a wrong external input. In that case, the fail-fast system will stop processing the request as soon as the wrong input is detected (vs. delegating to the state-machine implementation).
The term has been widely employed as a metaphor in business, dating back to at least 2001,[1] meaning that businesses should undertake bold experiments to determine the long-term viability of a product or strategy, rather than proceeding cautiously and investing years in a doomed approach. It became adopted as a kind of "mantra" within startup culture, i.e. "Fail fast, fail often."[2]

Crash-only software
Design by contract
Failing badly vs. failing well
Fail-safe
Fail-stop
Fail-silent system
Engineering failuresProgramming principles
Articles with short descriptionShort description is different from WikidataArticles lacking in-text citations from June 2016All articles lacking in-text citations




