import re

index_content = open('views/index.ejs', encoding='utf-8').read()

# Extract the <style> block from index.ejs (the one we added at the top)
style_regex = re.compile(r'(<style>\s*/\* Base Navigation Reset \*/.*?</style>)', re.DOTALL)
style_match = style_regex.search(index_content)
nav_style = style_match.group(1) if style_match else ''

# Extract the header block from index.ejs
header_regex = re.compile(r'(<header class="nm-nav-header".*?</header>)', re.DOTALL)
header_match = header_regex.search(index_content)
nav_header = header_match.group(1) if header_match else ''


header_partial = open('views/partials/header.ejs', encoding='utf-8').read()

# Replace the old topbar and site-header in header.ejs with the new one
# The old one starts at <div class="topbar-chintamani and ends at </header>
old_nav_regex = re.compile(r'<div class="topbar-chintamani top-utility-bar" id="topUtilityBar">.*?</header>', re.DOTALL)

# Insert the style just before the new header
new_nav = nav_style + '\n\n' + nav_header

header_partial = old_nav_regex.sub(new_nav, header_partial)

open('views/partials/header.ejs', 'w', encoding='utf-8').write(header_partial)
print("Updated header partial")
