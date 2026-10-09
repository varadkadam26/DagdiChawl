content = open('views/index.ejs', encoding='utf-8').read()

old_badge = '''            <span class="section-badge">
              <span class="lang-mr">?????? ???? ???? ???? ?? ????? ?????</span>
              <span class="lang-en">Hon. Shree Arun Gawli Ji's Thoughts</span>
            </span>'''

new_badge = '''            <span class="section-badge arun-gawli-badge">
              <span class="lang-mr">?????? ???? ???? ???? ?? ????? ?????</span>
              <span class="lang-en">Hon. Shree Arun Gawli Ji's Thoughts</span>
            </span>'''

if old_badge in content:
    content = content.replace(old_badge, new_badge)
else:
    print("Old badge not found. Let's try flexible search.")
    import re
    badge_regex = re.compile(r'<span class="section-badge">\s*<span class="lang-mr">?????? ???? ???? ???? ?? ????? ?????</span>\s*<span class="lang-en">Hon. Shree Arun Gawli Ji\'s Thoughts</span>\s*</span>')
    content = badge_regex.sub(new_badge, content)


css_to_add = '''
  .arun-gawli-badge {
    font-family: 'Baloo 2', sans-serif !important;
    font-weight: 700 !important;
    border: none !important;
    background: transparent !important;
    padding-left: 0 !important;
    padding-right: 0 !important;
    letter-spacing: 0.5px !important;
    white-space: nowrap !important;
  }
  @media (max-width: 768px) {
    .arun-gawli-badge {
      font-size: 11px !important;
      letter-spacing: 0 !important;
    }
  }
'''
content = content.replace('</style>', css_to_add + '\n</style>')

open('views/index.ejs', 'w', encoding='utf-8').write(content)
print("Badge updated")
