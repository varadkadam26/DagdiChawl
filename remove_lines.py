import re

content = open('views/partials/header.ejs', encoding='utf-8').read()

# Remove border and box-shadow from nm-nav-header
content = re.sub(
    r'border-bottom:\s*2px solid rgba\(212,\s*175,\s*55,\s*0\.9\);\s*box-shadow:\s*0\s*4px\s*20px\s*rgba\(212,\s*175,\s*55,\s*0\.6\);',
    'border-bottom: none;',
    content
)

# Just in case the first line was still there (though I reverted it, sometimes caching or multiple matches happen)
content = re.sub(
    r'border-bottom:\s*1\.5px solid rgba\(212,\s*175,\s*55,\s*0\.8\);\s*box-shadow:\s*0\s*4px\s*15px\s*rgba\(212,\s*175,\s*55,\s*0\.5\);',
    'border-bottom: none;',
    content
)

open('views/partials/header.ejs', 'w', encoding='utf-8').write(content)
print("Removed lines")
