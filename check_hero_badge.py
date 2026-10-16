import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's see the lines around lg:hidden in hero
pos = text.find('id="hero"')
pos_metrics = text.find('id="metrics"')
hero_html = text[pos:pos_metrics]

pos_badge = hero_html.find('lg:hidden')
print("Hero lg:hidden snippet:")
print(hero_html[pos_badge-50:pos_badge+500])
