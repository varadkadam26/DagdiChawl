import re

content = open('views/partials/header.ejs', encoding='utf-8').read()

old_nav = '''    <nav class="nm-nav-links">
      <a href="/" class="active">Home</a>
      <a href="/about">About</a>
      <a href="/schedule">Events</a>
      <a href="/glimpses">Gallery</a>
      <a href="/contact">Contact</a>
    </nav>'''

new_nav = '''    <nav class="nm-nav-links">
      <a href="/" class="<%= currentTabName === 'home' ? 'active' : '' %>">Home</a>
      <a href="/about" class="<%= currentTabName === 'about' ? 'active' : '' %>">About</a>
      <a href="/schedule" class="<%= currentTabName === 'schedule' ? 'active' : '' %>">Events</a>
      <a href="/glimpses" class="<%= (currentTabName === 'glimpses' || currentTabName === 'photobooth') ? 'active' : '' %>">Gallery</a>
      <a href="/contact" class="<%= currentTabName === 'contact' ? 'active' : '' %>">Contact</a>
    </nav>'''

content = content.replace(old_nav, new_nav)

open('views/partials/header.ejs', 'w', encoding='utf-8').write(content)
print("Updated nav links to be dynamic")
