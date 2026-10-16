import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect the entire head tag
pos_head = text.find('<head>')
pos_head_end = text.find('</head>')
print(text[pos_head:pos_head+2000])
