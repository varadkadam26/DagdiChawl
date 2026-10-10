import re

content = open('views/partials/header.ejs', encoding='utf-8').read()

content = content.replace(
    '''<div class="nm-top-bar" style="display: flex; justify-content: center; align-items: center; gap: 30px; padding: 10px 5%; background: <%= currentTabName === 'home' ? 'rgba(0,0,0,0.2)' : 'rgba(21, 19, 15, 0.7)' %>; border-bottom: none;">''',
    '''<div class="nm-top-bar" style="display: flex; justify-content: center; align-items: center; gap: 30px; padding: 10px 5%; background: transparent; border-bottom: none;">'''
)

open('views/partials/header.ejs', 'w', encoding='utf-8').write(content)
print("Set top bar to transparent")
