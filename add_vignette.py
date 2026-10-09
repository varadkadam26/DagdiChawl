content = open('views/index.ejs', encoding='utf-8').read()

old_desktop_bg = '''    /* Frosted glass to cover any blurry baked-in header */
    background: transparent;
    border-bottom: none;'''

new_desktop_bg = '''    /* Soft vignette effect to make text pop while blending perfectly */
    background: linear-gradient(to bottom, rgba(10, 8, 5, 0.95) 0%, rgba(10, 8, 5, 0) 100%);
    border-bottom: none;
    pointer-events: none; /* Let clicks pass through the gradient if needed */'''

# Wait, if we use pointer-events: none on the header, the links won't be clickable! 
# Better to apply the gradient to a pseudo-element or just keep pointer-events: auto.
new_desktop_bg = '''    /* Soft vignette effect to make text pop while blending perfectly */
    background: linear-gradient(to bottom, rgba(5, 5, 5, 0.9) 0%, rgba(5, 5, 5, 0) 100%);
    border-bottom: none;'''

content = content.replace(old_desktop_bg, new_desktop_bg)

old_mobile_bg = '''    /* Adjust header for mobile */
    .nm-nav-header {
      padding: 18px 5%;
      background: transparent;
    }'''

new_mobile_bg = '''    /* Adjust header for mobile */
    .nm-nav-header {
      padding: 18px 5%;
      background: linear-gradient(to bottom, rgba(5, 5, 5, 0.95) 0%, rgba(5, 5, 5, 0) 100%);
    }'''

content = content.replace(old_mobile_bg, new_mobile_bg)

open('views/index.ejs', 'w', encoding='utf-8').write(content)
print('Added vignette effect')
