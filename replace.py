import sys
content = open('views/index.ejs', encoding='utf-8').read()
new_logo = '''    <img src="/images/nav_logo.jpg" alt="Mandal Logo" style="width: 45px; height: 45px; object-fit: contain; border-radius: 50%; filter: drop-shadow(0 0 10px rgba(255, 165, 0, 0.7)); margin-right: 8px;">'''
lines = content.splitlines()
out = lines[:559] + [new_logo] + lines[567:]
open('views/index.ejs', 'w', encoding='utf-8').write('\n'.join(out))
