import requests
from bs4 import BeautifulSoup

def scrape_html_elements(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    data_elements = []

    # Example 1: Scraping text from a specific element by its CSS selector
    element1 = soup.select_one('h1.title')
    if element1:
        data_elements.append(element1.text)

    # Example 2: Scraping multiple elements by tag name
    elements = soup.find_all('a')[:5]
    for element in elements:
        data_elements.append(element.text)

    # Example 3: Scraping attribute value from an element
    element3 = soup.select_one('img.logo')
    if element3:
        src = element3['src']
        data_elements.append(src)

    return data_elements

# Example usage
url = "https://example.com"  # Replace with your desired URL
scraped_data = scrape_html_elements(url)
for data in scraped_data:
    print(data)

