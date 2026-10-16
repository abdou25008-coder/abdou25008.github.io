import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's find all data-i18n keys used in index.html
used_keys = set(re.findall(r'data-i18n="([^"]+)"', text))
print(f"Total used data-i18n keys: {len(used_keys)}")

# Let's extract ar and en keys from translations object
pos_trans = text.find('const translations = {')
pos_trans_end = text.find('function switchLanguage')
trans_code = text[pos_trans:pos_trans_end]

# Extract keys in ar
ar_part = trans_code[trans_code.find('ar: {'):trans_code.find('en: {')]
ar_keys = set(re.findall(r'(\b[a-zA-Z0-9_]+)\s*:\s*["\']', ar_part))

print(f"Total ar keys: {len(ar_keys)}")

# Check keys in used_keys that are NOT in ar_keys
missing = used_keys - ar_keys
print(f"Keys used in HTML but missing in translations.ar: {len(missing)}")
for k in sorted(missing):
    print("  Missing key:", k)
