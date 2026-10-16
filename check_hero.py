import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect:
# 1. hidden lg:flex lg:col-span-5 relative items-center justify-center
idx = text.find('hidden lg:flex lg:col-span-5')
if idx != -1:
    print("--- HERO RIGHT SIDE ---")
    print(text[idx:idx+1500])
    print("="*60)

# 2. Check the entire structure of index.html sections
sections = re.findall(r'<section[^>]*>', text)
for s in sections:
    print(s)
