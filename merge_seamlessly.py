import re

content_header = open('views/partials/header.ejs', encoding='utf-8').read()

# Make background transparent for 'about' tab as well
content_header = re.sub(
    r"background: <%= currentTabName === 'home' \? 'rgba\(0,0,0,0\.2\)' : 'rgba\(21, 19, 15, 0\.7\)' %>;",
    "background: transparent;",
    content_header
)

# Make pseudo-element opacity 0 for 'about' tab as well
content_header = re.sub(
    r"opacity: <%= currentTabName === 'home' \? '0' : '1' %>;",
    "opacity: <%= (currentTabName === 'home' || currentTabName === 'about') ? '0' : '1' %>;",
    content_header
)

open('views/partials/header.ejs', 'w', encoding='utf-8').write(content_header)


content_about = open('views/about.ejs', encoding='utf-8').read()

# Update page-hero-banner padding to push content below the absolute header
content_about = re.sub(
    r'\.main-content-gradient, \.page-hero-banner \{\n    background: transparent !important;\n    border: none !important;\n    box-shadow: none !important;\n  \}',
    '.main-content-gradient, .page-hero-banner {\n    background: transparent !important;\n    border: none !important;\n    box-shadow: none !important;\n  }\n  .page-hero-banner {\n    padding-top: 180px !important;\n  }',
    content_about
)

open('views/about.ejs', 'w', encoding='utf-8').write(content_about)
print("Merged seamlessly")
