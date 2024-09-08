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

first_static_data = soup.find('span', class_='body-2 truncate uppercase')
second_static_data = soup.find('p', class_='body-2 text-gray-60 dark:text-white mt-8')

# Extract content
first_content = first_static_data.text if first_static_data else 'No content found'
second_content = second_static_data.text if second_static_data else 'No content found'

# Print the contents
print(f"First content: {first_content}")
print(f"Second content: {second_content}")

# Write the output to the GitHub Actions environment file
with open(os.getenv('GITHUB_ENV', ''), 'a') as f:
    f.write(f'FIRST_CONTENT={first_content}\n')
    f.write(f'SECOND_CONTENT={second_content}\n')
