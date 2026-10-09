import re

content = open('views/index.ejs', encoding='utf-8').read()

# The container is grid-2. Let's match the first div (text) and the second div (image)
pattern = re.compile(
    r'(<div class="grid-2" style="align-items: center; gap: 4rem;">\s*)'
    r'(<div>.*?</div>\s*</div>\s*</div>\s*</div>\s*)'
    r'(<div style="position: relative;">.*?</div>\s*</div>\s*)'
    r'(</div>\s*<!-- Animated Stat Counter Row -->)',
    re.DOTALL
)

match = pattern.search(content)
if match:
    prefix = match.group(1)
    text_div = match.group(2)
    img_div = match.group(3)
    suffix = match.group(4)
    
    new_content = content[:match.start()] + prefix + img_div + text_div + suffix + content[match.end():]
    open('views/index.ejs', 'w', encoding='utf-8').write(new_content)
    print("Swapped using regex!")
else:
    print("Regex failed to match.")
