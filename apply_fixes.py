import re

with open('views/index.ejs', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Remove Faith, Culture title
old_faith = """            <h2 class="section-title" style="margin-top: 0.5rem; line-height: 1.3;">
              <span class="lang-mr">श्रद्धा, संस्कृती आणि भक्ती</span>
              <span class="lang-en">Faith, Culture & Devotion</span>
            </h2>"""
text = text.replace(old_faith, '')

# 2. Make second Arun Gawli white and glow
old_gawli = """<h4 style="margin: 0; color: var(--temple-maroon); font-size: 1.15rem;">"""
new_gawli = """<h4 style="margin: 0; color: #FFFFFF; font-size: 1.25rem; text-shadow: 0 0 12px rgba(203, 161, 53, 0.9), 0 0 24px rgba(203, 161, 53, 0.5), 0 0 35px rgba(203, 161, 53, 0.3); font-weight: 800; letter-spacing: 0.5px;">"""
text = text.replace(old_gawli, new_gawli)

# 3. Remove Enchanting Form section
# Regex is safer for removing the block
enchant_pattern = re.compile(r'\s*<section style="padding: 6rem 0;">\s*<div class="container">\s*<div class="grid-2" style="align-items: center; gap: 4rem;">\s*<div class="gold-motion-frame"[^>]*>.*?The Enchanting Form of Aai Mauli.*?</section>', re.DOTALL)
text = re.sub(enchant_pattern, '', text)

# 4. Marquee Mobile Size
text = text.replace('height: 145px !important;', 'height: 185px !important;')
text = text.replace('width: 115px !important;', 'width: 148px !important;')
text = text.replace('height: 135px !important;', 'height: 175px !important;')
text = text.replace('width: 108px !important;', 'width: 140px !important;')

# 5. Mandap Darshan Location
text = text.replace('<span class="section-badge">\n            <span class="lang-mr">मंडप स्थान व संपर्क', '<span class="section-badge" style="color: #FFFFFF; text-shadow: 0 0 8px rgba(203, 161, 53, 0.6);">\n            <span class="lang-mr">मंडप स्थान व संपर्क')

text = text.replace('<h2 class="section-title">\n            <span class="lang-mr">मंडप दर्शन स्थान व नकाशा</span>', '<h2 class="section-title" style="color: #FFFFFF; text-shadow: 0 0 10px rgba(203, 161, 53, 0.7);">\n            <span class="lang-mr">मंडप दर्शन स्थान व नकाशा</span>')

text = text.replace('<p class="section-subtitle">\n            <span class="lang-mr">७१४, दगडी चाळ, बापूराव जगताप मार्ग, भायखळा (पश्चिम), मुंबई - ४०००११.</span>', '<p class="section-subtitle" style="color: #FFFFFF; text-shadow: 0 0 6px rgba(203, 161, 53, 0.5);">\n            <span class="lang-mr">७१४, दगडी चाळ, बापूराव जगताप मार्ग, भायखळा (पश्चिम), मुंबई - ४०००११.</span>')

# 6. Contact Information Card
text = text.replace('<h3 style="color: var(--temple-maroon); font-size: 1.6rem; margin-bottom: 1.2rem;">', '<h3 style="color: #FFFFFF; text-shadow: 0 0 6px rgba(203, 161, 53, 0.5); font-size: 1.6rem; margin-bottom: 1.2rem;">')

text = text.replace('<p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 1.5rem;">', '<p style="color: #FFFFFF; text-shadow: 0 0 6px rgba(203, 161, 53, 0.5); line-height: 1.8; margin-bottom: 1.5rem;">')

text = text.replace('<i class="fa-solid fa-location-dot" style="color: var(--primary-saffron); margin-right: 10px;"></i>', '<i class="fa-solid fa-location-dot" style="color: #FFFFFF; text-shadow: 0 0 8px rgba(203, 161, 53, 0.6); margin-right: 10px;"></i>')

text = text.replace('<i class="fa-solid fa-file-shield" style="color: var(--primary-saffron); margin-right: 10px;"></i>', '<i class="fa-solid fa-file-shield" style="color: #FFFFFF; text-shadow: 0 0 8px rgba(203, 161, 53, 0.6); margin-right: 10px;"></i>')

text = text.replace('<a href="https://www.facebook.com/malabarhillcharaja" target="_blank" rel="noopener noreferrer"\n                class="btn btn-outline" style="font-size: 0.85rem;">\n                <i class="fa-brands fa-facebook" style="color: #1877F2; margin-right: 6px;"></i>', '<a href="https://www.facebook.com/malabarhillcharaja" target="_blank" rel="noopener noreferrer"\n                class="btn btn-outline" style="color: #FFFFFF; text-shadow: 0 0 6px rgba(203, 161, 53, 0.5); font-size: 0.85rem; border-color: rgba(203, 161, 53, 0.5);">\n                <i class="fa-brands fa-facebook" style="color: #FFFFFF; text-shadow: 0 0 8px rgba(203, 161, 53, 0.6); margin-right: 6px;"></i>')

with open('views/index.ejs', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixes applied successfully")
