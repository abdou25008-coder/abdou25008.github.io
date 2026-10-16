import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect platforms section data-i18n
pos_plat = text.find('id="platforms"')
pos_models = text.find('id="software-models"')
plat_html = text[pos_plat:pos_models]

i18n_plat = re.findall(r'data-i18n="([^"]+)"', plat_html)
print("data-i18n in platforms section:", i18n_plat)
