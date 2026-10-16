import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's check the bottom of index.html
print("=== BOTTOM OF INDEX.HTML ===")
print(text[-3500:])
