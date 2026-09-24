import React from 'react';
import { Brain, TrendingUp, Cloud, Sparkles } from 'lucide-react';

export default function Services() {
  const services = [
    {
      num: "01",
      icon: <Brain className="w-7 h-7" />,
      title: "أتمتة الأعمال بالذكاء الاصطناعي المستقل (Autonomous AI)",
      desc: "تصميم وبناء مسارات عمل ذكية ذاتية القيادة (AI Agents) لتنفيذ المهام المعقدة، وخدمة العملاء، وتحليل البيانات بأعلى مستويات الدقة والسرعة.",
      tags: ["وكلاء ذكاء اصطناعي متعدد المهام", "تكامل النماذج اللغوية المتطورة", "LangChain / RAG"]
    },
    {
      num: "02",
      icon: <TrendingUp className="w-7 h-7" />,
      title: "الهندسة المالية والنمذجة الاستراتيجية (FinTech & BI)",
      desc: "تصميم النماذج المحاسبية ولوحات التحكم التفاعلية (Power BI Dashboards) لتزويد سيادتكم برؤى مالية فورية وتوقعات التدفقات النقدية لدعم اتخاذ القرارات الصائبة.",
      tags: ["تخطيط مالي وتوقعات التدفقات", "لوحات قياس الأداء اللحظية", "Power BI / FastAPI"]
    },
    {
      num: "03",
      icon: <Cloud className="w-7 h-7" />,
      title: "البنية التحتية السحابية وتكامل البرمجيات (Cloud & APIs)",
      desc: "ربط الأنظمة السحابية والـ APIs المختلفة، وبناء منصات ويب متقدمة تتسم بالسرعة الفائقة والأمان الموثوق لدعم نمو وتوسع أعمالكم بلا انقطاع.",
      tags: ["منصات سحابية آمنة 100%", "معمارية برمجية قابلة للتوسع", "Docker / DevOps"]
    },
    {
      num: "04",
      icon: <Sparkles className="w-7 h-7" />,
      title: "استوديوهات الصوت التوليدي وصناعة المحتوى الرقمي",
      desc: "بناء محركات توليد الفويس أوفر البشري والموسيقى التصويرية بالذكاء الاصطناعي، وإدارة شبكات المحتوى الرقمي لخدمة ملايين المشاهدين.",
      tags: ["Voice Synthesis DAW", "إنتاج شورتس وميديا", "Whisper & Neural TTS"]
    }
  ];

  return (
    <section id="services" className="py-24 relative">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Header */}
        <div className="flex flex-col md:flex-row md:items-end justify-between mb-16 gap-6 text-right">
          <div>
            <div className="inline-flex items-center gap-2 text-xs font-bold text-purple-400 tracking-wider uppercase mb-2">
              <span className="w-6 h-[2px] bg-purple-500"></span>
              <span>مجالات التميز والخدمات الهندسية</span>
            </div>
            <h2 className="text-3xl sm:text-5xl font-black text-white">
              كيف نُسهم في تطوير <span className="text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-purple-600">وتسريع وتيرة أعمالكم؟</span>
            </h2>
          </div>
          <p className="text-zinc-400 text-sm max-w-md">
            نُحوّل التحديات المعقدة إلى منظومات ذكية ومستقرة تضمن لسيادتكم أعلى درجات الكفاءة التشغيلية والنمو المستدام.
          </p>
        </div>

        {/* Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {services.map((srv, idx) => (
            <div 
              key={idx}
              className="bg-[#16161a]/70 backdrop-blur-md rounded-3xl p-8 relative overflow-hidden group border border-white/5 hover:border-purple-500/40 transition-all duration-300 text-right"
            >
              <div className="absolute top-4 left-6 text-6xl font-black text-white/[0.03] group-hover:text-purple-500/10 font-mono transition-colors">
                {srv.num}
              </div>
              <div className="w-14 h-14 rounded-2xl bg-purple-950/80 border border-purple-500/40 flex items-center justify-center text-purple-400 mb-6 shadow-lg shadow-purple-950/60 group-hover:scale-110 transition-transform">
                {srv.icon}
              </div>
              <h3 className="text-xl font-bold text-white mb-3 group-hover:text-purple-300 transition-colors">
                {srv.title}
              </h3>
              <p className="text-zinc-400 text-sm leading-relaxed mb-6">
                {srv.desc}
              </p>
              <div className="flex flex-wrap gap-2 pt-4 border-t border-white/5">
                {srv.tags.map((t, i) => (
                  <span key={i} className="text-[11px] font-mono px-3 py-1 rounded-full bg-white/5 text-zinc-300 border border-white/5">
                    {t}
                  </span>
                ))}
              </div>
            </div>
          ))}
        </div>

      </div>
    </section>
  );
}