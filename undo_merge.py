import re

content_header = open('views/partials/header.ejs', encoding='utf-8').read()

# Revert background
content_header = re.sub(
    r"background: transparent;",
    "background: <%= currentTabName === 'home' ? 'rgba(0,0,0,0.2)' : 'rgba(21, 19, 15, 0.7)' %>;",
    content_header
)

# Revert opacity
content_header = re.sub(
    r"opacity: <%= \(currentTabName === 'home' \|\| currentTabName === 'about'\) \? '0' : '1' %>;",
    "opacity: <%= currentTabName === 'home' ? '0' : '1' %>;",
    content_header
)

open('views/partials/header.ejs', 'w', encoding='utf-8').write(content_header)


content_about = open('views/about.ejs', encoding='utf-8').read()

# Revert padding-top
content_about = re.sub(
    r'\n  \.page-hero-banner \{\n    padding-top: 180px !important;\n  \}',
    '',
    content_about
)

open('views/about.ejs', 'w', encoding='utf-8').write(content_about)
print("Undone merge")
