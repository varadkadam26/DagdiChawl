import re

content = open('views/index.ejs', encoding='utf-8').read()

# 1. Update Top Bar styling
content = content.replace(
    '''<div class="nm-top-bar" style="display: flex; justify-content: space-between; align-items: center; padding: 8px 5%; background: rgba(0,0,0,0.75); border-bottom: 1px solid rgba(212,175,55,0.2);">''',
    '''<div class="nm-top-bar" style="display: flex; justify-content: center; align-items: center; gap: 2rem; padding: 10px 5%; background: transparent; border-bottom: none;">'''
)

# 2. Update the language toggle container to remove inline overrides and add a capsule border CSS class
content = content.replace(
    '''<div class="lang-toggle-container" style="background: transparent; border: none; padding: 0; display: flex; gap: 8px; align-items: center;">''',
    '''<div class="lang-toggle-container" style="display: flex; gap: 8px; align-items: center; border: 1.5px solid #D4AF37; border-radius: 50px; padding: 4px 16px; background: rgba(0,0,0,0.4);">'''
)

# Make the unselected language text color slightly lighter so it's readable but not active
content = content.replace('color: rgba(244, 237, 224, 0.5);', 'color: rgba(244, 237, 224, 0.7);')

open('views/index.ejs', 'w', encoding='utf-8').write(content)
print("Updated top bar styling")
