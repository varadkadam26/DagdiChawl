import re

content = open('views/partials/header.ejs', encoding='utf-8').read()

content = re.sub(
    r'<header class="nm-nav-header" style="flex-direction: column; padding: 0; align-items: stretch; background: <%= currentTabName === \'home\' \? \'rgba\(0,0,0,0\.2\)\' : \'transparent\' %>; position: <%= currentTabName === \'home\' \? \'absolute\' : \'relative\' %>;">',
    '<header class="nm-nav-header" style="flex-direction: column; padding: 0; align-items: stretch; background: <%= currentTabName === \'home\' ? \'rgba(0,0,0,0.2)\' : \'rgba(21, 19, 15, 0.7)\' %>;">',
    content
)

content = re.sub(
    r"opacity: <%= \(currentTabName === 'home' \|\| currentTabName === 'about'\) \? '0' : '1' %>;",
    "opacity: <%= currentTabName === 'home' ? '0' : '1' %>;",
    content
)

content = re.sub(
    r'\.nm-nav-header::after \{\s*content: "";\s*position: absolute;\s*inset: 0;\s*box-shadow: inset 0 0 40px 10px rgba\(0,0,0,0\.6\), inset 0 -80px 60px -20px rgba\(0,0,0,1\);\s*z-index: -1;\s*pointer-events: none;\s*opacity: <%= currentTabName === \'about\' \? \'0\' : \'1\' %>;\s*\}',
    '.nm-nav-header::after {\n    content: "";\n    position: absolute;\n    inset: 0;\n    box-shadow: inset 0 0 40px 10px rgba(0,0,0,0.6), inset 0 -80px 60px -20px rgba(0,0,0,1);\n    z-index: -1;\n    pointer-events: none;\n  }',
    content
)

open('views/partials/header.ejs', 'w', encoding='utf-8').write(content)
print("Undone ultimate merge")
