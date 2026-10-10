import os

files_to_check = [
    r'c:\Users\Manish\Downloads\mmmdagdichawl-main (1)\mmmdagdichawl-main\views\contact.ejs',
    r'c:\Users\Manish\Downloads\mmmdagdichawl-main (1)\mmmdagdichawl-main\public\js\i18n.js',
    r'c:\Users\Manish\Downloads\mmmdagdichawl-main (1)\mmmdagdichawl-main\README.md'
]

for file_path in files_to_check:
    if not os.path.exists(file_path):
        continue
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacements
    content = content.replace("mcrofficial1973@gmail.com<br>\n            marketing.dagdichawlcharaja@gmail.com", "byculladagadichawlnavratri1973@gmail.com")
    content = content.replace("mcrofficial1973@gmail.com<br>\\r\\n            marketing.dagdichawlcharaja@gmail.com", "byculladagadichawlnavratri1973@gmail.com")
    
    # In i18n.js
    content = content.replace("mcrofficial1973@gmail.com\\nmarketing.dagdichawlcharaja@gmail.com", "byculladagadichawlnavratri1973@gmail.com")
    
    # In README
    content = content.replace("marketing.dagdichawlcharaja@gmail.com` & `mcrofficial1973@gmail.com", "byculladagadichawlnavratri1973@gmail.com")
    content = content.replace("marketing.dagdichawlcharaja@gmail.com", "byculladagadichawlnavratri1973@gmail.com")
    content = content.replace("mcrofficial1973@gmail.com", "byculladagadichawlnavratri1973@gmail.com")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
print('Done replacements 2')
