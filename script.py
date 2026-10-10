import re

with open('views/index.ejs', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace any existing query parameters or add ?v=4
content = re.sub(r'(/images/marquee/new_[^"\?]+)(\?v=\d+)?', r'\1?v=4', content)

with open('views/index.ejs', 'w', encoding='utf-8') as f:
    f.write(content)
