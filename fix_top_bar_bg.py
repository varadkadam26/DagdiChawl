import re

content = open('views/partials/header.ejs', encoding='utf-8').read()

content = content.replace(
    '<div class="nm-top-bar" style="display: flex; justify-content: center; align-items: center; gap: 30px; padding: 10px 5%; background: linear-gradient(to bottom, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0.2) 100%); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); border-bottom: none;">',
    '<div class="nm-top-bar" style="display: flex; justify-content: center; align-items: center; gap: 30px; padding: 10px 5%; background: transparent; border-bottom: none;">'
)

open('views/partials/header.ejs', 'w', encoding='utf-8').write(content)
print("Made top bar transparent")
