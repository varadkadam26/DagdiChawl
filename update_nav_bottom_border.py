import re

content = open('views/partials/header.ejs', encoding='utf-8').read()

# Replace border-bottom: none; in .nm-nav-header
content = re.sub(
    r'\.nm-nav-header \{([^}]*)border-bottom:\s*none;([^}]*)\}',
    r'.nm-nav-header {\1border-bottom: 2px solid rgba(212, 175, 55, 0.9); box-shadow: 0 4px 20px rgba(212, 175, 55, 0.6);\2}',
    content
)

open('views/partials/header.ejs', 'w', encoding='utf-8').write(content)
print("Updated main nav border")
