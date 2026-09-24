import React from 'react';

export default function Stats() {
  const stats = [
    {
      value: "04",
      label: "قنوات شورتس دولية",
      sub: "شبكة إعلامية ذكية ذاتية القيادة"
    },
    {
      value: "+10M",
      label: "مشاهدة وتفاعل عالمي",
      sub: "محتوى وثائقي واقتصادي وتقني رائد"
    },
    {
      value: "100%",
      label: "أتمتة متكاملة للعمليات",
      sub: "رفع كفاءة الأداء وتسريع القرار"
    },
    {
      value: "24/7",
      label: "جاهزية واستقرار سحابي",
      sub: "أنظمة وتشغيل مستمر بلا انقطاع"
    }
  ];

  return (
    <section id="metrics" className="relative py-12 border-y border-white/5 bg-[#0e0e12]">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-2 md:grid-cols-4 gap-6 sm:gap-8">
          {stats.map((s, idx) => (
            <div 
              key={idx} 
              className="flex flex-col items-center md:items-start text-center md:text-right p-4 rounded-2xl bg-[#16161a]/40 border border-white/5 hover:border-purple-500/30 transition-all duration-300"
            >
              <span className="text-3xl sm:text-4xl lg:text-5xl font-black text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-white font-mono mb-1">
                {s.value}
              </span>
              <span className="text-sm font-bold text-zinc-200 mb-0.5">{s.label}</span>
              <span className="text-xs text-zinc-500">{s.sub}</span>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}