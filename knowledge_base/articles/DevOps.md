


(Top)





1
Definition








2
History








3
Relationship to other approaches




Toggle Relationship to other approaches subsection





3.1
Agile








3.2
ArchOps








3.3
Continuous Integration and Delivery (CI/CD)








3.4
Mobile DevOps








3.5
Site-reliability engineering








3.6
Toyota production system, lean thinking, kaizen








3.7
DevSecOps, shifting security left










4
Cultural change




Toggle Cultural change subsection





4.1
Microservices








4.2
DevOps automation






4.2.1
Automation with version control












5
GitOps








6
See also








7
Notes








8
References








9
Further reading














3.1
Agile








3.2
ArchOps








3.3
Continuous Integration and Delivery (CI/CD)








3.4
Mobile DevOps








3.5
Site-reliability engineering








3.6
Toyota production system, lean thinking, kaizen








3.7
DevSecOps, shifting security left
























4.1
Microservices








4.2
DevOps automation






4.2.1
Automation with version control














4.2.1
Automation with version control




















DevOps is a methodology in the software development and IT industry. Used as a set of practices and tools, DevOps integrates and automates the work of software development (Dev) and IT operations (Ops) as a means for improving and shortening the systems development life cycle.[1] DevOps is complementary to agile software development; several DevOps aspects came from the agile way of working.

Automation is an important part of DevOps. Software programmers and architects should use "fitness functions" to keep their software in check.[2]

Other than it being a cross-functional combination (and a portmanteau) of the terms and concepts for "development" and "operations", academics and practitioners have not developed a universal definition for the term "DevOps".[a][b][c][d] Most often, DevOps is characterized by key principles: shared ownership, workflow automation, and rapid feedback.
From an academic perspective, Len Bass, Ingo Weber, and Liming Zhu—three computer science researchers from the CSIRO and the Software Engineering Institute—suggested defining DevOps as "a set of practices intended to reduce the time between committing a change to a system and the change being placed into normal production, while ensuring high quality".[6]
However, the term is used in multiple contexts. At its most successful, DevOps is a combination of specific practices, culture change, and tools.[7]

Proposals to combine software development methodologies with deployment and operations concepts began to appear in the late 80s and early 90s.[8]

Around 2007 and 2008, concerns were raised by those within the software development and IT communities that the separation between the two industries, where one wrote and created software entirely separate from those that deploy and support the software was creating a fatal level of dysfunction within the industry.[9]

In 2009, the first conference named DevOps Days was held in Ghent, Belgium. The conference was founded by Belgian consultant, project manager and agile practitioner Patrick Debois.[10][11] The conference has now spread to other countries.[12]

In 2012, a report called "State of DevOps" was first published by Alanna Brown at Puppet Labs.[13][14]

As of 2014, the annual State of DevOps report was published by Nicole Forsgren, Gene Kim, Jez Humble and others. They stated that the adoption of DevOps was accelerating.[15][16] Also in 2014, Lisa Crispin and Janet Gregory wrote the book More Agile Testing, containing a chapter on testing and DevOps.[17][18]

In 2016, the DORA metrics for throughput (deployment frequency, lead time for changes), and stability (mean time to recover, change failure rate) were published in the State of DevOps report.[13] However, the research methodology and metrics were criticized by experts.[19][20][21][22] In response to these criticisms, the 2023 State of DevOps report [23] published changes that updated the stability metric "mean time to recover" to "failed deployment recovery time" acknowledging the confusion the former metric has caused.[24]

Many of the ideas fundamental to DevOps practices are inspired by, or mirror, other well known practices such as Lean and Deming's Plan-Do-Check-Act cycle, through to The Toyota Way and the Agile approach of breaking down components and batch sizes.[25] Contrary to the "top-down" prescriptive approach and rigid framework of ITIL in the 1990s, DevOps is "bottom-up" and flexible, having been created by software engineers for their own needs.[26]

The motivations for what has become modern DevOps and several standard DevOps practices such as automated build and test, continuous integration, and continuous delivery originated in the Agile world, which dates (informally) to the 1990s, and formally to 2001. Agile development teams using methods such as extreme programming couldn't "satisfy the customer through early and continuous delivery of valuable software"[27] unless they took responsibility for operations and infrastructure for their applications, automating much of that work. Because Scrum emerged as the dominant Agile framework in the early 2000s and it omitted the engineering practices that were part of many Agile teams, the movement to automate operations and infrastructure functions splintered from Agile and expanded into what has become modern DevOps. Today, DevOps focuses on the deployment of developed software, whether it is developed using Agile oriented methodologies or other methodologies.

ArchOps presents an extension for DevOps practice, starting from software architecture artifacts, instead of source code, for operation deployment.[28] ArchOps states that architectural models are first-class entities in software development, deployment, and operations.

Automation is a core principle for achieving DevOps success and CI/CD is a critical component.[29] Plus, improved collaboration and communication between and within teams helps achieve faster time to market, with reduced risks.[30]

Mobile DevOps is a set of practices that applies the principles of DevOps specifically to the development of mobile applications. Traditional DevOps focuses on streamlining the software development process in general, but mobile development has its own unique challenges that require a tailored approach.[31] Mobile DevOps is not simply as a branch of DevOps specific to mobile app development, instead an extension and reinterpretation of the DevOps philosophy due to very specific requirements of the mobile world.

In 2003, Google developed site reliability engineering (SRE), an approach for releasing new features continuously into large-scale high-availability systems while maintaining high-quality end-user experience.[32] While SRE predates the development of DevOps, they are generally viewed as being related to each other.

Toyota production system, also known under the acronym TPS, was the inspiration for lean thinking with its focus on continuous improvement, kaizen, flow and small batches. The andon cord principle to create fast feedback, swarm and solve problems stems from TPS.[33][34]

DevSecOps is an augmentation of DevOps to allow for security practices to be integrated into the DevOps approach. Contrary to a traditional centralized security team model, each delivery team is empowered to factor in the correct security controls into their software delivery. Security practices and testing are performed earlier in the development lifecycle, hence the term "shift left". Security is tested in three main areas: static, software composition, and dynamic.

Checking software statically via static application security testing (SAST) is white-box testing with special focus on security. Depending on the programming language, different tools are needed to do such static code analysis. The software composition is analyzed, especially libraries, and the version of each component is checked against vulnerability lists published by CERT and other expert groups. When giving software to clients, library licenses and their match to the license of the software distributed are in focus, especially copyleft licenses.

In dynamic testing, also called black-box testing, software is tested without knowing its inner functions. In DevSecOps this practice may be referred to as dynamic application security testing (DAST) or penetration testing. The goal is early detection of defects including cross-site scripting and SQL injection vulnerabilities. Threat types are published by the open web application security project, e.g. its TOP10,[35] and by other bodies. 

DevSecOps has also been described as a cultural shift involving a holistic approach to producing secure software by integrating security education, security by design, and security automation.[36]

DevOps initiatives can create cultural changes in companies[37] by transforming the way operations, developers, and testers collaborate during the development and delivery processes.[38] Getting these groups to work cohesively is a critical challenge in enterprise DevOps adoption.[39][40] DevOps is as much about culture as it is about the toolchain.[41]

Although in principle it is possible to practice DevOps with any architectural style, the microservices architectural style is becoming the standard for building continuously deployed systems. Small size service allows the architecture of an individual service to emerge through continuous refactoring.[42]

It also supports consistency, reliability, and efficiency within the organization, and is usually enabled by a shared code repository or version control. As DevOps researcher Ravi Teja Yarlagadda hypothesizes, "Through DevOps, there is an assumption that all functions can be carried out, controlled, and managed in a central place using a simple code."[43]

Many organizations use version control to power DevOps automation technologies like virtual machines, containerization (or OS-level virtualization), and CI/CD. The paper "DevOps: development of a toolchain in the banking domain" notes that with teams of developers working on the same project, "All developers need to make changes to the same codebase and sometimes edit even the same files. For efficient working, there has to be a system that helps engineers avoid conflicts and retain the codebase history,"[44] with the Git version control system and the GitHub platform referenced as examples.

GitOps evolved from DevOps. The specific state of deployment configuration is version-controlled. Because the most popular version-control is Git, GitOps' approach has been named after Git. Changes to configuration can be managed using code review practices, and can be rolled back using version-controlling. Essentially, all of the changes to a code are tracked, bookmarked, and making any updates to the history can be made easier. As explained by Red Hat, "visibility to change means the ability to trace and reproduce issues quickly, improving overall security."[45]

DataOps
DevOps toolchain
Twelve-factor app
Infrastructure as code
Lean software development
Site reliability engineering
Value stream
List of build automation software

^ Dyck et al. (2015) "To our knowledge, there is no uniform definition for the terms release engineering and DevOps. As a consequence, many people use their own definitions or rely on others, which results in confusion about those terms."[3]

^ Jabbari et al. (2016) "The research results of this study showed the need for a definition as individual studies do not consistently define DevOps."[4]

^ Erich et al. (2017) "We noticed that there are various gaps in the study of DevOps: There is no consensus of what concepts DevOps covers, nor how DevOps is defined."[5]

^ Erich et al. (2017) "We discovered that there exists little agreement about the characteristics of DevOps in the academic literature."[5]


Agile software developmentSoftware development processInformation technology managementSoftware development
CS1 errors: missing periodicalArticles with short descriptionShort description is different from WikidataWikipedia pending changes protected pagesCS1 maint: location missing publisher




