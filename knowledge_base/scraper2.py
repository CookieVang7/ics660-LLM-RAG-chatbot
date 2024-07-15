import requests
from bs4 import BeautifulSoup
import markdownify as md

article_titles = ["Agile_software_development"]

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

    combined_content = ""

    # The tags selected are ones I found generally make up the bulk of the article's content - avoiding side content
    for thing in soup.select('p, ol, ul, tbody'):
        combined_content += thing.getText() + "\n"

    markdown_content = md.markdownify(combined_content)

    with open(f'knowledge_base/root_article/{article}.md', 'w', encoding='utf-8') as file:
        file.write(markdown_content)

    print(f"Article {article} saved to markdown.")