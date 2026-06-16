import glob
import re

for file in glob.glob("*.html"):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # Fix Shopping Bag buttons
    content = re.sub(r'(<button[^>]*aria-label="Shopping Bag"[^>]*)>', r'\1 onclick="alert(\'Your shopping bag is currently empty.\')">', content)

    # Fix Gallery filter buttons (if they don't have onclick)
    if "gallery.html" in file:
        content = re.sub(r'(<button[^>]*>)\s*All\s*</button>', r'\1 All </button>', content) # All is already active usually, but let's just add alert to all
        content = re.sub(r'(<button class="snap-start[^>]*)(>)(\s*(?:All|Dishes|Ambience|Events)\s*</button>)', r'\1 onclick="alert(\'Photo filtering coming soon!\')"\2\3', content)

    # Fix Menu filter buttons
    if "menu.html" in file:
        content = re.sub(r'(<button class="font-label-caps[^>]*)(>)(\s*(?:Starters|Mains|Desserts|Drinks)\s*</button>)', r'\1 onclick="alert(\'Menu filtering coming soon!\')"\2\3', content)
        content = content.replace('href="#">Private Dining', 'href="contact.html">Private Dining')
        
    # Fix Social Links
    content = content.replace('href="#" aria-label="Instagram"', 'href="https://instagram.com/" target="_blank" aria-label="Instagram"')
    content = content.replace('href="#" aria-label="Facebook"', 'href="https://facebook.com/" target="_blank" aria-label="Facebook"')
    content = content.replace('href="#" aria-label="TripAdvisor"', 'href="https://tripadvisor.com/" target="_blank" aria-label="TripAdvisor"')
    # And specifically for text links like "IG", "FB"
    content = re.sub(r'href="#"([^>]*>)\s*IG\s*</a>', r'href="https://instagram.com/" target="_blank"\1 IG </a>', content)
    content = re.sub(r'href="#"([^>]*>)\s*FB\s*</a>', r'href="https://facebook.com/" target="_blank"\1 FB </a>', content)
    content = re.sub(r'href="#"([^>]*>)\s*TA\s*</a>', r'href="https://tripadvisor.com/" target="_blank"\1 TA </a>', content)

    # Fix story.html bottom nav which might have been missed
    if "story.html" in file:
        content = re.sub(r'href="#"([^>]*>\s*<span[^>]*>home)', r'href="index.html"\1', content)
        content = re.sub(r'href="#"([^>]*>\s*<span[^>]*>restaurant_menu)', r'href="menu.html"\1', content)
        content = re.sub(r'href="#"([^>]*>\s*<span[^>]*>calendar_month)', r'href="reservation.html"\1', content)
        content = re.sub(r'href="#"([^>]*>\s*<span[^>]*>auto_stories)', r'href="story.html"\1', content)

    with open(file, "w", encoding="utf-8") as f:
        f.write(content)

print("Buttons fixed.")
