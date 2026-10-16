import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Let's replace the mobile badge with a more luxurious, prominent mobile hero profile
old_snippet = """          <!-- Verification Micro-Chip (Optimized for minimal vertical scroll on phone) -->
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

new_snippet = """          <!-- Verification Card (Rich & prominent on mobile) -->
          <div class="lg:hidden w-full max-w-sm mb-3">
            <div class="flex items-center gap-3 bg-[#111116]/90 border border-purple-500/35 rounded-2xl p-2.5 backdrop-blur-md shadow-lg">
              <div class="w-14 h-14 rounded-xl overflow-hidden border border-purple-400/50 relative shadow-md flex-shrink-0 bg-[#09090d]">
                <img src="assets/abdou_real_portrait.jpg" alt="Abdou Ali Mousa" class="w-full h-full object-contain object-top" onerror="this.src='assets/hero_architect.jpg'" />
              </div>
              <div class="flex flex-col text-right align-start-dir flex-1 min-w-0">
                <div class="flex items-center justify-between gap-1 mb-0.5">
                  <span class="text-xs font-black text-white truncate">عبده علي موسى</span>
                  <span class="text-[8.5px] font-mono text-purple-300 bg-purple-950/80 px-1.5 py-0.5 rounded border border-purple-500/30">AI Systems</span>
                </div>
                <p class="text-[10px] text-zinc-300 leading-snug truncate">هندسة وتكامل خوارزميات الذكاء الاصطناعي</p>
                <div class="flex items-center gap-1.5 text-[8.5px] font-mono text-emerald-400 mt-1">
                  <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
                  <span>Active Engineer & Innovator</span>
                </div>
              </div>
            </div>
          </div>"""

if old_snippet in html:
    html = html.replace(old_snippet, new_snippet)
    print("Replaced mobile hero badge successfully!")
else:
    print("Could not find exact old_snippet")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
