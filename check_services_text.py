import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect serv_title and serv_sub in HTML and in translations
pos = text.find('id="services"')
print("HTML services header:")
print(text[pos:pos+1000])

print("="*60)
pos_ar = text.find('serv_title:')
print("translations.ar snippet:")
print(text[pos_ar:pos_ar+500])
