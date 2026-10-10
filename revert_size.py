content = open('views/index.ejs', encoding='utf-8').read()

# 1. Desktop container-wrapper
old_desktop_wrapper = '''  .container-wrapper {
    width: 100%;
    display: block;
    position: relative;
    height: 85vh;
    overflow: hidden;
  }'''

new_desktop_wrapper = '''  .container-wrapper {
    width: 100%;
    display: block;
    position: relative;
  }'''

content = content.replace(old_desktop_wrapper, new_desktop_wrapper)

# 2. Mobile container-wrapper
old_mobile_wrapper = '''    /* Reset container layout */
    .container-wrapper {
      height: 85vh;
      overflow: hidden;
    }'''

new_mobile_wrapper = '''    /* Reset container layout */
    .container-wrapper {
      height: auto;
    }'''

content = content.replace(old_mobile_wrapper, new_mobile_wrapper)

# 3. Mobile bg-image height
old_mobile_bg = '''    .image-container img.bg-image {
      display: block;
      width: 100vw;
      height: 85vh;'''

new_mobile_bg = '''    .image-container img.bg-image {
      display: block;
      width: 100vw;
      height: 100vh;'''

content = content.replace(old_mobile_bg, new_mobile_bg)

open('views/index.ejs', 'w', encoding='utf-8').write(content)
print('Reverted sizes')
