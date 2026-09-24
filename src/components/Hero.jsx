import React from 'react';
import { motion } from 'framer-motion';
import { Layers, MessageSquare, Sparkles } from 'lucide-react';

export default function Hero() {
  return (
    <section className="relative min-h-screen pt-32 pb-20 flex items-center justify-center overflow-hidden">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-8 items-center">
          
          {/* Right Column: Hero Content (RTL) */}
          <motion.div 
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, ease: "easeOut" }}
            className="lg:col-span-7 flex flex-col items-start text-right z-10"
          >
            {/* Status Pill */}
            <div className="inline-flex items-center gap-2.5 px-4 py-1.5 rounded-full bg-purple-950/60 border border-purple-500/30 text-purple-300 text-xs font-semibold mb-4 shadow-lg shadow-purple-950/50 backdrop-blur-md">
              <span className="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
              <span>نشط ومتاح حالياً للتعاقدات الخاصة والاستشارات التقنية</span>
            </div>

            <div className="flex items-center gap-3 mb-3">
              <span className="text-xs sm:text-sm font-mono font-bold text-purple-300 bg-purple-950/80 px-3 py-1 rounded-lg border border-purple-500/30">
                Abdou Ali Mousa // مهندس أنظمة وذكاء اصطناعي
              </span>
            </div>

            {/* Massive Headline */}
            <h1 className="text-4xl sm:text-6xl xl:text-7xl font-black tracking-tight text-white leading-[1.2] mb-4">
              أحوّل التعقيد إلى
              <br />
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-purple-400 via-purple-300 to-purple-600">
                أنظمة ذكية فائقة.
              </span>
            </h1>

            {/* Cursive Accent */}
            <div className="flex items-center gap-3 mb-6">
              <span className="text-2xl sm:text-3xl text-purple-400 font-serif italic">
                بورتفوليو الأنظمة والأتمتة والإنتاج الرقمي 2025
              </span>
              <div className="h-[1px] w-20 bg-gradient-to-l from-purple-500 to-transparent"></div>
            </div>

            {/* Exact Bio */}
            <p className="text-base sm:text-lg text-zinc-300 max-w-2xl font-normal leading-relaxed mb-6">
              أبني حلولًا تعتمد على الذكاء الاصطناعي والأتمتة لتحويل العمليات المعقدة إلى <strong className="text-white font-bold">أنظمة أكثر ذكاءً، كفاءةً وقابليةً للتوسع</strong>؛ من أتمتة سير العمل والنماذج المالية والمحاسبية، إلى البنية السحابية وأنظمة الإنتاج الرقمي — أصمم حلولًا تقنية تخدم <strong className="text-purple-300 font-bold">القرار، الكفاءة، والنمو</strong>.
            </p>

            {/* Core Tags */}
            <div className="flex flex-wrap gap-2 mb-8 text-xs font-mono text-zinc-400">
              <span className="bg-white/5 border border-white/10 px-3 py-1 rounded-full">AI Multi-Agents</span>
              <span className="bg-white/5 border border-white/10 px-3 py-1 rounded-full">Autonomous Automation</span>
              <span className="bg-white/5 border border-white/10 px-3 py-1 rounded-full">FinTech & BI Dashboards</span>
              <span className="bg-white/5 border border-white/10 px-3 py-1 rounded-full">Voice & Music DAW</span>
            </div>

            {/* CTAs */}
            <div className="flex flex-wrap items-center gap-4 w-full sm:w-auto mb-10">
              <a 
                href="#platforms" 
                className="w-full sm:w-auto inline-flex items-center justify-center gap-3 px-8 py-4 rounded-2xl bg-gradient-to-r from-purple-600 to-purple-800 hover:from-purple-500 hover:to-purple-700 text-white font-bold text-sm shadow-lg shadow-purple-600/40 hover:shadow-purple-500/60 transition-all duration-300 border border-purple-400/40"
              >
                <span>استكشف المنظومات والنماذج</span>
                <Layers className="w-5 h-5" />
              </a>
              <a 
                href="https://wa.me/201092519210" 
                target="_blank" 
                rel="noopener noreferrer"
                className="w-full sm:w-auto inline-flex items-center justify-center gap-3 px-8 py-4 rounded-2xl bg-[#16161a] hover:bg-[#1f1f26] text-zinc-200 hover:text-white font-bold text-sm border border-[#27272e] hover:border-emerald-500/50 transition-all duration-300"
              >
                <MessageSquare className="w-5 h-5 text-emerald-400" />
                <span>محادثة واتساب (+20 109 251 9210)</span>
              </a>
            </div>

            {/* Code Snippet Badge */}
            <div className="w-full max-w-lg bg-[#121215]/90 border border-[#27272e] rounded-xl p-3.5 flex items-center justify-between font-mono text-xs text-zinc-400 backdrop-blur-md">
              <div className="flex items-center gap-2">
                <span className="w-2.5 h-2.5 rounded-full bg-red-500/80"></span>
                <span className="w-2.5 h-2.5 rounded-full bg-amber-500/80"></span>
                <span className="w-2.5 h-2.5 rounded-full bg-emerald-500/80"></span>
                <span className="text-zinc-500 mr-2">|</span>
                <span className="text-purple-300 font-semibold">sys.architect("Abdou Ali Mousa")</span>
              </div>
              <div className="text-zinc-400 truncate dir-ltr font-mono">
                <span className="text-zinc-500">deploy:</span> <span className="text-emerald-400">"Autonomous_Active"</span>
              </div>
            </div>

          </motion.div>

          {/* Left Column: Portrait & Badge */}
          <motion.div 
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.8, delay: 0.2 }}
            className="lg:col-span-5 relative flex items-center justify-center"
          >
            <div className="relative w-full max-w-md aspect-[4/5] rounded-3xl p-[2px] bg-gradient-to-b from-purple-500/60 via-purple-800/30 to-zinc-900 shadow-2xl shadow-purple-950/80 group">
              
              <div className="relative w-full h-full bg-[#0a0a0c] rounded-[22px] overflow-hidden">
                <img 
                  src="assets/abdou_real_portrait.jpg" 
                  alt="Abdou Ali Mousa" 
                  className="w-full h-full object-cover object-top filter grayscale contrast-110 brightness-95 group-hover:grayscale-0 group-hover:scale-105 transition-all duration-700"
                  onError={(e) => { e.currentTarget.src = 'assets/hero_architect.jpg'; }}
                />

                <div className="absolute inset-0 bg-gradient-to-t from-[#0a0a0c] via-transparent to-transparent opacity-90"></div>
                <div className="absolute inset-0 bg-purple-950/20 mix-blend-color"></div>

                <div className="absolute top-4 left-4 bg-[#0a0a0c]/80 border border-purple-500/40 rounded-xl px-3 py-1.5 backdrop-blur-md text-[11px] font-mono text-purple-300">
                  <span>AI_ARCHITECT // 2025</span>
                </div>

                <div className="absolute bottom-4 right-4 left-4 bg-[#121216]/90 border border-white/10 rounded-2xl p-4 backdrop-blur-md text-right">
                  <div className="flex items-center justify-between mb-1">
                    <h3 className="font-bold text-white text-base">عبده علي موسى | Abdou Ali</h3>
                    <span className="text-xs font-mono text-purple-400 bg-purple-950/80 px-2 py-0.5 rounded-md border border-purple-500/30">Verified Engineer</span>
                  </div>
                  <p className="text-xs text-zinc-400 leading-tight">
                    أحوّل التعقيد إلى أنظمة ذكية، أتمتة الأعمال، والإنتاج الرقمي
                  </p>
                </div>
              </div>

              {/* Rotating Circular Stamp Badge */}
              <div className="absolute -top-7 -right-7 w-28 h-28 sm:w-32 sm:h-32 rounded-full bg-[#0a0a0c] border-2 border-purple-500/60 p-1.5 shadow-2xl shadow-purple-900/80 z-20 flex items-center justify-center cursor-pointer group/stamp">
                <svg className="w-full h-full animate-[spin_20s_linear_infinite]" viewBox="0 0 100 100">
                  <path id="heroCirclePath" d="M 50, 50 m -37, 0 a 37,37 0 1,1 74,0 a 37,37 0 1,1 -74,0" fill="transparent" />
                  <text className="text-[8px] font-extrabold fill-purple-300 tracking-widest uppercase">
                    <textPath href="#heroCirclePath" startOffset="0%">
                      • استشارات تقنية • حلول ذكاء اصطناعي • أنظمة فائقة •
                    </textPath>
                  </text>
                </svg>

                <div className="absolute w-10 h-10 rounded-full bg-purple-900/60 border border-purple-400/50 flex items-center justify-center text-purple-300 group-hover/stamp:scale-110 transition-transform">
                  <Sparkles className="w-5 h-5 text-purple-300" />
                </div>
              </div>

            </div>
          </motion.div>

        </div>
      </div>
    </section>
  );
}