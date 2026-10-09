import re

content = open('views/about.ejs', encoding='utf-8').read()

content = re.sub(
    r'body \{\s*background: linear-gradient\(to bottom, #080A08 0%, #15130F 50%, #30190F 100%\) !important;\s*background-attachment: fixed !important;\s*background-size: cover !important;\s*\}',
    'body {\n    background: linear-gradient(to bottom, #080A08 0%, #15130F 40%, #30190F 100%) !important;\n    min-height: 100vh;\n  }',
    content
)

open('views/about.ejs', 'w', encoding='utf-8').write(content)
print("Fixed gradient scrolling")
