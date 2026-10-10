import re

content = open('views/partials/header.ejs', encoding='utf-8').read()

# Replace the pseudo element that handles the vignette to also add a smooth gradient merge at the bottom
content = re.sub(
    r'\.nm-nav-header::after \{\s*content: "";\s*position: absolute;\s*inset: 0;\s*box-shadow: inset 0 0 40px 10px rgba\(0,0,0,0\.6\), inset 0 -80px 60px -20px rgba\(0,0,0,1\);\s*z-index: -1;\s*pointer-events: none;\s*\}',
    '.nm-nav-header::after {\n    content: "";\n    position: absolute;\n    inset: 0;\n    box-shadow: inset 0 0 40px 10px rgba(0,0,0,0.6);\n    background: linear-gradient(to bottom, transparent 40%, #080A08 100%);\n    z-index: -1;\n    pointer-events: none;\n  }',
    content
)

# Set the inline style background of the header to transparent on non-home pages so the fade works properly
content = re.sub(
    r"background: <%= currentTabName === 'home' \? 'rgba\(0,0,0,0\.2\)' : 'rgba\(21, 19, 15, 0\.7\)' %>;",
    "background: <%= currentTabName === 'home' ? 'rgba(0,0,0,0.2)' : 'transparent' %>;",
    content
)

open('views/partials/header.ejs', 'w', encoding='utf-8').write(content)
print("Applied gradient fade merge")
