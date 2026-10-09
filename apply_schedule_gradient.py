import re

content = open('views/schedule.ejs', encoding='utf-8').read()

style_block = '''<style>
  body {
    background: linear-gradient(to bottom, #080A08 0%, #15130F 40%, #30190F 100%) !important;
    min-height: 100vh;
  }
  .main-content-gradient, .page-hero-banner {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
  }
</style>
'''

# Insert after <%- include('partials/header') %>
content = content.replace("<%- include('partials/header') %>", "<%- include('partials/header') %>\n\n" + style_block)

open('views/schedule.ejs', 'w', encoding='utf-8').write(content)
print("Applied gradient to schedule page")
