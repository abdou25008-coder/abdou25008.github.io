import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect contact-cta section
pos_cta = text.find('id="contact-cta"')
print("=== CONTACT CTA ===")
print(text[pos_cta:pos_cta+3500])
