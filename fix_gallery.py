import os
import re

directory = r"e:\Allwebsites\newinpro"

# 1. Extract header from index.html
with open(os.path.join(directory, "index.html"), "r", encoding="utf-8") as f:
    index_content = f.read()

header_match = re.search(r'<header.*?</header>', index_content, re.DOTALL)
if header_match:
    universal_header = header_match.group(0)
else:
    raise Exception("Could not find header in index.html")

def fix_page(filename):
    path = os.path.join(directory, filename)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace header
    content = re.sub(r'<header.*?</header>', universal_header, content, flags=re.DOTALL)
    
    # Remove md:hidden from body
    content = content.replace('<body class="bg-background text-on-background font-body-md antialiased md:hidden', '<body class="bg-background text-on-background font-body-md antialiased')
    
    # Remove any un-rendered template variables
    content = content.replace('{{DATA:SCREEN:SCREEN_4}}', '')
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

fix_page("gallery.html")
fix_page("story.html")
print("Fixed gallery.html and story.html")
