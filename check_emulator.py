import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect the mobile emulator (lines around emulator-modal)
pos = text.find('id="emulator-modal"')
print("Emulator modal code snippet:")
print(text[pos:pos+2500])
