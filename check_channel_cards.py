import io, sys, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's inspect Channel 1, 2, 3, 4 markup
pos_media = html.find('id="media-network"')
pos_cta = html.find('id="contact-cta"')
media_markup = html[pos_media:pos_cta]

print(media_markup[:2500])
