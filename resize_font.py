content = open('views/index.ejs', encoding='utf-8').read()

content = content.replace('font-size: 11px !important;', 'font-size: min(15.5px, 4.2vw) !important;')

open('views/index.ejs', 'w', encoding='utf-8').write(content)
print("Font size updated")
