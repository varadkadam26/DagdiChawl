from bs4 import BeautifulSoup
import codecs

with codecs.open('dagdi chawl.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

body = soup.find('body')
if body:
    children = body.find_all(recursive=False)
    for i, child in enumerate(children):
        c_id = child.get('id', '')
        c_class = child.get('class', [])
        print(f"[{i}] <{child.name}> id: {c_id} class: {c_class}")
