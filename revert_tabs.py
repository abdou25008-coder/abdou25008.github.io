import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Remove the content-section display:none CSS
css_pattern = r'/\* Content Tab Display \*/.*?@keyframes fadeIn \{.*?\}'
html = re.sub(css_pattern, '', html, flags=re.DOTALL)

# 2. Change the desktop nav back to standard anchor tags
nav_old = r'<nav class="hidden xl:flex items-center gap-1 bg-\[#111116\]/90 border border-white/10 rounded-full px-3 py-1 shadow-inner backdrop-blur-md" id="main-nav-tabs">.*?</nav>'
nav_new = """      <nav class="hidden xl:flex items-center gap-1 bg-[#111116]/90 border border-white/10 rounded-full px-3 py-1 shadow-inner backdrop-blur-md" id="main-nav-tabs">
        <a href="#services" class="nav-tab px-3 py-1 text-xs font-bold text-zinc-300 hover:text-white hover:bg-purple-950/60 rounded-full transition-all duration-200" data-i18n="nav_services">المهارات</a>
        <a href="#platforms" class="nav-tab px-3 py-1 text-xs font-bold text-zinc-300 hover:text-white hover:bg-purple-950/60 rounded-full transition-all duration-200" data-i18n="nav_platforms">المنظومات الحية</a>
        <a href="#software-models" class="nav-tab px-3 py-1 text-xs font-bold text-zinc-300 hover:text-white hover:bg-purple-950/60 rounded-full transition-all duration-200" data-i18n="nav_models">النماذج الذكية</a>
        <a href="#media-network" class="nav-tab px-3 py-1 text-xs font-bold text-zinc-300 hover:text-white hover:bg-purple-950/60 rounded-full transition-all duration-200" data-i18n="nav_media">شبكة الميديا</a>
      </nav>"""
html = re.sub(nav_old, nav_new, html, flags=re.DOTALL)

# 3. Change the mobile dock buttons back to anchor tags
dock_old = r'<button onclick="triggerHaptic\(\); switchTab\(\'services\'\)" class="dock-tab.*?<span class="text-\[8px\] font-bold" data-i18n="dock_media">الميديا</span>\s*</button>'
dock_new = """      <a href="#services" onclick="triggerHaptic()" class="dock-tab flex flex-col items-center gap-0.5 text-zinc-400 hover:text-purple-400 transition-colors touch-press">
        <i class="fa-solid fa-house text-xs"></i>
        <span class="text-[8px] font-bold" data-i18n="dock_home">المهارات</span>
      </a>

      <a href="#platforms" onclick="triggerHaptic()" class="dock-tab flex flex-col items-center gap-0.5 text-zinc-400 hover:text-purple-400 transition-colors touch-press">
        <i class="fa-solid fa-layer-group text-xs"></i>
        <span class="text-[8px] font-bold" data-i18n="dock_platforms">المنظومات</span>
      </a>

      <!-- Highlighted Center WhatsApp Action -->
      <a href="https://wa.me/201092519210" target="_blank" rel="noopener noreferrer" onclick="triggerHaptic()" class="flex flex-col items-center -mt-4 group touch-press">
        <div class="w-10 h-10 rounded-full bg-emerald-500 hover:bg-emerald-400 text-white flex items-center justify-center shadow-lg shadow-emerald-950/80 border-2 border-[#050508] transition-transform group-hover:scale-105">
          <i class="fa-brands fa-whatsapp text-base"></i>
        </div>
        <span class="text-[8px] font-black text-emerald-400 mt-0.5" data-i18n="dock_contact">تواصل</span>
      </a>

      <a href="#software-models" onclick="triggerHaptic()" class="dock-tab flex flex-col items-center gap-0.5 text-zinc-400 hover:text-purple-400 transition-colors touch-press">
        <i class="fa-solid fa-code text-xs"></i>
        <span class="text-[8px] font-bold" data-i18n="dock_models">النماذج</span>
      </a>

      <a href="#media-network" onclick="triggerHaptic()" class="dock-tab flex flex-col items-center gap-0.5 text-zinc-400 hover:text-pink-400 transition-colors touch-press">
        <i class="fa-solid fa-clapperboard text-xs"></i>
        <span class="text-[8px] font-bold" data-i18n="dock_media">الميديا</span>
      </a>"""
html = re.sub(dock_old, dock_new, html, flags=re.DOTALL)

# 4. Remove `content-section` and `active-section` classes from sections to clean up
html = html.replace('class="content-section active-section ', 'class="')
html = html.replace('class="content-section ', 'class="')

# 5. Remove the switchTab JS function
js_pattern = r'<!-- Tab Switching Logic -->\s*<script>\s*function switchTab\(tabId\) \{.*?</script>'
html = re.sub(js_pattern, '', html, flags=re.DOTALL)

# Make sure smooth scrolling is enabled in CSS
if 'scroll-behavior: smooth;' not in html:
    html = html.replace('<style>', '<style>\n    html { scroll-behavior: smooth; }\n')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
