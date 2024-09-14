import requests
from bs4 import BeautifulSoup
import os

# Get the current script directory
current_dir = os.path.dirname(os.path.abspath(__file__))

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

# Locate the 'best-deal-section' first
best_deal_section = soup.find('section', id='best-deal-section')

# If the section is found, then find the required elements within it
if best_deal_section:
    zeroth_static_data = best_deal_section.find('h4', class_=['text-left', 'capitalize', 'truncate', 'select-none', 'subheadline-2'])
    first_static_data = best_deal_section.find('span', class_=['body-2', 'truncate', 'uppercase'])

    second_static_data = best_deal_section.find('p', class_=['mt-8', 'body-2', 'text-gray-60', 'dark:text-white'])
else:
    zeroth_static_data = None
    first_static_data = None
    second_static_data = None

# Extract content
discount = zeroth_static_data.text if zeroth_static_data else 'No content found'
code = first_static_data.text if first_static_data else 'No content found'
description = second_static_data.text if second_static_data else 'No content found'

# Print the contents
print(f"Discount: {discount}")
print(f"Code: {code}")
print(f"Description: {description}")


# Save the content to an HTML file
output_dir = os.path.join(current_dir, 'output/html')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save the content to an HTML file
#output_file_path = os.path.join(current_dir, 'output/output.html')
output_file_path = os.path.join(current_dir, 'output/html/output_brotector.html')
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(soup.text)

print(f'Page content saved to {output_file_path}')

# Write the output to the GitHub Actions environment file
with open(os.getenv('GITHUB_ENV', ''), 'a') as f:
    f.write(f'COUPON_DISCOUNT={discount}\n')    
    f.write(f'COUPON_CODE={code}\n')
    f.write(f'COUPON_DESCRIPTION={description}\n')
