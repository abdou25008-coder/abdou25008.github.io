import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Let's find the whole div with regex
pattern = r'<!-- Mobile-Only Compact Avatar Badge.*?</div>\s*</div>\s*</div>'
match = re.search(pattern, html, flags=re.DOTALL)
if match:
    print("Found match:")
    print(match.group(0))
    
    new_badge = """<!-- Mobile-Only Rich Engineer Profile Card (Visible on mobile only) -->
          <div class="lg:hidden w-full max-w-sm mb-3">
            <div class="flex items-center gap-3 bg-[#111116]/90 border border-purple-500/35 rounded-2xl p-2.5 backdrop-blur-md shadow-lg">
              <div class="w-14 h-14 rounded-xl overflow-hidden border border-purple-400/50 relative shadow-md flex-shrink-0 bg-[#09090d]">
                <img src="assets/abdou_real_portrait.jpg" alt="Abdou Ali Mousa" class="w-full h-full object-contain object-top" onerror="this.src='assets/hero_architect.jpg'" />
              </div>
              <div class="flex flex-col text-right align-start-dir flex-1 min-w-0">
                <div class="flex items-center justify-between gap-1 mb-0.5">
                  <span class="text-xs font-black text-white truncate">عبده علي موسى</span>
                  <span class="text-[8.5px] font-mono text-purple-300 bg-purple-950/80 px-1.5 py-0.5 rounded border border-purple-500/30">Verified Pro</span>
                </div>
                <p class="text-[10px] text-zinc-300 leading-snug truncate">هندسة المنظومات والذكاء الاصطناعي</p>
                <div class="flex items-center gap-1.5 text-[8.5px] font-mono text-emerald-400 mt-1">
                  <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
                  <span>Active Engineer & Innovator</span>
                </div>
              </div>
            </div>
          </div>"""
          
    html = html.replace(match.group(0), new_badge)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Successfully upgraded mobile badge!")
else:
    print("Pattern match not found.")
