import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect CSS styles for bottom padding on body or main
print("Body tag and style classes:")
pos_body = text.find('<body')
print(text[pos_body:pos_body+300])

# Check if pb-24 or similar exists for mobile dock spacing
print("pb- on body or wrapper:", re.findall(r'pb-\d+', text[:pos_body+1000]))
