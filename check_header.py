import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect the header navigation
pos_header = text.find('<header')
pos_hero = text.find('id="hero"')
print("=== HEADER CONTENT ===")
print(text[pos_header:pos_hero])
