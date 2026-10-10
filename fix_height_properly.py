content = open('views/index.ejs', encoding='utf-8').read()

# Revert desktop img.bg-image
old_desktop_css = '''  .image-container img.bg-image {
    width: 100%;
    height: 85vh;
    object-fit: cover;
    object-position: center top;
    display: block;
  }'''
new_desktop_css = '''  .image-container img.bg-image {
    width: 100%;
    height: auto;
    display: block;
  }'''
content = content.replace(old_desktop_css, new_desktop_css)

# Revert mobile img.bg-image height to 100vh so it scales correctly if needed, OR 
# wait, on mobile it was already height: 100vh originally.
old_mobile_css = '''    .image-container img.bg-image {
      display: block;
      width: 100vw;
      height: 85vh;
      object-fit: cover;'''
new_mobile_css = '''    .image-container img.bg-image {
      display: block;
      width: 100vw;
      height: 100vh;
      object-fit: cover;'''
content = content.replace(old_mobile_css, new_mobile_css)

# Now, apply 85vh and overflow: hidden to .container-wrapper
old_wrapper_css = '''  .container-wrapper {
    width: 100%;
    display: block;
    position: relative;
  }'''
new_wrapper_css = '''  .container-wrapper {
    width: 100%;
    display: block;
    position: relative;
    height: 85vh;
    overflow: hidden;
  }'''
content = content.replace(old_wrapper_css, new_wrapper_css)

# For mobile, it had:
old_mobile_wrapper = '''    /* Reset container layout */
    .container-wrapper {
      height: auto;
    }'''
new_mobile_wrapper = '''    /* Reset container layout */
    .container-wrapper {
      height: 85vh;
      overflow: hidden;
    }'''
content = content.replace(old_mobile_wrapper, new_mobile_wrapper)

open('views/index.ejs', 'w', encoding='utf-8').write(content)
print('Fixed height via wrapper cropping')
