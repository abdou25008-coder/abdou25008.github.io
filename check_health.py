import json
import os
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

base_path = r'C:\Users\LENOVO\.gemini\antigravity\brain'
cid = 'a0450921-1436-4e92-a81d-3cbfc87535b3'
log_path = os.path.join(base_path, cid, '.system_generated', 'logs', 'transcript.jsonl')

if os.path.exists(log_path):
    with open(log_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                data = json.loads(line)
                if data.get('type') == 'PLANNER_RESPONSE':
                    content = data.get('content', '')
                    if 'قناة' in content or 'Smart Health' in content or 'صحة' in content or 'اسم' in content:
                        print("FOUND IN PLANNER:", content[:400])
                        print("="*40)
            except:
                pass
