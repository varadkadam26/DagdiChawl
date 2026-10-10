import re

content = open('views/index.ejs', encoding='utf-8').read()

header_regex = re.compile(r'(<header class="nm-nav-header">)(.*?)(</header>)', re.DOTALL)
match = header_regex.search(content)

if match:
    # First, let's remove the language toggle from the previous location so it isn't duplicated
    inner_content = match.group(2)
    inner_content = re.sub(
        r'<div class="lang-toggle-container">.*?</div>',
        '',
        inner_content,
        flags=re.DOTALL
    )

    new_header = '''<header class="nm-nav-header" style="flex-direction: column; padding: 0; align-items: stretch; background: linear-gradient(to bottom, rgba(5,5,5,0.95) 0%, rgba(5,5,5,0) 100%);">
  
  <!-- Pre-Header (Top Bar) -->
  <div class="nm-top-bar" style="display: flex; justify-content: space-between; align-items: center; padding: 8px 5%; background: rgba(0,0,0,0.75); border-bottom: 1px solid rgba(212,175,55,0.2);">
    
    <!-- Social Icons -->
    <div class="nm-social-icons" style="display: flex; gap: 15px;">
      <a href="https://www.facebook.com/BycullaDagadiChawl/" target="_blank" style="color: #F4EDE0; font-size: 16px; transition: color 0.3s;"><i class="fa-brands fa-facebook-f"></i></a>
      <a href="https://www.instagram.com/byculla_dagadichawl_navratri/" target="_blank" style="color: #F4EDE0; font-size: 16px; transition: color 0.3s;"><i class="fa-brands fa-instagram"></i></a>
      <a href="https://www.youtube.com/@DagdiChawlChaRaja-e2z" target="_blank" style="color: #F4EDE0; font-size: 16px; transition: color 0.3s;"><i class="fa-brands fa-youtube"></i></a>
    </div>

    <!-- Language Toggle -->
    <div class="lang-toggle-container" style="background: transparent; border: none; padding: 0; display: flex; gap: 8px; align-items: center;">
      <a href="#" class="lang-btn active" data-lang="mr" style="color: rgba(244, 237, 224, 0.5); text-decoration: none; font-size: 14px; font-family: 'Baloo 2', sans-serif; font-weight: 700; transition: all 0.3s ease;">?????</a>
      <span style="color: rgba(212, 175, 55, 0.3); font-size: 12px;">|</span>
      <a href="#" class="lang-btn" data-lang="en" style="color: rgba(244, 237, 224, 0.5); text-decoration: none; font-size: 14px; font-family: 'Baloo 2', sans-serif; font-weight: 700; transition: all 0.3s ease;">EN</a>
    </div>
  </div>

  <!-- Main Navigation Bar -->
  <div class="nm-main-nav" style="display: flex; justify-content: space-between; align-items: center; padding: 12px 5%; width: 100%; box-sizing: border-box;">
''' + inner_content + '''
  </div>
</header>'''

    # Since we added styles dynamically to header, we should remove conflicting CSS rules
    content = content[:match.start()] + new_header + content[match.end():]
    
    # We must remove padding from .nm-nav-header in standard CSS so it doesn't override our flex-direction column stuff
    content = content.replace('padding: 24px 5%;', '/* padding: 24px 5%; removed for top bar */')
    content = content.replace('padding: 18px 5%;', '/* padding: 18px 5%; removed for top bar */')
    content = content.replace('justify-content: space-between;', '/* justify-content: space-between; removed for top bar */')

    open('views/index.ejs', 'w', encoding='utf-8').write(content)
    print("Header rewritten successfully!")
else:
    print("Could not find header")

