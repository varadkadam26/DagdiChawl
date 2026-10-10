content = open('views/index.ejs', encoding='utf-8').read()

old_html = '''              <picture>
                <source srcset="/images/dagdi chawl_ganpati_06.webp" type="image/webp">
                <img src="/images/dagdi chawl_ganpati_06.jpg" alt="Dagdi Chawl Cha Raja Ganpati" width="600" height="460"
                  loading="lazy"
                  style="width: 100%; height: 460px; object-fit: cover; object-position: center center; display: block;">
              </picture>'''

new_html = '''              <picture>
                <img src="/images/president.jpg" alt="President" width="600" height="460"
                  loading="lazy"
                  style="width: 100%; height: 460px; object-fit: cover; object-position: center top; display: block;">
              </picture>'''

content = content.replace(old_html, new_html)

open('views/index.ejs', 'w', encoding='utf-8').write(content)
print('Updated photo')
