import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect services_html data-i18n tags
pos_services = text.find('id="services"')
pos_plat = text.find('id="platforms"')
services_html = text[pos_services:pos_plat]

i18n_matches = re.findall(r'data-i18n="([^"]+)"', services_html)
print("data-i18n attributes in services section:", i18n_matches)

# Print lines with data-i18n in services_html
for line in services_html.splitlines():
    if 'data-i18n' in line:
        print(line)
