import re

with open('views/index.ejs', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the HTML structure
old_html = """    <img src="/images/final_page_no_text.jpg" alt="Shree Navratri Mandal Home" class="bg-image" id="devi-bg-img" />
    
    <!-- Animated Fire Glows for the Lamps (Auto-aligned by JS) -->
    <div class="fire-glow lamp-left"></div>
    <div class="fire-glow lamp-right"></div>
    
    <!-- Razor-sharp HD Devi Idol overlaid EXACTLY on top -->
    
    <div class="hd-devi-wrapper">
      <img src="/devi-idol.png" alt="HD Devi" class="hd-devi" />
    </div>"""

# Fallback without fire glows if they are different
old_html_fallback = """    <img src="/images/final_page_no_text.jpg" alt="Shree Navratri Mandal Home" class="bg-image" id="devi-bg-img" />
    
    <!-- Razor-sharp HD Devi Idol overlaid EXACTLY on top -->
    <div class="hd-devi-wrapper">
      <img src="/devi-idol.png" alt="HD Devi" class="hd-devi" />
    </div>"""

new_html = """    <div class="aspect-wrapper">
      <img src="/images/final_page_no_text.jpg" alt="Shree Navratri Mandal Home" class="bg-image" id="devi-bg-img" />
      
      <!-- Animated Fire Glows for the Lamps (Auto-aligned by JS) -->
      <div class="fire-glow lamp-left"></div>
      <div class="fire-glow lamp-right"></div>
      
      <!-- Razor-sharp HD Devi Idol overlaid EXACTLY on top -->
      <div class="hd-devi-wrapper">
        <img src="/devi-idol.png" alt="HD Devi" class="hd-devi" />
      </div>
    </div>"""

new_html_fallback = """    <div class="aspect-wrapper">
      <img src="/images/final_page_no_text.jpg" alt="Shree Navratri Mandal Home" class="bg-image" id="devi-bg-img" />
      
      <!-- Razor-sharp HD Devi Idol overlaid EXACTLY on top -->
      <div class="hd-devi-wrapper">
        <img src="/devi-idol.png" alt="HD Devi" class="hd-devi" />
      </div>
    </div>"""

if old_html in text:
    text = text.replace(old_html, new_html)
elif old_html_fallback in text:
    text = text.replace(old_html_fallback, new_html_fallback)
else:
    print("Could not find the target HTML to replace!")

# Add CSS for aspect-wrapper and remove old bg-image styles
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

if '.aspect-wrapper' not in text:
    text = text.replace('  .image-container img.bg-image {', css_update + '\n  .image-container img.bg-image {')

# Remove the hidden rule for mobile
text = re.sub(r'@media \(max-width: 1200px\)\s*\{\s*\.hd-devi-wrapper \{ display: none !important; \}\s*\}', '', text)
text = re.sub(r'\.hd-devi-wrapper \{ display: none !important; \}', '/* Removed hidden rule to show HD devi on mobile */', text)

# Remove the object-fit cover from mobile media query
text = text.replace('object-fit: cover;', '/* object-fit: cover; removed for aspect-wrapper */')
text = text.replace('object-position: 74% center;', '/* object-position removed for aspect-wrapper */')

with open('views/index.ejs', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated index.ejs for mobile HD Devi')
