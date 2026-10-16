import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect the mobile dock section completely
pos_dock = text.find('ULTRA SLEEK ERGONOMIC MOBILE DOCK')
pos_emu = text.find('DUAL SMARTPHONE LIVE EMULATOR')
print(text[pos_dock:pos_emu])
