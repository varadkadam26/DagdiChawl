import re

index_content = open('views/index.ejs', encoding='utf-8').read()

# Get the CSS for the top bar and glass switch
style_regex = re.compile(r'(<style>\s*/\* Base Navigation Reset \*/.*?</style>)', re.DOTALL)
style_match = style_regex.search(index_content)
nav_style = style_match.group(1) if style_match else ''

# Extract the <div class="nm-top-bar"> block from index.ejs
topbar_regex = re.compile(r'(<!-- Pre-Header \(Top Bar\) -->\s*<div class="nm-top-bar".*?</div>\s*</div>)', re.DOTALL)
topbar_match = topbar_regex.search(index_content)
new_topbar = topbar_match.group(1) if topbar_match else ''


header_partial = open('views/partials/header.ejs', encoding='utf-8').read()

# Replace the topbar-chintamani block in header.ejs with the new topbar + css
old_topbar_regex = re.compile(r'<!-- Mandal Top Header Banner -->\s*<div class="topbar-chintamani top-utility-bar" id="topUtilityBar">.*?</div>\s*</div>\s*</div>', re.DOTALL)

replacement = nav_style + '\n\n' + '<!-- Mandal Top Header Banner -->\n' + new_topbar

header_partial = old_topbar_regex.sub(replacement, header_partial)

open('views/partials/header.ejs', 'w', encoding='utf-8').write(header_partial)
print("Fixed topbar replacement")
