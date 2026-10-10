import os
import re

def rename_and_replace():
    # 1. Replace text in files
    for root, dirs, files in os.walk('.'):
        if '.git' in root or 'node_modules' in root:
            continue
        for file in files:
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except:
                continue
                
            # Replace filenames first
            content = content.replace("dagdichawl.html", "dagdichawl.html")
            content = content.replace("dagdichawl_ganpati", "dagdichawl_ganpati")
            
            # Case insensitive replace but keep original casing for the replacement (always uppercase words as it's a name)
            content = re.sub(r'(?i)Dagdi Chawl Chi Aai Mauli', 'Dagdi Chawl Chi Aai Mauli', content)
            content = re.sub(r'(?i)Dagdi Chawl', 'Dagdi Chawl', content)
            content = re.sub(r'(?i)Dagdi Chawl', 'Dagdi Chawl', content)
            
            try:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
            except:
                pass

    # 2. Rename files
    for root, dirs, files in os.walk('.', topdown=False):
        if '.git' in root or 'node_modules' in root:
            continue
        for file in files:
            if 'Dagdi Chawl' in file.lower():
                old_filepath = os.path.join(root, file)
                new_filename = file.replace('Dagdi Chawl', 'dagdichawl').replace('Dagdi Chawl', 'Dagdichawl')
                new_filepath = os.path.join(root, new_filename)
                os.rename(old_filepath, new_filepath)

rename_and_replace()
