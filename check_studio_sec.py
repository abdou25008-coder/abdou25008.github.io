import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect toggleSection or how hiddenSections works
pos = text.find('function toggleSection')
print(text[pos:pos+600])

# Let's check what default state or toggle sections exist in studio
pos_sec = text.find('studio-panel-sections')
if pos_sec != -1:
    print("=== SECTIONS PANEL IN STUDIO ===")
    print(text[pos_sec:pos_sec+1200])
