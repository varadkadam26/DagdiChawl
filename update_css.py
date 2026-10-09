content = open('views/index.ejs', encoding='utf-8').read()

# I need to add CSS specifically for .ios-glass-switch elements
# Let's see if the old lang-toggle-container CSS is still there and replace it
import re

old_css_regex = re.compile(r'\.lang-toggle-container \{.*?\}', re.DOTALL)
content = old_css_regex.sub('', content)

old_css_regex2 = re.compile(r'\.lang-toggle-container \.lang-btn \{.*?\}', re.DOTALL)
content = old_css_regex2.sub('', content)

old_css_regex3 = re.compile(r'\.lang-toggle-container \.lang-btn\.active \{.*?\}', re.DOTALL)
content = old_css_regex3.sub('', content)

old_css_regex4 = re.compile(r'\.lang-toggle-container span \{.*?\}', re.DOTALL)
content = old_css_regex4.sub('', content)

old_media = re.compile(r'@media \(max-width: 768px\) \{.*?\.lang-toggle-container \{.*?\}', re.DOTALL)
# Actually, I'll just append new styles which will overwrite any leftovers

new_css = '''
  .ios-glass-switch .lang-btn {
    color: rgba(255, 255, 255, 0.5) !important;
  }
  .ios-glass-switch .lang-btn:hover {
    color: rgba(255, 255, 255, 0.8) !important;
  }
  .ios-glass-switch .lang-btn.active {
    background: #ffffff !important;
    color: #1a1a1a !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.2) !important;
  }
'''

content = content.replace('</style>', new_css + '\n</style>')

open('views/index.ejs', 'w', encoding='utf-8').write(content)
