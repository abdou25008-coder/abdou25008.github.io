import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# We need to deeply rewrite the 4 platform cards we added earlier:
# Shayrha, E-Commerce, NovaCraft, OpenMontage

shayrha_new = """
        <!-- Platform Card 5: Shayrha -->
        <div class="glass-panel rounded-xl sm:rounded-2xl p-3 sm:p-5 border border-purple-500/25 hover:border-purple-500/60 transition-all flex flex-col justify-between text-right align-start-dir group">
          <div>
            <div class="w-full aspect-[16/9] rounded-xl bg-[#08080c] border border-white/10 overflow-hidden mb-3 relative shadow-lg group-hover:border-purple-500/50 transition-all flex items-center justify-center">
              <img src="assets/shayrha_preview.jpg" alt="Shayrha Platform" class="w-full h-full object-contain group-hover:scale-105 transition-all duration-700" onerror="this.src='assets/hero_architect.jpg'" loading="lazy" />
              <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-transparent to-black/20"></div>
              <div class="absolute top-2 left-2 bg-purple-950/90 border border-purple-500/40 px-2 py-0.5 rounded-full text-[8.5px] font-mono text-purple-300 flex items-center gap-1 backdrop-blur-md shadow-sm">
                <span class="w-1.5 h-1.5 rounded-full bg-purple-400 animate-pulse"></span>
                <span>Live Platform</span>
              </div>
            </div>
            
            <div class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-purple-950/70 border border-purple-500/30 text-purple-300 text-[9.5px] font-mono mb-1.5">
              <i class="fa-solid fa-share-nodes text-purple-400 text-[10px]"></i>
              <span>منصة شبكات اجتماعية متكاملة</span>
            </div>
            
            <h3 class="text-xs sm:text-base font-bold text-white mb-1.5 leading-snug group-hover:text-purple-300 transition-colors">
              منصة شيرها (Shayrha) - نبض التواصل الرقمي المصري
            </h3>
            
            <p class="text-zinc-300 text-[11px] sm:text-xs leading-relaxed mb-3">
              تحفة برمجية تجسد الجيل الجديد من منصات التواصل الاجتماعي؛ تم هندستها بالكامل لتكون منصة تفاعلية متطورة للمستخدم العربي. تجمع المنصة بين جمالية التصميم وقوة الأداء لتتيح للمستخدمين مشاركة الأفكار، والتواصل المباشر، وبناء مجتمعات رقمية نابضة بالحياة، مع لوحة تحكم ذكية وصلاحيات أمان صارمة.
            </p>

            <div class="grid grid-cols-2 gap-1.5 mb-3 text-[9.5px] sm:text-xs text-zinc-300">
              <div class="flex items-center gap-1.5 bg-black/40 p-1.5 rounded-lg border border-white/5">
                <i class="fa-solid fa-bolt text-purple-400 text-[10px]"></i>
                <span>محرك تفاعل لحظي فائق السرعة</span>
              </div>
              <div class="flex items-center gap-1.5 bg-black/40 p-1.5 rounded-lg border border-white/5">
                <i class="fa-solid fa-shield-halved text-purple-400 text-[10px]"></i>
                <span>بنية سحابية قوية ومؤمنة (Supabase)</span>
              </div>
            </div>
          </div>
          
          <div class="flex flex-row items-center gap-1.5 pt-2 border-t border-white/10">
            <a href="https://shayrha.surge.sh" target="_blank" rel="noopener noreferrer" class="flex-1 inline-flex items-center justify-center gap-1.5 px-2.5 py-2 rounded-lg sm:rounded-xl bg-purple-600 hover:bg-purple-500 text-white font-bold text-[10px] sm:text-xs shadow-glow-purple transition-all touch-press">
              <i class="fa-solid fa-rocket text-[9px]"></i>
              <span>زيارة المنصة الحية</span>
            </a>
          </div>
        </div>
"""

ecommerce_new = """
        <!-- Platform Card 6: E-Commerce Store -->
        <div class="glass-panel rounded-xl sm:rounded-2xl p-3 sm:p-5 border border-cyan-500/25 hover:border-cyan-500/60 transition-all flex flex-col justify-between text-right align-start-dir group">
          <div>
            <div class="w-full aspect-[16/9] rounded-xl bg-[#08080c] border border-white/10 overflow-hidden mb-3 relative shadow-lg group-hover:border-cyan-500/50 transition-all flex items-center justify-center">
              <img src="assets/ecommerce_preview.jpg" alt="E-Commerce Store" class="w-full h-full object-contain group-hover:scale-105 transition-all duration-700" onerror="this.src='assets/hero_architect.jpg'" loading="lazy" />
              <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-transparent to-black/20"></div>
              <div class="absolute top-2 left-2 bg-cyan-950/90 border border-cyan-500/40 px-2 py-0.5 rounded-full text-[8.5px] font-mono text-cyan-300 flex items-center gap-1 backdrop-blur-md shadow-sm">
                <span class="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-pulse"></span>
                <span>E-Commerce Engine</span>
              </div>
            </div>
            
            <div class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-cyan-950/70 border border-cyan-500/30 text-cyan-300 text-[9.5px] font-mono mb-1.5">
              <i class="fa-solid fa-store text-cyan-400 text-[10px]"></i>
              <span>معمارية تجارة إلكترونية متطورة</span>
            </div>
            
            <h3 class="text-xs sm:text-base font-bold text-white mb-1.5 leading-snug group-hover:text-cyan-300 transition-colors">
              منظومة المتجر الإلكتروني الذكية
            </h3>
            
            <p class="text-zinc-300 text-[11px] sm:text-xs leading-relaxed mb-3">
              منصة بيع رقمية تم بناؤها من الصفر لتكون محركاً جباراً للمبيعات؛ لا تقتصر على عرض المنتجات فحسب، بل تدير دورة المبيعات بالكامل بدءاً من بوابات الدفع اللحظية وصولاً إلى إدارة المخزون وتحليل السلوك الشرائي للعملاء، لتقديم تجربة تسوق لا تُنسى.
            </p>

            <div class="grid grid-cols-2 gap-1.5 mb-3 text-[9.5px] sm:text-xs text-zinc-300">
              <div class="flex items-center gap-1.5 bg-black/40 p-1.5 rounded-lg border border-white/5">
                <i class="fa-solid fa-credit-card text-cyan-400 text-[10px]"></i>
                <span>بوابات دفع سريعة وآمنة</span>
              </div>
              <div class="flex items-center gap-1.5 bg-black/40 p-1.5 rounded-lg border border-white/5">
                <i class="fa-solid fa-chart-line text-cyan-400 text-[10px]"></i>
                <span>لوحة تحكم إدارية ومؤشرات مالية</span>
              </div>
            </div>
          </div>
        </div>
"""

novacraft_new = """
        <!-- Platform Card 7: NovaCraft -->
        <div class="glass-panel rounded-xl sm:rounded-2xl p-3 sm:p-5 border border-emerald-500/25 hover:border-emerald-500/60 transition-all flex flex-col justify-between text-right align-start-dir group">
          <div>
            <div class="w-full aspect-[16/9] rounded-xl bg-[#08080c] border border-white/10 overflow-hidden mb-3 relative shadow-lg group-hover:border-emerald-500/50 transition-all flex items-center justify-center">
              <img src="assets/novacraft_preview.jpg" alt="NovaCraft" class="w-full h-full object-contain group-hover:scale-105 transition-all duration-700" onerror="this.src='assets/hero_architect.jpg'" loading="lazy" />
              <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-transparent to-black/20"></div>
              <div class="absolute top-2 left-2 bg-emerald-950/90 border border-emerald-500/40 px-2 py-0.5 rounded-full text-[8.5px] font-mono text-emerald-300 flex items-center gap-1 backdrop-blur-md shadow-sm">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
                <span>No-Code AI SaaS</span>
              </div>
            </div>
            
            <div class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-emerald-950/70 border border-emerald-500/30 text-emerald-300 text-[9.5px] font-mono mb-1.5">
              <i class="fa-solid fa-layer-group text-emerald-400 text-[10px]"></i>
              <span>محرك بناء التطبيقات بالذكاء الاصطناعي</span>
            </div>
            
            <h3 class="text-xs sm:text-base font-bold text-white mb-1.5 leading-snug group-hover:text-emerald-300 transition-colors">
              منصة NovaCraft (من الفكرة إلى الإبداع للانتشار)
            </h3>
            
            <p class="text-zinc-300 text-[11px] sm:text-xs leading-relaxed mb-3">
              مشروع طموح وثوري في عالم الـ SaaS (No-Code Builder). يتيح لأي شخص تحويل فكرته إلى تطبيق أو موقع إلكتروني بالكامل من خلال الأوامر الصوتية أو النصوص البسيطة فقط؛ حيث يقوم محرك الذكاء الاصطناعي بتحليل المدخلات وتوليد الواجهات، مع توفير محرر بصري شامل للتعديل اليدوي.
            </p>

            <div class="grid grid-cols-2 gap-1.5 mb-3 text-[9.5px] sm:text-xs text-zinc-300">
              <div class="flex items-center gap-1.5 bg-black/40 p-1.5 rounded-lg border border-white/5">
                <i class="fa-solid fa-wand-magic-sparkles text-emerald-400 text-[10px]"></i>
                <span>توليد الواجهات عبر الأوامر الصوتية والنصية</span>
              </div>
              <div class="flex items-center gap-1.5 bg-black/40 p-1.5 rounded-lg border border-white/5">
                <i class="fa-solid fa-cubes text-emerald-400 text-[10px]"></i>
                <span>محرر بصري تفاعلي شامل (Universal Visual Editor)</span>
              </div>
            </div>
          </div>
          
          <div class="flex flex-row items-center gap-1.5 pt-2 border-t border-white/10">
            <a href="https://github.com/abdou25008-coder/appcraft-builder.git" target="_blank" rel="noopener noreferrer" class="flex-1 inline-flex items-center justify-center gap-1.5 px-2.5 py-2 rounded-lg sm:rounded-xl bg-emerald-600 hover:bg-emerald-500 text-zinc-950 font-bold text-[10px] sm:text-xs shadow-glow-emerald transition-all touch-press">
              <i class="fa-brands fa-github text-[9px]"></i>
              <span>مستودع المحرك (AppCraft)</span>
            </a>
          </div>
        </div>
"""

openmontage_new = """
        <!-- Platform Card 8: OpenMontage -->
        <div class="glass-panel rounded-xl sm:rounded-2xl p-3 sm:p-5 border border-pink-500/25 hover:border-pink-500/60 transition-all flex flex-col justify-between text-right align-start-dir group">
          <div>
            <div class="w-full aspect-[16/9] rounded-xl bg-[#08080c] border border-white/10 overflow-hidden mb-3 relative shadow-lg group-hover:border-pink-500/50 transition-all flex items-center justify-center">
              <img src="assets/openmontage_preview.jpg" alt="OpenMontage" class="w-full h-full object-contain group-hover:scale-105 transition-all duration-700" onerror="this.src='assets/hero_architect.jpg'" loading="lazy" />
              <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-transparent to-black/20"></div>
              <div class="absolute top-2 left-2 bg-pink-950/90 border border-pink-500/40 px-2 py-0.5 rounded-full text-[8.5px] font-mono text-pink-300 flex items-center gap-1 backdrop-blur-md shadow-sm">
                <span class="w-1.5 h-1.5 rounded-full bg-pink-400 animate-pulse"></span>
                <span>AI Video Studio</span>
              </div>
            </div>
            
            <div class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-pink-950/70 border border-pink-500/30 text-pink-300 text-[9.5px] font-mono mb-1.5">
              <i class="fa-solid fa-film text-pink-400 text-[10px]"></i>
              <span>استوديو المونتاج الذاتي المتكامل</span>
            </div>
            
            <h3 class="text-xs sm:text-base font-bold text-white mb-1.5 leading-snug group-hover:text-pink-300 transition-colors">
              منظومة OpenMontage لإنتاج الفيديو الذكي
            </h3>
            
            <p class="text-zinc-300 text-[11px] sm:text-xs leading-relaxed mb-3">
              منظومة توليدية ضخمة مصممة لأتمتة صناعة محتوى اليوتيوب (Shorts/Reels) بدقة سينمائية؛ تدعم توليد مقاطع ترويجية وتسجيلات وثائقية (مثل فيديوهات كائنات الأعماق لقناة Fathom X) من مجرد سطر نصي، مع ربط مباشر بحسابات السوشيال ميديا للنشر الآلي والذاتي.
            </p>

            <div class="grid grid-cols-2 gap-1.5 mb-3 text-[9.5px] sm:text-xs text-zinc-300">
              <div class="flex items-center gap-1.5 bg-black/40 p-1.5 rounded-lg border border-white/5">
                <i class="fa-solid fa-clapperboard text-pink-400 text-[10px]"></i>
                <span>إنتاج 9:16 Shorts آلياً بجودة 4K</span>
              </div>
              <div class="flex items-center gap-1.5 bg-black/40 p-1.5 rounded-lg border border-white/5">
                <i class="fa-brands fa-facebook text-pink-400 text-[10px]"></i>
                <span>النشر التلقائي عبر الشبكات (Auto-Publish)</span>
              </div>
            </div>
          </div>
          
          <div class="flex flex-row items-center gap-1.5 pt-2 border-t border-white/10">
            <a href="https://github.com/calesthio/OpenMontage.git" target="_blank" rel="noopener noreferrer" class="flex-1 inline-flex items-center justify-center gap-1.5 px-2.5 py-2 rounded-lg sm:rounded-xl bg-pink-600 hover:bg-pink-500 text-white font-bold text-[10px] sm:text-xs shadow-glow-purple transition-all touch-press">
              <i class="fa-brands fa-github text-[9px]"></i>
              <span>تصفح الكود الرسمي</span>
            </a>
          </div>
        </div>
"""

# Let's replace the old placeholders with these majestic ones
# The old ones have specific patterns

old_shayrha_pattern = r'<!-- Platform Card 5: Shayrha -->.*?</div>\s*</div>\s*<!-- Platform Card 6: E-Commerce Store -->'
html = re.sub(old_shayrha_pattern, shayrha_new + "\n        <!-- Platform Card 6: E-Commerce Store -->", html, flags=re.DOTALL)

old_ecommerce_pattern = r'<!-- Platform Card 6: E-Commerce Store -->.*?</div>\s*</div>\s*<!-- Platform Card 7: NovaCraft -->'
html = re.sub(old_ecommerce_pattern, ecommerce_new + "\n        <!-- Platform Card 7: NovaCraft -->", html, flags=re.DOTALL)

old_novacraft_pattern = r'<!-- Platform Card 7: NovaCraft -->.*?</div>\s*</div>\s*<!-- Platform Card 8: OpenMontage -->'
html = re.sub(old_novacraft_pattern, novacraft_new + "\n        <!-- Platform Card 8: OpenMontage -->", html, flags=re.DOTALL)

old_openmontage_pattern = r'<!-- Platform Card 8: OpenMontage -->.*?</div>\s*</div>\s*</div>'
html = re.sub(old_openmontage_pattern, openmontage_new + "\n      </div>", html, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
