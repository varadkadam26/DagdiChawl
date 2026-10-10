import re

content = open('views/index.ejs', encoding='utf-8').read()

# Replace the base class CSS
new_base = '''  .arun-gawli-badge {
    font-family: 'Baloo 2', sans-serif !important;
    font-weight: 700 !important;
    border: none !important;
    background: transparent !important;
    padding-left: 0 !important;
    padding-right: 0 !important;
    letter-spacing: 0.5px !important;
    white-space: nowrap !important;
    font-size: 1.25rem !important; /* BIGGER IN LAPTOP VIEW */
  }'''

content = re.sub(
    r'\.arun-gawli-badge\s*\{[^}]*\}',
    new_base,
    content,
    count=1
)

# Replace the media query CSS
new_mobile = '''  @media (max-width: 768px) {
    .arun-gawli-badge {
      font-size: min(15.5px, 4.2vw) !important;
      letter-spacing: 0 !important;
      display: block !important;
      text-align: center !important;
      width: 100% !important;
    }
  }'''

content = re.sub(
    r'@media \(max-width: 768px\)\s*\{\s*\.arun-gawli-badge\s*\{[^}]*\}\s*\}',
    new_mobile,
    content
)

open('views/index.ejs', 'w', encoding='utf-8').write(content)
print("Updated CSS")
