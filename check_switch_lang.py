import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect where switchLanguage is defined and how it updates data-i18n
pos = text.find('function switchLanguage')
print(text[pos:pos+1500])
