import glob

search_str = '<a class="font-label-caps text-label-caps text-on-surface-variant hover:text-primary transition-colors duration-300 uppercase" href="menu.html">Menu</a>'
replace_str = '<a class="font-label-caps text-label-caps text-on-surface-variant hover:text-primary transition-colors duration-300 uppercase" href="index.html">Home</a>\n<a class="font-label-caps text-label-caps text-on-surface-variant hover:text-primary transition-colors duration-300 uppercase" href="menu.html">Menu</a>'

for file in glob.glob("*.html"):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
        
    if search_str in content and '<a class="font-label-caps text-label-caps text-on-surface-variant hover:text-primary transition-colors duration-300 uppercase" href="index.html">Home</a>' not in content:
        content = content.replace(search_str, replace_str)
        with open(file, "w", encoding="utf-8") as f:
            f.write(content)

print("Home button added to navigation bar.")
