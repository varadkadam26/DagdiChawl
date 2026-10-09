import re

content = open('views/partials/header.ejs', encoding='utf-8').read()

content = re.sub(
    r'background: url\(/images/final_page_no_text\.jpg\) center top / cover no-repeat;',
    'background: url(/images/final_page_no_text.jpg) center top / cover no-repeat;\n    -webkit-mask-image: linear-gradient(to bottom, black 50%, transparent 95%);\n    mask-image: linear-gradient(to bottom, black 50%, transparent 95%);',
    content
)

open('views/partials/header.ejs', 'w', encoding='utf-8').write(content)
print("Added mask image")
