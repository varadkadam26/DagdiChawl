content = open('views/index.ejs', encoding='utf-8').read()

# Change inline style to height: auto
old_img = '''<img src="/images/president.jpg" alt="President" class="president-img" width="600" height="460"
                  loading="lazy"
                  style="width: 100%; height: 460px; object-fit: cover; object-position: center top; display: block;">'''

new_img = '''<img src="/images/president.jpg" alt="President" class="president-img" width="600" height="460"
                  loading="lazy"
                  style="width: 100%; height: auto; display: block; border-radius: 8px;">'''
                  
content = content.replace(old_img, new_img)

# Change mobile CSS to height: auto
old_mobile_css = '''    .president-img {
      height: 350px !important;
    }'''

new_mobile_css = '''    .president-img {
      height: auto !important;
    }'''

content = content.replace(old_mobile_css, new_mobile_css)

open('views/index.ejs', 'w', encoding='utf-8').write(content)
print('Fixed photo visibility')
