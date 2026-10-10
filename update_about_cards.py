import re

content = open('views/about.ejs', encoding='utf-8').read()

new_style = '''<style>
  body {
    background: linear-gradient(to bottom, #15130F 0%, #24170F 50%, #62462C 100%) !important;
    background-attachment: fixed !important;
    background-size: cover !important;
  }
  .main-content-gradient, .page-hero-banner {
    background: transparent !important;
  }
  
  /* Transparent Cards with Golden Border */
  .main-content-gradient > .container > div,
  .main-content-gradient .grid-2 > div,
  .stat-counter-card {
    background: rgba(212, 175, 55, 0.03) !important;
    border: 1px solid rgba(212, 175, 55, 0.4) !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2) !important;
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
  }

  /* Text Colors to compliment dark background */
  .main-content-gradient p,
  .main-content-gradient p span,
  .stat-label-text span {
    color: #E8DCC4 !important;
  }
  
  .main-content-gradient h2,
  .main-content-gradient h2 span,
  .main-content-gradient h3,
  .main-content-gradient h3 span,
  .stat-num-value {
    color: #D4AF37 !important;
    text-shadow: 0 2px 4px rgba(0,0,0,0.5) !important;
  }
  
  .main-content-gradient h2 {
    border-left-color: #D4AF37 !important;
  }
  
  .page-hero-banner h1 span,
  .page-hero-banner p span {
    color: #F4EDE0 !important;
  }
</style>'''

content = re.sub(r'<style>.*?</style>', new_style, content, flags=re.DOTALL)

open('views/about.ejs', 'w', encoding='utf-8').write(content)
print("Updated about us styles")
