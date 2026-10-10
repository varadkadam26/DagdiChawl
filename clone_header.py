import re

index_content = open('views/index.ejs', encoding='utf-8').read()

# 1. Extract style block
style_regex = re.compile(r'(<style>\s*body, html \{.*?</style>)', re.DOTALL)
style_match = style_regex.search(index_content)
nav_style = style_match.group(1) if style_match else ''

# 2. Extract header block
header_regex = re.compile(r'(<!-- HD Animated Header -->\s*<header class="nm-nav-header".*?</header>)', re.DOTALL)
header_match = header_regex.search(index_content)
nav_header = header_match.group(1) if header_match else ''

if not nav_style or not nav_header:
    print("Could not find style or header!")
    exit(1)

# 3. Read partials/header.ejs
header_partial = open('views/partials/header.ejs', encoding='utf-8').read()

# 4. Replace from <!-- Mandal Top Header Banner --> to </header>
old_header_regex = re.compile(r'<!-- Mandal Top Header Banner -->.*?</header>', re.DOTALL)
replacement = nav_style + '\n\n' + nav_header

new_partial = old_header_regex.sub(replacement, header_partial)

open('views/partials/header.ejs', 'w', encoding='utf-8').write(new_partial)
print("Successfully cloned full header to all pages")
