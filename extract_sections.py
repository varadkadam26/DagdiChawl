import re
with open('dagdi chawl.html', 'r', encoding='utf-8') as f:
    html = f.read()

sections = re.findall(r'(<section.*?</section>)', html, re.DOTALL | re.IGNORECASE)
for i, s in enumerate(sections):
    match = re.search(r'<section\s+[^>]*id=\"([^\"]+)\"', s, re.IGNORECASE)
    sec_id = match.group(1) if match else 'no-id'
    match2 = re.search(r'<section\s+[^>]*class=\"([^\"]+)\"', s, re.IGNORECASE)
    sec_class = match2.group(1) if match2 else 'no-class'
    print(f'Section {i}: id={sec_id}, class={sec_class}')

