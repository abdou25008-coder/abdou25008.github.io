import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's search for "mode=mobile_inner" or "mobile_inner" in scripts
for line in text.splitlines():
    if 'mobile_inner' in line or 'mode=' in line:
        print(line)

# Let's see all occurrences of url params or iframe handling
matches = re.findall(r'[^\n]*URLSearchParams[^\n]*', text)
for m in matches:
    print("URLSearchParams:", m)
