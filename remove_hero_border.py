import re

content = open('views/about.ejs', encoding='utf-8').read()

content = content.replace(
    '.main-content-gradient, .page-hero-banner {\n    background: transparent !important;\n  }',
    '.main-content-gradient, .page-hero-banner {\n    background: transparent !important;\n    border: none !important;\n    box-shadow: none !important;\n  }'
)

open('views/about.ejs', 'w', encoding='utf-8').write(content)
print("Removed border from hero banner")
