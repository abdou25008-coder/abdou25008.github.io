import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos_hero = text.find('id="hero"')
pos_metrics = text.find('id="metrics"')
hero_html = text[pos_hero:pos_metrics]

pos_small_img = hero_html.find('assets/abdou_real_portrait.jpg')
print(hero_html[pos_small_img-200:pos_small_img+400])
