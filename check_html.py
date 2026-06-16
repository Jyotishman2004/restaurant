import sys
from bs4 import BeautifulSoup
import re

def check_html(filename):
    print(f"--- Checking {filename} ---")
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # 1. Check for basic structure
    if len(soup.find_all('html')) != 1: print("Warning: Multiple or missing <html> tags")
    if len(soup.find_all('head')) != 1: print("Warning: Multiple or missing <head> tags")
    if len(soup.find_all('body')) != 1: print(f"Warning: Multiple or missing <body> tags. Count: {len(soup.find_all('body'))}")
    
    # 2. Check for duplicate IDs
    ids = [tag.get('id') for tag in soup.find_all(id=True)]
    duplicate_ids = set([id for id in ids if ids.count(id) > 1])
    if duplicate_ids:
        print(f"Warning: Duplicate IDs found: {duplicate_ids}")
        
    # 3. Check for multiple headers
    if len(soup.find_all('header')) > 1:
        print(f"Warning: Multiple <header> tags found ({len(soup.find_all('header'))})")

    # 4. Check for broken or empty links (we already did, but let's double check)
    empty_links = [a for a in soup.find_all('a') if a.get('href') == '#' or not a.get('href')]
    if empty_links:
        print(f"Warning: {len(empty_links)} empty or '#' links found")

    # 5. Check missing styles/scripts
    if 'output.css' not in html:
        print("Warning: output.css is missing!")
        
    # 6. Check for tailwind setup (we removed CDN right?)
    if 'cdn.tailwindcss.com' in html:
        print("Warning: Tailwind CDN is still present!")

    # 7. Check for nested forms or buttons (which are invalid HTML)
    nested_buttons = soup.find_all(lambda tag: tag.name in ['button', 'a'] and tag.find(['button', 'a']))
    if nested_buttons:
        print("Warning: Nested interactive elements found (button inside button, or a inside button)")

    print("Check complete.\n")

check_html('index.html')
check_html('gallery.html')
