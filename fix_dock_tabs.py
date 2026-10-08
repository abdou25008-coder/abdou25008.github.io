import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Make sure all 4 sections have content-section class and hide by default
# They were:
# <section id="services" class="content-section active-section py-6 sm:py-14 relative">
# <section id="platforms" class="content-section py-6 sm:py-14 relative bg-[#07070b]">
# <section id="software-models" class="content-section py-6 sm:py-14 relative">
# <section id="media-network" class="content-section py-6 sm:py-14 relative bg-[#07070b]">

# Wait, let's update the mobile dock too so it calls switchTab

dock_old = """      <a href="#hero" onclick="triggerHaptic()" class="flex flex-col items-center gap-0.5 text-zinc-400 hover:text-purple-400 active:text-purple-300 transition-colors touch-press">
        <i class="fa-solid fa-house text-xs"></i>
        <span class="text-[8px] font-bold" data-i18n="dock_home">الرئيسية</span>
      </a>

      <a href="#platforms" onclick="triggerHaptic()" class="flex flex-col items-center gap-0.5 text-zinc-400 hover:text-purple-400 active:text-purple-300 transition-colors touch-press">
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

      <a href="#software-models" onclick="triggerHaptic()" class="flex flex-col items-center gap-0.5 text-zinc-400 hover:text-purple-400 active:text-purple-300 transition-colors touch-press">
        <i class="fa-solid fa-code text-xs"></i>
        <span class="text-[8px] font-bold" data-i18n="dock_models">النماذج</span>
      </a>

      <a href="#media-network" onclick="triggerHaptic()" class="flex flex-col items-center gap-0.5 text-zinc-400 hover:text-pink-400 active:text-pink-300 transition-colors touch-press">
        <i class="fa-solid fa-clapperboard text-xs"></i>
        <span class="text-[8px] font-bold" data-i18n="dock_media">الميديا</span>
      </a>"""

dock_new = """      <button onclick="triggerHaptic(); switchTab('services')" class="dock-tab active-dock-tab flex flex-col items-center gap-0.5 text-zinc-400 hover:text-purple-400 transition-colors touch-press" data-target="services">
        <i class="fa-solid fa-house text-xs"></i>
        <span class="text-[8px] font-bold" data-i18n="dock_home">المهارات</span>
      </button>

      <button onclick="triggerHaptic(); switchTab('platforms')" class="dock-tab flex flex-col items-center gap-0.5 text-zinc-400 hover:text-purple-400 transition-colors touch-press" data-target="platforms">
        <i class="fa-solid fa-layer-group text-xs"></i>
        <span class="text-[8px] font-bold" data-i18n="dock_platforms">المنظومات</span>
      </button>

      <!-- Highlighted Center WhatsApp Action -->
      <a href="https://wa.me/201092519210" target="_blank" rel="noopener noreferrer" onclick="triggerHaptic()" class="flex flex-col items-center -mt-4 group touch-press">
        <div class="w-10 h-10 rounded-full bg-emerald-500 hover:bg-emerald-400 text-white flex items-center justify-center shadow-lg shadow-emerald-950/80 border-2 border-[#050508] transition-transform group-hover:scale-105">
          <i class="fa-brands fa-whatsapp text-base"></i>
        </div>
        <span class="text-[8px] font-black text-emerald-400 mt-0.5" data-i18n="dock_contact">تواصل</span>
      </a>

      <button onclick="triggerHaptic(); switchTab('software-models')" class="dock-tab flex flex-col items-center gap-0.5 text-zinc-400 hover:text-purple-400 transition-colors touch-press" data-target="software-models">
        <i class="fa-solid fa-code text-xs"></i>
        <span class="text-[8px] font-bold" data-i18n="dock_models">النماذج</span>
      </button>

      <button onclick="triggerHaptic(); switchTab('media-network')" class="dock-tab flex flex-col items-center gap-0.5 text-zinc-400 hover:text-pink-400 transition-colors touch-press" data-target="media-network">
        <i class="fa-solid fa-clapperboard text-xs"></i>
        <span class="text-[8px] font-bold" data-i18n="dock_media">الميديا</span>
      </button>"""

if dock_old in html:
    html = html.replace(dock_old, dock_new)
else:
    # use regex
    html = re.sub(r'<a href="#hero".*?<span class="text-\[8px\] font-bold" data-i18n="dock_media">.*?</a>', dock_new, html, flags=re.DOTALL)

# Update Javascript
old_js = """  <!-- Tab Switching Logic -->
  <script>
    function switchTab(tabId) {
      // 1. Hide all sections
      const sections = ['services', 'platforms', 'software-models', 'media-network'];
      sections.forEach(id => {
        const el = document.getElementById(id);
        if(el) {
          el.classList.remove('active-section');
        }
      });
      
      // 2. Show target section
      const targetEl = document.getElementById(tabId);
      if(targetEl) {
        targetEl.classList.add('active-section');
      }

      // 3. Update tab buttons styles
      const tabs = document.querySelectorAll('.nav-tab');
      tabs.forEach(tab => {
        if(tab.getAttribute('data-target') === tabId) {
          tab.classList.add('active-tab');
        } else {
          tab.classList.remove('active-tab');
        }
      });
      
      // Smooth scroll slightly to the section start (optional, maybe just scroll to hero bottom)
      // window.scrollTo({ top: document.getElementById('metrics').offsetTop, behavior: 'smooth' });
    }
  </script>"""

new_js = """  <!-- Tab Switching Logic -->
  <script>
    function switchTab(tabId) {
      // 1. Hide all sections
      const sections = ['services', 'platforms', 'software-models', 'media-network'];
      sections.forEach(id => {
        const el = document.getElementById(id);
        if(el) {
          el.classList.remove('active-section');
        }
      });
      
      // 2. Show target section
      const targetEl = document.getElementById(tabId);
      if(targetEl) {
        targetEl.classList.add('active-section');
      }

      // 3. Update desktop tab buttons styles
      const tabs = document.querySelectorAll('.nav-tab');
      tabs.forEach(tab => {
        if(tab.getAttribute('data-target') === tabId) {
          tab.classList.add('active-tab');
        } else {
          tab.classList.remove('active-tab');
        }
      });

      // 4. Update mobile dock buttons styles
      const dockTabs = document.querySelectorAll('.dock-tab');
      dockTabs.forEach(tab => {
        if(tab.getAttribute('data-target') === tabId) {
          tab.classList.add('text-purple-400');
          tab.classList.remove('text-zinc-400');
        } else {
          tab.classList.remove('text-purple-400');
          tab.classList.add('text-zinc-400');
        }
      });
      
      // Optional: Smooth scroll to content
      const metricsEl = document.getElementById('metrics');
      if (metricsEl) {
         const y = metricsEl.getBoundingClientRect().top + window.scrollY - 80;
         window.scrollTo({ top: y, behavior: 'smooth' });
      }
    }
  </script>"""

html = html.replace(old_js, new_js)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
