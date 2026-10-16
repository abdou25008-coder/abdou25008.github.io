import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's check where 'dock_home' or translations for dock are defined
pos = text.find('dock_home')
while pos != -1:
    print(text[max(0, pos-100):min(len(text), pos+150)])
    print("="*40)
    pos = text.find('dock_home', pos+1)
