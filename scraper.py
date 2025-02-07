import requests
from bs4 import BeautifulSoup

def scrape_webpage(url: str, max_paragraphs: int = 15) -> str:
    """
    Fetches the given URL and extracts text content from its paragraphs.
    Limits the amount of text to the specified max_paragraphs for brevity.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        collected_text = [p.get_text(strip=True) for p in paragraphs[:max_paragraphs]]
        return "\n".join(collected_text)
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return ""
