import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's check sections by id
sections = ['hero', 'metrics', 'services', 'platforms', 'software-models', 'media-network', 'contact-cta']

for sec in sections:
    pos = text.find(f'id="{sec}"')
    print(f"=== SECTION: {sec} (at index {pos}) ===")
    snippet = text[pos:pos+400]
    print(snippet)
    print("\n" + "="*50 + "\n")

# Check footer and dock
pos_dock = text.find('ULTRA SLEEK ERGONOMIC MOBILE DOCK')
print("=== MOBILE DOCK ===")
print(text[pos_dock:pos_dock+1000] if pos_dock != -1 else "NOT FOUND")
