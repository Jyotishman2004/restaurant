import glob
from bs4 import BeautifulSoup

for file in glob.glob("*.html"):
    with open(file, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
    
    print(f"--- {file} ---")
    
    # Check a tags with href="#"
    links = soup.find_all("a", href="#")
    for a in links:
        print(f"Empty link: {a.text.strip()} | classes: {' '.join(a.get('class', []))} | aria: {a.get('aria-label')}")
        
    # Check buttons without onclick or type=submit or id used by JS
    buttons = soup.find_all("button")
    for b in buttons:
        if not b.get("onclick") and b.get("type") != "submit" and b.get("id") not in ["mobile-menu-btn", "close-mobile-menu-btn"]:
            print(f"Static button: {b.text.strip()} | classes: {' '.join(b.get('class', []))} | aria: {b.get('aria-label')}")
