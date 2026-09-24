import React from 'react';
import { Youtube, Instagram, Share2, Facebook, MessageCircle, Send, Globe } from 'lucide-react';

export default function MediaNetwork() {
  const shorts = [
    {
      img: "assets/media_network.jpg",
      cat: "AI Shorts #01",
      catColor: "text-purple-300 bg-purple-950/80 border-purple-500/40",
      views: "+2.5M",
      title: "آفاق الذكاء الاصطناعي والتقنية",
      desc: "مقاطع قصيرة تشرح أحدث أدوات ونماذج الذكاء الاصطناعي وكيفية توظيفها في تحويل الأعمال.",
      links: [
        { label: "شورتس", url: "https://youtube.com" },
        { label: "تيك توك", url: "https://tiktok.com" },
        { label: "ريلز", url: "https://instagram.com" }
      ]
    },
    {
      img: "assets/fintech_model_preview.jpg",
      cat: "Economy #02",
      catColor: "text-cyan-300 bg-cyan-950/80 border-cyan-500/40",
      views: "+3.8M",
      title: "الاقتصاد والتحليلات العالمية",
      desc: "تحليل الصراعات الاقتصادية، حركة الأسواق المالية، وحقائق التجارة الدولية بأسلوب بصري تفاعلي.",
      links: [
        { label: "شورتس", url: "https://youtube.com" },
        { label: "فيسبوك", url: "https://facebook.com" }
      ]
    },
    {
      img: "assets/exec_ai_preview.jpg",
      cat: "Automation #03",
      catColor: "text-purple-300 bg-purple-950/80 border-purple-500/40",
      views: "+1.9M",
      title: "التحول الرقمي وأتمتة الأعمال",
      desc: "شروحات سريعة توضح كواليس ربط الأنظمة السحابية وأتمتة المهام اليومية في الشركات.",
      links: [
        { label: "شورتس", url: "https://youtube.com" },
        { label: "ريلز", url: "https://instagram.com" }
      ]
    },
    {
      img: "assets/voice_studio_preview.jpg",
      cat: "Audio VO #04",
      catColor: "text-pink-300 bg-pink-950/80 border-pink-500/40",
      views: "+2.2M",
      title: "معمل الصوت والإنتاج التوليدي",
      desc: "استعراض نماذج الفويس أوفر الواقعي، الإلقاء الوثائقي، والموسيقى التوليدية بالذكاء الاصطناعي.",
      links: [
        { label: "شورتس", url: "https://youtube.com" },
        { label: "ساوند", url: "https://soundcloud.com" }
      ]
    }
  ];

  return (
    <section id="media-network" className="py-24 relative bg-[#0e0e12] border-t border-white/5">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Header */}
        <div className="flex flex-col md:flex-row md:items-end justify-between mb-16 gap-6 text-right">
          <div>
            <div className="inline-flex items-center gap-2 text-xs font-bold text-amber-400 tracking-wider uppercase mb-2">
              <Globe className="w-3.5 h-3.5" />
              <span>الشبكة الإعلامية العالمية</span>
            </div>
            <h2 className="text-3xl sm:text-5xl font-black text-white">
              شبكة القنوات الرقمية <span className="text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-purple-600">والمحتوى القصير (Shorts)</span>
            </h2>
          </div>
          <p className="text-zinc-400 text-xs sm:text-sm max-w-md">
            إدارة وإنتاج محتوى متكامل عبر 4 قنوات شورتس دولية تعتمد على الذكاء الاصطناعي التوليدي لسرد قصص التاريخ والاقتصاد والتقنية لملايين المشاهدين.
          </p>
        </div>

        {/* 9:16 Shorts Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-12">
          {shorts.map((card, idx) => (
            <div 
              key={idx}
              className="group relative rounded-3xl overflow-hidden bg-[#16161a] border border-[#27272e] hover:border-purple-500/60 transition-all duration-500 aspect-[9/16] flex flex-col justify-between p-6 shadow-lg text-right"
            >
              <div className="absolute inset-0 z-0">
                <img 
                  src={card.img} 
                  alt={card.title}
                  className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700 opacity-60" 
                />
                <div className="absolute inset-0 bg-gradient-to-t from-[#0a0a0c] via-[#0a0a0c]/60 to-transparent"></div>
              </div>

              <div className="relative z-10 flex items-center justify-between">
                <span className={`text-xs font-mono font-bold px-2.5 py-1 rounded-full border ${card.catColor}`}>
                  {card.cat}
                </span>
                <span className="text-xs font-mono font-bold bg-black/60 px-2.5 py-1 rounded-full text-zinc-300 backdrop-blur-md border border-white/10">
                  {card.views}
                </span>
              </div>

              <div className="relative z-10">
                <h3 className="text-base font-extrabold text-white leading-snug mb-1.5 group-hover:text-purple-200 transition-colors">
                  {card.title}
                </h3>
                <p className="text-xs text-zinc-400 line-clamp-2 mb-3">
                  {card.desc}
                </p>
                <div className="flex items-center gap-2 pt-2 border-t border-white/10">
                  {card.links.map((lnk, i) => (
                    <a 
                      key={i} 
                      href={lnk.url} 
                      target="_blank" 
                      rel="noopener noreferrer" 
                      className="text-[11px] text-zinc-300 hover:text-purple-400 font-mono"
                    >
                      {lnk.label}
                    </a>
                  ))}
                </div>
              </div>
            </div>
          ))}
        </div>

        {/* Hub Bar */}
        <div className="p-6 rounded-2xl bg-[#16161a]/60 border border-white/5 flex flex-col sm:flex-row items-center justify-between gap-4">
          <div className="flex items-center gap-3 text-sm font-bold text-zinc-300">
            <Globe className="w-4 h-4 text-amber-400" />
            <span>تابع وتواصل عبر كافة منصات السوشيال ميديا الرسمية:</span>
          </div>
          <div className="flex items-center gap-3">
            <a href="https://wa.me/201092519210" target="_blank" rel="noopener noreferrer" className="w-10 h-10 rounded-xl bg-emerald-950/60 border border-emerald-500/40 flex items-center justify-center text-emerald-400 hover:bg-emerald-600 hover:text-white transition-colors" title="WhatsApp"><MessageCircle className="w-4 h-4" /></a>
            <a href="https://t.me/abdou25008" target="_blank" rel="noopener noreferrer" className="w-10 h-10 rounded-xl bg-cyan-950/60 border border-cyan-500/40 flex items-center justify-center text-cyan-400 hover:bg-cyan-600 hover:text-white transition-colors" title="Telegram"><Send className="w-4 h-4" /></a>
            <a href="https://youtube.com" target="_blank" rel="noopener noreferrer" className="w-10 h-10 rounded-xl bg-red-950/60 border border-red-500/40 flex items-center justify-center text-red-400 hover:bg-red-600 hover:text-white transition-colors" title="YouTube"><Youtube className="w-4 h-4" /></a>
            <a href="https://instagram.com" target="_blank" rel="noopener noreferrer" className="w-10 h-10 rounded-xl bg-pink-950/60 border border-pink-500/40 flex items-center justify-center text-pink-400 hover:bg-pink-600 hover:text-white transition-colors" title="Instagram"><Instagram className="w-4 h-4" /></a>
            <a href="https://facebook.com" target="_blank" rel="noopener noreferrer" className="w-10 h-10 rounded-xl bg-blue-950/60 border border-blue-500/40 flex items-center justify-center text-blue-400 hover:bg-blue-600 hover:text-white transition-colors" title="Facebook"><Facebook className="w-4 h-4" /></a>
          </div>
        </div>

      </div>
    </section>
  );
}