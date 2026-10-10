import re

content = open('views/about.ejs', encoding='utf-8').read()

content = re.sub(
    r'background: rgba\(212, 175, 55, 0\.03\) !important;\s*border: 1px solid rgba\(212, 175, 55, 0\.4\) !important;\s*box-shadow: 0 4px 15px rgba\(0,0,0,0\.2\) !important;\s*backdrop-filter: blur\(8px\);\s*-webkit-backdrop-filter: blur\(8px\);',
    'background: transparent !important;\n    border: 1px solid rgba(212, 175, 55, 0.4) !important;\n    box-shadow: none !important;',
    content
)

open('views/about.ejs', 'w', encoding='utf-8').write(content)
print("Removed color from cards")
