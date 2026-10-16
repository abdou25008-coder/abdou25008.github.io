import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect where hero image is in HTML
pos_hero = text.find('id="hero"')
pos_metrics = text.find('id="metrics"')
hero_html = text[pos_hero:pos_metrics]

print("Images inside hero section:")
for img in re.findall(r'<img[^>]+>', hero_html):
    print(img)
