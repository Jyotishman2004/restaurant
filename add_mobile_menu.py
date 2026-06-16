import os
import glob
import re

html_files = glob.glob("*.html")

mobile_menu_code = """
<!-- Mobile Navigation Drawer -->
<div id="mobile-menu-drawer" class="fixed inset-0 bg-background/95 backdrop-blur-xl z-[60] transform translate-x-full transition-transform duration-300 flex flex-col pt-20 px-8 md:hidden">
    <button id="close-mobile-menu-btn" aria-label="Close Menu" class="absolute top-5 left-6 text-on-surface-variant hover:text-primary transition-colors">
        <span class="material-symbols-outlined text-[28px]">close</span>
    </button>
    <div class="flex justify-center mb-12">
        <span class="font-display-lg-mobile text-2xl tracking-widest text-primary">EMBER &amp; GRAIN</span>
    </div>
    <div class="flex flex-col gap-8 items-center mt-4">
        <a href="index.html" class="font-label-caps text-lg uppercase tracking-[0.2em] text-on-background hover:text-primary transition-colors">Home</a>
        <a href="menu.html" class="font-label-caps text-lg uppercase tracking-[0.2em] text-on-background hover:text-primary transition-colors">Menu</a>
        <a href="story.html" class="font-label-caps text-lg uppercase tracking-[0.2em] text-on-background hover:text-primary transition-colors">Our Story</a>
        <a href="gallery.html" class="font-label-caps text-lg uppercase tracking-[0.2em] text-on-background hover:text-primary transition-colors">Gallery</a>
        <a href="reservation.html" class="mt-8 px-10 py-4 border border-primary-container text-primary-container font-label-caps text-sm uppercase tracking-widest hover:bg-primary-container hover:text-on-primary-container transition-all">Reserve</a>
    </div>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const menuBtns = document.querySelectorAll('button[aria-label="Menu"]');
        const closeBtn = document.getElementById('close-mobile-menu-btn');
        const drawer = document.getElementById('mobile-menu-drawer');
        
        if (drawer && closeBtn) {
            menuBtns.forEach(btn => {
                btn.addEventListener('click', () => {
                    drawer.classList.remove('translate-x-full');
                });
            });
            
            closeBtn.addEventListener('click', () => {
                drawer.classList.add('translate-x-full');
            });
        }
    });
</script>
</body>
"""

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Avoid injecting multiple times
    if 'id="mobile-menu-drawer"' not in content:
        content = content.replace('</body>', mobile_menu_code)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Mobile menu added to all files.")
