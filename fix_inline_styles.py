content = open('views/index.ejs', encoding='utf-8').read()

content = content.replace(
    'class="lang-btn active" data-lang="mr" style="color: rgba(244, 237, 224, 0.5);',
    'class="lang-btn active" data-lang="mr" style="'
)
content = content.replace(
    'class="lang-btn" data-lang="en" style="color: rgba(244, 237, 224, 0.5);',
    'class="lang-btn" data-lang="en" style="'
)

# Also let's fix social icons hover color!
css_add = '''
  .nm-social-icons a:hover {
    color: #D4AF37 !important;
  }
'''
content = content.replace('</style>', css_add + '\n</style>')

open('views/index.ejs', 'w', encoding='utf-8').write(content)
