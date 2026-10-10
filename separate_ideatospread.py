import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# First, correct the NovaCraft card because I previously merged its title.
# I wrote: "منصة NovaCraft (من الفكرة إلى الإبداع للانتشار)"
# I need to change it to just "منصة NovaCraft"
html = html.replace("منصة NovaCraft (من الفكرة إلى الإبداع للانتشار)", "منصة NovaCraft")

# Now, create the new card for "من الفكرة للإبداع للانتشار"
new_card = """
        <!-- Platform Card 9: Idea to Spread -->
        <div class="glass-panel rounded-xl sm:rounded-2xl p-3 sm:p-5 border border-amber-500/25 hover:border-amber-500/60 transition-all flex flex-col justify-between text-right align-start-dir group">
          <div>
            <div class="w-full aspect-[16/9] rounded-xl bg-[#08080c] border border-white/10 overflow-hidden mb-3 relative shadow-lg group-hover:border-amber-500/50 transition-all flex items-center justify-center">
              <img src="assets/hero_architect.jpg" alt="Idea To Spread" class="w-full h-full object-cover group-hover:scale-105 transition-all duration-700" loading="lazy" />
              <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-transparent to-black/20"></div>
              <div class="absolute top-2 left-2 bg-amber-950/90 border border-amber-500/40 px-2 py-0.5 rounded-full text-[8.5px] font-mono text-amber-300 flex items-center gap-1 backdrop-blur-md shadow-sm">
                <span class="w-1.5 h-1.5 rounded-full bg-amber-400 animate-pulse"></span>
                <span>Growth Ecosystem</span>
              </div>
            </div>
            
            <div class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-amber-950/70 border border-amber-500/30 text-amber-300 text-[9.5px] font-mono mb-1.5">
              <i class="fa-solid fa-lightbulb text-amber-400 text-[10px]"></i>
              <span>إطار عمل متكامل للمشاريع الرقمية</span>
            </div>
            
            <h3 class="text-xs sm:text-base font-bold text-white mb-1.5 leading-snug group-hover:text-amber-300 transition-colors">
              من الفكرة للإبداع للانتشار (Idea to Spread)
            </h3>
            
            <p class="text-zinc-300 text-[11px] sm:text-xs leading-relaxed mb-3">
              منهجية ومنظومة عمل متكاملة لاحتضان وإطلاق المشاريع؛ تبدأ ببلورة "الفكرة"، وتنتقل لمرحلة "الإبداع" في التصميم المعماري والتنفيذ البرمجي، وتتوج بخوارزميات "الانتشار" الرقمي لتحقيق أعلى وصول وتأثير في السوق.
            </p>

            <div class="grid grid-cols-2 gap-1.5 mb-3 text-[9.5px] sm:text-xs text-zinc-300">
              <div class="flex items-center gap-1.5 bg-black/40 p-1.5 rounded-lg border border-white/5">
                <i class="fa-solid fa-seedling text-amber-400 text-[10px]"></i>
                <span>احتضان وتطوير المنتجات (Incubation)</span>
              </div>
              <div class="flex items-center gap-1.5 bg-black/40 p-1.5 rounded-lg border border-white/5">
                <i class="fa-solid fa-chart-pie text-amber-400 text-[10px]"></i>
                <span>استراتيجيات نمو وانتشار ذكية</span>
              </div>
            </div>
          </div>
        </div>
"""

# Inject after NovaCraft
# NovaCraft ends with: </a>\n          </div>\n        </div>
pattern = r'(<!-- Platform Card 7: NovaCraft -->.*?</a>\s*</div>\s*</div>)'
if "Platform Card 7: NovaCraft" in html:
    html = re.sub(pattern, r'\1\n' + new_card, html, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
