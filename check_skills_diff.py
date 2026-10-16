import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect s1, s2, s3, s4 in HTML
pos_services = text.find('id="services"')
pos_plat = text.find('id="platforms"')
services_html = text[pos_services:pos_plat]

skills_headers = re.findall(r'<h3[^>]*>([^<]+)</h3>', services_html)
print("Skills headers in HTML:", skills_headers)

# Let's inspect translations.ar s1..s4
pos_trans = text.find('const translations = {')
pos_en = text.find('en: {')
ar_text = text[pos_trans:pos_en]

for line in ar_text.splitlines():
    if any(k in line for k in ['s1_title', 's2_title', 's3_title', 's4_title']):
        print("translations.ar skill:", line)
