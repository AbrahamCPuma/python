import requests
import re
from bs4 import BeautifulSoup

def fetch_and_parse_url(url):
    """Fetches a URL, handles errors, and returns a BeautifulSoup object."""
    try:
        response = requests.get(url, timeout=10)
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return None

def main():
    """Main function to run the web scraper."""
    url = 'https://www.blogdepelis.cc/los-4-fantasticos-primeros-pasos.html'
    soup = fetch_and_parse_url(url)

    if soup:
        title = soup.title.string if soup.title else "No Title Found"

        # Extract and clean text
        raw_text = soup.get_text(strip=True)
        cleaned_text = re.sub(r'\{3,}', '\n\n', raw_text)

        print(title, '\n')
        print(cleaned_text)

if __name__ == "__main__":
    main()