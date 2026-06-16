import os
import shutil
import re

src_dir = r"E:\Allwebsites\newinpro\stitch_ember_grain_restaurant_design\stitch_ember_grain_restaurant_design"
dest_dir = r"E:\Allwebsites\newinpro"

pages = {
    "hero_with_signature_dishes_ember_grain": "index.html",
    "menu_animated_ember_grain": "menu.html",
    "our_story_animated_ember_grain": "story.html",
    "gallery_animated_ember_grain": "gallery.html",
    "reservations_animated_ember_grain": "reservation.html",
    "reservation_confirmation_ember_grain": "confirmation.html",
    "contact_animated_ember_grain": "contact.html"
}

def update_html(content, current_page):
    # Desktop Nav links
    content = re.sub(r'href="#"([^>]*)>Menu</a>', r'href="menu.html"\1>Menu</a>', content)
    content = re.sub(r'href="#"([^>]*)>Our Story</a>', r'href="story.html"\1>Our Story</a>', content)
    content = re.sub(r'href="#"([^>]*)>Gallery</a>', r'href="gallery.html"\1>Gallery</a>', content)
    content = re.sub(r'href="#"([^>]*)>Reserve</a>', r'href="reservation.html"\1>Reserve</a>', content)
    
    # Desktop Logo link
    content = re.sub(
        r'<span([^>]*)>EMBER &amp; GRAIN</span>',
        r'<a href="index.html"\1>EMBER &amp; GRAIN</a>',
        content
    )
    
    # Mobile Bottom Nav
    # Home
    content = re.sub(
        r'<button([^>]*)>(\s*<span[^>]*>home</span>\s*<span[^>]*>Home</span>\s*)</button>',
        r'<a href="index.html"\1>\2</a>',
        content, flags=re.IGNORECASE
    )
    # Menu
    content = re.sub(
        r'<button([^>]*)>(\s*<span[^>]*>restaurant_menu</span>\s*<span[^>]*>Menu</span>\s*)</button>',
        r'<a href="menu.html"\1>\2</a>',
        content, flags=re.IGNORECASE
    )
    # Book
    content = re.sub(
        r'<button([^>]*)>(\s*<span[^>]*>calendar_month</span>\s*<span[^>]*>Book</span>\s*)</button>',
        r'<a href="reservation.html"\1>\2</a>',
        content, flags=re.IGNORECASE
    )
    # Story
    content = re.sub(
        r'<button([^>]*)>(\s*<span[^>]*>auto_stories</span>\s*<span[^>]*>Story</span>\s*)</button>',
        r'<a href="story.html"\1>\2</a>',
        content, flags=re.IGNORECASE
    )

    # Any other generic "Reserve a Table" buttons that might need to go to reservation
    content = re.sub(r'<button([^>]*)>\s*Reserve a Table\s*</button>', r'<a href="reservation.html"\1>Reserve a Table</a>', content)

    # Fix relative paths to images if necessary? Not needed since they are absolute URLs mostly (https://lh3.googleusercontent.com/...)
    
    return content

def main():
    for src_folder, dest_filename in pages.items():
        src_path = os.path.join(src_dir, src_folder, "code.html")
        dest_path = os.path.join(dest_dir, dest_filename)
        
        if not os.path.exists(src_path):
            print(f"Warning: {src_path} does not exist.")
            continue
            
        with open(src_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        updated_content = update_html(content, dest_filename)
        
        with open(dest_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
            
        print(f"Created {dest_filename}")

if __name__ == "__main__":
    main()
