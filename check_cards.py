import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect platforms section
pos_plat = text.find('id="platforms"')
pos_models = text.find('id="software-models"')
print("=== PLATFORMS SECTION SNIPPET ===")
plat_content = text[pos_plat:pos_models]
cards = re.findall(r'<!-- Platform Card \d+:? ([^\n]+) -->', plat_content)
print("Found Platform Cards:", cards)

# Let's inspect software-models section
pos_media = text.find('id="media-network"')
print("=== SOFTWARE MODELS SECTION SNIPPET ===")
models_content = text[pos_models:pos_media]
model_cards = re.findall(r'<!-- Model \d+:? ([^\n]+) -->', models_content)
print("Found Model Cards:", model_cards)

# Let's inspect media-network section
pos_cta = text.find('id="contact-cta"')
print("=== MEDIA NETWORK SECTION SNIPPET ===")
media_content = text[pos_media:pos_cta]
media_cards = re.findall(r'<!-- Channel \d+:? ([^\n]+) -->', media_content)
print("Found Media Cards:", media_cards)
