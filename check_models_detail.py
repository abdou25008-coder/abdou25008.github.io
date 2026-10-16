import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect software-models section in full
pos_models = text.find('id="software-models"')
pos_media = text.find('id="media-network"')
models_html = text[pos_models:pos_media]

print(models_html[:2500])
