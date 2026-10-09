import re

content = open('views/partials/header.ejs', encoding='utf-8').read()

# Revert .nm-nav-header inline background
content = re.sub(
    r"background: <%= currentTabName === 'home' \? 'rgba\(0,0,0,0\.2\)' : 'transparent' %>;",
    "background: <%= currentTabName === 'home' ? 'rgba(0,0,0,0.2)' : 'rgba(21, 19, 15, 0.7)' %>;",
    content
)

# Revert ::before
content = re.sub(
    r'\.nm-nav-header::before \{\s*content: "";\s*position: absolute;\s*top: 0; left: 0; right: 0; bottom: 0;\s*background: url\(/images/final_page_no_text\.jpg\) center top / cover no-repeat;\s*-webkit-mask-image: linear-gradient\(to bottom, black 20%, transparent 100%\);\s*mask-image: linear-gradient\(to bottom, black 20%, transparent 100%\);\s*z-index: -2;\s*opacity: <%= currentTabName === \'home\' \? \'0\' : \'1\' %>;\s*\}',
    '.nm-nav-header::before {\n    content: "";\n    position: absolute;\n    top: -20px; left: -20px; right: -20px; bottom: -20px;\n    background: url(/images/final_page_no_text.jpg) center top / cover no-repeat;\n    z-index: -2;\n    opacity: <%= currentTabName === \'home\' ? \'0\' : \'1\' %>;\n  }',
    content
)

# Revert ::after
content = re.sub(
    r'\.nm-nav-header::after \{\s*content: "";\s*position: absolute;\s*inset: 0;\s*box-shadow: inset 0 0 40px 10px rgba\(0,0,0,0\.8\);\s*-webkit-mask-image: linear-gradient\(to bottom, black 20%, transparent 100%\);\s*mask-image: linear-gradient\(to bottom, black 20%, transparent 100%\);\s*z-index: -1;\s*pointer-events: none;\s*\}',
    '.nm-nav-header::after {\n    content: "";\n    position: absolute;\n    inset: 0;\n    box-shadow: inset 0 0 40px 10px rgba(0,0,0,0.6), inset 0 -80px 60px -20px rgba(0,0,0,1);\n    z-index: -1;\n    pointer-events: none;\n  }',
    content
)

open('views/partials/header.ejs', 'w', encoding='utf-8').write(content)
print("Reverted all merging")
