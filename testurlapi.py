# Import necessary libraries for web scraping.
import requests
import re
from bs4 import BeautifulSoup

def fetch_and_parse_url(url):
    """Fetches a URL, handles errors, and returns a BeautifulSoup object."""
    # Use a try-except block to gracefully handle network errors or bad responses.
    try:
        response = requests.get(url, timeout=10)
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()
        # Parse the HTML content of the page.
        return BeautifulSoup(response.text, 'html.parser')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return None

def main():
    """Main function to run the web scraper."""
    url = 'https://www.blogdepelis.cc/los-4-fantasticos-primeros-pasos.html'
    # Fetch and parse the URL.
    soup = fetch_and_parse_url(url)

    if soup:
        # Extract the title of the page.
        title = soup.title.string if soup.title else "No Title Found"

        # Extract and clean text
        # Get all the text from the page and use a regular expression to clean up extra whitespace.
        raw_text = soup.get_text(strip=True)
        cleaned_text = re.sub(r'\{3,}', '\n\n', raw_text)

        print(title, '\n')
        print(cleaned_text)

# Standard Python entry point to run the main function.
if __name__ == "__main__":
    main()