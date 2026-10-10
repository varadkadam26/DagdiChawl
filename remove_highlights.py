import codecs

with codecs.open('views/index.ejs', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_del = -1
end_del = -1

# Find where the MOCKUP HIGHLIGHTS CSS and HTML start and end
for i, l in enumerate(lines):
    if '<style>' in l and 'HIGHLIGHTS SECTION' in lines[i+1] if i+1 < len(lines) else False:
        start_del = i
    if '</section>' in l and start_del != -1 and '<!-- EXTRACTED FROM dagdichawlcharaja.in -->' in lines[i+2] if i+2 < len(lines) else False:
        end_del = i
        break
    # In case the exact spacing varies:
    if '<!-- EXTRACTED FROM dagdichawlcharaja.in -->' in l and start_del != -1:
        end_del = i - 1
        break

if start_del != -1 and end_del != -1:
    print(f"Deleting from line {start_del} to {end_del}")
    del lines[start_del:end_del+1]

with codecs.open('views/index.ejs', 'w', encoding='utf-8') as f:
    f.writelines(lines)
