import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect the entire mobile dock in detail
pos_dock = text.find('ULTRA SLEEK ERGONOMIC MOBILE DOCK')
pos_dock_end = text.find('DUAL SMARTPHONE LIVE EMULATOR')
print(text[pos_dock:pos_dock_end])
