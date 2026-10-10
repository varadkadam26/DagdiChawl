content = open('views/index.ejs', encoding='utf-8').read()

old_desktop_css = '''  .image-container img.bg-image {
    width: 100%;
    height: auto;
    display: block;
  }'''

new_desktop_css = '''  .image-container img.bg-image {
    width: 100%;
    height: 85vh;
    object-fit: cover;
    object-position: center top;
    display: block;
  }'''
content = content.replace(old_desktop_css, new_desktop_css)

old_mobile_css = '''    .image-container img.bg-image {
      display: block;
      width: 100vw;
      height: 100vh;
      object-fit: cover;
      /* Adjusted to 74% to perfectly center the 68% idol mark on mobile screens */
      object-position: 74% center; 
    }'''

new_mobile_css = '''    .image-container img.bg-image {
      display: block;
      width: 100vw;
      height: 85vh;
      object-fit: cover;
      /* Adjusted to 74% to perfectly center the 68% idol mark on mobile screens */
      object-position: 74% center; 
    }'''
content = content.replace(old_mobile_css, new_mobile_css)

open('views/index.ejs', 'w', encoding='utf-8').write(content)
print('Fixed height')
