



From Wikipedia, the free encyclopedia




|  | The topic of this article **may not meet Wikipedia's [general notability guideline](/wiki/Wikipedia:Notability "Wikipedia:Notability")**. Please help to demonstrate the notability of the topic by citing [reliable secondary sources](/wiki/Wikipedia:Reliable_sources "Wikipedia:Reliable sources") that are [independent](/wiki/Wikipedia:Independent_sources "Wikipedia:Independent sources") of the topic and provide significant coverage of it beyond a mere trivial mention. If notability cannot be shown, the article is likely to be [merged](/wiki/Wikipedia:Merging "Wikipedia:Merging"), [redirected](/wiki/Wikipedia:Redirect "Wikipedia:Redirect"), or [deleted](/wiki/Wikipedia:Deletion_policy "Wikipedia:Deletion policy").*Find sources:* ["Build light indicator"](https://www.google.com/search?as_eq=wikipedia&q=%22Build+light+indicator%22) – [news](https://www.google.com/search?tbm=nws&q=%22Build+light+indicator%22+-wikipedia&tbs=ar:1) **·** [newspapers](https://www.google.com/search?&q=%22Build+light+indicator%22&tbs=bkt:s&tbm=bks) **·** [books](https://www.google.com/search?tbs=bks:1&q=%22Build+light+indicator%22+-wikipedia) **·** [scholar](https://scholar.google.com/scholar?q=%22Build+light+indicator%22) **·** [JSTOR](https://www.jstor.org/action/doBasicSearch?Query=%22Build+light+indicator%22&acc=on&wc=on) *(August 2012)* *([Learn how and when to remove this message](/wiki/Help:Maintenance_template_removal "Help:Maintenance template removal"))* |
| --- | --- |


[![](//upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Series_of_build_lights.jpg/220px-Series_of_build_lights.jpg)](/wiki/File:Series_of_build_lights.jpg)

A series of build lights applied to processes such as [unit testing](/wiki/Unit_testing "Unit testing") in addition to an actual build


A **build light indicator** is a simple visual indicator used in [Agile software development](/wiki/Agile_software_development "Agile software development") to inform a team of [software developers](/wiki/Software_developers "Software developers") about the current status of their project. The actual object used can vary from a [pressure gauge](/wiki/Pressure_gauge "Pressure gauge") to a [lava lamp](/wiki/Lava_lamp "Lava lamp"), but its purpose remains the same: to quickly communicate whether a software process (such as a ['build'](/wiki/Software_build "Software build")) is successful or not.




History[[edit](/w/index.php?title=Build_light_indicator&action=edit&section=1 "Edit section: History")]
-------------------------------------------------------------------------------------------------------


The build light indicator originated from [CruiseControl](/wiki/CruiseControl "CruiseControl"),[*[citation needed](/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")*] a continuous integration tool created by employees of [ThoughtWorks](/wiki/ThoughtWorks "ThoughtWorks"). Though it primarily functioned as a web page dashboard that could report more detailed information about a build, the software could also control external devices for simpler reporting.[[1]](#cite_note-Cohn2009-1)



Use[[edit](/w/index.php?title=Build_light_indicator&action=edit&section=2 "Edit section: Use")]
-----------------------------------------------------------------------------------------------


The traditional use of a build light is to determine the success of a [software build](/wiki/Software_build "Software build") in a [continuous integration](/wiki/Continuous_integration "Continuous integration") (CI) system.[[2]](#cite_note-Orb-2) Different development teams have used different indicators, but a popular choice is the green and red lava lamp – green when the build is successful and red when something is wrong.[[3]](#cite_note-Collier2011-3) Build lights may even be remotely accessible through a [webcam](/wiki/Webcam "Webcam") or other means.[[4]](#cite_note-4) However, since many of the tests in busy development offices will always be in a state of re-test after the latest changes, some indicators have a [three state](/wiki/Three-state_logic "Three-state logic") display[[2]](#cite_note-Orb-2) – *pass*, *fail* and *being re-tested*, to provide a more nuanced indicator for staff and managers.[[5]](#cite_note-5)



### Beyond single indicators[[edit](/w/index.php?title=Build_light_indicator&action=edit&section=3 "Edit section: Beyond single indicators")]


With the growth from continuous integration to [continuous testing](/wiki/Continuous_testing "Continuous testing"), the number of simultaneous build targets may increase, even for a single codebase. As well as a simple build (i.e. compilation) target, there will now be [unit testing](/wiki/Unit_testing "Unit testing") and various levels of system testing. As extensive tests are slow and it is desirable to keep fast tests running on a fast cycle to give rapid feedback to the developers, the number of build targets may increase to fifty or more. This is too many to show with a simple lava lamp display. Integration servers like [Jenkins](/wiki/Jenkins_(software) "Jenkins (software)") offer a web-accessible dashboard page and this may be permanently displayed on a wall-mounted flat screen monitor instead. The details of such a dashboard are too small to read across an office, but the colour changes present an overall picture of status.


With a methodology of [continuous test-driven development](/wiki/Continuous_test-driven_development "Continuous test-driven development"), new tests are released before working code is developed to pass them. There is thus a period when some tests are known, and indeed *required* to be failing.[[6]](#cite_note-6) Failing tests are needed as they demonstrate the capability of the new tests to detect the situation of concern. Once the new code is developed and working, these tests begin to pass. A continuous testing environment into which new tests are released before their code thus requires two build targets: one tracks the latest code and tests, the other 'release candidate' is only updated in increments when all tests are fulfilled by passing code. For the build indicator this also implies that one of those targets will frequently be shown as "failing" its tests. As this anticipated "failure" would be misleading to naive watchers, the build indicator should either hide it or present it distinctly.


Where several code targets, such as old product versions, are still supported for CI, but are not under such active development, then a complete dashboard may become dominated by "stale" targets that rarely change. In this case a selected dashboard may be more appropriate, where only those targets that are either failing, or are recently active, are displayed. The full dashboard is available to developer's desktops, but the wall display shows only the significant highlights. Such dashboards are often coded locally by [screen-scraping](/wiki/Screen-scraping "Screen-scraping") the main dashboard and applying relevant local filters to it, according to local needs. One drawback to a dynamic filtered dashboard, compared to a static dashboard, is that the position of icons for a particular target may shift on the screen, making it hard to read from across an office. In this case, distinctive icons, such as a product logo, may be displayed rather than simple colour blocks.



References[[edit](/w/index.php?title=Build_light_indicator&action=edit&section=4 "Edit section: References")]
-------------------------------------------------------------------------------------------------------------




![](//upload.wikimedia.org/wikipedia/en/thumb/4/4a/Commons-logo.svg/30px-Commons-logo.svg.png)
Wikimedia Commons has media related to [Build light indicators](https://commons.wikimedia.org/wiki/Category:Build_light_indicators "commons:Category:Build light indicators").


1. **[^](#cite_ref-Cohn2009_1-0)** Mike Cohn (10 July 2009). [*Succeeding with Agile: Software Development Using Scrum*](https://books.google.com/books?id=8IglA6i_JwAC&pg=PT245). Pearson Education. pp. 245–. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-0-321-57936-2](/wiki/Special:BookSources/978-0-321-57936-2 "Special:BookSources/978-0-321-57936-2"). Retrieved 23 August 2011.
2. ^ [***a***](#cite_ref-Orb_2-0) [***b***](#cite_ref-Orb_2-1) ["The Orb - Build Indicator Lamp"](https://web.archive.org/web/20100611004354/http://www.agileskunkworks.org/Articles/TheOrbBuildIndicatorLamp/tabid/114/Default.aspx). *agileskunkworks.org*. Archived from [the original](http://www.agileskunkworks.org/Articles/TheOrbBuildIndicatorLamp/tabid/114/Default.aspx) on June 11, 2010.
3. **[^](#cite_ref-Collier2011_3-0)** Ken W. Collier (27 July 2011). [*Agile Analytics: A Value-Driven Approach to Business Intelligence and Data Warehousing*](https://books.google.com/books?id=YMR3HynGQjUC&pg=PA281). Addison-Wesley. pp. 281–. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-0-321-50481-4](/wiki/Special:BookSources/978-0-321-50481-4 "Special:BookSources/978-0-321-50481-4"). Retrieved 23 August 2011.
4. **[^](#cite_ref-4)** Karsten, Paul; Cannizzo, Fabrizzio (2007). ["The Creation of a Distributed Agile Team"](http://dl.acm.org/citation.cfm?id=1769014). *Agile Processes in Software Engineering and Extreme Programming*. Lecture Notes in Computer Science. Vol. 4536. [Association for Computing Machinery](/wiki/Association_for_Computing_Machinery "Association for Computing Machinery"). pp. 235–239. [doi](/wiki/Doi_(identifier) "Doi (identifier)"):[10.1007/978-3-540-73101-6\_44](https://doi.org/10.1007%2F978-3-540-73101-6_44). [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [978-3-540-73100-9](/wiki/Special:BookSources/978-3-540-73100-9 "Special:BookSources/978-3-540-73100-9").
5. **[^](#cite_ref-5)** [Build Light – Continuous Delivery meets Reengineering an[sic](http://blog.comsysto.com/2013/09/09/build-light-continuous-delivery-meets-reengineering-an-usb-driver/) USB driver] [Archived](https://web.archive.org/web/20130915063407/http://blog.comsysto.com/2013/09/09/build-light-continuous-delivery-meets-reengineering-an-usb-driver/) September 15, 2013, at the [Wayback Machine](/wiki/Wayback_Machine "Wayback Machine") - Bernd Zuther, comSysto GmbH, 2013
6. **[^](#cite_ref-6)** Madeyski, L.; Kawalerowicz, M. (4–6 July 2013). *Continuous Test-Driven Development - A Novel Agile Software Development Practice and Supporting Tool*. Proc. 8th International Conference on Evaluation of Novel Approaches to Software Engineering (ENASE). Angers, France. p. 262.




![](https://login.wikimedia.org/wiki/Special:CentralAutoLogin/start?type=1x1)
Retrieved from "<https://en.wikipedia.org/w/index.php?title=Build_light_indicator&oldid=1173785154>"
[Category](/wiki/Help:Category "Help:Category"): * [Agile software development](/wiki/Category:Agile_software_development "Category:Agile software development")
Hidden categories: * [Webarchive template wayback links](/wiki/Category:Webarchive_template_wayback_links "Category:Webarchive template wayback links")
* [Articles with topics of unclear notability from August 2012](/wiki/Category:Articles_with_topics_of_unclear_notability_from_August_2012 "Category:Articles with topics of unclear notability from August 2012")
* [All articles with topics of unclear notability](/wiki/Category:All_articles_with_topics_of_unclear_notability "Category:All articles with topics of unclear notability")
* [All articles with unsourced statements](/wiki/Category:All_articles_with_unsourced_statements "Category:All articles with unsourced statements")
* [Articles with unsourced statements from April 2017](/wiki/Category:Articles_with_unsourced_statements_from_April_2017 "Category:Articles with unsourced statements from April 2017")
* [Commons category link is on Wikidata](/wiki/Category:Commons_category_link_is_on_Wikidata "Category:Commons category link is on Wikidata")

