import codecs
import re

with codecs.open('views/index.ejs', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove HTML
html = re.sub(
    r'<div class="hd-devi-wrapper">.*?</div>\s*</div>',
    '', 
    html,
    flags=re.DOTALL
)

# Remove CSS
html = re.sub(
    r'\.hd-devi-wrapper\s*\{.*?\}(?=\s*\.)',
    '',
    html,
    flags=re.DOTALL
)
html = re.sub(
    r'\.devi-interactive-light\s*\{.*?\}(?=\s*\.)',
    '',
    html,
    flags=re.DOTALL
)
html = re.sub(
    r'\.hd-devi\s*\{.*?\}(?=\s*\.)',
    '',
    html,
    flags=re.DOTALL
)
html = re.sub(
    r'\.hd-devi-wrapper::after\s*\{.*?\}(?=\s*\.)',
    '',
    html,
    flags=re.DOTALL
)
# For the mobile media query
html = re.sub(
    r'\.hd-devi-wrapper\s*\{\s*display:\s*none;\s*\}',
    '',
    html,
    flags=re.DOTALL
)

with codecs.open('views/index.ejs', 'w', encoding='utf-8') as f:
    f.write(html)
