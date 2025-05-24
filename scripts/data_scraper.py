#!/usr/bin/env python3
import sys
import requests
from bs4 import BeautifulSoup
import json
import datetime

def scrape_data(url):
    """
    Scrape the given URL and extract sample data.
    For demonstration purposes, this script extracts the page title.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as e:
        print(f"Error fetching the URL: {e}")
        sys.exit(1)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract the title as a sample indicator
    title = soup.title.string if soup.title else "No Title Found"
    
    data = {
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "url": url,
        "extracted_title": title,
        "source": "Public Web Page"
    }
    
    return data

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python data_scraper.py --url <URL>")
        sys.exit(1)
    
    url = sys.argv[2] if sys.argv[1] == "--url" else None
    if not url:
        print("Please provide a valid URL.")
        sys.exit(1)
    
    scraped_data = scrape_data(url)
    print("Scraped Data:")
    print(json.dumps(scraped_data, indent=2))
