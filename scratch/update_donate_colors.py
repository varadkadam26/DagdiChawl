import os

filepath = r'c:\Users\Manish\Downloads\mmmdagdichawl-main (1)\mmmdagdichawl-main\views\donate.ejs'
if os.path.exists(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update text colors in labels and texts
    content = content.replace('color: var(--text-main);', 'color: #FFFFFF;')
    content = content.replace('color: var(--text-dark);', 'color: #FFFFFF;')
    
    # 2. Update temple-maroon which is too dark for the background
    content = content.replace('color: var(--temple-maroon);', 'color: var(--royal-gold);')
    
    # 3. Update the small info text color
    content = content.replace('color: #666;', 'color: #D1D5DB;')
    
    # 4. Bank account card needs contrast adjustments
    # the bank account list text might be white now.
    
    # 5. Fix card backgrounds. The cards have inline styles:
    # background: #FFFFFF; -> background: transparent; or rgba(0,0,0,0.5)
    content = content.replace('background: #FFFFFF;', 'background: rgba(10, 10, 10, 0.6);')
    content = content.replace('background: var(--bg-cream);', 'background: rgba(255, 255, 255, 0.05);')
    
    # Note: Modal uses background: #FFFFFF; too, which is replaced. Modal text is still dark, so let's adjust modal text.
    # We replaced temple-maroon with royal-gold so modal title will be royal gold.
    # we replaced text-main with #FFF so it's okay.
    content = content.replace('color: #4B5563;', 'color: #E5E7EB;')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Colors updated in donate.ejs")
