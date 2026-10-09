content = open('views/index.ejs', encoding='utf-8').read()

old_desktop_bg = 'background: linear-gradient(to bottom, rgba(5,5,6,0.95), rgba(5,5,6,0.7));'
new_desktop_bg = 'background: linear-gradient(to bottom, rgba(25, 18, 12, 0.9), rgba(15, 10, 8, 0.6));'

old_mobile_bg = 'background: linear-gradient(180deg, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0) 100%);'
new_mobile_bg = 'background: linear-gradient(180deg, rgba(25, 18, 12, 0.95) 0%, rgba(15, 10, 8, 0) 100%);'

content = content.replace(old_desktop_bg, new_desktop_bg)
content = content.replace(old_mobile_bg, new_mobile_bg)

# Also update the mobile dropdown menu background to match!
old_mobile_dropdown = 'background: rgba(5,5,6,0.95);'
new_mobile_dropdown = 'background: rgba(25, 18, 12, 0.98);'
content = content.replace(old_mobile_dropdown, new_mobile_dropdown)

open('views/index.ejs', 'w', encoding='utf-8').write(content)
print('Updated nav background')
