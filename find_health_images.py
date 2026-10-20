import io, sys, os

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Search for smart health assets
paths_to_check = [
    r'd:\SMART HELTHY',
    r'd:\Smart Health',
    r'd:\smart health usa',
    r'C:\Users\LENOVO\.gemini\antigravity\brain\a0450921-1436-4e92-a81d-3cbfc87535b3'
]

for p in paths_to_check:
    if os.path.exists(p):
        print(f"Path exists: {p}")
        for root, dirs, files in os.walk(p):
            img_files = [f for f in files if f.endswith('.jpg') or f.endswith('.png')]
            if img_files:
                print(f"  In {root}: {len(img_files)} images, samples: {img_files[:5]}")
    else:
        print(f"Path does not exist: {p}")
