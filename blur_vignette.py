import re

header_partial = open('views/partials/header.ejs', encoding='utf-8').read()

# Replace the top bar background
header_partial = header_partial.replace(
    '<div class="nm-top-bar" style="display: flex; justify-content: center; align-items: center; gap: 30px; padding: 10px 5%; background: transparent; border-bottom: none;">',
    '<div class="nm-top-bar" style="display: flex; justify-content: center; align-items: center; gap: 30px; padding: 10px 5%; background: linear-gradient(to bottom, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0.2) 100%); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); border-bottom: none;">'
)

# Actually, let's also apply a general gradient to the entire header so it looks perfect everywhere
# The user wants "same background... in other pages too"
header_partial = header_partial.replace(
    '<header class="nm-nav-header" style="flex-direction: column; padding: 0; align-items: stretch; background: <%= currentTabName === \'home\' ? \'transparent\' : \'#0a0a0a\' %>;">',
    '<header class="nm-nav-header" style="flex-direction: column; padding: 0; align-items: stretch; background: <%= currentTabName === \'home\' ? \'transparent\' : \'url(/images/final_page_no_text.jpg) center top / cover no-repeat\' %>;">'
)

open('views/partials/header.ejs', 'w', encoding='utf-8').write(header_partial)
print("Updated top bar")
