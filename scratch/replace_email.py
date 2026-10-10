import os

file_path = r'c:\Users\Manish\Downloads\mmmdagdichawl-main (1)\mmmdagdichawl-main\public\js\i18n.min.js'

if os.path.exists(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacing in i18n
    content = content.replace("mcrofficial1973@gmail.com\\nmarketing.dagdichawlichiaaimauli@gmail.com", "byculladagadichawlnavratri1973@gmail.com")
    content = content.replace("mcrofficial1973@gmail.com\\\\nmarketing.dagdichawlichiaaimauli@gmail.com", "byculladagadichawlnavratri1973@gmail.com")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
print('Done replacement in i18n')
