import requests
from bs4 import BeautifulSoup
import markdownify as md

#article_titles = ["Agile_software_development"]
article_titles = ["Agile_software_development","Software_development","Software_development_process","Scrum_(software_development)","Iterative_and_incremental_development","Waterfall_model","Feature-driven_development","V-model_(software_development)","DevOps","Systems_development_life_cycle","Software_craftsmanship","Scott_Ambler","Timeboxing","Unit_testing","Test-driven_development","Pair_programming","Stand-up_meeting","Continuous_integration","Code_refactoring","Rolling-wave_planning","Change_control_board","Risk_management","PDCA","Dynamic_systems_development_method","Rational_unified_process","Agile_modeling","Agile_unified_process","Disciplined_agile_delivery","Extreme_programming","Lean_software_development","Lean_startup","Kanban_(development)","Rapid_application_development","Scrumban","Acceptance_test-driven_development","Agile_testing","Behavior-driven_development","Planning_poker","Retrospective","Specification_by_example","User_story","Velocity_(software_development)","Product_backlog","Technical_debt","Story-driven_modeling","Unified_Modeling_Language","Distributed_agile_software_development","Refinement_(computing)","Test_automation","Project_management_triangle","Extreme_project_management","Project_team","Business_agility","Management_fad","Alistair_Cockburn","Project_management","Fail-fast_system","Build_light_indicator"]

for article in article_titles:
    print(f"Processing article: {article}")
    url = f'https://en.wikipedia.org/wiki/{article}'
    page = requests.get(url)

    # Parse the content
    soup = BeautifulSoup(page.content, 'html.parser')

    # Find and remove the references and external links sections
    for reference in soup.find_all('span', {'id': ['References', 'External_links']}):
        parent = reference.find_parent('h2')
        if parent:
            for sibling in parent.find_next_siblings():
                sibling.decompose()
            parent.decompose()

    # Find and remove the footer-info and footer-places html sections
    for reference in soup.find_all('ul', {'id': ['footer-info', 'footer-places']}):
        parent = reference.find_parent('footer')
        if parent:
            for sibling in parent.find_next_siblings():
                sibling.decompose()
            parent.decompose()

    # Find and remove the footer-info and footer-places html sections
    for reference in soup.find_all('ul', {'class': 'vector-menu-content-list'}):
        parent = reference.find_parent('div')
        if parent:
            for sibling in parent.find_next_siblings():
                sibling.decompose()
            parent.decompose()

    combined_content = ""

    # The tags selected are ones I found generally make up the bulk of the article's content - avoiding side content
    for thing in soup.select('p, ol, ul, tbody'):
        combined_content += thing.getText() + "\n"

    markdown_content = md.markdownify(combined_content)

    with open(f'knowledge_base/articles/{article}.md', 'w', encoding='utf-8') as file:
        file.write(markdown_content)

    print(f"Article {article} saved to markdown.")