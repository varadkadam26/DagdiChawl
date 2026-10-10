import re

content = open('views/partials/header.ejs', encoding='utf-8').read()

# Fix ::before
content = re.sub(
    r'top: -20px; left: -20px; right: -20px; bottom: -20px;',
    'top: 0; left: 0; right: 0; bottom: 0;',
    content
)

content = re.sub(
    r'-webkit-mask-image: linear-gradient\(to bottom, black 60%, transparent 100%\);\s*mask-image: linear-gradient\(to bottom, black 60%, transparent 100%\);',
    '-webkit-mask-image: linear-gradient(to bottom, black 20%, transparent 100%);\n    mask-image: linear-gradient(to bottom, black 20%, transparent 100%);',
    content
)

open('views/partials/header.ejs', 'w', encoding='utf-8').write(content)
print("Fixed mask clipping")
