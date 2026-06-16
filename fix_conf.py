import os

directory = r"e:\Allwebsites\newinpro"
for filename in ["confirmation.html"]:
    path = os.path.join(directory, filename)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    content = content.replace('href="#"', 'href="index.html"')
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("done")
