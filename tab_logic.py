import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update the navigation links in the header to act as tabs
nav_old = """      <nav class="hidden xl:flex items-center gap-1 bg-[#111116]/90 border border-white/10 rounded-full px-3 py-1 shadow-inner backdrop-blur-md">
        <a href="#services" class="px-3 py-1 text-xs font-bold text-zinc-300 hover:text-white hover:bg-purple-950/60 rounded-full transition-all duration-200" data-i18n="nav_services">المهارات</a>
        <a href="#platforms" class="px-3 py-1 text-xs font-bold text-zinc-300 hover:text-white hover:bg-purple-950/60 rounded-full transition-all duration-200" data-i18n="nav_platforms">المنظومات الحية</a>
        <a href="#software-models" class="px-3 py-1 text-xs font-bold text-zinc-300 hover:text-white hover:bg-purple-950/60 rounded-full transition-all duration-200" data-i18n="nav_models">النماذج الذكية</a>
        <a href="#media-network" class="px-3 py-1 text-xs font-bold text-zinc-300 hover:text-white hover:bg-purple-950/60 rounded-full transition-all duration-200" data-i18n="nav_media">شبكة الميديا</a>
      </nav>"""

nav_new = """      <nav class="hidden xl:flex items-center gap-1 bg-[#111116]/90 border border-white/10 rounded-full px-3 py-1 shadow-inner backdrop-blur-md" id="main-nav-tabs">
        <button onclick="switchTab('services')" class="nav-tab active-tab px-3 py-1 text-xs font-bold text-zinc-300 hover:text-white hover:bg-purple-950/60 rounded-full transition-all duration-200" data-i18n="nav_services" data-target="services">المهارات</button>
        <button onclick="switchTab('platforms')" class="nav-tab px-3 py-1 text-xs font-bold text-zinc-300 hover:text-white hover:bg-purple-950/60 rounded-full transition-all duration-200" data-i18n="nav_platforms" data-target="platforms">المنظومات الحية</button>
        <button onclick="switchTab('software-models')" class="nav-tab px-3 py-1 text-xs font-bold text-zinc-300 hover:text-white hover:bg-purple-950/60 rounded-full transition-all duration-200" data-i18n="nav_models" data-target="software-models">النماذج الذكية</button>
        <button onclick="switchTab('media-network')" class="nav-tab px-3 py-1 text-xs font-bold text-zinc-300 hover:text-white hover:bg-purple-950/60 rounded-full transition-all duration-200" data-i18n="nav_media" data-target="media-network">شبكة الميديا</button>
      </nav>"""

if nav_old in html:
    html = html.replace(nav_old, nav_new)
else:
    # Try more robust replacement if spacing differs
    html = re.sub(r'<nav class="hidden xl:flex items-center gap-1[^>]+>.*?</nav>', nav_new, html, flags=re.DOTALL)


# 2. Add the CSS for active tab
style_insertion = """
    /* Active Tab Style */
    .nav-tab.active-tab {
      background-color: rgba(59, 7, 100, 0.8) !important; /* purple-950/80 */
      color: #ffffff !important;
      border: 1px solid rgba(168, 85, 247, 0.4);
      box-shadow: 0 0 10px rgba(168, 85, 247, 0.2);
    }
    
    /* Content Tab Display */
    .content-section {
      display: none;
      animation: fadeIn 0.4s ease-in-out;
    }
    .content-section.active-section {
      display: block;
    }
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(10px); }
      to { opacity: 1; transform: translateY(0); }
    }
  </style>
"""
html = html.replace("</style>", style_insertion)

# 3. Add the content-section classes to the sections
html = html.replace('<section id="services" class="py-6 sm:py-14 relative">', '<section id="services" class="content-section active-section py-6 sm:py-14 relative">')
html = html.replace('<section id="platforms" class="py-6 sm:py-14 relative bg-[#07070b]">', '<section id="platforms" class="content-section py-6 sm:py-14 relative bg-[#07070b]">')
html = html.replace('<section id="software-models" class="py-6 sm:py-14 relative">', '<section id="software-models" class="content-section py-6 sm:py-14 relative">')
html = html.replace('<section id="media-network" class="py-6 sm:py-14 relative bg-[#07070b]">', '<section id="media-network" class="content-section py-6 sm:py-14 relative bg-[#07070b]">')

# 4. Add the JavaScript for switching tabs
js_insertion = """
  <!-- Tab Switching Logic -->
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
  </script>
</body>
"""
html = html.replace("</body>", js_insertion)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
