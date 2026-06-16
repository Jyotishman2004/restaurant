import glob
import re

for file in glob.glob("*.html"):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # Generic fix for shopping_bag
    content = re.sub(r'<button[^>]*>\s*<span class="material-symbols-outlined">shopping_bag</span>\s*</button>', r'<button aria-label="Shopping Bag" onclick="alert(\'Your shopping bag is currently empty.\')" class="text-on-surface-variant hover:text-primary transition-colors duration-300">\n<span class="material-symbols-outlined">shopping_bag</span>\n</button>', content)

    # Generic fix for missing social href="#"
    content = re.sub(r'href="#"([^>]*aria-label="Instagram")', r'href="https://instagram.com/emberandgrain" target="_blank"\1', content)
    content = re.sub(r'href="#"([^>]*>\s*Instagram\s*</a>)', r'href="https://instagram.com/emberandgrain" target="_blank"\1', content)
    
    # Generic fix for All gallery filter
    content = re.sub(r'<button([^>]*>\s*All\s*</button>)', r'<button onclick="alert(\'Photo filtering coming soon!\')"\1', content)

    # Remove extra duplicates of onClick if I ran it multiple times
    content = content.replace('onclick="alert(\'Your shopping bag is currently empty.\')" onclick', 'onclick')

    with open(file, "w", encoding="utf-8") as f:
        f.write(content)

print("Second pass complete.")
