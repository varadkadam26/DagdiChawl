with open('views/index.ejs', 'r', encoding='utf-8') as f:
    text = f.read()

historic_start = text.find('<span class="lang-en">HISTORIC GOLDEN MOMENTS</span>')
if historic_start != -1:
    section_start = text.rfind('<section', 0, historic_start)
    section_end = text.find('</section>', historic_start)
    if section_start != -1 and section_end != -1:
        text = text[:section_start] + text[section_end + len('</section>'):]

with open('views/index.ejs', 'w', encoding='utf-8') as f:
    f.write(text)
