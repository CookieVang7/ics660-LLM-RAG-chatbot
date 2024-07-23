


(Top)





1
Program refinement








2
Data refinement








3
Refinement calculus








4
Refinement types








5
See also








6
References


















This article needs additional citations for verification. Please help improve this article by adding citations to reliable sources. Unsourced material may be challenged and removed.Find sources: "Refinement" computing – news · newspapers · books · scholar · JSTOR (September 2010) (Learn how and when to remove this message)
Data transformation
Concepts
Metadata
Data element
Data mapping
Data migration
Data transformation
Model transformation
Macro
Preprocessor

Transformation languages
ATL
AWK
MOFM2T
QVT
XML languages

Techniques and transforms
Identity transform
Data refinement

Applications
Data conversion
Data migration
Data integration
Extract, transform, load (ETL)
Web template system

Related
Data wrangling
Transformation languages
vte
Metadata
Data element
Data mapping
Data migration
Data transformation
Model transformation
Macro
Preprocessor
ATL
AWK
MOFM2T
QVT
XML languages
Identity transform
Data refinement
Data conversion
Data migration
Data integration
Extract, transform, load (ETL)
Web template system
Data wrangling
Transformation languages
vte
Refinement is a generic term of computer science that encompasses various approaches for producing correct computer programs and simplifying existing programs to enable their formal verification.

In formal methods, program refinement is the verifiable transformation of an abstract (high-level) formal specification into a concrete (low-level) executable program.[citation needed] Stepwise refinement allows this process to be done in stages. Logically, refinement normally involves implication, but there can be additional complications.

The progressive just-in-time preparation of the product backlog (requirements list) in agile software development approaches, such as Scrum, is also commonly described as refinement.[1]

Data refinement is used to convert an abstract data model (in terms of sets for example) into implementable data structures (such as arrays).[citation needed] Operation refinement converts a specification of an operation on a system into an implementable program (e.g., a procedure). The postcondition can be strengthened and/or the precondition weakened in this process. This reduces any nondeterminism in the specification, typically to a completely deterministic implementation.

For example, x ∈ {1,2,3} (where x is the value of the variable x after an operation) could be refined to x ∈ {1,2}, then x ∈ {1}, and implemented as x := 1. Implementations of x := 2 and x := 3 would be equally acceptable in this case, using a different route for the refinement. However, we must be careful not to refine to x ∈ {} (equivalent to false) since this is unimplementable; it is impossible to select a member from the empty set.

The term reification is also sometimes used (coined by Cliff Jones). Retrenchment is an alternative technique when formal refinement is not possible. The opposite of refinement is abstraction.

Refinement calculus is a formal system (inspired from Hoare logic) that promotes program refinement. The FermaT Transformation System is an industrial-strength implementation of refinement. The B-Method is also a formal method that extends refinement calculus with a component language: it has been used in industrial developments.

In type theory, a refinement type[2][3][4] is a type endowed with a predicate which is assumed to hold for any element of the refined type. Refinement types can express preconditions when used as function arguments or postconditions when used as return types: for instance, the type of a function which accepts natural numbers and returns natural numbers greater than 5 may be written as 



f
:

N

→
{
n
:

N



|


n
>
5
}


{\displaystyle f:\mathbb {N} \rightarrow \{n:\mathbb {N} \,|\,n>5\}}

. Refinement types are thus related to behavioral subtyping.

Reification (computer science)
Formal methods terminologyComputer programmingSoftware engineering stubs
Articles needing additional references from September 2010All articles needing additional referencesAll articles with unsourced statementsArticles with unsourced statements from September 2010All stub articles




