import glob

# 1. Update style.css
css_path = 'public/css/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Add a powerful override at the end
css_override = """
/* USER REQUEST: EVERY TEXT MUST BE BALOO 2 BOLD */
body, h1, h2, h3, h4, h5, h6, p, span:not([class*='fa']), a, div, li, button, input, textarea, strong, em, b, i:not([class*='fa']) {
    font-family: 'Baloo 2', sans-serif !important;
    font-weight: 700 !important;
}
:root {
    --font-en-head: 'Baloo 2', sans-serif !important;
    --font-mr-head: 'Baloo 2', sans-serif !important;
    --font-body: 'Baloo 2', sans-serif !important;
}
"""
if 'USER REQUEST: EVERY TEXT MUST BE BALOO 2 BOLD' not in css:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write('\n' + css_override)

# 2. Update inline styles in all EJS files
for path in glob.glob('views/**/*.ejs', recursive=True):
    with open(path, 'r', encoding='utf-8') as f:
        data = f.read()
    
    # Replace inline font families
    data = data.replace("font-family: 'Lato', sans-serif;", "font-family: 'Baloo 2', sans-serif;")
    data = data.replace("font-family: 'Cinzel', serif;", "font-family: 'Baloo 2', sans-serif;")
    data = data.replace("font-weight: 400", "font-weight: 700")
    data = data.replace("font-weight: 500", "font-weight: 700")
    data = data.replace("font-weight: 600", "font-weight: 700")
    data = data.replace("font-weight: 300", "font-weight: 700")
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(data)

print('Updated all text to Baloo 2 Bold')
