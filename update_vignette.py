import re

content = open('views/partials/header.ejs', encoding='utf-8').read()

# Update the pseudo-element box-shadow to be heavy on the bottom
content = re.sub(
    r'\.nm-nav-header::after \{\s*content: "";\s*position: absolute;\s*inset: 0;\s*box-shadow: inset 0 0 60px 20px rgba\(0,0,0,0\.9\);\s*z-index: -1;\s*pointer-events: none;\s*\}',
    '.nm-nav-header::after {\n    content: "";\n    position: absolute;\n    inset: 0;\n    box-shadow: inset 0 0 40px 10px rgba(0,0,0,0.6), inset 0 -80px 60px -20px rgba(0,0,0,1);\n    z-index: -1;\n    pointer-events: none;\n  }',
    content
)

# Remove the inline box shadow
content = content.replace(' box-shadow: inset 0 0 40px 15px rgba(0,0,0,0.9);', '')

open('views/partials/header.ejs', 'w', encoding='utf-8').write(content)
print("Updated vignette weighting")
