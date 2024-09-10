import requests
from bs4 import BeautifulSoup
import os

# Headers to avoid bot detection
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Fetch and parse the page
url = 'https://simplycodes.com/store/cottoncarrier.com'
response = requests.get(url, headers=headers)

if response.status_code == 429:
    print("Rate limited. Try again after", response.headers.get('Retry-After'))
    exit()

soup = BeautifulSoup(response.text, 'html.parser')


zeroth_static_data = soup.find('h4', class_='subheadline-2 capitalize select-none truncate text-left')
first_static_data = soup.find('span', class_='body-2 truncate uppercase')
second_static_data = soup.find('p', class_='body-2 text-gray-60 dark:text-white mt-8')

# Extract content
discount = zeroth_static_data.text if zeroth_static_data else 'No content found'
code = first_static_data.text if first_static_data else 'No content found'
description = second_static_data.text if second_static_data else 'No content found'

# Print the contents
print(f"Discount: {discount}")
print(f"Code: {code}")
print(f"Description: {description}")

# Write the output to the GitHub Actions environment file
with open(os.getenv('GITHUB_ENV', ''), 'a') as f:
    f.write(f'COUPON_DISCOUNT={discount}\n')    
    f.write(f'COUPON_CODE={code}\n')
    f.write(f'COUPON_DESCRIPTION={description}\n')
