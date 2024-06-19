# run script with command: python knowledge_base/scraper.py

# import required modules
import requests
from bs4 import BeautifulSoup
import markdownify as md

article_titles = ["Agile_software_development","Software_development","Software_development_process","Scrum_(software_development)","Iterative_and_incremental_development","Waterfall_model","Feature-driven_development","V-model_(software_development)","DevOps","Systems_development_life_cycle","Software_craftsmanship","Scott_Ambler","Timeboxing","Unit_testing","Test-driven_development","Pair_programming","Stand-up_meeting","Continuous_integration","Code_refactoring","Rolling-wave_planning","Change_control_board","Risk_management","PDCA","Dynamic_systems_development_method","Rational_unified_process","Agile_modeling","Agile_unified_process","Disciplined_agile_delivery","Extreme_programming","Lean_software_development","Lean_startup","Kanban_(development)","Rapid_application_development","Scrumban","Acceptance_test-driven_development","Agile_testing","Behavior-driven_development","Planning_poker","Retrospective","Specification_by_example","User_story","Velocity_(software_development)","Product_backlog","Technical_debt","Story-driven_modeling","Unified_Modeling_Language","Distributed_agile_software_development","Refinement_(computing)","Test_automation","Project_management_triangle","Extreme_project_management","Project_team","Business_agility","Management_fad","Alistair_Cockburn","Project_management","Fail-fast_system","Build_light_indicator"]

for article in article_titles:
    print(article)
    url = f'https://en.wikipedia.org/wiki/{article}'
    page = requests.get(url)

    # parse the content
    soup = BeautifulSoup(page.content, 'html.parser')

    # find the content text
    # Typically, Wikipedia articles are within <div id="content">, and the main article text is within <div id="bodyContent">
    content_div = soup.find('div', id='bodyContent')

    # convert HTML to markdown
    markdown_content = md.markdownify(str(content_div))

    # save to markdown file
    with open(f'knowledge_base/articles/{article}.md', 'w', encoding='utf-8') as file:
        file.write(markdown_content)