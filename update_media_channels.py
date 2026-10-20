import io, sys, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# ---------------------------------------------------------------------------
# 1. Update Media Network Section Header & Description
# ---------------------------------------------------------------------------
old_media_header = """          <div class="inline-flex items-center gap-1.5 text-[10px] sm:text-xs font-bold text-purple-400 tracking-wider uppercase mb-1">
            <span class="w-4 h-[2px] bg-purple-500"></span>
            <span data-i18n="media_badge">الشبكة الإعلامية العالمية</span>
          </div>
          <h2 class="text-lg sm:text-2xl lg:text-3xl font-black text-white" data-i18n="media_title">
            شبكة القنوات الرقمية <span class="purple-gradient-text">والمحتوى الوثائقي (Shorts)</span>
          </h2>
        </div>
        <p class="text-zinc-400 text-[11px] sm:text-xs max-w-md" data-i18n="media_sub">
          إدارة وإنتاج محتوى متكامل عبر 4 قنوات دولية تعتمد على الذكاء الاصطناعي التوليدي لسرد قصص التاريخ والاقتصاد والتقنية واستكشافات الأعماق لملايين المشاهدين.
        </p>"""

new_media_header = """          <div class="inline-flex items-center gap-1.5 text-[10px] sm:text-xs font-bold text-cyan-400 tracking-wider uppercase mb-1">
            <span class="w-4 h-[2px] bg-cyan-500"></span>
            <span data-i18n="media_badge">شبكة الإنتاج الرقمي والقنوات الدولية</span>
          </div>
          <h2 class="text-lg sm:text-2xl lg:text-3xl font-black text-white" data-i18n="media_title">
            منظومة قنوات السوشيال ميديا <span class="purple-gradient-text">والإنتاج التوليدي المؤتمت</span>
          </h2>
        </div>
        <p class="text-zinc-400 text-[11px] sm:text-xs max-w-md" data-i18n="media_sub">
          معمارية إنتاج ونشر مؤتمتة تدير شبكة قنوات دولية متعددة المنصات (YouTube, TikTok, Instagram, Facebook) عبر خطوط أنابيب الذكاء الاصطناعي التوليدي والجدولة السحابية الدقيقة.
        </p>"""

html = html.replace(old_media_header, new_media_header)

# ---------------------------------------------------------------------------
# 2. Update Media Highlights Badges
# ---------------------------------------------------------------------------
old_badges = """      <!-- Section Highlights Badges -->
      <div class="flex flex-wrap items-center gap-1.5 mb-3 sm:mb-6">
        <span class="px-2 py-0.5 rounded-full bg-blue-950/80 border border-blue-500/40 text-blue-300 font-mono text-[9px] sm:text-[10px] flex items-center gap-1">
          <i class="fa-brands fa-facebook-f text-blue-400"></i> Fathom X (الرسمية)
        </span>
        <span class="px-2 py-0.5 rounded-full bg-red-950/80 border border-red-500/40 text-red-300 font-mono text-[9px] sm:text-[10px] flex items-center gap-1">
          <i class="fa-brands fa-youtube text-red-400"></i> +10M مشاهدة شورتس
        </span>
        <span class="px-2 py-0.5 rounded-full bg-purple-950/80 border border-purple-500/40 text-purple-300 font-mono text-[9px] sm:text-[10px] flex items-center gap-1">
          <i class="fa-solid fa-bolt text-purple-400"></i> 4 قنوات دولية نشطة
        </span>
      </div>"""

new_badges = """      <!-- Section Highlights Badges -->
      <div class="flex flex-wrap items-center gap-1.5 mb-3 sm:mb-6">
        <span class="px-2 py-0.5 rounded-full bg-cyan-950/80 border border-cyan-500/40 text-cyan-300 font-mono text-[9px] sm:text-[10px] flex items-center gap-1">
          <i class="fa-solid fa-water text-cyan-400"></i> Fathom X (Deep Sea)
        </span>
        <span class="px-2 py-0.5 rounded-full bg-emerald-950/80 border border-emerald-500/40 text-emerald-300 font-mono text-[9px] sm:text-[10px] flex items-center gap-1">
          <i class="fa-solid fa-heart-pulse text-emerald-400"></i> Smart Health USA
        </span>
        <span class="px-2 py-0.5 rounded-full bg-amber-950/80 border border-amber-500/40 text-amber-300 font-mono text-[9px] sm:text-[10px] flex items-center gap-1">
          <i class="fa-solid fa-gem text-amber-400"></i> Meta Lapse (Cinematic ASMR)
        </span>
        <span class="px-2 py-0.5 rounded-full bg-purple-950/80 border border-purple-500/40 text-purple-300 font-mono text-[9px] sm:text-[10px] flex items-center gap-1">
          <i class="fa-solid fa-bolt text-purple-400"></i> أتمتة Buffer & Multi-Platform
        </span>
      </div>"""

html = html.replace(old_badges, new_badges)

# ---------------------------------------------------------------------------
# 3. Replace the 4 Channels Cards Grid with our 3 Core Strategic Channels
# ---------------------------------------------------------------------------
old_channels_grid_pattern = r'<!-- 4 Channels Reel Cards.*?<!-- Dedicated Verified Official Pages & Channels Hub -->'

new_channels_grid = """<!-- 3 Flagship Channels Reel Cards (3 Prominent Pillars) -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-3.5 sm:gap-6 mb-4 sm:mb-8">
        
        <!-- Channel 1: Fathom X (Cinematic Deep Sea Documentary) -->
        <div class="glass-panel rounded-xl sm:rounded-2xl p-3 sm:p-4 border border-cyan-500/35 hover:border-cyan-500/80 transition-all flex flex-col justify-between text-right align-start-dir group touch-press">
          <div>
            <div class="aspect-[9/13] max-h-72 rounded-xl bg-[#08080c] border border-white/10 mb-3 overflow-hidden relative shadow-md flex items-center justify-center">
              <img 
                src="assets/fathom_x_deep_sea_cover.jpg" 
                alt="Fathom X Deep Sea Documentary" 
                class="w-full h-full object-cover object-center group-hover:scale-105 transition-all duration-700" 
                onerror="this.src='assets/hero_architect.jpg'"
                loading="lazy" 
              />
              <div class="absolute inset-0 bg-gradient-to-t from-black/95 via-black/20 to-transparent"></div>
              
              <div class="absolute top-2 left-2 bg-cyan-950/90 border border-cyan-500/40 text-cyan-300 px-2.5 py-0.5 rounded-full text-[8.5px] font-mono flex items-center gap-1 shadow-sm backdrop-blur-md">
                <i class="fa-solid fa-water text-[9px] text-cyan-400"></i>
                <span>Fathom X // Deep Sea</span>
              </div>

              <div class="absolute top-2 right-2 bg-black/70 border border-white/10 text-white px-2 py-0.5 rounded-full text-[8px] font-mono backdrop-blur-md">
                <span>Multi-Platform</span>
              </div>

              <!-- Animated Play Icon Indicator -->
              <div class="absolute inset-0 flex items-center justify-center pointer-events-none">
                <div class="w-11 h-11 rounded-full bg-cyan-500/20 border border-cyan-400/50 backdrop-blur-md flex items-center justify-center text-cyan-300 shadow-lg group-hover:scale-110 group-hover:bg-cyan-500 group-hover:text-black transition-all">
                  <i class="fa-solid fa-play text-xs mr-0.5"></i>
                </div>
              </div>

              <div class="absolute bottom-2 right-2 left-2 text-right">
                <div class="flex items-center gap-1.5 justify-between">
                  <span class="text-[8.5px] font-mono bg-cyan-950/90 text-cyan-300 border border-cyan-500/40 px-2 py-0.5 rounded">MiniMax-H3 + Imagen 3</span>
                  <span class="text-[8px] font-mono text-zinc-400">FB + YT + TT + IG</span>
                </div>
              </div>
            </div>
            
            <div class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-md bg-cyan-950/60 border border-cyan-500/30 text-cyan-300 text-[9.5px] font-mono mb-1.5">
              <i class="fa-solid fa-film text-cyan-400 text-[10px]"></i>
              <span>وثائقيات الأعماق والغموض</span>
            </div>
            
            <h4 class="font-bold text-white text-xs sm:text-sm mb-1 leading-snug group-hover:text-cyan-300 transition-colors">
              مشروع وقناة Fathom X العالمية
            </h4>
            
            <p class="text-zinc-300 text-[10.5px] sm:text-xs leading-relaxed mb-3">
              منظومة إنتاج وثائقيات سينمائية فائقة الغموض لأعماق المحيطات والمخلوقات النادرة والكوارث الغارقة. مبنية بخوارزميات تحريك الفيديو المتتالي دون استوك (No-Stock)، مع هندسة صوتية واقعية لمحاكاة أجهزة الغوص وعزل كامل للضوضاء.
            </p>

            <div class="space-y-1 mb-3 text-[9.5px] font-mono text-zinc-400 bg-black/40 p-2 rounded-lg border border-white/5">
              <div class="flex items-center justify-between">
                <span>توزيع سحابي تلقائي:</span>
                <span class="text-cyan-300 font-bold">Buffer 4-Channel Push</span>
              </div>
              <div class="flex items-center justify-between">
                <span>المحتوى المنجز:</span>
                <span class="text-emerald-400 font-bold">+50 حلقة وثائقية متكاملة</span>
              </div>
            </div>
          </div>

          <div class="flex items-center gap-1.5 w-full">
            <a href="https://www.facebook.com/FathomX01/" target="_blank" rel="noopener noreferrer" onclick="triggerHaptic()" class="flex-1 inline-flex items-center justify-center gap-1.5 py-2 px-2.5 rounded-xl bg-cyan-600/90 hover:bg-cyan-500 text-white font-bold text-[10.5px] shadow-sm transition-all touch-press">
              <i class="fa-brands fa-facebook-f text-xs"></i>
              <span>صفحة فيسبوك الرسمية</span>
            </a>
          </div>
        </div>

        <!-- Channel 2: Smart Health USA (Medical & Health Infographics) -->
        <div class="glass-panel rounded-xl sm:rounded-2xl p-3 sm:p-4 border border-emerald-500/35 hover:border-emerald-500/80 transition-all flex flex-col justify-between text-right align-start-dir group touch-press">
          <div>
            <div class="aspect-[9/13] max-h-72 rounded-xl bg-[#08080c] border border-white/10 mb-3 overflow-hidden relative shadow-md flex items-center justify-center">
              <img 
                src="assets/smart_health_cover.jpg" 
                alt="Smart Health USA Channel" 
                class="w-full h-full object-cover object-center group-hover:scale-105 transition-all duration-700" 
                onerror="this.src='assets/hero_architect.jpg'"
                loading="lazy" 
              />
              <div class="absolute inset-0 bg-gradient-to-t from-black/95 via-black/20 to-transparent"></div>
              
              <div class="absolute top-2 left-2 bg-emerald-950/90 border border-emerald-500/40 text-emerald-300 px-2.5 py-0.5 rounded-full text-[8.5px] font-mono flex items-center gap-1 shadow-sm backdrop-blur-md">
                <i class="fa-solid fa-heart-pulse text-[9px] text-emerald-400"></i>
                <span>Smart Health USA</span>
              </div>

              <div class="absolute top-2 right-2 bg-black/70 border border-white/10 text-white px-2 py-0.5 rounded-full text-[8px] font-mono backdrop-blur-md">
                <span>Verified Channel</span>
              </div>

              <!-- Animated Play Icon Indicator -->
              <div class="absolute inset-0 flex items-center justify-center pointer-events-none">
                <div class="w-11 h-11 rounded-full bg-emerald-500/20 border border-emerald-400/50 backdrop-blur-md flex items-center justify-center text-emerald-300 shadow-lg group-hover:scale-110 group-hover:bg-emerald-500 group-hover:text-black transition-all">
                  <i class="fa-solid fa-play text-xs mr-0.5"></i>
                </div>
              </div>

              <div class="absolute bottom-2 right-2 left-2 text-right">
                <div class="flex items-center gap-1.5 justify-between">
                  <span class="text-[8.5px] font-mono bg-emerald-950/90 text-emerald-300 border border-emerald-500/40 px-2 py-0.5 rounded">Imagen 3 + MedVision</span>
                  <span class="text-[8px] font-mono text-zinc-400">Shorts + 4:5 Carousels</span>
                </div>
              </div>
            </div>
            
            <div class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-md bg-emerald-950/60 border border-emerald-500/30 text-emerald-300 text-[9.5px] font-mono mb-1.5">
              <i class="fa-solid fa-shield-halved text-emerald-400 text-[10px]"></i>
              <span>محتوى طبي وتوعوي عالمي</span>
            </div>
            
            <h4 class="font-bold text-white text-xs sm:text-sm mb-1 leading-snug group-hover:text-emerald-300 transition-colors">
              قناة ومنظومة Smart Health USA
            </h4>
            
            <p class="text-zinc-300 text-[10.5px] sm:text-xs leading-relaxed mb-3">
              شبكة محتوى طبي دولي موجه للجمهور الأمريكي والعالمي؛ تشمل إنتاج مقاطع الشورتس ثلاثية الأبعاد لشخصيات وأجهزة الجسم (Sammy Stomach)، وباقات الكاروسيل الطبية بنسبة 4:5 الأكثر تفاعلاً، مع ربط مباشر ومؤتمت بـ YouTube Shorts وTikTok.
            </p>

            <div class="space-y-1 mb-3 text-[9.5px] font-mono text-zinc-400 bg-black/40 p-2 rounded-lg border border-white/5">
              <div class="flex items-center justify-between">
                <span>نموذج التوليد البصري:</span>
                <span class="text-emerald-300 font-bold">Zero-Watermark 4K Medical</span>
              </div>
              <div class="flex items-center justify-between">
                <span>الربط والجدولة:</span>
                <span class="text-emerald-400 font-bold">YouTube API + Buffer Live</span>
              </div>
            </div>
          </div>

          <div class="flex items-center gap-1.5 w-full">
            <a href="https://wa.me/201092519210?text=استعراض%20نماذج%20وحلقات%20Smart%20Health%20USA" target="_blank" rel="noopener noreferrer" onclick="triggerHaptic()" class="flex-1 inline-flex items-center justify-center gap-1.5 py-2 px-2.5 rounded-xl bg-emerald-600/90 hover:bg-emerald-500 text-white font-bold text-[10.5px] shadow-sm transition-all touch-press">
              <i class="fa-brands fa-youtube text-xs"></i>
              <span>استعراض أعمال القناة</span>
            </a>
          </div>
        </div>

        <!-- Channel 3: Meta Lapse (AI Cinematic ASMR Crafting) -->
        <div class="glass-panel rounded-xl sm:rounded-2xl p-3 sm:p-4 border border-amber-500/35 hover:border-amber-500/80 transition-all flex flex-col justify-between text-right align-start-dir group touch-press">
          <div>
            <div class="aspect-[9/13] max-h-72 rounded-xl bg-[#08080c] border border-white/10 mb-3 overflow-hidden relative shadow-md flex items-center justify-center">
              <img 
                src="assets/meta_lapse_asmr_cover.jpg" 
                alt="Meta Lapse Cinematic ASMR" 
                class="w-full h-full object-cover object-center group-hover:scale-105 transition-all duration-700" 
                onerror="this.src='assets/hero_architect.jpg'"
                loading="lazy" 
              />
              <div class="absolute inset-0 bg-gradient-to-t from-black/95 via-black/20 to-transparent"></div>
              
              <div class="absolute top-2 left-2 bg-amber-950/90 border border-amber-500/40 text-amber-300 px-2.5 py-0.5 rounded-full text-[8.5px] font-mono flex items-center gap-1 shadow-sm backdrop-blur-md">
                <i class="fa-solid fa-gem text-[9px] text-amber-400"></i>
                <span>Meta Lapse // ASMR</span>
              </div>

              <div class="absolute top-2 right-2 bg-black/70 border border-white/10 text-white px-2 py-0.5 rounded-full text-[8px] font-mono backdrop-blur-md">
                <span>Gemini Omni Flash</span>
              </div>

              <!-- Animated Play Icon Indicator -->
              <div class="absolute inset-0 flex items-center justify-center pointer-events-none">
                <div class="w-11 h-11 rounded-full bg-amber-500/20 border border-amber-400/50 backdrop-blur-md flex items-center justify-center text-amber-300 shadow-lg group-hover:scale-110 group-hover:bg-amber-500 group-hover:text-black transition-all">
                  <i class="fa-solid fa-play text-xs mr-0.5"></i>
                </div>
              </div>

              <div class="absolute bottom-2 right-2 left-2 text-right">
                <div class="flex items-center gap-1.5 justify-between">
                  <span class="text-[8.5px] font-mono bg-amber-950/90 text-amber-300 border border-amber-500/40 px-2 py-0.5 rounded">Multi-Shot Cutting (9:16)</span>
                  <span class="text-[8px] font-mono text-zinc-400">Audio Crescendo</span>
                </div>
              </div>
            </div>
            
            <div class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-md bg-amber-950/60 border border-amber-500/30 text-amber-300 text-[9.5px] font-mono mb-1.5">
              <i class="fa-solid fa-wand-magic-sparkles text-amber-400 text-[10px]"></i>
              <span>حرف دقيقة ومونتاج حسي (ASMR)</span>
            </div>
            
            <h4 class="font-bold text-white text-xs sm:text-sm mb-1 leading-snug group-hover:text-amber-300 transition-colors">
              قناة وعلامة Meta Lapse العالمية
            </h4>
            
            <p class="text-zinc-300 text-[10.5px] sm:text-xs leading-relaxed mb-3">
              سلسلة حلقات سينمائية عالية الجودة تركز على صناعة التحف والمجسمات الدقيقة (مثل ساعات الفولاذ الدمشقي والأبراج النحاسية). تعتمد على بروتوكول التقطيع الديناميكي (+20 زاوية ماكرو بالدقيقة) مع هندسة صوتية حسية وتصعيد نغمي.
            </p>

            <div class="space-y-1 mb-3 text-[9.5px] font-mono text-zinc-400 bg-black/40 p-2 rounded-lg border border-white/5">
              <div class="flex items-center justify-between">
                <span>محرك التوليد بالفيديو:</span>
                <span class="text-amber-300 font-bold">Google Flow (Omni Flash)</span>
              </div>
              <div class="flex items-center justify-between">
                <span>استراتيجية الانتشار:</span>
                <span class="text-amber-400 font-bold">Viral Algorithm Playbook</span>
              </div>
            </div>
          </div>

          <div class="flex items-center gap-1.5 w-full">
            <a href="https://wa.me/201092519210?text=استعراض%20فيديوهات%20Meta%20Lapse%20ASMR" target="_blank" rel="noopener noreferrer" onclick="triggerHaptic()" class="flex-1 inline-flex items-center justify-center gap-1.5 py-2 px-2.5 rounded-xl bg-amber-600/90 hover:bg-amber-500 text-white font-bold text-[10.5px] shadow-sm transition-all touch-press">
              <i class="fa-solid fa-film text-xs"></i>
              <span>استعراض نماذج الحلقات</span>
            </a>
          </div>
        </div>

      </div>

      <!-- Dedicated Verified Official Pages & Channels Hub -->"""

html = re.sub(old_channels_grid_pattern, new_channels_grid, html, flags=re.DOTALL)

# ---------------------------------------------------------------------------
# 4. Update the Official Hub items to reflect these actual channels
# ---------------------------------------------------------------------------
old_hub_pages_pattern = r'<!-- Official Page 1: Fathom X Facebook -->.*?<!-- 8\. HIGH-CONVERTING'

new_hub_pages = """<!-- Official Page 1: Fathom X Facebook -->
          <a href="https://www.facebook.com/FathomX01/" target="_blank" rel="noopener noreferrer" onclick="triggerHaptic()" class="p-2.5 sm:p-3 rounded-xl bg-blue-950/30 border border-blue-500/30 hover:border-blue-500/80 transition-all flex flex-col justify-between text-right align-start-dir group touch-press">
            <div class="flex items-center gap-2 mb-1.5">
              <div class="w-7 h-7 rounded-lg bg-blue-600 flex items-center justify-center text-white text-xs shadow-md">
                <i class="fa-brands fa-facebook-f"></i>
              </div>
              <div>
                <span class="text-[11px] font-bold text-white block leading-tight group-hover:text-blue-300 transition-colors">Fathom X</span>
                <span class="text-[8px] font-mono text-blue-400">صفحة فيسبوك الرسمية</span>
              </div>
            </div>
            <span class="text-[9px] text-zinc-400 line-clamp-1 mb-2">وثائقيات الأعماق والغموض</span>
            <div class="w-full py-1 px-2 rounded-md bg-blue-600/80 hover:bg-blue-600 text-white text-[9.5px] font-bold text-center flex items-center justify-center gap-1 shadow-sm">
              <span>متابعة الصفحة</span>
              <i class="fa-solid fa-arrow-up-right-from-square text-[7.5px]"></i>
            </div>
          </a>

          <!-- Official Page 2: Smart Health USA YouTube & Buffer Hub -->
          <a href="https://wa.me/201092519210?text=روابط%20حسابات%20Smart%20Health%20USA" target="_blank" rel="noopener noreferrer" onclick="triggerHaptic()" class="p-2.5 sm:p-3 rounded-xl bg-emerald-950/30 border border-emerald-500/30 hover:border-emerald-500/80 transition-all flex flex-col justify-between text-right align-start-dir group touch-press">
            <div class="flex items-center gap-2 mb-1.5">
              <div class="w-7 h-7 rounded-lg bg-emerald-600 flex items-center justify-center text-white text-xs shadow-md">
                <i class="fa-brands fa-youtube"></i>
              </div>
              <div>
                <span class="text-[11px] font-bold text-white block leading-tight group-hover:text-emerald-300 transition-colors">Smart Health USA</span>
                <span class="text-[8px] font-mono text-emerald-400">YouTube + TikTok</span>
              </div>
            </div>
            <span class="text-[9px] text-zinc-400 line-clamp-1 mb-2">محتوى طبي 3D + إنفوجرافيك</span>
            <div class="w-full py-1 px-2 rounded-md bg-emerald-600/80 hover:bg-emerald-600 text-white text-[9.5px] font-bold text-center flex items-center justify-center gap-1 shadow-sm">
              <span>استعراض القناة</span>
              <i class="fa-solid fa-arrow-up-right-from-square text-[7.5px]"></i>
            </div>
          </a>

          <!-- Official Page 3: Meta Lapse (ASMR Cinematic Hub) -->
          <a href="https://wa.me/201092519210?text=روابط%20حسابات%20Meta%20Lapse" target="_blank" rel="noopener noreferrer" onclick="triggerHaptic()" class="p-2.5 sm:p-3 rounded-xl bg-amber-950/30 border border-amber-500/30 hover:border-amber-500/80 transition-all flex flex-col justify-between text-right align-start-dir group touch-press">
            <div class="flex items-center gap-2 mb-1.5">
              <div class="w-7 h-7 rounded-lg bg-amber-600 flex items-center justify-center text-white text-xs shadow-md">
                <i class="fa-solid fa-gem"></i>
              </div>
              <div>
                <span class="text-[11px] font-bold text-white block leading-tight group-hover:text-amber-300 transition-colors">Meta Lapse</span>
                <span class="text-[8px] font-mono text-amber-400">سلسلة ASMR السينمائية</span>
              </div>
            </div>
            <span class="text-[9px] text-zinc-400 line-clamp-1 mb-2">YouTube + TikTok + Reels</span>
            <div class="w-full py-1 px-2 rounded-md bg-amber-600/80 hover:bg-amber-600 text-white text-[9.5px] font-bold text-center flex items-center justify-center gap-1 shadow-sm">
              <span>استعراض الأعمال</span>
              <i class="fa-solid fa-arrow-up-right-from-square text-[7.5px]"></i>
            </div>
          </a>

          <!-- Official Page 4: Telegram & Technical Systems -->
          <a href="https://t.me/abdou25008" target="_blank" rel="noopener noreferrer" onclick="triggerHaptic()" class="p-2.5 sm:p-3 rounded-xl bg-sky-950/30 border border-sky-500/30 hover:border-sky-500/80 transition-all flex flex-col justify-between text-right align-start-dir group touch-press">
            <div class="flex items-center gap-2 mb-1.5">
              <div class="w-7 h-7 rounded-lg bg-sky-600 flex items-center justify-center text-white text-xs shadow-md">
                <i class="fa-brands fa-telegram"></i>
              </div>
              <div>
                <span class="text-[11px] font-bold text-white block leading-tight group-hover:text-sky-300 transition-colors">تيليجرام التقني</span>
                <span class="text-[8px] font-mono text-sky-400">@abdou25008</span>
              </div>
            </div>
            <span class="text-[9px] text-zinc-400 line-clamp-1 mb-2">تحديثات المنظومات والذكاء الاصطناعي</span>
            <div class="w-full py-1 px-2 rounded-md bg-sky-600/80 hover:bg-sky-600 text-white text-[9.5px] font-bold text-center flex items-center justify-center gap-1 shadow-sm">
              <span>انضمام ومتابعة</span>
              <i class="fa-solid fa-arrow-up-right-from-square text-[7.5px]"></i>
            </div>
          </a>

        </div>
      </div>

    </div>
  </section>


  <!-- ========================================== -->
  <!-- 8. HIGH-CONVERTING"""

html = re.sub(old_hub_pages_pattern, new_hub_pages, html, flags=re.DOTALL)

# ---------------------------------------------------------------------------
# 5. Update translations.ar and translations.en for Media Section
# ---------------------------------------------------------------------------
html = html.replace('media_badge: "الشبكة الإعلامية العالمية",', 'media_badge: "شبكة الإنتاج الرقمي والقنوات الدولية",')
html = html.replace('media_title: "شبكة القنوات الرقمية <span class=\'purple-gradient-text\'>والمحتوى الوثائقي (Shorts)</span>",',
                    'media_title: "منظومة قنوات السوشيال ميديا <span class=\'purple-gradient-text\'>والإنتاج التوليدي المؤتمت</span>",')
html = html.replace('media_sub: "إدارة وإنتاج محتوى متكامل عبر 4 قنوات دولية تعتمد على الذكاء الاصطناعي التوليدي لسرد قصص التاريخ والاقتصاد والتقنية واستكشافات الأعماق لملايين المشاهدين.",',
                    'media_sub: "معمارية إنتاج ونشر مؤتمتة تدير شبكة قنوات دولية متعددة المنصات (YouTube, TikTok, Instagram, Facebook) عبر خطوط أنابيب الذكاء الاصطناعي التوليدي والجدولة السحابية الدقيقة.",')

html = html.replace('social_hub_text: "مركز الصفحات والقنوات الرسمية الموثقة:",',
                    'social_hub_text: "مركز القنوات والمنصات الرسمية الموثقة:",')

html = html.replace('social_hub_text: "تابع وتواصل عبر كافة منصات السوشيال ميديا الرسمية:",',
                    'social_hub_text: "مركز القنوات والمنصات الرسمية الموثقة:",')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("index.html updated with the 3 flagship channels successfully!")
