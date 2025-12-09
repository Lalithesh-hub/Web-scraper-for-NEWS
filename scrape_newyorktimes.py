import requests
from bs4 import BeautifulSoup

def scrape_article(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')

        title_tag = soup.find('h1')
        title = title_tag.get_text(strip=True) if title_tag else 'No Title Found'

        paragraphs = soup.find_all('p')
        content= ' '.join([para.get_text(strip=True) for para in paragraphs])

        
        return {   
            "url": url,
            "title": title,
            "content": content
        }
    except requests.exceptions.RequestException as e:
        return {
            "url": url,
            "title": "Error",
            "content": str(e)
        }
    except Exception as e:
        return {
            "url": url,
            "title": "Error",
            "content": f"An error occurred: {str(e)}"
        }