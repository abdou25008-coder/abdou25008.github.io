import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("File size:", len(text))

# Search for classes that hide on mobile (e.g. hidden md:block, hidden lg:flex, hidden sm:block, etc.)
hidden_mobile = re.findall(r'class="[^"]*\bhidden\b[^"]*"', text)
print(f"Total elements with 'hidden': {len(hidden_mobile)}")
for h in hidden_mobile:
    if 'lg:hidden' not in h and 'md:hidden' not in h and 'sm:hidden' not in h:
        print("Hidden by default (likely hidden on mobile):", h[:100])

# Search for simulator/emulator code
print("\n--- Simulator / Emulator check ---")
for line in text.splitlines():
    if 'emulator' in line.lower() or 'simulator' in line.lower() or 'iframe' in line.lower():
        print(line[:120])
