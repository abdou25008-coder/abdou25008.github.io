import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's search where window.self !== window.top appears
pos = text.find("window.self !== window.top")
print(text[pos-100:pos+1500])
