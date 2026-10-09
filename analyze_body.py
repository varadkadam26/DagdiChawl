import re

with open('malabar.html', 'r', encoding='utf-8') as f:
    html = f.read()

body_match = re.search(r'<body[^>]*>(.*?)</body>', html, re.DOTALL | re.IGNORECASE)
if body_match:
    body = body_match.group(1)
    # Let's see the main tags at the top level of body
    tags = re.findall(r'<([a-zA-Z0-9\-]+)(?:\s+[^>]*)?>', body)
    
    print("Top level tags inside body:")
    print(tags[:30])
