import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect the first 2 platform cards, especially grid classes and mobile styling
pos_plat = text.find('id="platforms"')
print(text[pos_plat:pos_plat+2200])
