# Python Job Listings Scraper

A Python script that collects job listings from the practice website [Fake Python Jobs](https://realpython.github.io/fake-jobs/) and saves them to a CSV file.

## What it collects

For each job it saves:

- Job title
- Company name
- Location
- Link to the job detail page

If a field is missing on the page, the script saves an empty value instead of crashing.

## How to install

1. Install Python 3.9 or newer.
2. Install the libraries:

```
pip install -r requirements.txt
```

## How to run

```
python scraper.py
```

The script creates a file named `jobs.csv` in the same folder. You should see this message:

```
Saved 100 jobs to jobs.csv
```

## Tools used

- Python
- Requests (downloads the web page)
- Beautiful Soup (reads the HTML)
- csv module (saves the results)

## What I learned

- How to inspect a web page and find the HTML tags and classes to scrape.
- How to download a page with Requests and read it with Beautiful Soup.
- How to handle missing fields and network errors.
- How to save data to a CSV file.

## Note

This website is built for practice, so it has no anti-scraping protection. Real websites are harder and may have rules about scraping.
