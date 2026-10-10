content = open('views/index.ejs', encoding='utf-8').read()

old_text_css = '''  .nm-logo-text {
    display: flex;
    flex-direction: column;
    align-items: center;
  }'''

new_text_css = '''  .nm-logo-text {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
  }'''

old_title_css = '''  .nm-logo-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: min(1.2rem, 1.8vw);
    font-weight: 500;
    color: #F4EDE0;
    letter-spacing: 2px;
    text-transform: uppercase;
    line-height: 1.1;
    white-space: nowrap;
  }'''

new_title_css = '''  .nm-logo-title {
    font-family: 'Baloo 2', sans-serif;
    font-size: min(1.2rem, 1.8vw);
    font-weight: 700;
    color: #F4EDE0;
    letter-spacing: 1px;
    text-transform: uppercase;
    line-height: 1.1;
    white-space: nowrap;
  }'''

old_gap = '''  .nm-logo-container {
    display: flex;
    align-items: center;
    gap: 15px;'''

new_gap = '''  .nm-logo-container {
    display: flex;
    align-items: center;
    gap: 8px;'''

content = content.replace(old_text_css, new_text_css)
content = content.replace(old_title_css, new_title_css)
content = content.replace(old_gap, new_gap)

open('views/index.ejs', 'w', encoding='utf-8').write(content)
print('Done!')
