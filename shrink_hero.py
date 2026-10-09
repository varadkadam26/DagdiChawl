content = open('views/index.ejs', encoding='utf-8').read()

old_css = '''    .image-container img.bg-image {
      display: block;
      width: 100vw;
      height: 100vh;'''

new_css = '''    .image-container img.bg-image {
      display: block;
      width: 100vw;
      height: 85vh;'''

content = content.replace(old_css, new_css)
open('views/index.ejs', 'w', encoding='utf-8').write(content)
print('Done shrinking hero')
