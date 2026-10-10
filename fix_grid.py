content = open('views/index.ejs', encoding='utf-8').read()

old_mobile = '''    /* Adjust header for mobile */
    .nm-nav-header {'''

new_mobile = '''    /* Fix extracted layout sections for mobile */
    .grid-2 {
      display: flex !important;
      flex-direction: column !important;
      gap: 2rem !important;
    }
    .grid-4 {
      display: grid !important;
      grid-template-columns: 1fr 1fr !important; /* Stats counter 2x2 on mobile */
      gap: 1rem !important;
    }
    section[style*="padding: 6rem 0"] {
      padding: 3rem 0 !important; /* Reduce massive desktop padding on mobile */
    }

    /* Adjust header for mobile */
    .nm-nav-header {'''

content = content.replace(old_mobile, new_mobile)

# Also ensure the photo container uses a sensible height on mobile
# Let's add a specific class to the photo so we can style it if needed, or just let CSS handle it.
# The inline style has height: 460px which might be too tall for mobile.
old_img = '''<img src="/images/president.jpg" alt="President" width="600" height="460"'''
new_img = '''<img src="/images/president.jpg" alt="President" class="president-img" width="600" height="460"'''
content = content.replace(old_img, new_img)

new_mobile2 = '''    .nm-donate-btn {
      display: none; /* Hide on mobile to fit long title */
    }'''

new_mobile3 = '''    .nm-donate-btn {
      display: none; /* Hide on mobile to fit long title */
    }
    .president-img {
      height: 350px !important;
    }'''
content = content.replace(new_mobile2, new_mobile3)

open('views/index.ejs', 'w', encoding='utf-8').write(content)
print('Fixed grid')
