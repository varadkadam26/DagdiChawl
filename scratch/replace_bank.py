import os

files_to_modify = [
    r'c:\Users\Manish\Downloads\mmmmalabarhill-main (1)\mmmmalabarhill-main\views\donate.ejs',
    r'c:\Users\Manish\Downloads\mmmmalabarhill-main (1)\mmmmalabarhill-main\views\tshirt.ejs'
]

replacements = {
    "SVC Co-Operative Bank Ltd.": "Bank of Maharashtra",
    "Shree Bal Gopal Ganeshutsav Mandal (Bal Gopal Mandal)": "BYCULLA DAGDI CHAWL SARVAJANIK NAVRATROTSAV MANDAL",
    "100903130041974": "20023347685",
    "SVCB0000009": "MAHB0000294",
    "Sleater Road": "MUMBAI JACOB CIRCLE"
}

for fp in files_to_modify:
    if os.path.exists(fp):
        with open(fp, 'r', encoding='utf-8') as f:
            content = f.read()

        for old_str, new_str in replacements.items():
            content = content.replace(old_str, new_str)

        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)

print("Done bank details replacement")
