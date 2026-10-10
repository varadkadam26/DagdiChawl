import re

header_partial = open('views/partials/header.ejs', encoding='utf-8').read()

header_partial = header_partial.replace(
    '<header class="nm-nav-header" style="flex-direction: column; padding: 0; align-items: stretch; background: transparent;">',
    '<header class="nm-nav-header" style="flex-direction: column; padding: 0; align-items: stretch; background: <%= currentTabName === \'home\' ? \'transparent\' : \'#0a0a0a\' %>;">'
)

open('views/partials/header.ejs', 'w', encoding='utf-8').write(header_partial)
print("Updated header background")
