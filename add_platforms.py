import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Define the new cards
new_cards = """
        <!-- Platform Card 5: Shayrha -->
        <div class="glass-panel rounded-xl sm:rounded-2xl p-3 sm:p-5 border border-purple-500/25 hover:border-purple-500/60 transition-all flex flex-col justify-between text-right align-start-dir group">
          <div>
            <div class="w-full aspect-[16/9] rounded-xl bg-[#08080c] border border-white/10 overflow-hidden mb-3 relative shadow-lg group-hover:border-purple-500/50 transition-all flex items-center justify-center">
              <img src="assets/shayrha_preview.jpg" alt="Shayrha Platform" class="w-full h-full object-contain group-hover:scale-105 transition-all duration-700" onerror="this.src='assets/hero_architect.jpg'" loading="lazy" />
              <div class="absolute top-2 left-2 bg-purple-950/90 border border-purple-500/40 px-2 py-0.5 rounded-full text-[8.5px] font-mono text-purple-300 flex items-center gap-1 backdrop-blur-md shadow-sm">
                <span class="w-1.5 h-1.5 rounded-full bg-purple-400 animate-pulse"></span>
                <span>Egyptian Platform</span>
              </div>
            </div>
            <div class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-purple-950/70 border border-purple-500/30 text-purple-300 text-[9.5px] font-mono mb-1.5">
              <i class="fa-solid fa-share-nodes text-purple-400 text-[10px]"></i>
              <span>منصة التواصل والمشاركة</span>
            </div>
            <h3 class="text-xs sm:text-base font-bold text-white mb-1.5 leading-snug group-hover:text-purple-300 transition-colors">منصة شيرها المصرية</h3>
            <p class="text-zinc-300 text-[11px] sm:text-xs leading-relaxed mb-3">
              منصة تواصل ومشاركة مصرية مبتكرة تجمع بين الأصالة والمعاصرة، مصممة بأحدث التقنيات لتقديم تجربة مستخدم سلسة وعصرية تلبي تطلعات الشباب وتواكب تطورات المنصات العالمية.
            </p>
          </div>
          <div class="flex flex-row items-center gap-1.5 pt-2 border-t border-white/10">
            <a href="https://shayrha.surge.sh" target="_blank" rel="noopener noreferrer" class="flex-1 inline-flex items-center justify-center gap-1.5 px-2.5 py-2 rounded-lg sm:rounded-xl bg-purple-600 hover:bg-purple-500 text-white font-bold text-[10px] sm:text-xs shadow-glow-purple transition-all touch-press">
              <i class="fa-solid fa-rocket text-[9px]"></i>
              <span>زيارة المنصة</span>
            </a>
          </div>
        </div>

        <!-- Platform Card 6: E-Commerce Store -->
        <div class="glass-panel rounded-xl sm:rounded-2xl p-3 sm:p-5 border border-cyan-500/25 hover:border-cyan-500/60 transition-all flex flex-col justify-between text-right align-start-dir group">
          <div>
            <div class="w-full aspect-[16/9] rounded-xl bg-[#08080c] border border-white/10 overflow-hidden mb-3 relative shadow-lg group-hover:border-cyan-500/50 transition-all flex items-center justify-center">
              <img src="assets/ecommerce_preview.jpg" alt="E-Commerce Store" class="w-full h-full object-contain group-hover:scale-105 transition-all duration-700" onerror="this.src='assets/hero_architect.jpg'" loading="lazy" />
              <div class="absolute top-2 left-2 bg-cyan-950/90 border border-cyan-500/40 px-2 py-0.5 rounded-full text-[8.5px] font-mono text-cyan-300 flex items-center gap-1 backdrop-blur-md shadow-sm">
                <span class="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-pulse"></span>
                <span>E-Commerce</span>
              </div>
            </div>
            <div class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-cyan-950/70 border border-cyan-500/30 text-cyan-300 text-[9.5px] font-mono mb-1.5">
              <i class="fa-solid fa-store text-cyan-400 text-[10px]"></i>
              <span>منظومة البيع الذكية</span>
            </div>
            <h3 class="text-xs sm:text-base font-bold text-white mb-1.5 leading-snug group-hover:text-cyan-300 transition-colors">المتجر الإلكتروني</h3>
            <p class="text-zinc-300 text-[11px] sm:text-xs leading-relaxed mb-3">
              منظومة تجارة إلكترونية متكاملة توفر تجربة تسوق فائقة السرعة والأمان، مع لوحة تحكم ذكية لإدارة المنتجات، الطلبات، والمدفوعات بكفاءة عالية، مما يساهم في مضاعفة المبيعات.
            </p>
          </div>
        </div>

        <!-- Platform Card 7: NovaCraft -->
        <div class="glass-panel rounded-xl sm:rounded-2xl p-3 sm:p-5 border border-emerald-500/25 hover:border-emerald-500/60 transition-all flex flex-col justify-between text-right align-start-dir group">
          <div>
            <div class="w-full aspect-[16/9] rounded-xl bg-[#08080c] border border-white/10 overflow-hidden mb-3 relative shadow-lg group-hover:border-emerald-500/50 transition-all flex items-center justify-center">
              <img src="assets/novacraft_preview.jpg" alt="NovaCraft" class="w-full h-full object-contain group-hover:scale-105 transition-all duration-700" onerror="this.src='assets/hero_architect.jpg'" loading="lazy" />
              <div class="absolute top-2 left-2 bg-emerald-950/90 border border-emerald-500/40 px-2 py-0.5 rounded-full text-[8.5px] font-mono text-emerald-300 flex items-center gap-1 backdrop-blur-md shadow-sm">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
                <span>Creative Engine</span>
              </div>
            </div>
            <div class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-emerald-950/70 border border-emerald-500/30 text-emerald-300 text-[9.5px] font-mono mb-1.5">
              <i class="fa-solid fa-cube text-emerald-400 text-[10px]"></i>
              <span>أدوات الإبداع</span>
            </div>
            <h3 class="text-xs sm:text-base font-bold text-white mb-1.5 leading-snug group-hover:text-emerald-300 transition-colors">NovaCraft</h3>
            <p class="text-zinc-300 text-[11px] sm:text-xs leading-relaxed mb-3">
              محرك إبداعي وأدوات تصميم متطورة لبناء واجهات ومنتجات رقمية مذهلة، يتيح تحويل الأفكار إلى واقع ملموس بسرعة فائقة ومرونة غير مسبوقة في التخصيص والتحكم.
            </p>
          </div>
        </div>

        <!-- Platform Card 8: OpenMontage -->
        <div class="glass-panel rounded-xl sm:rounded-2xl p-3 sm:p-5 border border-pink-500/25 hover:border-pink-500/60 transition-all flex flex-col justify-between text-right align-start-dir group">
          <div>
            <div class="w-full aspect-[16/9] rounded-xl bg-[#08080c] border border-white/10 overflow-hidden mb-3 relative shadow-lg group-hover:border-pink-500/50 transition-all flex items-center justify-center">
              <img src="assets/openmontage_preview.jpg" alt="OpenMontage" class="w-full h-full object-contain group-hover:scale-105 transition-all duration-700" onerror="this.src='assets/hero_architect.jpg'" loading="lazy" />
              <div class="absolute top-2 left-2 bg-pink-950/90 border border-pink-500/40 px-2 py-0.5 rounded-full text-[8.5px] font-mono text-pink-300 flex items-center gap-1 backdrop-blur-md shadow-sm">
                <span class="w-1.5 h-1.5 rounded-full bg-pink-400 animate-pulse"></span>
                <span>Video Studio</span>
              </div>
            </div>
            <div class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-pink-950/70 border border-pink-500/30 text-pink-300 text-[9.5px] font-mono mb-1.5">
              <i class="fa-solid fa-film text-pink-400 text-[10px]"></i>
              <span>المونتاج الذكي</span>
            </div>
            <h3 class="text-xs sm:text-base font-bold text-white mb-1.5 leading-snug group-hover:text-pink-300 transition-colors">OpenMontage</h3>
            <p class="text-zinc-300 text-[11px] sm:text-xs leading-relaxed mb-3">
              استوديو إنتاج فيديو آلي متكامل يجمع بين قوة الذكاء الاصطناعي والمونتاج الاحترافي، لتوليد، تحرير، ودمج المشاهد بدقة سينمائية، مما يختصر وقت الإنتاج إلى دقائق.
            </p>
          </div>
        </div>
"""

# Insert before the end of the platforms grid
pattern = r'(</div>\s*</div>\s*</section>\s*<!-- ========================================== -->\s*<!-- 6. AI SOFTWARE MODELS)'

match = re.search(pattern, html)
if match:
    # We want to insert inside the grid. Wait, the grid ends right before the section ends.
    # The grid is inside the section.
    # Let's find the end of the platforms grid more safely.
    grid_end = r'(</div>\s*</div>\s*</section>\s*<!-- ========================================== -->\s*<!-- 6. AI SOFTWARE MODELS)'
    html = re.sub(grid_end, new_cards + r'\1', html)
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Added platform cards successfully!")
else:
    print("Could not find insertion point for platform cards.")

# Also center existing thumbnails by changing object-cover to object-contain and adding flex items-center justify-center
html = html.replace('class="w-full h-full object-cover', 'class="w-full h-full object-contain')
html = html.replace('overflow-hidden mb-3 relative shadow-lg group-hover:border-purple-500/50 transition-all"', 'overflow-hidden mb-3 relative shadow-lg group-hover:border-purple-500/50 transition-all flex items-center justify-center"')
html = html.replace('overflow-hidden mb-3 relative shadow-lg group-hover:border-emerald-500/50 transition-all"', 'overflow-hidden mb-3 relative shadow-lg group-hover:border-emerald-500/50 transition-all flex items-center justify-center"')
html = html.replace('overflow-hidden mb-3 relative shadow-lg group-hover:border-cyan-500/50 transition-all"', 'overflow-hidden mb-3 relative shadow-lg group-hover:border-cyan-500/50 transition-all flex items-center justify-center"')
html = html.replace('overflow-hidden mb-2.5 relative shadow-sm mx-auto"', 'overflow-hidden mb-2.5 relative shadow-sm mx-auto flex items-center justify-center"')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
