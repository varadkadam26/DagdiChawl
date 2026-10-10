import re

with open('views/index.ejs', 'r', encoding='utf-8') as f:
    text = f.read()

# Restore HTML structure
old_html = """    <div class="aspect-wrapper">
      <img src="/images/final_page_no_text.jpg" alt="Shree Navratri Mandal Home" class="bg-image" id="devi-bg-img" />
      
      <!-- Animated Fire Glows for the Lamps (Auto-aligned by JS) -->
      <div class="fire-glow lamp-left"></div>
      <div class="fire-glow lamp-right"></div>
      
      <!-- Razor-sharp HD Devi Idol overlaid EXACTLY on top -->
      <div class="hd-devi-wrapper">
        <img src="/devi-idol.png" alt="HD Devi" class="hd-devi" />
      </div>
    </div>"""

old_html_fallback = """    <div class="aspect-wrapper">
      <img src="/images/final_page_no_text.jpg" alt="Shree Navratri Mandal Home" class="bg-image" id="devi-bg-img" />
      
      <!-- Razor-sharp HD Devi Idol overlaid EXACTLY on top -->
      <div class="hd-devi-wrapper">
        <img src="/devi-idol.png" alt="HD Devi" class="hd-devi" />
      </div>
    </div>"""

new_html = """    <img src="/images/final_page_no_text.jpg" alt="Shree Navratri Mandal Home" class="bg-image" id="devi-bg-img" />
    
    <!-- Animated Fire Glows for the Lamps (Auto-aligned by JS) -->
    <div class="fire-glow lamp-left"></div>
    <div class="fire-glow lamp-right"></div>
    
    <!-- Razor-sharp HD Devi Idol overlaid EXACTLY on top -->
    <div class="hd-devi-wrapper">
      <img src="/devi-idol.png" alt="HD Devi" class="hd-devi" />
    </div>"""

new_html_fallback = """    <img src="/images/final_page_no_text.jpg" alt="Shree Navratri Mandal Home" class="bg-image" id="devi-bg-img" />
    
    <!-- Razor-sharp HD Devi Idol overlaid EXACTLY on top -->
    <div class="hd-devi-wrapper">
      <img src="/devi-idol.png" alt="HD Devi" class="hd-devi" />
    </div>"""

if old_html in text:
    text = text.replace(old_html, new_html)
elif old_html_fallback in text:
    text = text.replace(old_html_fallback, new_html_fallback)
else:
    print("WARNING: Could not find HTML to replace!")

css_update = """
  /* HD Devi Wrapper for Mobile Fix */
  .aspect-wrapper {
    position: absolute;
    top: 50%;
    left: 74%; /* matches previous object-position */
    width: max(100vw, calc(100vh * 1.556231));
    height: max(100vh, calc(100vw * 0.642578));
    transform: translate(-74%, -50%);
  }
  .aspect-wrapper img.bg-image {
    width: 100%;
    height: 100%;
    object-fit: fill;
    display: block;
  }
"""

text = text.replace(css_update, '')
text = text.replace('/* object-fit: cover; removed for aspect-wrapper */', 'object-fit: cover;')
text = text.replace('/* object-position removed for aspect-wrapper */', 'object-position: 74% center;')

with open('views/index.ejs', 'w', encoding='utf-8') as f:
    f.write(text)

print("Restored views/index.ejs")
