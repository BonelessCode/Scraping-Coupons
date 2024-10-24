# Web Scraper for SimplyCodes

## Overview
This project is a **web scraper** built using Python that extracts and organizes relevant data related to SimplyCodes website, a coupon code website specifically designed for deals and discounts using coupons. The tool scrapes relevant discount information and stores it in a structured HTML file for easy access.

It also includes a GitHub Actions workflow that runs the scraper at scheduled intervals, checks for changes in coupon data, and sends notifications via email and Slack if any changes are detected.

## Features
- Scrapes coupon codes from chosen pages on SimplyCodes
- Extracts discount percentages, coupon codes, and store names
- Sends notifications via email and Slack when new coupon codes or changes are detected.
- Automated daily checks using GitHub Actions.
- Utilizes **Selenium** and **BeautifulSoup** for web interaction and parsing

## Setup Instructions

### Prerequisites
Make sure you have the following installed:
1. **Python 3.x** – You can download it from [Python's official website](https://www.python.org/downloads/).
2. **Pip** – Python package manager (should come pre-installed with Python).

### Install Required Dependencies
To install the necessary Python libraries, navigate to the project's root directory and run the following command:

```bash
pip install -r requirements.txt
```

The required packages can be found in the `requirements.txt` file, which includes:
- `requests`
- `beautifulsoup4`
- `selenium`

### Geckodriver Setup
You'll need **geckodriver** for Selenium to automate the browser interaction. Make sure to have it in your `PATH` or download it manually from [Mozilla's website](https://github.com/mozilla/geckodriver/releases).

Once downloaded, place the `geckodriver.exe` file in the same directory or configure the system path accordingly.

### How to Run the Scraper
To execute the web scraper, simply run the following command:

```bash
python scrapper.py
```

This will start the scraper and generate an HTML file with the extracted discount codes.

### Example Output
The output of the scraper will be an HTML file that contains well-organized information about current active discount codes, similar to this:

- **Store Name:** Chanel
- **Best Discount:** 35% off store-wide until 29/09 !
- **Coupon Codes:** CARDTM, SAVE20, CHRISTMAS etc.

The output file is used in Github Actions Workflow to notify you of the coupon updates on the website.

### GitHub Actions Workflow
This repository includes a GitHub Actions workflow that automates the coupon-checking process. The workflow runs the scraper at scheduled intervals (thrice a day), compares the current coupon data with the previous check's data, and sends notifications if changes are detected.

Workflow File: .github/workflows/daily_coupon_check.yml

### Customization
- Currently, it is targetted toward the "Cotton Carrier" page of SimplyCodes, but you can easily modify the scraping logic by editing `scrapper.py` to target different pages or additional data fields.

## Summary
This project provides an automated solution to gather and display coupon codes from various websites in a clean HTML format, with a GitHub Actions integration for daily checks and notifications. The workflow will notify you of any changes via email or Slack, keeping you updated.
