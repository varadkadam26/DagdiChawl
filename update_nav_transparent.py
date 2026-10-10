content = open('views/index.ejs', encoding='utf-8').read()

old_desktop_bg = 'background: linear-gradient(to bottom, rgba(25, 18, 12, 0.9), rgba(15, 10, 8, 0.6));'
new_desktop_bg = 'background: transparent;'

old_backdrop = 'backdrop-filter: blur(15px);\n      -webkit-backdrop-filter: blur(15px);'
new_backdrop = '/* No backdrop blur so it matches exactly */'

old_border = 'border-bottom: 1px solid rgba(212, 175, 55, 0.15);'
new_border = 'border-bottom: none;'

old_mobile_bg = 'background: linear-gradient(180deg, rgba(25, 18, 12, 0.95) 0%, rgba(15, 10, 8, 0) 100%);'
new_mobile_bg = 'background: transparent;'

content = content.replace(old_desktop_bg, new_desktop_bg)
content = content.replace(old_backdrop, new_backdrop)
content = content.replace(old_border, new_border)
content = content.replace(old_mobile_bg, new_mobile_bg)

open('views/index.ejs', 'w', encoding='utf-8').write(content)
print('Made navbar transparent')
