


[![Page protected with pending changes](//upload.wikimedia.org/wikipedia/en/thumb/b/b7/Pending-protection-shackle.svg/20px-Pending-protection-shackle.svg.png)](/wiki/Wikipedia:Protection_policy#pending "All edits by unregistered and new users are subject to review prior to becoming visible to unregistered users")

From Wikipedia, the free encyclopedia


This is the [latest accepted revision](/wiki/Wikipedia:Pending_changes "Wikipedia:Pending changes"), [reviewed](https://en.wikipedia.org/w/index.php?title=Special:Log&type=review&page=DevOps) on *9 June 2024*.



Set of software development practices



**DevOps** is a methodology in the software development and IT industry. Used as a set of practices and tools, DevOps integrates and automates the work of [software development](/wiki/Software_development "Software development") (*Dev*) and [IT operations](/wiki/IT_operations "IT operations") (*Ops*) as a means for improving and shortening the [systems development life cycle](/wiki/Systems_development_life_cycle "Systems development life cycle").[[1]](#cite_note-1) DevOps is complementary to [agile software development](/wiki/Agile_software_development "Agile software development"); several DevOps aspects came from the *agile* way of working.


Automation is an important part of DevOps. [Software programmers](/wiki/Software_programmer "Software programmer") and [architects](/wiki/Software_architect "Software architect") should use "[fitness functions](/wiki/Fitness_function "Fitness function")" to keep their software in check.[[2]](#cite_note-2)




Definition[[edit](/w/index.php?title=DevOps&action=edit&section=1 "Edit section: Definition")]
----------------------------------------------------------------------------------------------


Other than it being a cross-functional combination (and a [portmanteau](/wiki/Portmanteau "Portmanteau")) of the terms and concepts for "development" and "operations", academics and practitioners have not developed a universal definition for the term "DevOps".[[a]](#cite_note-4)[[b]](#cite_note-6)[[c]](#cite_note-8)[[d]](#cite_note-9) Most often, DevOps is characterized by key principles: shared ownership, workflow automation, and rapid feedback.
From an academic perspective, [Len Bass](/wiki/Len_Bass "Len Bass"), Ingo Weber, and Liming Zhu—three computer science researchers from the [CSIRO](/wiki/CSIRO "CSIRO") and the [Software Engineering Institute](/wiki/Software_Engineering_Institute "Software Engineering Institute")—suggested defining DevOps as "a set of practices intended to reduce the time between committing a change to a system and the change being placed into normal production, while ensuring high quality".[[6]](#cite_note-10)
However, the term is used in multiple contexts. At its most successful, DevOps is a combination of specific practices, culture change, and tools.[[7]](#cite_note-11)



History[[edit](/w/index.php?title=DevOps&action=edit&section=2 "Edit section: History")]
----------------------------------------------------------------------------------------


Proposals to combine software development methodologies with deployment and operations concepts began to appear in the late 80s and early 90s.[[8]](#cite_note-12)


Around 2007 and 2008, concerns were raised by those within the software development and IT communities that the separation between the two industries, where one wrote and created software entirely separate from those that deploy and support the software was creating a fatal level of dysfunction within the industry.[[9]](#cite_note-13)


In 2009, the first conference named DevOps Days was held in [Ghent](/wiki/Ghent "Ghent"), [Belgium](/wiki/Belgium "Belgium"). The conference was founded by Belgian consultant, project manager and agile practitioner Patrick Debois.[[10]](#cite_note-14)[[11]](#cite_note-15) The conference has now spread to other countries.[[12]](#cite_note-16)


In 2012, a report called "State of DevOps" was first published by Alanna Brown at [Puppet Labs](/wiki/Puppet_(software) "Puppet (software)").[[13]](#cite_note-2016_State_of_DevOps_Report-17)[[14]](#cite_note-18)


As of 2014, the annual State of DevOps report was published by [Nicole Forsgren](/wiki/Nicole_Forsgren "Nicole Forsgren"), Gene Kim, Jez Humble and others. They stated that the adoption of DevOps was accelerating.[[15]](#cite_note-19)[[16]](#cite_note-20) Also in 2014, Lisa Crispin and Janet Gregory wrote the book More Agile Testing, containing a chapter on testing and DevOps.[[17]](#cite_note-21)[[18]](#cite_note-22)


In 2016, the DORA metrics for throughput (deployment frequency, lead time for changes), and stability (mean time to recover, change failure rate) were published in the State of DevOps report.[[13]](#cite_note-2016_State_of_DevOps_Report-17) However, the research methodology and metrics were criticized by experts.[[19]](#cite_note-23)[[20]](#cite_note-24)[[21]](#cite_note-25)[[22]](#cite_note-26) In response to these criticisms, the 2023 State of DevOps report [[23]](#cite_note-2023_State_of_DevOps_Report-27) published changes that updated the stability metric "mean time to recover" to "failed deployment recovery time" acknowledging the confusion the former metric has caused.[[24]](#cite_note-Culture_is_everything-28)



Relationship to other approaches[[edit](/w/index.php?title=DevOps&action=edit&section=3 "Edit section: Relationship to other approaches")]
------------------------------------------------------------------------------------------------------------------------------------------


Many of the ideas fundamental to DevOps practices are inspired by, or mirror, other well known practices such as [Lean](/wiki/Lean_manufacturing "Lean manufacturing") and [Deming's](/wiki/W._Edwards_Deming "W. Edwards Deming") [Plan-Do-Check-Act](/wiki/PDCA "PDCA") cycle, through to [The Toyota Way](/wiki/The_Toyota_Way "The Toyota Way") and the [Agile](/wiki/Agile_software_development "Agile software development") approach of breaking down components and batch sizes.[[25]](#cite_note-29) Contrary to the "top-down" prescriptive approach and rigid framework of [ITIL](/wiki/ITIL "ITIL") in the 1990s, DevOps is "bottom-up" and flexible, having been created by software engineers for their own needs.[[26]](#cite_note-30)



### Agile[[edit](/w/index.php?title=DevOps&action=edit&section=4 "Edit section: Agile")]


Main article: [Agile software development](/wiki/Agile_software_development "Agile software development")
The motivations for what has become modern DevOps and several standard DevOps practices such as automated build and test, [continuous integration](/wiki/Continuous_integration "Continuous integration"), and [continuous delivery](/wiki/Continuous_delivery "Continuous delivery") originated in the Agile world, which dates (informally) to the 1990s, and formally to 2001. Agile development teams using methods such as [extreme programming](/wiki/Extreme_programming "Extreme programming") couldn't "satisfy the customer through early and continuous delivery of valuable software"[[27]](#cite_note-31) unless they took responsibility for operations and infrastructure for their applications, automating much of that work. Because [Scrum](/wiki/Scrum_(software_development) "Scrum (software development)") emerged as the dominant Agile framework in the early 2000s and it omitted the engineering practices that were part of many Agile teams, the movement to automate operations and infrastructure functions splintered from Agile and expanded into what has become modern DevOps. Today, DevOps focuses on the deployment of developed software, whether it is developed using Agile oriented methodologies or other methodologies.



### ArchOps[[edit](/w/index.php?title=DevOps&action=edit&section=5 "Edit section: ArchOps")]


ArchOps presents an extension for DevOps practice, starting from [software architecture](/wiki/Software_architecture "Software architecture") artifacts, instead of source code, for operation deployment.[[28]](#cite_note-32) ArchOps states that architectural models are first-class entities in software development, deployment, and operations.



### Continuous Integration and Delivery (CI/CD)[[edit](/w/index.php?title=DevOps&action=edit&section=6 "Edit section: Continuous Integration and Delivery (CI/CD)")]


Main article: [CI/CD](/wiki/CI/CD "CI/CD")
Automation is a core principle for achieving DevOps success and CI/CD is a critical component.[[29]](#cite_note-33) Plus, improved collaboration and communication between and within teams helps achieve faster [time to market](/wiki/Time_to_market "Time to market"), with reduced risks.[[30]](#cite_note-34)



### Mobile DevOps[[edit](/w/index.php?title=DevOps&action=edit&section=7 "Edit section: Mobile DevOps")]


Main article: [Mobile DevOps](/wiki/Mobile_DevOps "Mobile DevOps")
Mobile DevOps is a set of practices that applies the principles of DevOps specifically to the development of mobile applications. Traditional DevOps focuses on streamlining the [software development process](/wiki/Software_development_process "Software development process") in general, but [mobile development](/wiki/Mobile_app_development "Mobile app development") has its own unique challenges that require a tailored approach.[[31]](#cite_note-35) Mobile DevOps is not simply as a branch of DevOps specific to mobile app development, instead an extension and reinterpretation of the DevOps philosophy due to very specific requirements of the mobile world.



### Site-reliability engineering[[edit](/w/index.php?title=DevOps&action=edit&section=8 "Edit section: Site-reliability engineering")]


Main article: [Site reliability engineering](/wiki/Site_reliability_engineering "Site reliability engineering")
In 2003, [Google](/wiki/Google "Google") developed [site reliability engineering](/wiki/Site_reliability_engineering "Site reliability engineering") (SRE), an approach for releasing new features continuously into large-scale high-availability systems while maintaining high-quality end-user experience.[[32]](#cite_note-36) While SRE predates the development of DevOps, they are generally viewed as being related to each other.



### Toyota production system, lean thinking, kaizen[[edit](/w/index.php?title=DevOps&action=edit&section=9 "Edit section: Toyota production system, lean thinking, kaizen")]


Main article: [Toyota Production System](/wiki/Toyota_Production_System "Toyota Production System")
Toyota production system, also known under the acronym TPS, was the inspiration for [lean thinking](/wiki/Lean_thinking "Lean thinking") with its focus on [continuous improvement](/wiki/Continuous_improvement_process "Continuous improvement process"), [kaizen](/wiki/Kaizen "Kaizen"), flow and small batches. The [andon cord principle](/wiki/Andon_(manufacturing) "Andon (manufacturing)") to create fast feedback, swarm and solve problems stems from TPS.[[33]](#cite_note-37)[[34]](#cite_note-38)



### DevSecOps, shifting security left[[edit](/w/index.php?title=DevOps&action=edit&section=10 "Edit section: DevSecOps, shifting security left")]


DevSecOps is an augmentation of DevOps to allow for security practices to be integrated into the DevOps approach. Contrary to a traditional centralized security team model, each delivery team is empowered to factor in the correct security controls into their software delivery. Security practices and testing are performed earlier in the development lifecycle, hence the term "[shift left](/wiki/Shift-left_testing "Shift-left testing")". Security is tested in three main areas: static, software composition, and dynamic.


Checking software statically via [static application security testing](/wiki/Static_application_security_testing "Static application security testing") (SAST) is [white-box testing](/wiki/White-box_testing "White-box testing") with special focus on security. Depending on the programming language, different tools are needed to do such static code analysis. The software composition is analyzed, especially libraries, and the version of each component is checked against vulnerability lists published by [CERT](/wiki/Computer_emergency_response_team "Computer emergency response team") and other expert groups. When giving software to clients, library licenses and their match to the license of the software distributed are in focus, especially [copyleft](/wiki/Copyleft "Copyleft") licenses.


In dynamic testing, also called [black-box testing](/wiki/Black-box_testing "Black-box testing"), software is tested without knowing its inner functions. In DevSecOps this practice may be referred to as [dynamic application security testing](/wiki/Dynamic_application_security_testing "Dynamic application security testing") (DAST) or penetration testing. The goal is early detection of defects including [cross-site scripting](/wiki/Cross-site_scripting "Cross-site scripting") and [SQL injection](/wiki/SQL_injection "SQL injection") vulnerabilities. Threat types are published by the [open web application security project](/wiki/OWASP "OWASP"), e.g. its TOP10,[[35]](#cite_note-39) and by other bodies. 


DevSecOps has also been described as a cultural shift involving a holistic approach to producing secure software by integrating security education, security by design, and security automation.[[36]](#cite_note-40)



Cultural change[[edit](/w/index.php?title=DevOps&action=edit&section=11 "Edit section: Cultural change")]
---------------------------------------------------------------------------------------------------------


DevOps initiatives can create cultural changes in companies[[37]](#cite_note-41) by transforming the way [operations](/wiki/Information_technology_operations "Information technology operations"), [developers](/wiki/Software_developer "Software developer"), and [testers](/wiki/Software_testing "Software testing") collaborate during the development and delivery processes.[[38]](#cite_note-42) Getting these groups to work cohesively is a critical challenge in enterprise DevOps adoption.[[39]](#cite_note-43)[[40]](#cite_note-44) DevOps is as much about culture as it is about the toolchain.[[41]](#cite_note-45)



### Microservices[[edit](/w/index.php?title=DevOps&action=edit&section=12 "Edit section: Microservices")]


Although in principle it is possible to practice DevOps with any architectural style, the [microservices](/wiki/Microservices "Microservices") architectural style is becoming the standard for building continuously deployed systems. Small size service allows the architecture of an individual service to emerge through continuous refactoring.[[42]](#cite_note-46)



### DevOps automation[[edit](/w/index.php?title=DevOps&action=edit&section=13 "Edit section: DevOps automation")]


It also supports consistency, reliability, and efficiency within the organization, and is usually enabled by a shared code repository or version control. As DevOps researcher Ravi Teja Yarlagadda hypothesizes, "Through DevOps, there is an assumption that all functions can be carried out, controlled, and managed in a central place using a simple code."[[43]](#cite_note-47)



#### Automation with version control[[edit](/w/index.php?title=DevOps&action=edit&section=14 "Edit section: Automation with version control")]


Many organizations use [version control](/wiki/Version_control "Version control") to power DevOps automation technologies like [virtual machines](/wiki/Virtual_machines "Virtual machines"), containerization (or [OS-level virtualization](/wiki/OS-level_virtualization "OS-level virtualization")), and [CI/CD](/wiki/CI/CD "CI/CD"). The paper "DevOps: development of a toolchain in the banking domain" notes that with teams of developers working on the same project, "All developers need to make changes to the same codebase and sometimes edit even the same files. For efficient working, there has to be a system that helps engineers avoid conflicts and retain the codebase history,"[[44]](#cite_note-48) with the [Git](/wiki/Git "Git") version control system and the [GitHub](/wiki/GitHub "GitHub") platform referenced as examples.



GitOps[[edit](/w/index.php?title=DevOps&action=edit&section=15 "Edit section: GitOps")]
---------------------------------------------------------------------------------------


GitOps evolved from DevOps. The specific state of deployment configuration is [version-controlled](/wiki/Version-control "Version-control"). Because the most popular [version-control](/wiki/Version-control "Version-control") is [Git](/wiki/Git "Git"), GitOps' approach has been named after [Git](/wiki/Git "Git"). Changes to configuration can be managed using [code review](/wiki/Code_review "Code review") practices, and can be rolled back using version-controlling. Essentially, all of the changes to a code are tracked, bookmarked, and making any updates to the history can be made easier. As explained by [Red Hat](/wiki/Red_Hat "Red Hat"), *"visibility to change means the ability to trace and reproduce issues quickly, improving overall security."*[[45]](#cite_note-49)



See also[[edit](/w/index.php?title=DevOps&action=edit&section=16 "Edit section: See also")]
-------------------------------------------------------------------------------------------


* [DataOps](/wiki/DataOps "DataOps")
* [DevOps toolchain](/wiki/DevOps_toolchain "DevOps toolchain")
* [Twelve-factor app](/wiki/Twelve-factor_app "Twelve-factor app")
* [Infrastructure as code](/wiki/Infrastructure_as_code "Infrastructure as code")
* [Lean software development](/wiki/Lean_software_development "Lean software development")
* [Site reliability engineering](/wiki/Site_reliability_engineering "Site reliability engineering")
* [Value stream](/wiki/Value_stream "Value stream")


Notes[[edit](/w/index.php?title=DevOps&action=edit&section=17 "Edit section: Notes")]
-------------------------------------------------------------------------------------



1. **[^](#cite_ref-4)** Dyck et al. (2015) "To our knowledge, there is no uniform definition for the terms release engineering and DevOps. As a consequence, many people use their own definitions or rely on others, which results in confusion about those terms."[[3]](#cite_note-3)
2. **[^](#cite_ref-6)** Jabbari et al. (2016) "The research results of this study showed the need for a definition as individual studies do not consistently define DevOps."[[4]](#cite_note-5)
3. **[^](#cite_ref-8)** Erich et al. (2017) "We noticed that there are various gaps in the study of DevOps: There is no consensus of what concepts DevOps covers, nor how DevOps is defined."[[5]](#cite_note-erich-2017-7)
4. **[^](#cite_ref-9)** Erich et al. (2017) "We discovered that there exists little agreement about the characteristics of DevOps in the academic literature."[[5]](#cite_note-erich-2017-7)

References[[edit](/w/index.php?title=DevOps&action=edit&section=18 "Edit section: References")]
-----------------------------------------------------------------------------------------------



1. **[^](#cite_ref-1)** Courtemanche, Meredith; Mell, Emily; Gills, Alexander S. ["What Is DevOps? The Ultimate Guide"](https://www.techtarget.com/searchitoperations/definition/DevOps). *TechTarget*. Retrieved 2023-01-22.
2. **[^](#cite_ref-2)** *Fundamentals of Software Architecture: An Engineering Approach*. O'Reilly Media. 2020. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-1492043454](/wiki/Special:BookSources/978-1492043454 "Special:BookSources/978-1492043454").
3. **[^](#cite_ref-3)** Dyck, Andrej; Penners, Ralf; Lichter, Horst (2015-05-19). "Towards Definitions for Release Engineering and DevOps". *2015 IEEE/ACM 3rd International Workshop on Release Engineering*. [IEEE](/wiki/Institute_of_Electrical_and_Electronics_Engineers "Institute of Electrical and Electronics Engineers"). p. 3. [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.1109/RELENG.2015.10](https://doi.org/10.1109%2FRELENG.2015.10). [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-1-4673-7070-7](/wiki/Special:BookSources/978-1-4673-7070-7 "Special:BookSources/978-1-4673-7070-7"). [S2CID](/wiki/S2CID_(identifier) "S2CID (identifier)") [4659735](https://api.semanticscholar.org/CorpusID:4659735).
4. **[^](#cite_ref-5)** Jabbari, Ramtin; bin Ali, Nauman; Petersen, Kai; Tanveer, Binish (May 2016). "What is DevOps?: A Systematic Mapping Study on Definitions and Practices". *Proceedings of the 2016 Scientific Workshop*. [Association for Computing Machinery](/wiki/Association_for_Computing_Machinery "Association for Computing Machinery").
5. ^ [***a***](#cite_ref-erich-2017_7-0) [***b***](#cite_ref-erich-2017_7-1) Erich, F.M.A.; Amrit, C.; Daneva, M. (June 2017). ["A Qualitative Study of DevOps Usage in Practice"](https://ris.utwente.nl/ws/files/19208022/Erich_et_al_2017_Journal_of_Software_Evolution_and_Process.pdf) (PDF). *Journal of Software: Evolution and Process*. **29** (6): e1885. [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.1002/smr.1885](https://doi.org/10.1002%2Fsmr.1885). [S2CID](/wiki/S2CID_(identifier) "S2CID (identifier)") [35914007](https://api.semanticscholar.org/CorpusID:35914007).
6. **[^](#cite_ref-10)** Bass, Len; Weber, Ingo; Zhu, Liming (2015). *DevOps: A Software Architect's Perspective*. Addison-Wesley. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-0134049847](/wiki/Special:BookSources/978-0134049847 "Special:BookSources/978-0134049847").
7. **[^](#cite_ref-11)** Muñoz, Mirna; Negrete Rodríguez, Mario (April 2021). "A guidance to implement or reinforce a DevOps approach in organizations: A case study". `{{[cite journal](/wiki/Template:Cite_journal "Template:Cite journal")}}`: Cite journal requires `|journal=` ([help](/wiki/Help:CS1_errors#missing_periodical "Help:CS1 errors"))
8. **[^](#cite_ref-12)** Chapman, M., Gatti, N: A model of a service life cycle, Proceedings of TINA '93, pp. I-205–I-215, Sep., 1993.
9. **[^](#cite_ref-13)** Atlassian. ["History of DevOps"](https://www.atlassian.com/devops/what-is-devops/history-of-devops). *Atlassian*. Retrieved 2023-02-23.
10. **[^](#cite_ref-14)** Mezak, Steve (25 January 2018). ["The Origins of DevOps: What's in a Name?"](https://devops.com/the-origins-of-devops-whats-in-a-name/). devops.com. Retrieved 6 May 2019.
11. **[^](#cite_ref-15)** Debois, Patrick (9 October 2008). ["Agile 2008 Toronto"](http://www.jedi.be/blog/2008/10/09/agile-2008-toronto-agile-infrastructure-and-operations-presentation/). Just Enough Documented Information. Retrieved 12 March 2015.
12. **[^](#cite_ref-16)** Debois, Patrick. ["DevOps Days"](http://www.devopsdays.org/). DevOps Days. Retrieved 31 March 2011.
13. ^ [***a***](#cite_ref-2016_State_of_DevOps_Report_17-0) [***b***](#cite_ref-2016_State_of_DevOps_Report_17-1) Alana Brown; Nicole Forsgren; Jez Humble; Nigel Kersten; Gene Kim (2016). ["2016 State of DevOps Report"](https://dora.dev/research/2017-and-earlier/2016-state-of-devops-report.pdf) (PDF). Puppet Labs, DORA (DevOps Research. Retrieved 2024-04-24.
14. **[^](#cite_ref-18)** ["Puppet - Alanna Brown"](https://puppet.com/people/alanna-brown). Puppet Labs. Retrieved 2019-04-27.
15. **[^](#cite_ref-19)** Nicole Forsgren; Gene Kim; Nigel Kersten; Jez Humble (2014). ["2014 State of DevOps Report"](https://dora.dev/research/2017-and-earlier/2014-state-of-devops-report.pdf) (PDF). Puppet Labs, IT Revolution Press and ThoughtWorks. Retrieved 2024-04-24.
16. **[^](#cite_ref-20)** ["2015 State of DevOps Report"](https://dora.dev/research/2017-and-earlier/2015-state-of-devops-report.pdf) (PDF). Puppet Labs, Pwc, IT Revolution Press. 2015. Retrieved 2024-04-24.
17. **[^](#cite_ref-21)** ["More Agile Testing"](https://agiletester.ca/wp-content/uploads/sites/26/2014/09/TOC.pdf) (PDF). October 2014. Retrieved 2019-05-06.
18. **[^](#cite_ref-22)** Crispin, Lisa; Gregory, Janet (October 2014). [*More Agile Testing*](https://www.oreilly.com/library/view/more-agile-testing/9780133749571/). Addison-Wesley. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [9780133749571](/wiki/Special:BookSources/9780133749571 "Special:BookSources/9780133749571"). Retrieved 2019-05-06.
19. **[^](#cite_ref-23)** Turner, Graham (20 November 2023). ["Report: Software Engineers Face Backlash for Reporting Wrongdoing"](https://www.digit.fyi/report-software-engineers-facing-retaliation-for-reporting-wrongdoing/). *DIGIT*. Retrieved 5 January 2024.
20. **[^](#cite_ref-24)** Saran, Cliff. ["Software engineers worry about speaking out - Computer Weekly"](https://www.computerweekly.com/news/366560292/Software-engineers-worry-about-speaking-out). *ComputerWeekly.com*. Retrieved 5 January 2024.
21. **[^](#cite_ref-25)** ["75% of software engineers faced retaliation the last time they reported wrongdoing - ETHRWorldSEA"](https://hrsea.economictimes.indiatimes.com/news/workplace/75-of-software-engineers-faced-retaliation-the-last-time-they-reported-wrongdoing/105335733). *ETHRWorld.com*.
22. **[^](#cite_ref-26)** Cummins, Holly. ["Holly Cummins on X"](https://twitter.com/holly_cummins/status/1448357917384744964). *X.com*. Retrieved 5 January 2024.
23. **[^](#cite_ref-2023_State_of_DevOps_Report_27-0)** DeBellis, Derek; Lewis, Amanda; Villalba, Daniella; Farley, Dave. ["2023 State of DevOps Report"](https://cloud.google.com/devops/state-of-devops). Google Cloud DevOps Research and Assessment. Retrieved 2024-04-24.
24. **[^](#cite_ref-Culture_is_everything_28-0)** DeBellis, Derek; Harvey, Nathan. ["2023 State of DevOps Report: Culture is everything"](https://cloud.google.com/blog/products/devops-sre/announcing-the-2023-state-of-devops-report). *Google Cloud Blog*. Retrieved 2024-04-24.
25. **[^](#cite_ref-29)** Klein, Brandon Thorin (2021-05-01). ["The DevOps: A Concise Understanding to the DevOps Philosophy and Science"](https://www.osti.gov/biblio/1785164/). *Osti.gov*. [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.2172/1785164](https://doi.org/10.2172%2F1785164). [OSTI](/wiki/OSTI_(identifier) "OSTI (identifier)") [1785164](https://www.osti.gov/biblio/1785164). [S2CID](/wiki/S2CID_(identifier) "S2CID (identifier)") [236606284](https://api.semanticscholar.org/CorpusID:236606284).
26. **[^](#cite_ref-30)** ["The History and Evolution of DevOps | Tom Geraghty"](https://tomgeraghty.co.uk/index.php/the-history-and-evolution-of-devops/). 5 July 2020. Retrieved 2020-11-29.
27. **[^](#cite_ref-31)** ["Principles behind the Agile Manifesto"](https://agilemanifesto.org/principles.html). *agilemanifesto.org*. Retrieved 2020-12-06.
28. **[^](#cite_ref-32)** Castellanos, Camilo; Correal, Dario (15 September 2018). "Executing Architectural Models for Big Data Analytics". *Software Architecture*. Lecture Notes in Computer Science. Vol. 11048. pp. 364–371. [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.1007/978-3-030-00761-4\_24](https://doi.org/10.1007%2F978-3-030-00761-4_24). [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-3-030-00760-7](/wiki/Special:BookSources/978-3-030-00760-7 "Special:BookSources/978-3-030-00760-7").
29. **[^](#cite_ref-33)** Humble, Jez; Farley, David (2011). *Continuous Delivery: reliable software releases through build, test, and deployment automation*. Pearson Education Inc. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-0-321-60191-9](/wiki/Special:BookSources/978-0-321-60191-9 "Special:BookSources/978-0-321-60191-9").
30. **[^](#cite_ref-34)** Chen, Lianping (2015). "Continuous Delivery: Huge Benefits, but Challenges Too". *IEEE Software*. **32** (2): 50–54. [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.1109/MS.2015.27](https://doi.org/10.1109%2FMS.2015.27). [S2CID](/wiki/S2CID_(identifier) "S2CID (identifier)") [1241241](https://api.semanticscholar.org/CorpusID:1241241).
31. **[^](#cite_ref-35)** Tak, Rohin; Modi, Jhalak (2018). *Mobile DevOps: Deliver continuous integration and deployment within your mobile applications*. Packt Publishing. pp. 12–18. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [9781788296243](/wiki/Special:BookSources/9781788296243 "Special:BookSources/9781788296243").
32. **[^](#cite_ref-36)** Beyer, Betsy; Jones, Chris; Petoff, Jennifer; Murphy, Niall Richard (April 2016). *Site Reliability Engineering*. O'Reilly Media. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-1-4919-2909-4](/wiki/Special:BookSources/978-1-4919-2909-4 "Special:BookSources/978-1-4919-2909-4").
33. **[^](#cite_ref-37)** [Analyzing the DNA of DevOps](https://opensource.com/article/18/11/analyzing-devops), Brent Aaron Reed, Willy Schaub, 2018-11-14.
34. **[^](#cite_ref-38)** Gene Kim; Patrick Debois; John Willis; Jezz Humble (2016). *The DevOps Handbook: How to Create World-Class Agility, Reliability, and Security in Technology Organizations*.
35. **[^](#cite_ref-39)** ["OWASP TOP10"](https://owasp.org/Top10/). [Archived](https://web.archive.org/web/20230608171837/https://owasp.org/Top10/) from the original on June 8, 2023. Retrieved June 8, 2023.
36. **[^](#cite_ref-40)** Wilson, Glenn (December 2020). *'DevSecOps: A leader's guide to producing secure software with compromising flow, feedback and continuous improvement'*. Rethink Press. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-1781335024](/wiki/Special:BookSources/978-1781335024 "Special:BookSources/978-1781335024").
37. **[^](#cite_ref-41)** Emerging Technology Analysis: DevOps a Culture Shift, Not a Technology (Report). Gartner.
38. **[^](#cite_ref-42)** Loukides, Mike (7 June 2012). ["What is DevOps?"](http://radar.oreilly.com/2012/06/what-is-devops.html). [O'Reilly Media](/wiki/O%27Reilly_Media "O'Reilly Media").
39. **[^](#cite_ref-43)** ["Gartner IT Glossary – devops"](http://www.gartner.com/it-glossary/devops/). *Gartner*. Retrieved 30 October 2015.
40. **[^](#cite_ref-44)** Jones, Stephen; Noppen, Joost; Lettice, Fiona (21 July 2016). [*Proceedings of the 2nd International Workshop on Quality-Aware DevOps - QUDOS 2016*](https://ueaeprints.uea.ac.uk/id/eprint/59131/4/Accepted_manuscript.pdf) (PDF). pp. 7–11. [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.1145/2945408.2945410](https://doi.org/10.1145%2F2945408.2945410). [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [9781450344111](/wiki/Special:BookSources/9781450344111 "Special:BookSources/9781450344111"). [S2CID](/wiki/S2CID_(identifier) "S2CID (identifier)") [515140](https://api.semanticscholar.org/CorpusID:515140).
41. **[^](#cite_ref-45)** Mandi Walls (25 September 2015). ["Building a DevOps culture"](https://www.oreilly.com/ideas/building-a-devops-culture). O'Reilly.
42. **[^](#cite_ref-46)** Chen, Lianping; Ali Babar, Muhammad (2014). "2014 IEEE/IFIP Conference on Software Architecture". *The 11th Working IEEE/IFIP Conference on Software Architecture(WICSA 2014)*. IEEE. pp. 195–204. [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.1109/WICSA.2014.45](https://doi.org/10.1109%2FWICSA.2014.45). [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-1-4799-3412-6](/wiki/Special:BookSources/978-1-4799-3412-6 "Special:BookSources/978-1-4799-3412-6").
43. **[^](#cite_ref-47)** Teja Yarlagadda, Ravi (9 March 2021). "DevOps and Its Practices". [SSRN](/wiki/SSRN_(identifier) "SSRN (identifier)") [3798877](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3798877).
44. **[^](#cite_ref-48)** Morisio, Maurizio (16 April 2021). [*DevOps: development of a toolchain in the banking domain*](https://webthesis.biblio.polito.it/18120/). *Politecnico di Torino* (laurea thesis). Retrieved 16 August 2021.
45. **[^](#cite_ref-49)** ["What is GitOps?"](https://www.redhat.com/en/topics/devops/what-is-gitops). *www.redhat.com*. Retrieved 2023-03-30.

Further reading[[edit](/w/index.php?title=DevOps&action=edit&section=19 "Edit section: Further reading")]
---------------------------------------------------------------------------------------------------------


* Davis, Jennifer; Daniels, Ryn (2016-05-30). *Effective DevOps : building a culture of collaboration, affinity, and tooling at scale*. Sebastopol, CA: O'Reilly. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [9781491926437](/wiki/Special:BookSources/9781491926437 "Special:BookSources/9781491926437"). [OCLC](/wiki/OCLC_(identifier) "OCLC (identifier)") [951434424](https://www.worldcat.org/oclc/951434424).


* Kim, Gene; Debois, Patrick; Willis, John; Humble, Jez; Allspaw, John (2015-10-07). *The DevOps handbook : how to create world-class agility, reliability, and security in technology organizations* (First ed.). Portland, OR. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [9781942788003](/wiki/Special:BookSources/9781942788003 "Special:BookSources/9781942788003"). [OCLC](/wiki/OCLC_(identifier) "OCLC (identifier)") [907166314](https://www.worldcat.org/oclc/907166314).`{{[cite book](/wiki/Template:Cite_book "Template:Cite book")}}`: CS1 maint: location missing publisher ([link](/wiki/Category:CS1_maint:_location_missing_publisher "Category:CS1 maint: location missing publisher"))


* Forsgren, Nicole; Humble, Jez; Kim, Gene (27 March 2018). *Accelerate: The Science of Lean Software and DevOps: Building and Scaling High Performing Technology Organizations* (First ed.). IT Revolution Press. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [9781942788331](/wiki/Special:BookSources/9781942788331 "Special:BookSources/9781942788331").




| * [v](/wiki/Template:Software_engineering "Template:Software engineering") * [t](/wiki/Template_talk:Software_engineering "Template talk:Software engineering") * [e](/wiki/Special:EditPage/Template:Software_engineering "Special:EditPage/Template:Software engineering") [Software engineering](/wiki/Software_engineering "Software engineering") | |
| --- | --- |
| Fields | * [Computer programming](/wiki/Computer_programming "Computer programming") * DevOps * [Empirical software engineering](/wiki/Empirical_software_engineering "Empirical software engineering") * [Experimental software engineering](/wiki/Experimental_software_engineering "Experimental software engineering") * [Formal methods](/wiki/Formal_methods "Formal methods") * [Requirements engineering](/wiki/Requirements_engineering "Requirements engineering") * [Search-based software engineering](/wiki/Search-based_software_engineering "Search-based software engineering") * [Site reliability engineering](/wiki/Site_reliability_engineering "Site reliability engineering") * [Social software engineering](/wiki/Social_software_engineering "Social software engineering") * [Software deployment](/wiki/Software_deployment "Software deployment") * [Software design](/wiki/Software_design "Software design") * [Software maintenance](/wiki/Software_maintenance "Software maintenance") * [Software testing](/wiki/Software_testing "Software testing") * [Systems analysis](/wiki/Systems_analysis "Systems analysis") |
| Concepts | * [Abstraction](/wiki/Abstraction_(computer_science) "Abstraction (computer science)") * [Component-based software engineering](/wiki/Component-based_software_engineering "Component-based software engineering") * [Software compatibility](/wiki/Computer_compatibility "Computer compatibility") 	+ [Backward compatibility](/wiki/Backward_compatibility "Backward compatibility") 	+ [Compatibility layer](/wiki/Compatibility_layer "Compatibility layer") 	+ [Compatibility mode](/wiki/Compatibility_mode "Compatibility mode") 	+ [Forward compatibility](/wiki/Forward_compatibility "Forward compatibility") 	+ [Software incompatibility](/wiki/Software_incompatibility "Software incompatibility") * [Data modeling](/wiki/Data_modeling "Data modeling") * [Enterprise architecture](/wiki/Enterprise_architecture "Enterprise architecture") * [Functional specification](/wiki/Functional_specification "Functional specification") * [Modeling language](/wiki/Modeling_language "Modeling language") * [Programming paradigm](/wiki/Programming_paradigm "Programming paradigm") * [Software](/wiki/Software "Software") * [Software archaeology](/wiki/Software_archaeology "Software archaeology") * [Software architecture](/wiki/Software_architecture "Software architecture") * [Software configuration management](/wiki/Software_configuration_management "Software configuration management") * [Software development process/methodology](/wiki/Software_development_process "Software development process") * [Software quality](/wiki/Software_quality "Software quality") * [Software quality assurance](/wiki/Software_quality_assurance "Software quality assurance") * [Software verification and validation](/wiki/Software_verification_and_validation "Software verification and validation") * [Software system](/wiki/Software_system "Software system") * [Structured analysis](/wiki/Structured_analysis "Structured analysis") 	+ [Essential analysis](/wiki/Essential_systems_analysis "Essential systems analysis") * [CI/CD](/wiki/CI/CD "CI/CD") |
| Orientations | * [Agile](/wiki/Agile_software_development "Agile software development") * [Aspect-oriented](/wiki/Aspect-oriented_programming "Aspect-oriented programming") * [Object orientation](/wiki/Object-oriented_programming "Object-oriented programming") * [Ontology](/wiki/Ontology_(information_science) "Ontology (information science)") * [Service orientation](/wiki/Service-oriented_architecture "Service-oriented architecture") * [SDLC](/wiki/Systems_development_life_cycle "Systems development life cycle") |
| Models | | Developmental | * [Agile](/wiki/Agile_software_development "Agile software development") * [EUP](/wiki/Enterprise_unified_process "Enterprise unified process") * [Executable UML](/wiki/Executable_UML "Executable UML") * [Incremental model](/wiki/Incremental_build_model "Incremental build model") * [Iterative model](/wiki/Iterative_and_incremental_development "Iterative and incremental development") * [Prototype model](/wiki/Software_prototyping "Software prototyping") * [RAD](/wiki/Rapid_application_development "Rapid application development") * [UP](/wiki/Unified_Process "Unified Process") * [Scrum](/wiki/Scrum_(software_development) "Scrum (software development)") * [Spiral model](/wiki/Spiral_model "Spiral model") * [V-model](/wiki/V-model_(software_development) "V-model (software development)") * [Waterfall model](/wiki/Waterfall_model "Waterfall model") * [XP](/wiki/Extreme_programming "Extreme programming") * [Model-driven engineering](/wiki/Model-driven_engineering "Model-driven engineering") * [Round-trip engineering](/wiki/Round-trip_engineering "Round-trip engineering") | | --- | --- | | Other | * [SPICE](/wiki/ISO/IEC_15504 "ISO/IEC 15504") * [CMMI](/wiki/Capability_Maturity_Model_Integration "Capability Maturity Model Integration") * [Data model](/wiki/Data_model "Data model") * [ER model](/wiki/Entity%E2%80%93relationship_model "Entity–relationship model") * [Function model](/wiki/Function_model "Function model") * [Information model](/wiki/Information_model "Information model") * [Metamodeling](/wiki/Metamodeling "Metamodeling") * [Object model](/wiki/Object_model "Object model") * [Systems model](/wiki/Systems_modeling "Systems modeling") * [View model](/wiki/View_model "View model") | | Languages | * [IDEF](/wiki/IDEF "IDEF") * [UML](/wiki/Unified_Modeling_Language "Unified Modeling Language") * [USL](/wiki/Universal_Systems_Language "Universal Systems Language") * [SysML](/wiki/Systems_modeling_language "Systems modeling language") | |
| Related fields | * [Computer science](/wiki/Computer_science "Computer science") * [Computer engineering](/wiki/Computer_engineering "Computer engineering") * [Information science](/wiki/Information_science "Information science") * [Project management](/wiki/Project_management "Project management") * [Risk management](/wiki/Risk_management "Risk management") * [Systems engineering](/wiki/Systems_engineering "Systems engineering") |
| * [Commons](https://commons.wikimedia.org/wiki/Category:Software_engineering "commons:Category:Software engineering") * [Category](/wiki/Category:Software_engineering "Category:Software engineering") | |

![](https://login.wikimedia.org/wiki/Special:CentralAutoLogin/start?type=1x1)
Retrieved from "<https://en.wikipedia.org/w/index.php?title=DevOps&oldid=1228043198>"
[Categories](/wiki/Help:Category "Help:Category"): * [Agile software development](/wiki/Category:Agile_software_development "Category:Agile software development")
* [Software development process](/wiki/Category:Software_development_process "Category:Software development process")
* [Information technology management](/wiki/Category:Information_technology_management "Category:Information technology management")
* [Software development](/wiki/Category:Software_development "Category:Software development")
Hidden categories: * [CS1 errors: missing periodical](/wiki/Category:CS1_errors:_missing_periodical "Category:CS1 errors: missing periodical")
* [Articles with short description](/wiki/Category:Articles_with_short_description "Category:Articles with short description")
* [Short description is different from Wikidata](/wiki/Category:Short_description_is_different_from_Wikidata "Category:Short description is different from Wikidata")
* [Wikipedia pending changes protected pages](/wiki/Category:Wikipedia_pending_changes_protected_pages "Category:Wikipedia pending changes protected pages")
* [CS1 maint: location missing publisher](/wiki/Category:CS1_maint:_location_missing_publisher "Category:CS1 maint: location missing publisher")

