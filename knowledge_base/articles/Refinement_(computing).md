



From Wikipedia, the free encyclopedia




|  | This article **needs additional citations for [verification](/wiki/Wikipedia:Verifiability "Wikipedia:Verifiability")**. Please help [improve this article](/wiki/Special:EditPage/Refinement_(computing) "Special:EditPage/Refinement (computing)") by [adding citations to reliable sources](/wiki/Help:Referencing_for_beginners "Help:Referencing for beginners"). Unsourced material may be challenged and removed.*Find sources:* ["Refinement" computing](https://www.google.com/search?as_eq=wikipedia&q=%22Refinement%22+computing) – [news](https://www.google.com/search?tbm=nws&q=%22Refinement%22+computing+-wikipedia&tbs=ar:1) **·** [newspapers](https://www.google.com/search?&q=%22Refinement%22+computing&tbs=bkt:s&tbm=bks) **·** [books](https://www.google.com/search?tbs=bks:1&q=%22Refinement%22+computing+-wikipedia) **·** [scholar](https://scholar.google.com/scholar?q=%22Refinement%22+computing) **·** [JSTOR](https://www.jstor.org/action/doBasicSearch?Query=%22Refinement%22+computing&acc=on&wc=on) *(September 2010)* *([Learn how and when to remove this message](/wiki/Help:Maintenance_template_removal "Help:Maintenance template removal"))* |
| --- | --- |




| [Data transformation](/wiki/Data_transformation_(computing) "Data transformation (computing)") |
| --- |
| Concepts |
| * [Metadata](/wiki/Metadata "Metadata") * [Data element](/wiki/Data_element "Data element") * [Data mapping](/wiki/Data_mapping "Data mapping") * [Data migration](/wiki/Data_migration "Data migration") * [Data transformation](/wiki/Data_transformation_(computing) "Data transformation (computing)") * [Model transformation](/wiki/Model_transformation "Model transformation") * [Macro](/wiki/Macro_(computer_science) "Macro (computer science)") * [Preprocessor](/wiki/Preprocessor "Preprocessor") |
| [Transformation languages](/wiki/Transformation_language "Transformation language") |
| * [ATL](/wiki/ATLAS_Transformation_Language "ATLAS Transformation Language") * [AWK](/wiki/AWK "AWK") * [MOFM2T](/wiki/MOFM2T "MOFM2T") * [QVT](/wiki/QVT "QVT") * [XML languages](/wiki/XML_transformation_language "XML transformation language") |
| Techniques and transforms |
| * [Identity transform](/wiki/Identity_transform "Identity transform") * [Data refinement](/wiki/Data_refinement "Data refinement") |
| Applications |
| * [Data conversion](/wiki/Data_conversion "Data conversion") * [Data migration](/wiki/Data_migration "Data migration") * [Data integration](/wiki/Data_integration "Data integration") * [Extract, transform, load](/wiki/Extract,_transform,_load "Extract, transform, load") (ETL) * [Web template system](/wiki/Web_template_system "Web template system") |
| Related |
| * [Data wrangling](/wiki/Data_wrangling "Data wrangling") * [Transformation languages](/wiki/Transformation_language "Transformation language") |
| * [v](/wiki/Template:Data_transformation "Template:Data transformation") * [t](/wiki/Template_talk:Data_transformation "Template talk:Data transformation") * [e](/wiki/Special:EditPage/Template:Data_transformation "Special:EditPage/Template:Data transformation") |


**Refinement** is a generic term of computer science that encompasses various approaches for producing [correct](/wiki/Correctness_(computer_science) "Correctness (computer science)") computer programs and simplifying existing programs to enable their formal verification.




Program refinement[[edit](/w/index.php?title=Refinement_(computing)&action=edit&section=1 "Edit section: Program refinement")]
------------------------------------------------------------------------------------------------------------------------------


In [formal methods](/wiki/Formal_methods "Formal methods"), **program refinement** is the [verifiable](/wiki/Formal_verification "Formal verification") transformation of an *abstract* (high-level) [formal specification](/wiki/Formal_specification "Formal specification") into a *concrete* (low-level) [executable program](/wiki/Executable_program "Executable program").[*[citation needed](/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")*] *[Stepwise refinement](/wiki/Stepwise_refinement "Stepwise refinement")* allows this process to be done in stages. Logically, refinement normally involves [implication](/wiki/Logical_consequence "Logical consequence"), but there can be additional complications.


The progressive just-in-time preparation of the product backlog (requirements list) in [agile software development](/wiki/Agile_software_development "Agile software development") approaches, such as [Scrum](/wiki/Scrum_(software_development) "Scrum (software development)"), is also commonly described as refinement.[[1]](#cite_note-1)



Data refinement[[edit](/w/index.php?title=Refinement_(computing)&action=edit&section=2 "Edit section: Data refinement")]
------------------------------------------------------------------------------------------------------------------------


**Data refinement** is used to convert an abstract data model (in terms of [sets](/wiki/Set_(mathematics) "Set (mathematics)") for example) into implementable [data structures](/wiki/Data_structures "Data structures") (such as [arrays](/wiki/Array_data_structure "Array data structure")).[*[citation needed](/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")*] Operation refinement converts a [specification](/wiki/Specification "Specification") of an operation on a system into an implementable [program](/wiki/Computer_program "Computer program") (e.g., a [procedure](/wiki/Procedure_(computer_science) "Procedure (computer science)")). The [postcondition](/wiki/Postcondition "Postcondition") can be strengthened and/or the [precondition](/wiki/Precondition "Precondition") weakened in this process. This reduces any [nondeterminism](/wiki/Nondeterministic_algorithm "Nondeterministic algorithm") in the specification, typically to a completely [deterministic](/wiki/Deterministic "Deterministic") implementation.


For example, *x* ∈ {1,2,3} (where *x* is the value of the [variable](/wiki/Variable_(programming) "Variable (programming)") *x* after an operation) could be refined to *x* ∈ {1,2}, then *x* ∈ {1}, and implemented as *x* := 1. Implementations of *x* := 2 and *x* := 3 would be equally acceptable in this case, using a different route for the refinement. However, we must be careful not to refine to *x* ∈ {} (equivalent to *false*) since this is unimplementable; it is impossible to select a [member](/wiki/Element_(mathematics) "Element (mathematics)") from the [empty set](/wiki/Empty_set "Empty set").


The term [reification](/wiki/Reification_(computer_science) "Reification (computer science)") is also sometimes used (coined by [Cliff Jones](/wiki/Cliff_Jones_(computer_scientist) "Cliff Jones (computer scientist)")). [Retrenchment](/wiki/Retrenchment_(computing) "Retrenchment (computing)") is an alternative technique when formal refinement is not possible. The opposite of refinement is [abstraction](/wiki/Abstraction_(computer_science) "Abstraction (computer science)").



Refinement calculus[[edit](/w/index.php?title=Refinement_(computing)&action=edit&section=3 "Edit section: Refinement calculus")]
--------------------------------------------------------------------------------------------------------------------------------


[Refinement calculus](/wiki/Refinement_calculus "Refinement calculus") is a [formal system](/wiki/Formal_system "Formal system") (inspired from [Hoare logic](/wiki/Hoare_logic "Hoare logic")) that promotes program refinement. The [FermaT Transformation System](/w/index.php?title=FermaT_Transformation_System&action=edit&redlink=1 "FermaT Transformation System (page does not exist)") is an industrial-strength implementation of refinement. The [B-Method](/wiki/B-Method "B-Method") is also a [formal method](/wiki/Formal_method "Formal method") that extends refinement calculus with a component language: it has been used in industrial developments.



Refinement types[[edit](/w/index.php?title=Refinement_(computing)&action=edit&section=4 "Edit section: Refinement types")]
--------------------------------------------------------------------------------------------------------------------------


Main article: [Refinement type](/wiki/Refinement_type "Refinement type")
In [type theory](/wiki/Type_theory "Type theory"), a **refinement type**[[2]](#cite_note-2)[[3]](#cite_note-3)[[4]](#cite_note-4) is a type endowed with a predicate which is assumed to hold for any element of the refined type. Refinement types can express [preconditions](/wiki/Precondition "Precondition") when used as [function arguments](/wiki/Function_argument "Function argument") or [postconditions](/wiki/Postcondition "Postcondition") when used as [return types](/wiki/Return_type "Return type"): for instance, the type of a function which accepts natural numbers and returns natural numbers greater than 5 may be written as 



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

![{\displaystyle f:\mathbb {N} \rightarrow \{n:\mathbb {N} \,|\,n>5\}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/cb75138a80e82b05d953d03eb48736bf009db47c). Refinement types are thus related to [behavioral subtyping](/wiki/Behavioral_subtyping "Behavioral subtyping").



See also[[edit](/w/index.php?title=Refinement_(computing)&action=edit&section=5 "Edit section: See also")]
----------------------------------------------------------------------------------------------------------


* [Reification (computer science)](/wiki/Reification_(computer_science) "Reification (computer science)")


References[[edit](/w/index.php?title=Refinement_(computing)&action=edit&section=6 "Edit section: References")]
--------------------------------------------------------------------------------------------------------------



1. **[^](#cite_ref-1)** Cho, L (2009). "Adopting an Agile Culture a User Experience Team's Journey". *2009 Agile Conference*. pp. 416–421. [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.1109/AGILE.2009.76](https://doi.org/10.1109%2FAGILE.2009.76). [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-0-7695-3768-9](/wiki/Special:BookSources/978-0-7695-3768-9 "Special:BookSources/978-0-7695-3768-9"). [S2CID](/wiki/S2CID_(identifier) "S2CID (identifier)") [38580329](https://api.semanticscholar.org/CorpusID:38580329).
2. **[^](#cite_ref-2)** Freeman, T.; Pfenning, F. (1991). ["Refinement types for ML"](https://www.cs.cmu.edu/~fp/papers/pldi91.pdf) (PDF). *Proceedings of the ACM Conference on Programming Language Design and Implementation*. pp. 268–277. [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.1145/113445.113468](https://doi.org/10.1145%2F113445.113468).
3. **[^](#cite_ref-3)** Hayashi, S. (1993). "Logic of refinement types". *Proceedings of the Workshop on Types for Proofs and Programs*. pp. 157–172. [CiteSeerX](/wiki/CiteSeerX_(identifier) "CiteSeerX (identifier)") [10.1.1.38.6346](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.38.6346). [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.1007/3-540-58085-9\_74](https://doi.org/10.1007%2F3-540-58085-9_74).
4. **[^](#cite_ref-4)** Denney, E. (1998). "Refinement types for specification". *Proceedings of the IFIP International Conference on Programming Concepts and Methods*. Vol. 125. Chapman & Hall. pp. 148–166. [CiteSeerX](/wiki/CiteSeerX_(identifier) "CiteSeerX (identifier)") [10.1.1.22.4988](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.22.4988).

  






| [Stub icon](/wiki/File:Software_spanner.svg) | This [software-engineering](/wiki/Software_engineering "Software engineering")-related article is a [stub](/wiki/Wikipedia:Stub "Wikipedia:Stub"). You can help Wikipedia by [expanding it](https://en.wikipedia.org/w/index.php?title=Refinement_(computing)&action=edit). |
| --- | --- |

* [v](/wiki/Template:Software-eng-stub "Template:Software-eng-stub")
* [t](/wiki/Template_talk:Software-eng-stub "Template talk:Software-eng-stub")
* [e](/wiki/Special:EditPage/Template:Software-eng-stub "Special:EditPage/Template:Software-eng-stub")




![](https://login.wikimedia.org/wiki/Special:CentralAutoLogin/start?type=1x1)
Retrieved from "<https://en.wikipedia.org/w/index.php?title=Refinement_(computing)&oldid=1215731572>"
[Categories](/wiki/Help:Category "Help:Category"): * [Formal methods terminology](/wiki/Category:Formal_methods_terminology "Category:Formal methods terminology")
* [Computer programming](/wiki/Category:Computer_programming "Category:Computer programming")
* [Software engineering stubs](/wiki/Category:Software_engineering_stubs "Category:Software engineering stubs")
Hidden categories: * [Articles needing additional references from September 2010](/wiki/Category:Articles_needing_additional_references_from_September_2010 "Category:Articles needing additional references from September 2010")
* [All articles needing additional references](/wiki/Category:All_articles_needing_additional_references "Category:All articles needing additional references")
* [All articles with unsourced statements](/wiki/Category:All_articles_with_unsourced_statements "Category:All articles with unsourced statements")
* [Articles with unsourced statements from September 2010](/wiki/Category:Articles_with_unsourced_statements_from_September_2010 "Category:Articles with unsourced statements from September 2010")
* [All stub articles](/wiki/Category:All_stub_articles "Category:All stub articles")

