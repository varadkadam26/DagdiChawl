content = open('views/index.ejs', encoding='utf-8').read()

# 1. Update Social Icons
content = content.replace(
    '''<a href="https://www.facebook.com/BycullaDagadiChawl/" target="_blank" style="color: #F4EDE0; font-size: 16px; transition: color 0.3s;"><i class="fa-brands fa-facebook-f"></i></a>''',
    '''<a href="https://www.facebook.com/BycullaDagadiChawl/" target="_blank" style="color: #d8ba66; font-size: 16px; transition: color 0.3s; text-shadow: 0 0 5px rgba(216,186,102,0.3);"><i class="fa-brands fa-facebook-f"></i></a>'''
)
content = content.replace(
    '''<a href="https://www.instagram.com/byculla_dagadichawl_navratri/" target="_blank" style="color: #F4EDE0; font-size: 16px; transition: color 0.3s;"><i class="fa-brands fa-instagram"></i></a>''',
    '''<a href="https://www.instagram.com/byculla_dagadichawl_navratri/" target="_blank" style="color: #d8ba66; font-size: 16px; transition: color 0.3s; text-shadow: 0 0 5px rgba(216,186,102,0.3);"><i class="fa-brands fa-instagram"></i></a>'''
)
content = content.replace(
    '''<a href="https://www.youtube.com/@MalabarHillChaRaja-e2z" target="_blank" style="color: #F4EDE0; font-size: 16px; transition: color 0.3s;"><i class="fa-brands fa-youtube"></i></a>''',
    '''<a href="https://www.youtube.com/@MalabarHillChaRaja-e2z" target="_blank" style="color: #d8ba66; font-size: 16px; transition: color 0.3s; text-shadow: 0 0 5px rgba(216,186,102,0.3);"><i class="fa-brands fa-youtube"></i></a>'''
)

# 2. Update Toggle Button colors
# We previously appended to the CSS, let's just append more CSS to override it
css_add = '''
  .ios-glass-switch {
    border-color: rgba(212, 175, 55, 0.4) !important;
  }
  .ios-glass-switch .lang-btn {
    color: rgba(212, 175, 55, 0.5) !important;
  }
  .ios-glass-switch .lang-btn:hover {
    color: rgba(212, 175, 55, 0.9) !important;
  }
  .ios-glass-switch .lang-btn.active {
    background: #d8ba66 !important;
    color: #1a1403 !important;
    box-shadow: 0 2px 10px rgba(212, 175, 55, 0.4) !important;
  }
  
  /* Golden glow behind President photo */
  .president-img {
    box-shadow: 0 0 60px rgba(212, 175, 55, 0.5), 0 0 20px rgba(212, 175, 55, 0.3) !important;
  }
  .gold-motion-frame {
    box-shadow: 0 0 40px rgba(212, 175, 55, 0.3) !important;
  }
'''
content = content.replace('</style>', css_add + '\n</style>')

open('views/index.ejs', 'w', encoding='utf-8').write(content)
print("Done!")
