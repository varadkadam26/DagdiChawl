import re

content = open('views/partials/header.ejs', encoding='utf-8').read()

# Update ::before to fade out fully by 100%
content = re.sub(
    r'-webkit-mask-image: linear-gradient\(to bottom, black 50%, transparent 95%\);\s*mask-image: linear-gradient\(to bottom, black 50%, transparent 95%\);',
    '-webkit-mask-image: linear-gradient(to bottom, black 60%, transparent 100%);\n    mask-image: linear-gradient(to bottom, black 60%, transparent 100%);',
    content
)

# Update ::after to remove the hardcoded background color and also fade out!
content = re.sub(
    r'\.nm-nav-header::after \{\s*content: "";\s*position: absolute;\s*inset: 0;\s*box-shadow: inset 0 0 40px 10px rgba\(0,0,0,0\.6\);\s*background: linear-gradient\(to bottom, transparent 40%, #080A08 100%\);\s*z-index: -1;\s*pointer-events: none;\s*\}',
    '.nm-nav-header::after {\n    content: "";\n    position: absolute;\n    inset: 0;\n    box-shadow: inset 0 0 40px 10px rgba(0,0,0,0.8);\n    -webkit-mask-image: linear-gradient(to bottom, black 60%, transparent 100%);\n    mask-image: linear-gradient(to bottom, black 60%, transparent 100%);\n    z-index: -1;\n    pointer-events: none;\n  }',
    content
)

open('views/partials/header.ejs', 'w', encoding='utf-8').write(content)
print("Masked pseudo elements")
