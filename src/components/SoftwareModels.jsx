import React from 'react';
import { Truck, Wand2, Rocket, Play, Info, ExternalLink } from 'lucide-react';

export default function SoftwareModels() {
  const models = [
    {
      img: "assets/fintech_model_preview.jpg",
      badge: "نموذج تشغيلي",
      badgeColor: "text-emerald-400 bg-emerald-950/80 border-emerald-500/40",
      title: "نظام الأتمتة والنمذجة المالية التفاعلية",
      desc: "محرك مالي متكامل لتحليل التدفقات النقدية، تقييم المخاطر، وبناء سيناريوهات الموازنات التقديرية بالذكاء الاصطناعي مع لوحات تحكم تفاعلية فورية.",
      tags: ["FinTech", "Power BI", "FastAPI"],
      waText: "استفسار عن نظام النمذجة المالية"
    },
    {
      img: "assets/doc_ai_preview.jpg",
      badge: "ذكاء اصطناعي OCR",
      badgeColor: "text-cyan-400 bg-cyan-950/80 border-cyan-500/40",
      title: "منظومة معالجة المستندات واستخراج البيانات الذكي",
      desc: "أداة ذكية لاستخراج وهيكلة البيانات من الفواتير والعقود والملفات بصيغ PDF/صور وربطها بقواعد البيانات آلياً دون أي تدخل بشري.",
      tags: ["Vision OCR", "LLM Extraction", "Python"],
      waText: "استفسار عن منظومة معالجة المستندات"
    },
    {
      img: "assets/exec_ai_preview.jpg",
      badge: "إدارة استراتيجية",
      badgeColor: "text-amber-400 bg-amber-950/80 border-amber-500/40",
      title: "مساعد القرار الاستراتيجي للمؤسسات",
      desc: "منصة قيادة وتحليلات تنبؤية لكبار المدراء التنفيذيين تجمع بيانات المبيعات والتسويق والتشغيل وتقدم توصيات استراتيجية مدعومة بالبيانات.",
      tags: ["Executive BI", "AI Agents", "Cloud"],
      waText: "استفسار عن مساعد القرار التنفيذي"
    }
  ];

  return (
    <div>
      {/* 1. Live Platforms Section */}
      <section id="platforms" className="py-24 relative bg-[#0d0d10] border-t border-white/5">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          
          <div className="text-center max-w-3xl mx-auto mb-16">
            <div className="inline-flex items-center gap-2 px-4 py-1 rounded-full bg-purple-950/50 border border-purple-500/30 text-purple-300 text-xs font-bold mb-3">
              <Rocket className="w-4 h-4" />
              <span>المنظومات والتطبيقات البرمجية التشغيلية</span>
            </div>
            <h2 className="text-3xl sm:text-5xl font-black text-white mb-4">
              تطبيقات ومنصات حية <span className="text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-purple-600">تقود العمليات في الواقع</span>
            </h2>
            <p className="text-zinc-400 text-sm sm:text-base leading-relaxed">
              نماذج لتطبيقات برمجية ومنصات سحابية متكاملة تخدم آلاف العمليات اليومية بكفاءة مطلقة ودقة متناهية.
            </p>
          </div>

          {/* Platform 1: Logistics */}
          <div className="bg-[#16161a]/70 rounded-3xl p-8 sm:p-10 mb-12 border border-cyan-500/30 relative overflow-hidden group text-right">
            <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
              <div className="lg:col-span-7 flex flex-col">
                <div className="inline-flex items-center gap-2 px-3 py-1 rounded-lg bg-cyan-950/80 border border-cyan-500/40 text-cyan-300 text-xs font-mono mb-4 w-fit">
                  <Truck className="w-3.5 h-3.5" />
                  <span>منظومة لوجستية ذكية متكاملة</span>
                </div>
                <h3 className="text-2xl sm:text-3xl font-black text-white mb-2 group-hover:text-cyan-300 transition-colors">
                  منظومة إدارة اللوجستيات وعمليات الشحن والأسطول والمتجر الذكي
                </h3>
                <span className="text-xs font-mono text-cyan-400 mb-4 block dir-ltr text-right">
                  ElQaed Logistics, Fleet Command & E-Commerce Suite
                </span>
                <p className="text-zinc-300 text-sm leading-relaxed mb-6">
                  تطبيق متكامل لإدارة سلاسل الإمداد، وتتبع الشحنات والأسطول والمناديب في الوقت الفعلي عبر الخريطة، مع ربط مباشر مع المتجر الإلكتروني وإدارة المخازن، ولوحة تحكم مالية دقيقة لحسابات التحصيل اليومي.
                </p>
                <div className="flex flex-wrap gap-4">
                  <a href="https://elqaedtravel-netizen.github.io/logistics/" target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-2.5 px-6 py-3 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-zinc-950 font-bold text-xs shadow-lg shadow-cyan-900/50 transition-all">
                    <Rocket className="w-4 h-4" />
                    <span>تشغيل منظومة اللوجستيات الحية</span>
                    <ExternalLink className="w-3.5 h-3.5" />
                  </a>
                </div>
              </div>
              <div className="lg:col-span-5 rounded-2xl overflow-hidden border border-cyan-500/30 shadow-2xl bg-zinc-950">
                <img src="assets/logistics_preview.jpg" alt="معاينة لوحة تحكم اللوجستيات" className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
              </div>
            </div>
          </div>

          {/* Platform 2: Abdou Studio VO */}
          <div className="bg-[#16161a]/70 rounded-3xl p-8 sm:p-10 border border-purple-500/30 relative overflow-hidden group text-right">
            <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
              <div className="lg:col-span-7 flex flex-col">
                <div className="inline-flex items-center gap-2 px-3 py-1 rounded-lg bg-purple-950/80 border border-purple-500/40 text-purple-300 text-xs font-mono mb-4 w-fit">
                  <Wand2 className="w-3.5 h-3.5" />
                  <span>استوديو صوتي وموسيقي سحابي فائق الجودة</span>
                </div>
                <h3 className="text-2xl sm:text-3xl font-black text-white mb-2 group-hover:text-purple-300 transition-colors">
                  استوديو الذكاء الاصطناعي الصوتي والموسيقي المتكامل
                </h3>
                <span className="text-xs font-mono text-purple-400 mb-4 block dir-ltr text-right">
                  Abdou Studio VO & AI Music Synthesis DAW
                </span>
                <p className="text-zinc-300 text-sm leading-relaxed mb-6">
                  منصة برمجية متطورة لتوليد الفويس أوفر (Voiceover) الواقعي البشري بمختلف اللهجات واللغات، وتأليف وهندسة الموسيقى والمؤثرات الصوتية التوليدية بدقة استوديو 48kHz بمعالجة سحابية فورية.
                </p>
                <div className="flex flex-wrap gap-4">
                  <a href="https://abdou-studio-vo.ai.studio" target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-2.5 px-6 py-3 rounded-xl bg-gradient-to-r from-purple-600 to-purple-800 text-white font-bold text-xs shadow-lg shadow-purple-950/50 transition-all border border-purple-400/30">
                    <Play className="w-4 h-4" />
                    <span>تشغيل استوديو الصوت والموسيقى</span>
                    <ExternalLink className="w-3.5 h-3.5" />
                  </a>
                </div>
              </div>
              <div className="lg:col-span-5 rounded-2xl overflow-hidden border border-purple-500/30 shadow-2xl bg-zinc-950">
                <img src="assets/voice_studio_preview.jpg" alt="معاينة استوديو الصوت والموسيقى" className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
              </div>
            </div>
          </div>

        </div>
      </section>

      {/* 2. Software Models Grid */}
      <section id="software-models" className="py-24 relative bg-[#0a0a0c]">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center max-w-3xl mx-auto mb-16">
            <h2 className="text-3xl sm:text-5xl font-black text-white mb-4">
              نماذج ذكية <span className="text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-purple-600">وحلول برمجية متخصصة</span>
            </h2>
            <p className="text-zinc-400 text-sm sm:text-base leading-relaxed">
              معرض لأحدث النماذج البرمجية، محركات الأتمتة المالية، وأدوات تحليل البيانات الذكية المصممة لتمكين المؤسسات.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {models.map((m, idx) => (
              <div key={idx} className="bg-[#16161a]/80 rounded-3xl overflow-hidden border border-[#27272e] hover:border-purple-500/50 transition-all duration-300 flex flex-col group text-right">
                <div className="relative h-52 w-full overflow-hidden bg-zinc-950">
                  <img src={m.img} alt={m.title} className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
                  <div className="absolute inset-0 bg-gradient-to-t from-[#16161a] via-transparent to-transparent"></div>
                  <div className={`absolute top-4 right-4 border px-3 py-1 rounded-lg text-xs font-mono backdrop-blur-md ${m.badgeColor}`}>
                    {m.badge}
                  </div>
                </div>

                <div className="p-6 flex-1 flex flex-col justify-between">
                  <div>
                    <h3 className="text-lg font-bold text-white mb-2 group-hover:text-purple-300 transition-colors">
                      {m.title}
                    </h3>
                    <p className="text-zinc-400 text-xs leading-relaxed mb-6">
                      {m.desc}
                    </p>
                  </div>

                  <div>
                    <div className="flex flex-wrap gap-1.5 mb-5">
                      {m.tags.map((t, i) => (
                        <span key={i} className="text-[11px] font-mono bg-white/5 text-zinc-300 px-2.5 py-0.5 rounded-md border border-white/5">
                          {t}
                        </span>
                      ))}
                    </div>
                    <a href={`https://wa.me/201092519210?text=${encodeURIComponent(m.waText)}`} target="_blank" rel="noopener noreferrer" className="w-full block text-center py-2.5 rounded-xl bg-purple-950/70 hover:bg-purple-900 border border-purple-500/40 text-purple-200 text-xs font-bold transition-all">
                      <Info className="w-3.5 h-3.5 inline ml-1" /> طلب عرض توضيحي للنموذج
                    </a>
                  </div>
                </div>
              </div>
            ))}
          </div>

        </div>
      </section>
    </div>
  );
}