content = open('views/index.ejs', encoding='utf-8').read()

old_css = '''    /* 1. First Section: Full Screen Devi Image */
    .image-container img.bg-image {
      display: block;
      width: 100vw;
      height: 100vh;
      object-fit: cover;
      /* Centralize the Devi idol perfectly */
      object-position: center center; 
    }'''

new_css = '''    /* 1. First Section: Full Screen Devi Image */
    .image-container img.bg-image {
      display: block;
      width: 100vw;
      height: 100vh;
      object-fit: cover;
      /* Precisely calculated to center the idol in the viewport */
      object-position: 79% center; 
    }'''
content = content.replace(old_css, new_css)
open('views/index.ejs', 'w', encoding='utf-8').write(content)
print('Fixed idol position')
