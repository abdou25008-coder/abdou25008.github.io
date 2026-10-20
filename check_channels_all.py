import io, sys, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's inspect Channel 2, 3, 4 specifically
pos_ch1 = html.find('<!-- Channel 1: Fathom X')
pos_hub = html.find('<!-- Dedicated Verified Official Pages & Channels Hub -->')

print(html[pos_ch1:pos_hub])
