import io, sys, os, shutil

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

base_brain = r'C:\Users\LENOVO\.gemini\antigravity\brain'
repo_assets = r'C:\Users\LENOVO\.gemini\antigravity\scratch\abdou25008.github.io\assets'

# 1. Smart Health
# Let's see what images exist in Smart Health workspace: d:\SMART HELTHY or brain
sh_cid = 'a0450921-1436-4e92-a81d-3cbfc87535b3'
sh_dir = os.path.join(base_brain, sh_cid)
print("Smart Health brain files:", os.listdir(sh_dir) if os.path.exists(sh_dir) else "None")

# 2. ASMR (Meta Lapse)
asmr_cid = '254b2137-b3b6-450f-951b-2dfe176489b9'
asmr_dir = os.path.join(base_brain, asmr_cid)
print("ASMR brain files:", os.listdir(asmr_dir) if os.path.exists(asmr_dir) else "None")

# 3. Deep Sea (Fathom X)
fathom_cid = '4d1d5354-4166-4168-ac5c-95096a47ea26'
fathom_dir = os.path.join(base_brain, fathom_cid)
print("Fathom X brain files:", [f for f in os.listdir(fathom_dir) if f.endswith('.jpg') or f.endswith('.png')] if os.path.exists(fathom_dir) else "None")
