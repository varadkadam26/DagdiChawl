content = open('views/index.ejs', encoding='utf-8').read()

# Fix 1: Remove inline margin-right from logo
old_logo = '<img src="/images/nav_logo_transparent.png" alt="Mandal Logo" class="nm-nav-logo" style="object-fit: contain; filter: drop-shadow(0 0 10px rgba(255, 165, 0, 0.7)); margin-right: 8px;">'
new_logo = '<img src="/images/nav_logo_transparent.png" alt="Mandal Logo" class="nm-nav-logo" style="object-fit: contain; filter: drop-shadow(0 0 10px rgba(255, 165, 0, 0.7));">'
content = content.replace(old_logo, new_logo)

# Fix 2: Make mobile logo smaller and title strictly relative to vw
old_mobile_css = '''    .nm-nav-logo {
      width: 45px !important;
      height: 45px !important;
    }
    .nm-logo-container {
      gap: 6px;
    }
    .nm-trishul-icon {
      width: 22px;
      height: 30px;
    }
    .nm-logo-text {
      align-items: flex-start; /* Left align on mobile */
    }
    .nm-logo-title {
      font-size: clamp(8px, 2.3vw, 12px);
      white-space: nowrap;
      letter-spacing: 0px; /* Crucial: remove the 2px desktop letter spacing! */
    }'''

new_mobile_css = '''    .nm-nav-logo {
      width: 35px !important;
      height: 35px !important;
    }
    .nm-logo-container {
      gap: 4px;
      max-width: 80%; /* Ensure it doesn't push hamburger */
    }
    .nm-trishul-icon {
      width: 22px;
      height: 30px;
    }
    .nm-logo-text {
      align-items: flex-start;
      overflow: hidden;
    }
    .nm-logo-title {
      font-size: 2vw !important; /* Strictly scale with screen width to never overflow */
      white-space: nowrap;
      letter-spacing: 0px !important;
    }'''
content = content.replace(old_mobile_css, new_mobile_css)

open('views/index.ejs', 'w', encoding='utf-8').write(content)
print('Fixed mobile alignment')
