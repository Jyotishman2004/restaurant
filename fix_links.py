import os
import re

directory = r"e:\Allwebsites\newinpro"

# Fix index.html
with open(os.path.join(directory, "index.html"), "r", encoding="utf-8") as f:
    content = f.read()
content = re.sub(r'href="#"([^>]*>)\s*<span class="">View Our Menu', r'href="menu.html"\1\n<span class="">View Our Menu', content)
content = re.sub(r'href="#"([^>]*>\s*View Full Menu\s*</a>)', r'href="menu.html"\1', content)
with open(os.path.join(directory, "index.html"), "w", encoding="utf-8") as f:
    f.write(content)

# Fix menu.html
with open(os.path.join(directory, "menu.html"), "r", encoding="utf-8") as f:
    content = f.read()
content = re.sub(r'href="#">The Menu', r'href="menu.html">The Menu', content)
content = re.sub(r'href="#">Reservations', r'href="reservation.html">Reservations', content)
with open(os.path.join(directory, "menu.html"), "w", encoding="utf-8") as f:
    f.write(content)

# Fix confirmation.html
with open(os.path.join(directory, "confirmation.html"), "r", encoding="utf-8") as f:
    content = f.read()
# Replace href="#" that contains "Return to Home" or "Back to Home"
content = re.sub(r'href="#"([^>]*>\s*<span[^>]*>Return to Home)', r'href="index.html"\1', content, flags=re.IGNORECASE)
with open(os.path.join(directory, "confirmation.html"), "w", encoding="utf-8") as f:
    f.write(content)

print("Links fixed.")
