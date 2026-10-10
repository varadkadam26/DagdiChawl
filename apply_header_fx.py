import re

content = open('views/partials/header.ejs', encoding='utf-8').read()

# Replace the inline style of .nm-nav-header
content = re.sub(
    r'<header class="nm-nav-header" style="flex-direction: column; padding: 0; align-items: stretch; background: <%= currentTabName === \'home\' \? \'transparent\' : \'url\(/images/final_page_no_text\.jpg\) center top / cover no-repeat\' %>;">',
    '<header class="nm-nav-header" style="flex-direction: column; padding: 0; align-items: stretch; background: <%= currentTabName === \'home\' ? \'rgba(0,0,0,0.2)\' : \'rgba(21, 19, 15, 0.7)\' %>; backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); box-shadow: inset 0 0 40px 15px rgba(0,0,0,0.9);">',
    content
)

# On other pages, if the header is just rgba(21, 19, 15, 0.7) and blurred, but there is no image behind it, it will just blur the solid body background which looks okay, but it might not be the cave image.
# If they want the header on other pages to have the cave image BUT blurred, we need a pseudo-element. 
# Let's add a CSS block to do this perfectly.

new_css = '''  .nm-nav-header {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    z-index: 100;
    display: flex;
    align-items: center;
    box-sizing: border-box;
    border-bottom: none;
    overflow: hidden; /* For vignette and pseudo-element */
  }

  /* Only on non-home pages, inject the blurred cave background */
  body:not([data-lang]) .nm-nav-header::before,
  body[data-lang] .nm-nav-header::before {
    content: "";
    position: absolute;
    top: -20px; left: -20px; right: -20px; bottom: -20px;
    background: url(/images/final_page_no_text.jpg) center top / cover no-repeat;
    filter: blur(15px);
    z-index: -2;
    opacity: <%= currentTabName === 'home' ? '0' : '1' %>;
  }
  
  .nm-nav-header::after {
    content: "";
    position: absolute;
    inset: 0;
    box-shadow: inset 0 0 60px 20px rgba(0,0,0,0.9);
    z-index: -1;
    pointer-events: none;
  }
'''

content = re.sub(r'\.nm-nav-header \{.*?border-bottom: none;\s*\}', new_css, content, flags=re.DOTALL)

open('views/partials/header.ejs', 'w', encoding='utf-8').write(content)
print("Updated header effects")
