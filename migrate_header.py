import re

index_content = open('views/index.ejs', encoding='utf-8').read()

# 1. Extract the new CSS and header from index.ejs
style_regex = re.compile(r'(<style>\s*body, html \{.*?</style>)', re.DOTALL)
style_match = style_regex.search(index_content)
nav_style = style_match.group(1) if style_match else ''

header_regex = re.compile(r'(<!-- HD Animated Header -->\s*<header class="nm-nav-header".*?</header>)', re.DOTALL)
header_match = header_regex.search(index_content)
nav_header = header_match.group(1) if header_match else ''

if not nav_style or not nav_header:
    print("Could not find style or header in index.ejs")
    exit(1)

# 2. Remove them from index.ejs
index_content = index_content.replace(nav_style, '')
index_content = index_content.replace(nav_header, '')

# Save cleaned index.ejs
open('views/index.ejs', 'w', encoding='utf-8').write(index_content)


# 3. Replace old header in partials/header.ejs
header_partial = open('views/partials/header.ejs', encoding='utf-8').read()

# The old header consists of everything from <!-- Mandal Top Header Banner --> to </header>
old_header_regex = re.compile(r'<!-- Mandal Top Header Banner -->.*?</header>', re.DOTALL)

replacement = nav_style + '\n\n' + nav_header

header_partial = old_header_regex.sub(replacement, header_partial)

open('views/partials/header.ejs', 'w', encoding='utf-8').write(header_partial)
print("Migration complete")
