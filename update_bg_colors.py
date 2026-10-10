import re

content = open('views/about.ejs', encoding='utf-8').read()

# Replace the linear gradient line
content = re.sub(
    r'background: linear-gradient\(to bottom, #15130F 0%, #24170F 50%, #62462C 100%\) !important;',
    'background: linear-gradient(to bottom, #080A08 0%, #15130F 50%, #30190F 100%) !important;',
    content
)

# Replace paragraph color to a crisp off-white for better readability on darker BG
content = re.sub(
    r'color: #E8DCC4 !important;',
    'color: #F4EDE0 !important;',
    content
)

open('views/about.ejs', 'w', encoding='utf-8').write(content)
print("Updated gradient and text colors")
