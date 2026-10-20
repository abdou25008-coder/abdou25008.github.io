import io, sys, os, shutil

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

repo_assets = r'C:\Users\LENOVO\.gemini\antigravity\scratch\abdou25008.github.io\assets'

# 1. Smart Health USA Cover
src_health = r'C:\Users\LENOVO\.gemini\antigravity\brain\a0450921-1436-4e92-a81d-3cbfc87535b3\02_Midday_Short_SammyStomach_Cover.jpg'
dest_health = os.path.join(repo_assets, 'smart_health_cover.jpg')
if os.path.exists(src_health):
    shutil.copy2(src_health, dest_health)
    print("Copied smart_health_cover.jpg successfully!")
else:
    print("src_health not found:", src_health)

# 2. Meta Lapse ASMR Cover
src_asmr = r'C:\Users\LENOVO\.gemini\antigravity\brain\254b2137-b3b6-450f-951b-2dfe176489b9\viral_cover_eiffel_ar_9x16.jpg'
dest_asmr = os.path.join(repo_assets, 'meta_lapse_asmr_cover.jpg')
if os.path.exists(src_asmr):
    shutil.copy2(src_asmr, dest_asmr)
    print("Copied meta_lapse_asmr_cover.jpg successfully!")
else:
    print("src_asmr not found:", src_asmr)

# 3. Fathom X Deep Sea Cover
src_fathom = r'C:\Users\LENOVO\.gemini\antigravity\brain\4d1d5354-4166-4168-ac5c-95096a47ea26\Barreleye_Master_Official_Cover_AI.jpg'
dest_fathom = os.path.join(repo_assets, 'fathom_x_deep_sea_cover.jpg')
if os.path.exists(src_fathom):
    shutil.copy2(src_fathom, dest_fathom)
    print("Copied fathom_x_deep_sea_cover.jpg successfully!")
else:
    # try alternate
    src_fathom2 = r'C:\Users\LENOVO\.gemini\antigravity\brain\4d1d5354-4166-4168-ac5c-95096a47ea26\The_Barreleye_Fish_Official_Vertical_Cover.jpg'
    if os.path.exists(src_fathom2):
        shutil.copy2(src_fathom2, dest_fathom)
        print("Copied fathom_x_deep_sea_cover.jpg (alt) successfully!")
