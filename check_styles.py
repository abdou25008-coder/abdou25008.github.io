import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect CSS styles for responsive design
pos_style = text.find('<style>')
pos_style_end = text.find('</style>')
styles = text[pos_style:pos_style_end]

# Search for media queries in styles
media_queries = re.findall(r'@media[^{]+{[^}]+}', styles)
print(f"Total media queries in <style>: {len(media_queries)}")
for mq in media_queries[:15]:
    print(mq[:150])
