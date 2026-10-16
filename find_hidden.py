import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's check sections that have "hidden" or conditional display
# Particularly: "space-y-4 hidden"
matches = [m.start() for m in re.finditer(r'space-y-4 hidden', text)]
for idx in matches:
    print("Match around space-y-4 hidden:")
    print(text[max(0, idx-200):min(len(text), idx+200)])
    print("="*60)

# Check all hidden classes
print("\n--- Check all hidden instances ---")
for m in re.finditer(r'class="([^"]*hidden[^"]*)"', text):
    c = m.group(1)
    # filter out overflow-hidden
    c_clean = re.sub(r'overflow-hidden', '', c)
    if 'hidden' in c_clean:
        print(c)
