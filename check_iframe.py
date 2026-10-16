import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find iframe inside emulator
pos = text.find('id="emulator-modal"')
print(text[pos+1800:pos+3500])
