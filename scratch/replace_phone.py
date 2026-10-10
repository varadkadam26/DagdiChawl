import os

files_to_modify = [
    r'c:\Users\Manish\Downloads\mmmdagdichawl-main (1)\mmmdagdichawl-main\dagdi chawl.html',
    r'c:\Users\Manish\Downloads\mmmdagdichawl-main (1)\mmmdagdichawl-main\views\partials\header.ejs',
    r'c:\Users\Manish\Downloads\mmmdagdichawl-main (1)\mmmdagdichawl-main\views\contact.ejs',
    r'c:\Users\Manish\Downloads\mmmdagdichawl-main (1)\mmmdagdichawl-main\views\advertisement.ejs',
    r'c:\Users\Manish\Downloads\mmmdagdichawl-main (1)\mmmdagdichawl-main\README.md'
]

for fp in files_to_modify:
    if os.path.exists(fp):
        with open(fp, 'r', encoding='utf-8') as f:
            content = f.read()

        # Unspaced English
        content = content.replace("+919326150793", "+919594512999")
        
        # Spaced English
        content = content.replace("+91 93261 50793", "+91 95945 12999")

        # Spaced Marathi
        content = content.replace("+९१ ९३२६१ ५०७९३", "+९१ ९५९४५ १२९९९")

        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)

print("Done phone replacement")
