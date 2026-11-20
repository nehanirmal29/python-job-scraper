"""Scrape job listings from the Fake Python Jobs site and save them to a CSV file."""

import csv
import sys

import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
OUTPUT_FILE = "jobs.csv"
FIELDS = ["title", "company", "location", "url"]


def fetch_page(url):
    """Download the page and return its HTML."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as error:
        sys.exit(f"Could not fetch {url}: {error}")
    return response.text


def get_text(parent, selector):
    """Return the text of the first matching element, or '' if it is missing."""
    element = parent.select_one(selector)
    return element.get_text(strip=True) if element else ""


def get_job_url(card):
    """Return the job page link (the 'Apply' link), or '' if it is missing."""
    for link in card.select("footer a[href]"):
        if link.get_text(strip=True).lower() == "apply":
            return link["href"]
    return ""


def parse_jobs(html):
    """Turn the page HTML into a list of jobs."""
    soup = BeautifulSoup(html, "html.parser")
    jobs = []
    for card in soup.select("div.card-content"):
        job = {
            "title": get_text(card, "h2.title"),
            "company": get_text(card, "h3.company"),
            "location": get_text(card, "p.location"),
            "url": get_job_url(card),
        }
        if any(job.values()):
            jobs.append(job)
    return jobs


def save_to_csv(jobs, filename):
    """Write the jobs to a CSV file."""
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(jobs)


def main():
    html = fetch_page(URL)
    jobs = parse_jobs(html)
    if not jobs:
        sys.exit("No jobs found. The page layout may have changed.")
    save_to_csv(jobs, OUTPUT_FILE)
    print(f"Saved {len(jobs)} jobs to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()