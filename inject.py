import re

content = open('views/index.ejs', encoding='utf-8').read()

# Add desktop CSS for hamburger and logo
desktop_css = '''  .nm-logo-container:hover {
    transform: scale(1.02);
  }

  .nm-nav-logo {
    width: 70px;
    height: 70px;
  }

  .nm-hamburger {
    display: none;
    flex-direction: column;
    gap: 5px;
    cursor: pointer;
    z-index: 101;
  }
  .nm-hamburger span {
    display: block;
    width: 25px;
    height: 3px;
    background-color: #D4AF37;
    border-radius: 3px;
    transition: all 0.3s ease;
  }
'''
content = content.replace('  .nm-logo-container:hover {\n    transform: scale(1.02);\n  }', desktop_css)

# Update mobile CSS
mobile_css_old = '''    .nm-nav-links {
      display: none; 
    }
    .nm-logo-container {
      gap: 6px;
    }'''

mobile_css_new = '''    .nm-nav-links {
      display: none; 
      flex-direction: column;
      position: absolute;
      top: 100%;
      left: 0;
      width: 100%;
      background: rgba(5,5,6,0.95);
      backdrop-filter: blur(15px);
      -webkit-backdrop-filter: blur(15px);
      padding: 20px 5%;
      border-bottom: 1px solid rgba(212, 175, 55, 0.15);
      box-sizing: border-box;
      gap: 20px;
    }
    .nm-nav-links.active {
      display: flex;
    }
    .nm-hamburger {
      display: flex;
    }
    .nm-nav-logo {
      width: 45px !important;
      height: 45px !important;
    }
    .nm-logo-container {
      gap: 6px;
    }'''
content = content.replace(mobile_css_old, mobile_css_new)

# Update mobile title font size
content = content.replace('font-size: 2.7vw; /* Increased size to make it more readable */', 'font-size: clamp(8px, 2.3vw, 12px);')

open('views/index.ejs', 'w', encoding='utf-8').write(content)
print('Done injecting')
