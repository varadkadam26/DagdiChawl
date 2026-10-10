import re

content = open('views/partials/header.ejs', encoding='utf-8').read()

content = content.replace('backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);', 'backdrop-filter: blur(5px); -webkit-backdrop-filter: blur(5px);')
content = content.replace('filter: blur(15px);', 'filter: blur(5px);')

open('views/partials/header.ejs', 'w', encoding='utf-8').write(content)
print("Reduced blur")
