import re
import glob

# 1. Get the footer from index.html
with open("index.html", "r", encoding="utf-8") as f:
    index_content = f.read()

footer_match = re.search(r'<!-- Footer -->\s*<footer.*?</footer>', index_content, re.DOTALL)
if footer_match:
    footer = footer_match.group(0)
    
    for file in ["gallery.html", "story.html"]:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            
        # For gallery.html, replace the empty footer block
        if file == "gallery.html":
            content = re.sub(r'<!-- Embed established dark footer from previous screens -->\s*<div class="mt-8 border-t border-outline-variant/30 pt-8 opacity-80">\s*</div>', footer, content, flags=re.DOTALL)
        # For story.html, replace its existing footer
        elif file == "story.html":
            content = re.sub(r'<!-- Footer -->\s*<footer.*?</footer>', footer, content, flags=re.DOTALL)
            
        with open(file, "w", encoding="utf-8") as f:
            f.write(content)
            
print("Footers unified.")
