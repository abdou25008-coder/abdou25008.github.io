import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect where local storage or customContent is used
for line in text.splitlines():
    if 'localStorage' in line:
        print(line)
