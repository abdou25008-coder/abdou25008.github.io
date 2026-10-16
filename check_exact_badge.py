import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's see the exact text around "lg:hidden flex items-center"
pos = text.find('lg:hidden flex items-center')
print(repr(text[pos-100:pos+500]))
