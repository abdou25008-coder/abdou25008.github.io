import json
import os
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

conversations = [
    ('Smart Health Channel Revival Strategy', 'a0450921-1436-4e92-a81d-3cbfc87535b3'),
    ('AI Cinematic ASMR Video Planning', '254b2137-b3b6-450f-951b-2dfe176489b9'),
    ('Cinematic Deep Sea AI Project', '4d1d5354-4166-4168-ac5c-95096a47ea26')
]

base_path = r'C:\Users\LENOVO\.gemini\antigravity\brain'

for title, cid in conversations:
    print(f'==============================')
    print(f'=== {title} ({cid}) ===')
    print(f'==============================')
    log_path = os.path.join(base_path, cid, '.system_generated', 'logs', 'transcript.jsonl')
    if not os.path.exists(log_path):
        log_path = os.path.join(base_path, cid, '.system_generated', 'logs', 'transcript_full.jsonl')
    
    # Also check artifacts in that folder
    art_path = os.path.join(base_path, cid)
    if os.path.exists(art_path):
        files = os.listdir(art_path)
        print("Artifacts/Files in folder:", [f for f in files if not f.startswith('.')][:15])

    if os.path.exists(log_path):
        with open(log_path, 'r', encoding='utf-8') as f:
            count = 0
            for line in f:
                try:
                    data = json.loads(line)
                    if data.get('type') == 'USER_INPUT':
                        content = data.get('content', '')
                        print(f'\n--- USER PROMPT {count+1} ---')
                        print(content.strip()[:400])
                        count += 1
                        if count >= 5:
                            break
                except Exception as e:
                    pass
    else:
        print('Log not found at:', log_path)
    print('\n')
