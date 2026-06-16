import glob

script = """
<script>
document.addEventListener('DOMContentLoaded', () => {
    // Shopping bags
    const bags = document.querySelectorAll('button[aria-label="Shopping Bag"], button:has(span:contains("shopping_bag"))');
    bags.forEach(b => {
        b.addEventListener('click', (e) => {
            e.preventDefault();
            alert('Your shopping bag is currently empty.');
        });
    });

    // Handle generic href="#"
    const emptyLinks = document.querySelectorAll('a[href="#"]');
    emptyLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const aria = link.getAttribute('aria-label');
            if (aria === "Instagram" || link.textContent.includes("IG") || link.textContent.includes("Instagram")) {
                window.open("https://instagram.com/emberandgrain", "_blank");
            } else if (aria === "Facebook" || link.textContent.includes("FB")) {
                window.open("https://facebook.com/emberandgrain", "_blank");
            } else if (aria === "TripAdvisor" || link.textContent.includes("TA")) {
                window.open("https://tripadvisor.com/", "_blank");
            } else {
                alert("Coming soon!");
            }
        });
    });
});
</script>
"""

# I need to change :has(span:contains) because :contains is not valid CSS, only jQuery.
# Let's use pure JS instead.
