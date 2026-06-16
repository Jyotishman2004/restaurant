import re
import glob

# First, extract the header from index.html
with open("index.html", "r", encoding="utf-8") as f:
    index_content = f.read()

header_match = re.search(r'<!-- Top Navigation Structure \(Desktop & Mobile\) -->\s*<header.*?</header>', index_content, re.DOTALL)
if not header_match:
    print("Could not find header in index.html")
    exit(1)

new_header = header_match.group(0)

# Apply it to the remaining files
files_to_fix = ["menu.html", "reservation.html", "contact.html", "confirmation.html"]

for file in files_to_fix:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace TopAppBar with the new header
    # The existing header might be preceded by <!-- TopAppBar -->
    content = re.sub(r'<!-- TopAppBar -->\s*<header.*?</header>', new_header, content, flags=re.DOTALL)
    
    # Also, some might not have <!-- TopAppBar --> but just a <header> that starts with class="fixed...
    # Let's ensure it's replaced.
    if new_header not in content:
        content = re.sub(r'<header class="fixed top-0[^>]*>.*?</header>', new_header, content, flags=re.DOTALL)
        
    with open(file, "w", encoding="utf-8") as f:
        f.write(content)

print("Headers replaced successfully.")
