import glob

script = """
<script>
    document.addEventListener('DOMContentLoaded', () => {
        // Handle all shopping bag buttons
        const allButtons = document.querySelectorAll('button');
        allButtons.forEach(b => {
            if (b.textContent.includes('shopping_bag') || b.getAttribute('aria-label') === 'Shopping Bag') {
                b.addEventListener('click', (e) => {
                    e.preventDefault();
                    alert('Your shopping bag is currently empty.');
                });
            }
        });

        // Handle all remaining # links
        const emptyLinks = document.querySelectorAll('a[href="#"]');
        emptyLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const aria = link.getAttribute('aria-label') || '';
                const text = link.textContent || '';
                if (aria.includes("Instagram") || text.includes("IG") || text.includes("Instagram")) {
                    window.open("https://instagram.com/emberandgrain", "_blank");
                } else if (aria.includes("Facebook") || text.includes("FB")) {
                    window.open("https://facebook.com/emberandgrain", "_blank");
                } else if (aria.includes("TripAdvisor") || text.includes("TA")) {
                    window.open("https://tripadvisor.com/", "_blank");
                } else {
                    alert("This feature is coming soon!");
                }
            });
        });
    });
</script>
</body>
"""

for file in glob.glob("*.html"):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # Ensure we don't inject multiple times
    if "Handle all shopping bag buttons" not in content:
        content = content.replace("</body>", script)
        with open(file, "w", encoding="utf-8") as f:
            f.write(content)

print("Dynamic JS handlers injected.")
