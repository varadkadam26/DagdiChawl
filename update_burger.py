content = open('views/index.ejs', encoding='utf-8').read()

old_css = '''  .nm-hamburger {
    display: none;
    flex-direction: column;
    gap: 5px;
    cursor: pointer;
    z-index: 101;
  }
  .nm-hamburger span {
    display: block;
    width: 25px;
    height: 3px;
    background-color: #D4AF37;
    border-radius: 3px;
    transition: all 0.3s ease;
  }'''

new_css = '''  .nm-hamburger {
    display: none;
    flex-direction: column;
    gap: 4.5px;
    cursor: pointer;
    z-index: 101;
  }
  .nm-hamburger span {
    display: block;
    width: 21px;
    height: 2px;
    background: linear-gradient(90deg, #F9D423 0%, #FF4E50 200%);
    box-shadow: 0 0 8px rgba(249, 212, 35, 0.6);
    border-radius: 3px;
    transition: all 0.3s ease;
  }'''

content = content.replace(old_css, new_css)
open('views/index.ejs', 'w', encoding='utf-8').write(content)
print('Updated hamburger CSS')
