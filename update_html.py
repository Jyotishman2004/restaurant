import glob
import re

html_files = glob.glob("*.html")

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove the CDN script
    content = re.sub(
        r'<script src="https://cdn\.tailwindcss\.com\?[^"]*"></script>',
        '',
        content
    )
    
    # Remove the tailwind-config script block entirely
    content = re.sub(
        r'<script id="tailwind-config">.*?</script>',
        '',
        content,
        flags=re.DOTALL
    )

    # Insert the stylesheet link right before </head>
    if '<link href="output.css" rel="stylesheet">' not in content and '<link rel="stylesheet" href="output.css">' not in content:
        content = content.replace('</head>', '    <link href="output.css" rel="stylesheet">\n</head>')
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated all HTML files!")
