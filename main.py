import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

def fetch_schemes(base_url, max_pages, stop_text):
    """
    Fetch government schemes from india.gov.in.

    Parameters:
    - base_url (str): The base URL for the website.
    - max_pages (int): Maximum number of pages to scrape.
    - stop_text (str): The text to stop scraping further.

    Returns:
    - List[dict]: A list of dictionaries containing scheme information.
    """
    catalogue = []

    for x in range(max_pages):
        url = f'{base_url}/my-government/schemes?page={x}'

        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')

        # Extract scheme titles
        content = soup.find_all('div', class_='views-field views-field-title')

        for stuff in content:
            a_tag = stuff.find('a')
            if a_tag:
                if a_tag.string == stop_text:
                    return catalogue
                else:
                    scheme_data = extract_scheme_details(base_url, a_tag['href'])
                    if scheme_data:
                        catalogue.append(scheme_data)
        print(f'Page {x + 1} processed. Total Schemes Found: {len(catalogue)}')
        time.sleep(2)
    return catalogue

def extract_scheme_details(base_url, relative_link):
    """
    Extract details of a specific scheme.

    Parameters:
    - base_url (str): The base URL for the website.
    - relative_link (str): The relative link to the scheme details page.

    Returns:
    - dict: A dictionary containing scheme information.
    """
    full_link = base_url + relative_link
    r = requests.get(full_link)
    soup = BeautifulSoup(r.content, 'html.parser')

    # Extract scheme details
    contents_of_scheme = soup.find('ol', class_='result-page main_data')
    if contents_of_scheme:
        ext_link = contents_of_scheme.find('a')['href']
        description = contents_of_scheme.find('p').text

        return {
            'Scheme': a_tag.string,
            'External Link': ext_link,
            'Description': description,
            'Backup Link': full_link
        }
    return None

if __name__ == "__main__":
    BASE_URL = 'https://www.india.gov.in'
    MAX_PAGES = 194
    STOP_TEXT = 'New Millennium Indian Technology Leadership Initiative by CSIR'

    catalogue = fetch_schemes(BASE_URL, MAX_PAGES, STOP_TEXT)

    # Convert to DataFrame and save as CSV
    df = pd.DataFrame(catalogue)
    df.to_csv('catalogue.csv', index=False)
    print("Data saved to 'catalogue.csv'")
