import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect translations.ar for contact-cta and footer
pos_ar = text.find('ar: {')
pos_en = text.find('en: {')
ar_text = text[pos_ar:pos_en]

cta_lines = []
for line in ar_text.splitlines():
    if any(k in line for k in ['cta_', 'footer_', 'btn_header_cta']):
        cta_lines.append(line)

print('\n'.join(cta_lines))
