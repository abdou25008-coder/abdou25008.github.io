import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# ---------------------------------------------------------------------------
# 1. Update header button text: replace "استشارة مجانية" with "تواصل تقني" / "تواصل"
# ---------------------------------------------------------------------------
html = html.replace('<span class="hidden sm:inline" data-i18n="btn_header_cta">استشارة مجانية</span>', 
                    '<span class="hidden sm:inline" data-i18n="btn_header_cta">تواصل تقني</span>')

# ---------------------------------------------------------------------------
# 2. Add Mobile Hero Card right below mobile micro avatar badge in hero
# ---------------------------------------------------------------------------
# In Hero section, there is:
# <div class="lg:hidden flex items-center gap-2.5 mb-2.5 bg-[#111116]/85 py-1 px-2.5 rounded-full border border-purple-500/30 backdrop-blur-md shadow-md">
# Let's enrich this or add a sleek mobile visual badge
mobile_portrait_markup = """        <!-- Sleek Mobile Engineer Badge & Portrait Banner (Visible on mobile only) -->
        <div class="lg:hidden w-full max-w-sm mb-3">
          <div class="flex items-center gap-3 bg-[#111116]/90 border border-purple-500/30 rounded-2xl p-2.5 backdrop-blur-md shadow-lg">
            <div class="w-14 h-14 rounded-xl overflow-hidden border border-purple-400/50 relative shadow-md flex-shrink-0 bg-[#09090d]">
              <img src="assets/abdou_real_portrait.jpg" alt="Abdou Ali Mousa" class="w-full h-full object-contain object-top" onerror="this.src='assets/hero_architect.jpg'" />
            </div>
            <div class="flex flex-col text-right align-start-dir flex-1 min-w-0">
              <div class="flex items-center justify-between gap-1 mb-0.5">
                <span class="text-xs font-black text-white truncate">عبده علي موسى</span>
                <span class="text-[8.5px] font-mono text-purple-300 bg-purple-950/80 px-1.5 py-0.5 rounded border border-purple-500/30">AI Systems</span>
              </div>
              <p class="text-[10px] text-zinc-300 leading-snug truncate">هندسة المنظومات والذكاء الاصطناعي</p>
              <div class="flex items-center gap-1.5 text-[8.5px] font-mono text-emerald-400 mt-1">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
                <span>Active Engineer & Innovator</span>
              </div>
            </div>
          </div>
        </div>"""

old_mobile_hero_badge = """        <!-- Compact Verification Micro-Chip (Optimized for Mobile single view) -->
        <div class="lg:hidden flex items-center gap-2.5 mb-2.5 bg-[#111116]/85 py-1 px-2.5 rounded-full border border-purple-500/30 backdrop-blur-md shadow-md">
          <div class="w-8 h-8 rounded-full overflow-hidden border border-purple-400/50 relative shadow-sm flex-shrink-0">
            <img src="assets/abdou_real_portrait.jpg" alt="Abdou Ali Mousa" class="w-full h-full object-contain object-top" onerror="this.src='assets/hero_architect.jpg'" />
          </div>
          <div class="flex flex-col text-right align-start-dir">
            <div class="flex items-center gap-1.5">
              <span class="text-[11px] font-black text-white">عبده علي موسى</span>
              <span class="text-[8px] font-mono text-purple-400 bg-purple-950/80 px-1.5 py-0.2 rounded border border-purple-500/30">Verified</span>
            </div>
            <span class="text-[8.5px] text-zinc-400">هندسة المنظومات والذكاء الاصطناعي</span>
          </div>
        </div>"""

if old_mobile_hero_badge in html:
    html = html.replace(old_mobile_hero_badge, mobile_portrait_markup)
else:
    print("Warning: old_mobile_hero_badge not found via exact match")

# ---------------------------------------------------------------------------
# 3. Update Hero Bio text to be strictly personal portfolio / non-salesy
# ---------------------------------------------------------------------------
old_hero_bio = """          <!-- Authentic Focused Bio Paragraph -->
          <p class="text-[11px] sm:text-sm lg:text-base text-zinc-300 max-w-2xl font-normal leading-relaxed mb-2.5 sm:mb-4 px-0.5" data-i18n="hero_bio">
            مسيرة شغف في هندسة الذكاء الاصطناعي والأتمتة، أُسخر فيها التقنية لبناء <strong class="text-white font-bold">أنظمة ذكية تعكس طموحي وشغفي بالابتكار</strong>؛ من أتمتة سير العمل والنماذج المالية، إلى البنية السحابية وأنظمة الإنتاج الرقمي — أُوثق هنا رحلتي كمهندس يعشق تحويل التعقيد إلى إبداع تقني، وأرحب دوماً بتقديم أي استشارات مجانية.
          </p>"""

new_hero_bio = """          <!-- Authentic Focused Bio Paragraph -->
          <p class="text-[11px] sm:text-sm lg:text-base text-zinc-300 max-w-2xl font-normal leading-relaxed mb-2.5 sm:mb-4 px-0.5" data-i18n="hero_bio">
            بورتفوليو هندسي شخصي يوثق مسيرة شغف في تصميم وبناء <strong class="text-white font-bold">المنظومات الذكية، وهندسة الأتمتة والإنتاج الرقمي</strong>؛ من بناء المنصات الشاملة والمحررات المرئية، إلى النمذجة المتقدمة ومعمارية السحابة — سجل حي لإنجازاتي وتجاربي التقنية الحقيقية، مع كامل الترحيب بتبادل الخبرات أو تقديم أي استشارات مجانية لمن يحتاجها.
          </p>"""

html = html.replace(old_hero_bio, new_hero_bio)

# ---------------------------------------------------------------------------
# 4. Update the End CTA Section: Dignified personal CV closing & free consultations
# ---------------------------------------------------------------------------
old_cta_block = """      <!-- Main Strategic Consultation CTA Card -->
      <div class="glass-panel rounded-2xl sm:rounded-3xl p-4 sm:p-8 border border-purple-500/35 shadow-glow-purple-lg relative overflow-hidden">
        <div class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-purple-950/80 border border-purple-400/40 text-purple-300 text-[10.5px] sm:text-xs font-bold mb-2.5">
          <i class="fa-solid fa-sparkles text-purple-400 text-[10px]"></i>
          <span data-i18n="cta_badge">استشارة استراتيجية أولية مجانية</span>
        </div>

        <h2 class="text-base sm:text-2xl lg:text-3xl font-black text-white mb-2 leading-snug" data-i18n="cta_title">
          مستعد لتحويل فكرتك إلى منظومة ذكية خارقة ومضاعفة كفاءة أعمالك؟
        </h2>
        
        <p class="text-[11px] sm:text-sm text-zinc-300 max-w-xl mx-auto leading-relaxed mb-4 sm:mb-6" data-i18n="cta_desc">
          نبني حلولاً رقمية وأنظمة ذكاء اصطناعي تفوق التوقعات، تمنح مشروعك أسبقية تنافسية مطلقة وكفاءة تشغيلية لا تضاهى. دعنا نناقش أهدافك ونرسم معاً معمارية النظام القادم من خلال جلسة استشارية أولية مجانية ومباشرة.
        </p>

        <!-- CTA Buttons -->
        <div class="flex flex-col sm:flex-row items-center justify-center gap-2 w-full max-w-md mx-auto">
          <a href="https://wa.me/201092519210" target="_blank" rel="noopener noreferrer" onclick="triggerHaptic()" class="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-5 py-2.5 sm:py-3 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-black text-xs sm:text-sm shadow-glow-emerald transition-all touch-press">
            <i class="fa-brands fa-whatsapp text-sm sm:text-base"></i>
            <span data-i18n="cta_btn_wa">حجز جلسة استشارية عبر واتساب</span>
          </a>
          <a href="https://t.me/abdou25008" target="_blank" rel="noopener noreferrer" onclick="triggerHaptic()" class="w-full sm:w-auto inline-flex items-center justify-center gap-1.5 px-4 py-2.5 sm:py-3 rounded-xl bg-[#161622] hover:bg-[#201c34] text-zinc-200 hover:text-white font-bold text-xs sm:text-sm border border-white/10 hover:border-sky-500/50 transition-all touch-press">
            <i class="fa-brands fa-telegram text-sky-400 text-sm"></i>
            <span data-i18n="cta_btn_tg">تيليجرام (@abdou25008)</span>
          </a>
        </div>
      </div>"""

new_cta_block = """      <!-- Personal Engineering Legacy & Open Networking Closing Card -->
      <div class="glass-panel rounded-2xl sm:rounded-3xl p-4 sm:p-8 border border-purple-500/30 shadow-glow-purple-lg relative overflow-hidden text-center">
        <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-purple-950/80 border border-purple-400/40 text-purple-300 text-[10.5px] sm:text-xs font-bold mb-3">
          <i class="fa-solid fa-code-commit text-purple-400 text-[11px]"></i>
          <span data-i18n="cta_badge">خاتمة المسيرة وسجل الإنجازات</span>
        </div>

        <h2 class="text-base sm:text-2xl lg:text-3xl font-black text-white mb-2.5 leading-snug" data-i18n="cta_title">
          بناء المنظومات شغف هندسي مستمر وتوثيق دائم للابتكار
        </h2>
        
        <p class="text-[11px] sm:text-sm text-zinc-300 max-w-xl mx-auto leading-relaxed mb-5" data-i18n="cta_desc">
          هذا المعرض ليس منصة لبيع الخدمات، بل هو سجل شخصي وثائقي يجسد مسيرتي في تحويل المفاهيم المعقدة إلى برمجيات حقيقية حية. وإيماناً بأهمية مشاركة المعرفة ونقل الخبرة للمجتمع التقني، يسعدني دوماً تقديم أي استشارات أو مشورات برمجية مجانية لمن يطلبها.
        </p>

        <!-- CTA Buttons -->
        <div class="flex flex-col sm:flex-row items-center justify-center gap-2.5 w-full max-w-md mx-auto">
          <a href="https://wa.me/201092519210" target="_blank" rel="noopener noreferrer" onclick="triggerHaptic()" class="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-5 py-2.5 sm:py-3 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-black text-xs sm:text-sm shadow-glow-emerald transition-all touch-press">
            <i class="fa-brands fa-whatsapp text-sm sm:text-base"></i>
            <span data-i18n="cta_btn_wa">تواصل مباشر عبر واتساب</span>
          </a>
          <a href="https://t.me/abdou25008" target="_blank" rel="noopener noreferrer" onclick="triggerHaptic()" class="w-full sm:w-auto inline-flex items-center justify-center gap-1.5 px-4 py-2.5 sm:py-3 rounded-xl bg-[#161622] hover:bg-[#201c34] text-zinc-200 hover:text-white font-bold text-xs sm:text-sm border border-white/10 hover:border-sky-500/50 transition-all touch-press">
            <i class="fa-brands fa-telegram text-sky-400 text-sm"></i>
            <span data-i18n="cta_btn_tg">تيليجرام التقني (@abdou25008)</span>
          </a>
        </div>
      </div>"""

html = html.replace(old_cta_block, new_cta_block)

# ---------------------------------------------------------------------------
# 5. Update translations dictionary (ar and en) to match the non-salesy tone
# ---------------------------------------------------------------------------
# Replace in translations.ar
html = html.replace('btn_header_cta: "استشارة مجانية",', 'btn_header_cta: "تواصل تقني",')
html = html.replace('btn_header_cta_short: "تواصل",', 'btn_header_cta_short: "تواصل",')

html = html.replace('hero_stamp_text: "• استشارات تقنية • حلول ذكاء اصطناعي • أنظمة فائقة •",', 
                    'hero_stamp_text: "• توثيق هندسي • منظومات ذكية • شغف الابتكار •",')

html = html.replace('serv_title: "كيف نُسهم في تطوير <span class=\'purple-gradient-text\'>وتسريع وتيرة أعمالكم؟</span>",',
                    'serv_title: "شغف بناء المنظومات <span class=\'purple-gradient-text\'>وإتقان الحلول الذكية</span>",')

html = html.replace('cta_badge: "استشارة استراتيجية أولية مجانية",',
                    'cta_badge: "خاتمة المسيرة وسجل الإنجازات",')

html = html.replace('cta_title: "مستعد لتحويل فكرتك إلى منظومة ذكية خارقة ومضاعفة كفاءة أعمالك؟",',
                    'cta_title: "بناء المنظومات شغف هندسي مستمر وتوثيق دائم للابتكار",')

html = html.replace('cta_desc: "نبني حلولاً رقمية وأنظمة ذكاء اصطناعي تفوق التوقعات، تمنح مشروعك أسبقية تنافسية مطلقة وكفاءة تشغيلية لا تضاهى. دعنا نناقش أهدافك ونرسم معاً معمارية النظام القادم من خلال جلسة استشارية أولية مجانية ومباشرة.",',
                    'cta_desc: "هذا المعرض ليس منصة لبيع الخدمات، بل هو سجل شخصي وثائقي يجسد مسيرتي في تحويل المفاهيم المعقدة إلى برمجيات حقيقية حية. وإيماناً بأهمية مشاركة المعرفة ونقل الخبرة للمجتمع التقني، يسعدني دوماً تقديم أي استشارات أو مشورات برمجية مجانية لمن يطلبها.",')

html = html.replace('cta_btn_wa: "حجز جلسة استشارية عبر واتساب",',
                    'cta_btn_wa: "تواصل مباشر عبر واتساب",')

html = html.replace('cta_btn_tg: "تيليجرام (@abdou25008)",',
                    'cta_btn_tg: "تيليجرام التقني (@abdou25008)",')

html = html.replace('footer_location: "جمهورية مصر العربية | استشارات دولية",',
                    'footer_location: "جمهورية مصر العربية | مهندس برمجيات ونظم",')

# Update hero_bio in translations.ar
hero_bio_trans_old = 'hero_bio: "أبني حلولًا تعتمد على الذكاء الاصطناعي والأتمتة لتحويل العمليات المعقدة إلى أنظمة أكثر ذكاءً، كفاءةً وقابليةً للتوسع؛ من أتمتة سير العمل والنماذج المالية والمحاسبية، إلى البنية السحابية وأنظمة الإنتاج الرقمي — أصمم حلولًا تقنية تخدم القرار، الكفاءة، والنمو.",'
hero_bio_trans_new = 'hero_bio: "بورتفوليو هندسي شخصي يوثق مسيرة شغف في تصميم وبناء المنظومات الذكية، وهندسة الأتمتة والإنتاج الرقمي؛ من بناء المنصات الشاملة والمحررات المرئية، إلى النمذجة المتقدمة ومعمارية السحابة — سجل حي لإنجازاتي وتجاربي التقنية الحقيقية، مع كامل الترحيب بتبادل الخبرات أو تقديم أي استشارات مجانية لمن يحتاجها.",'
html = html.replace(hero_bio_trans_old, hero_bio_trans_new)

# Replace in translations.en
html = html.replace('btn_header_cta: "Free Consultation",', 'btn_header_cta: "Get in Touch",')
html = html.replace('cta_badge: "Free Strategic Initial Consultation",', 'cta_badge: "Engineering Legacy & Portfolio Summary",')
html = html.replace('cta_title: "Ready to Transform Your Idea into a Supercharged Intelligent System?",', 
                    'cta_title: "Building Systems is a Continuous Passion & Innovation Journey",')
html = html.replace('cta_desc: "We build digital solutions and AI systems that exceed expectations. Let us discuss your goals and architect the upcoming system through a direct free consultation session.",',
                    'cta_desc: "This portfolio is a personal engineering documentation of my journey turning complex concepts into robust digital platforms. In the spirit of knowledge sharing, I am always happy to offer free technical advice and consultations.",')
html = html.replace('cta_btn_wa: "Book Free Consultation via WhatsApp",', 'cta_btn_wa: "Direct WhatsApp Message",')

# ---------------------------------------------------------------------------
# 6. Ensure Mobile Dock text correctly points to sections and doesn't get overwritten
# ---------------------------------------------------------------------------
html = html.replace('dock_home: "الرئيسية",', 'dock_home: "المهارات",')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html successfully.")
