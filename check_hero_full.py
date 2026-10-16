import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect hero section on mobile
pos = text.find('id="hero"')
pos_metrics = text.find('id="metrics"')
print("=== HERO SECTION CONTENT ===")
print(text[pos:pos_metrics])
