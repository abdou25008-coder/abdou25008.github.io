import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect media-network section completely
pos_media = text.find('id="media-network"')
pos_cta = text.find('id="contact-cta"')
print(text[pos_media:pos_cta])
