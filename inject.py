import re
import codecs

with codecs.open('malabar.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract all sections
sections = re.findall(r'(<section.*?</section>)', html, re.DOTALL | re.IGNORECASE)

# Filter out the heroCarousel section
middle_sections = []
for s in sections:
    if 'id="heroCarousel"' not in s:
        middle_sections.append(s)

extracted_html = '\n\n'.join(middle_sections)

# Open current index.ejs and insert it before footer
with codecs.open('views/index.ejs', 'r', encoding='utf-8') as f:
    current = f.read()

# We will replace the "MOCKUP HIGHLIGHTS" section with this new extracted content
# Actually, the user says "add everything in the middle", so we should keep what we have and append?
# "leaving the top navigaation section,main hero section and footer ssectin add eveything in the middle present in the home page of this website :malabarhillcharaja.in into our new website"
# Let's just insert it right above the footer

new_content = "\n<!-- EXTRACTED FROM malabarhillcharaja.in -->\n" + extracted_html + "\n\n<%- include('partials/footer') %>"
current = current.replace("<%- include('partials/footer') %>", new_content)

with codecs.open('views/index.ejs', 'w', encoding='utf-8') as f:
    f.write(current)

print(f"Extracted {len(middle_sections)} sections.")
