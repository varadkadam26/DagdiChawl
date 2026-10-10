content = open('views/index.ejs', encoding='utf-8').read()

old_html = '''  <!-- Hamburger Menu Button (Mobile Only) -->
  <div class="nm-hamburger" onclick="document.querySelector('.nm-nav-links').classList.toggle('active')">
    <span></span>
    <span></span>
    <span></span>
  </div>

  <nav class="nm-nav-links">
    <a href="/" class="active">Home</a>
    <a href="/about">About</a>
    <a href="/gallery">Gallery</a>
    <a href="/contact">Contact</a>
  </nav>

  <a href="/donate" class="nm-donate-btn">Donate Now</a>'''

new_html = '''  <div style="display: flex; align-items: center; gap: 12px;">
    <!-- Language Toggle -->
    <div class="lang-toggle-container">
      <a href="#" class="lang-btn active" data-lang="mr">?????</a>
      <span>|</span>
      <a href="#" class="lang-btn" data-lang="en">EN</a>
    </div>

    <!-- Hamburger Menu Button (Mobile Only) -->
    <div class="nm-hamburger" onclick="document.querySelector('.nm-nav-links').classList.toggle('active')">
      <span></span>
      <span></span>
      <span></span>
    </div>

    <nav class="nm-nav-links">
      <a href="/" class="active">Home</a>
      <a href="/about">About</a>
      <a href="/gallery">Gallery</a>
      <a href="/contact">Contact</a>
    </nav>

    <a href="/donate" class="nm-donate-btn">Donate Now</a>
  </div>'''

content = content.replace(old_html, new_html)

css_to_add = '''
  .lang-toggle-container {
    display: flex;
    align-items: center;
    gap: 8px;
    background: rgba(0, 0, 0, 0.4);
    border: 1px solid rgba(212, 175, 55, 0.4);
    padding: 6px 12px;
    border-radius: 20px;
    z-index: 100;
  }
  .lang-toggle-container .lang-btn {
    color: rgba(244, 237, 224, 0.5);
    text-decoration: none;
    font-size: 14px;
    font-family: 'Baloo 2', sans-serif;
    font-weight: 700;
    transition: all 0.3s ease;
  }
  .lang-toggle-container .lang-btn.active {
    color: #D4AF37;
    text-shadow: 0 0 8px rgba(212, 175, 55, 0.6);
  }
  .lang-toggle-container span {
    color: rgba(212, 175, 55, 0.3);
    font-size: 12px;
  }
  
  @media (max-width: 768px) {
    .lang-toggle-container {
      padding: 4px 8px;
      gap: 5px;
    }
    .lang-toggle-container .lang-btn {
      font-size: 12px;
    }
  }
'''

# insert CSS right before </style>
content = content.replace('</style>', css_to_add + '\n</style>')

open('views/index.ejs', 'w', encoding='utf-8').write(content)
print('Added language toggle')
