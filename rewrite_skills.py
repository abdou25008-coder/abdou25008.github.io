import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Pattern to replace the 4 services cards
# The cards start at <div class="grid grid-cols-1 md:grid-cols-2 gap-2.5 sm:gap-5">
# and end right before </section> for services.

new_cards = """
      <!-- Services Grid (2 Columns) -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-2.5 sm:gap-5">
        
        <!-- Card 1: Web Apps & SaaS -->
        <div class="glass-panel rounded-xl sm:rounded-2xl p-3 sm:p-5 relative overflow-hidden group transition-all duration-300 text-right align-start-dir">
          <div class="flex items-center gap-2.5 mb-1.5 sm:mb-2.5">
            <div class="w-8 h-8 sm:w-11 sm:h-11 rounded-lg sm:rounded-xl bg-purple-950/80 border border-purple-500/40 flex-shrink-0 flex items-center justify-center text-purple-400 text-sm sm:text-lg shadow-md group-hover:scale-105 transition-transform">
              <i class="fa-solid fa-layer-group"></i>
            </div>
            <h3 class="text-xs sm:text-base font-bold text-white group-hover:text-purple-300 transition-colors leading-snug">
              هندسة المنظومات وتطبيقات الويب (SaaS & Platforms)
            </h3>
          </div>
          <p class="text-zinc-300 text-[10.5px] sm:text-xs leading-relaxed mb-2">
            تطوير وبناء منصات برمجية متكاملة؛ بدءاً من شبكات التواصل الاجتماعي وأنظمة التجارة الإلكترونية المتقدمة، وصولاً إلى لوحات التحكم الإدارية، مع ضمان أداء فائق وتجربة مستخدم عصرية وسلسة.
          </p>
          <div class="flex flex-wrap gap-1 pt-1.5 border-t border-white/5">
            <span class="text-[8.5px] sm:text-[10px] font-mono px-1.5 py-0.5 rounded-md bg-white/5 text-zinc-300 border border-white/5">Full-Stack Development</span>
            <span class="text-[8.5px] sm:text-[10px] font-mono px-1.5 py-0.5 rounded-md bg-white/5 text-zinc-300 border border-white/5">E-Commerce Architecture</span>
          </div>
        </div>

        <!-- Card 2: AI Content Engines -->
        <div class="glass-panel rounded-xl sm:rounded-2xl p-3 sm:p-5 relative overflow-hidden group transition-all duration-300 text-right align-start-dir">
          <div class="flex items-center gap-2.5 mb-1.5 sm:mb-2.5">
            <div class="w-8 h-8 sm:w-11 sm:h-11 rounded-lg sm:rounded-xl bg-pink-950/80 border border-pink-500/40 flex-shrink-0 flex items-center justify-center text-pink-400 text-sm sm:text-lg shadow-md group-hover:scale-105 transition-transform">
              <i class="fa-solid fa-photo-film"></i>
            </div>
            <h3 class="text-xs sm:text-base font-bold text-white group-hover:text-pink-300 transition-colors leading-snug">
              أدوات الإنتاج وتوليد المحتوى (AI Automation)
            </h3>
          </div>
          <p class="text-zinc-300 text-[10.5px] sm:text-xs leading-relaxed mb-2">
            برمجة محركات توليدية متخصصة لأتمتة صناعة الفيديو (Shorts/Reels) ومعالجة الصوتيات البشرية والموسيقى (DAW)، بهدف تسريع عملية الإنتاج الرقمي والنشر التلقائي المباشر على الشبكات.
          </p>
          <div class="flex flex-wrap gap-1 pt-1.5 border-t border-white/5">
            <span class="text-[8.5px] sm:text-[10px] font-mono px-1.5 py-0.5 rounded-md bg-white/5 text-zinc-300 border border-white/5">AI Video Generation</span>
            <span class="text-[8.5px] sm:text-[10px] font-mono px-1.5 py-0.5 rounded-md bg-white/5 text-zinc-300 border border-white/5">Voice Synthesis</span>
          </div>
        </div>

        <!-- Card 3: No-Code Builders -->
        <div class="glass-panel rounded-xl sm:rounded-2xl p-3 sm:p-5 relative overflow-hidden group transition-all duration-300 text-right align-start-dir">
          <div class="flex items-center gap-2.5 mb-1.5 sm:mb-2.5">
            <div class="w-8 h-8 sm:w-11 sm:h-11 rounded-lg sm:rounded-xl bg-emerald-950/80 border border-emerald-500/40 flex-shrink-0 flex items-center justify-center text-emerald-400 text-sm sm:text-lg shadow-md group-hover:scale-105 transition-transform">
              <i class="fa-solid fa-wand-magic-sparkles"></i>
            </div>
            <h3 class="text-xs sm:text-base font-bold text-white group-hover:text-emerald-300 transition-colors leading-snug">
              منصات الـ No-Code والمحررات المرئية
            </h3>
          </div>
          <p class="text-zinc-300 text-[10.5px] sm:text-xs leading-relaxed mb-2">
            ابتكار وتطوير محركات بناء تطبيقات تتيح تحويل الأوامر الصوتية والنصية إلى واجهات تفاعلية بالكامل، مع تصميم أدوات تحرير مرئية (Visual Editors) لمنح المستخدم مرونة مطلقة في التعديل.
          </p>
          <div class="flex flex-wrap gap-1 pt-1.5 border-t border-white/5">
            <span class="text-[8.5px] sm:text-[10px] font-mono px-1.5 py-0.5 rounded-md bg-white/5 text-zinc-300 border border-white/5">Visual App Builders</span>
            <span class="text-[8.5px] sm:text-[10px] font-mono px-1.5 py-0.5 rounded-md bg-white/5 text-zinc-300 border border-white/5">UI/UX Architecture</span>
          </div>
        </div>

        <!-- Card 4: Cloud & APIs -->
        <div class="glass-panel rounded-xl sm:rounded-2xl p-3 sm:p-5 relative overflow-hidden group transition-all duration-300 text-right align-start-dir">
          <div class="flex items-center gap-2.5 mb-1.5 sm:mb-2.5">
            <div class="w-8 h-8 sm:w-11 sm:h-11 rounded-lg sm:rounded-xl bg-cyan-950/80 border border-cyan-500/40 flex-shrink-0 flex items-center justify-center text-cyan-400 text-sm sm:text-lg shadow-md group-hover:scale-105 transition-transform">
              <i class="fa-solid fa-server"></i>
            </div>
            <h3 class="text-xs sm:text-base font-bold text-white group-hover:text-cyan-300 transition-colors leading-snug">
              البنية السحابية وتكامل الذكاء الاصطناعي
            </h3>
          </div>
          <p class="text-zinc-300 text-[10.5px] sm:text-xs leading-relaxed mb-2">
            تأسيس بنى تحتية سحابية صلبة ومؤمنة (مثل Supabase)، وهندسة ربط النماذج اللغوية المتطورة (LLMs) والواجهات البرمجية (APIs) لإنشاء مسارات عمل ذكية تعمل باستقرار وموثوقية عالية.
          </p>
          <div class="flex flex-wrap gap-1 pt-1.5 border-t border-white/5">
            <span class="text-[8.5px] sm:text-[10px] font-mono px-1.5 py-0.5 rounded-md bg-white/5 text-zinc-300 border border-white/5">Cloud Architecture</span>
            <span class="text-[8.5px] sm:text-[10px] font-mono px-1.5 py-0.5 rounded-md bg-white/5 text-zinc-300 border border-white/5">LLMs Integration</span>
          </div>
        </div>

      </div>
    </div>
  </section>
"""

# Now replace the grid block using regex
pattern = r'<!-- Services Grid \(2 Columns\) -->\s*<div class="grid grid-cols-1 md:grid-cols-2 gap-2\.5 sm:gap-5">.*?</section>'
html = re.sub(pattern, new_cards.strip(), html, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updated skills section.")
