import requests
from bs4 import BeautifulSoup
import csv

def scrape_comments(url):
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    review_blocks = soup.find_all("span", {"data-hook": "review-body"})
    comments = [r.get_text(strip=True) for r in review_blocks]

    if not comments:
        raise Exception("No comments found. Amazon might be blocking the request.")

    filename = "scraped_comments.csv"
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Review"])
        for c in comments:
            writer.writerow([c])

    return filename
