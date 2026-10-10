import os
import re

# Update tshirt.ejs
tshirt_path = r'c:\Users\Manish\Downloads\mmmmalabarhill-main (1)\mmmmalabarhill-main\views\tshirt.ejs'
if os.path.exists(tshirt_path):
    with open(tshirt_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the img tag
    content = re.sub(
        r'<img src="https://api\.qrserver\.com[^>]+>',
        r'<img src="/images/qr_code.png" alt="Bank of Maharashtra UPI QR Code for Byculla Dagdi Chawl Navratrotsav Mandal" style="width: 250px; height: auto; display: block;">',
        content
    )
    # Replace UPI
    content = content.replace('SVCMERC00301799@svcbank', 'bdc@mahb')
    # Replace Bank Name text
    content = content.replace('SVC CO-OPERATIVE BANK LTD.', 'Bank of Maharashtra')
    
    with open(tshirt_path, 'w', encoding='utf-8') as f:
        f.write(content)

# Update donate.js
donate_js_path = r'c:\Users\Manish\Downloads\mmmmalabarhill-main (1)\mmmmalabarhill-main\public\js\donate.js'
if os.path.exists(donate_js_path):
    with open(donate_js_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace dynamic QR with static image
    old_qr_code = """    const upiString = `upi://pay?pa=SVCMERC00301799@svcbank&pn=Shree%20Bal%20Gopal%20Ganeshutsav%20Mandal&am=${amount}&cu=INR`;
    if (upiQrCodeImg) {
      upiQrCodeImg.src = `https://api.qrserver.com/v1/create-qr-code/?size=220x220&data=${encodeURIComponent(upiString)}`;
    }"""
    
    new_qr_code = """    if (upiQrCodeImg) {
      upiQrCodeImg.src = `/images/qr_code.png`;
    }"""
    content = content.replace(old_qr_code, new_qr_code)
    content = content.replace('SVCMERC00301799@svcbank', 'bdc@mahb')
    
    with open(donate_js_path, 'w', encoding='utf-8') as f:
        f.write(content)

# Update donate.min.js
donate_min_js_path = r'c:\Users\Manish\Downloads\mmmmalabarhill-main (1)\mmmmalabarhill-main\public\js\donate.min.js'
if os.path.exists(donate_min_js_path):
    with open(donate_min_js_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace dynamic generation code
    content = re.sub(
        r'const p=`upi://pay\?pa=[^`]+`;l&&\(l\.src=`https://api\.qrserver\.com/v1/create-qr-code/\?size=220x220&data=\$\{encodeURIComponent\(p\)\}`\)',
        r'l&&(l.src=`/images/qr_code.png`)',
        content
    )
    content = content.replace('SVCMERC00301799@svcbank', 'bdc@mahb')
    
    with open(donate_min_js_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
# Update tshirt.min.js if it exists
tshirt_min_js_path = r'c:\Users\Manish\Downloads\mmmmalabarhill-main (1)\mmmmalabarhill-main\public\js\tshirt.min.js'
if os.path.exists(tshirt_min_js_path):
    with open(tshirt_min_js_path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = re.sub(
        r'const u=`upi://pay\?pa=[^`]+`;l&&\(l\.src=`https://api\.qrserver\.com/v1/create-qr-code/\?size=220x220&data=\$\{encodeURIComponent\(u\)\}`\)',
        r'l&&(l.src=`/images/qr_code.png`)',
        content
    )
    content = content.replace('SVCMERC00301799@svcbank', 'bdc@mahb')
    
    with open(tshirt_min_js_path, 'w', encoding='utf-8') as f:
        f.write(content)

# Update tshirt.js if it exists
tshirt_js_path = r'c:\Users\Manish\Downloads\mmmmalabarhill-main (1)\mmmmalabarhill-main\public\js\tshirt.js'
if os.path.exists(tshirt_js_path):
    with open(tshirt_js_path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = re.sub(
        r'const upiString = `upi://pay\?pa=[^`]+`;[\s\r\n]*if\s*\(upiQrCodeImg\)\s*{\s*upiQrCodeImg\.src = `https://api\.qrserver\.com/v1/create-qr-code/\?size=220x220&data=\$\{encodeURIComponent\(upiString\)\}`;\s*}',
        r'if (upiQrCodeImg) { upiQrCodeImg.src = `/images/qr_code.png`; }',
        content
    )
    content = content.replace('SVCMERC00301799@svcbank', 'bdc@mahb')
    
    with open(tshirt_js_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Replacement script executed")
