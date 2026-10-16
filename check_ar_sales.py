import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect translations.ar for hero_bio, cta_title, cta_desc, cta_badge, etc.
pos_trans = text.find('const translations = {')
pos_en = text.find('en: {')
ar_text = text[pos_trans:pos_en]

for line in ar_text.splitlines():
    if any(k in line for k in ['hero_bio', 'cta_', 'btn_header_cta', 'serv_', 'plat_']):
        print(line[:120])
