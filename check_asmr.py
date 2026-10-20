import json
import os
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

base_path = r'C:\Users\LENOVO\.gemini\antigravity\brain'
cid = '254b2137-b3b6-450f-951b-2dfe176489b9'
log_path = os.path.join(base_path, cid, '.system_generated', 'logs', 'transcript.jsonl')

if os.path.exists(log_path):
    with open(log_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                data = json.loads(line)
                if data.get('type') == 'PLANNER_RESPONSE':
                    content = data.get('content', '')
                    if any(w in content for w in ['اسم', 'قناة', 'ASMR', 'Damascus', 'ساعة', 'Channel', 'Crafting']):
                        print("FOUND IN ASMR PLANNER:", content[:400])
                        print("="*40)
            except:
                pass
