import requests
from bs4 import BeautifulSoup

def get_logo_url(website_url):
    try:
        response = requests.get(website_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Look for common logo tags
        logo = soup.find('link', rel='shortcut icon') or soup.find('link', rel='icon')

        if logo:
            return logo['href']
        else:
            return None
    except Exception as e:
        print(f"Error fetching logo: {e}")
        return None
