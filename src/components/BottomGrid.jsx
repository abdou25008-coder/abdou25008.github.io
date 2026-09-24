import React from 'react';
import { CheckCircle2, Gift, MessageCircle, Send, Mail } from 'lucide-react';

export default function BottomGrid() {
  const steps = [
    {
      num: "01",
      title: "الاستكشاف وتحديد المعمارية (Discovery & Architecture)",
      desc: "تحليل متطلبات العمل، وتحديد البنية التحتية، واختيار النماذج والأدوات الأمثل لضمان أعلى أداء وأقل تكلفة تشغيلية."
    },
    {
      num: "02",
      title: "هندسة النماذج والتطوير السريع (Rapid AI Prototyping)",
      desc: "بناء النواة البرمجية، وتدريب الخوارزميات، والربط البرمجي مع واجهات المستخدم التفاعلية من خلال مراحل تسليم أسبوعية واضحة."
    },
    {
      num: "03",
      title: "الاختبار المعياري والتحقق الصارم (Rigorous Benchmarking)",
      desc: "إجراء اختبارات الأحمال القصوى، وفحص دقة إجابات نماذج الذكاء الاصطناعي، وتأمين منافذ الـ API ضد الثغرات."
    },
    {
      num: "04",
      title: "النشر السحابي والمراقبة الحية (Production Deployment)",
      desc: "إطلاق النظام على الخوادم السحابية مع تفعيل لوحات المراقبة اللحظية وخوارزميات الصيانة الوقائية المستمرة."
    }
  ];

  const tools = [
    { name: "Python AI", color: "text-yellow-400" },
    { name: "React / Next", color: "text-cyan-400" },
    { name: "PyTorch", color: "text-orange-500" },
    { name: "FastAPI", color: "text-emerald-400" },
    { name: "Docker", color: "text-blue-400" },
    { name: "PostgreSQL", color: "text-indigo-400" },
    { name: "Redis Cache", color: "text-red-400" },
    { name: "LangChain", color: "text-purple-400" },
    { name: "AWS Cloud", color: "text-amber-500" },
    { name: "Git & CI/CD", color: "text-orange-600" },
    { name: "Linux DevOps", color: "text-zinc-300" },
    { name: "Tailwind CSS", color: "text-teal-400" }
  ];

  return (
    <section id="workflow" className="py-24 relative border-t border-white/5">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 items-start mb-24 text-right">
          
          {/* Workflow (7 cols) */}
          <div className="lg:col-span-7">
            <div className="inline-flex items-center gap-2 text-xs font-bold text-purple-400 tracking-wider uppercase mb-2">
              <span className="w-6 h-[2px] bg-purple-500"></span>
              <span>الانضباط والاحترافية</span>
            </div>
            <h2 className="text-3xl sm:text-4xl font-black text-white mb-8">
              منهجية التنفيذ <span className="text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-purple-600">الهندسية (4 مراحل)</span>
            </h2>

            <div className="space-y-6">
              {steps.map((st, idx) => (
                <div 
                  key={idx}
                  className="bg-[#16161a]/70 rounded-2xl p-6 flex items-start gap-5 border border-white/5 hover:border-purple-500/40 transition-all"
                >
                  <div className="w-12 h-12 rounded-xl bg-purple-950/80 border border-purple-500/40 flex-shrink-0 flex items-center justify-center font-mono font-bold text-purple-300 text-lg">
                    {st.num}
                  </div>
                  <div>
                    <h3 className="text-lg font-bold text-white mb-1.5">{st.title}</h3>
                    <p className="text-zinc-400 text-xs sm:text-sm leading-relaxed">
                      {st.desc}
                    </p>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Tech Stack (5 cols) */}
          <div id="tech-stack" className="lg:col-span-5">
            <div className="inline-flex items-center gap-2 text-xs font-bold text-purple-400 tracking-wider uppercase mb-2">
              <span className="w-6 h-[2px] bg-purple-500"></span>
              <span>الترسانة التقنية</span>
            </div>
            <h2 className="text-3xl sm:text-4xl font-black text-white mb-8">
              الأدوات <span className="text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-purple-600">والتقنيات المعتمدة</span>
            </h2>

            <div className="grid grid-cols-2 sm:grid-cols-3 gap-3.5">
              {tools.map((t, idx) => (
                <div 
                  key={idx}
                  className="bg-[#16161a] border border-[#27272e] rounded-xl p-3.5 flex items-center gap-3 hover:border-purple-500/50 transition-colors"
                >
                  <span className={`w-2 h-2 rounded-full ${t.color.replace('text-', 'bg-')}`}></span>
                  <div className="text-xs font-bold text-zinc-200">{t.name}</div>
                </div>
              ))}
            </div>

            <div className="mt-6 p-6 rounded-2xl bg-purple-950/30 border border-purple-500/30">
              <div className="flex items-center gap-3 mb-2 text-purple-300 font-bold text-sm">
                <CheckCircle2 className="w-5 h-5 text-emerald-400" />
                <span>التزام صارم بالجودة والمواعيد</span>
              </div>
              <p className="text-xs text-zinc-400 leading-relaxed">
                كود نظيف وموثق بالكامل، جاهز للتطوير المستقبلي مع دعم فني مستمر بعد التسليم.
              </p>
            </div>
          </div>

        </div>

        {/* FULL BLEED COLLABORATION BANNER */}
        <div id="contact" className="relative rounded-3xl overflow-hidden p-8 sm:p-14 bg-gradient-to-br from-purple-900 via-purple-950 to-zinc-950 border border-purple-500/40 shadow-2xl shadow-purple-950/80 text-center">
          
          <div className="relative z-10 max-w-3xl mx-auto">
            <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-emerald-950/80 border border-emerald-500/40 text-emerald-300 text-xs font-bold mb-6">
              <Gift className="w-3.5 h-3.5" />
              <span>جلسة استشارية أولية مجانية بالكامل</span>
            </div>

            <h2 className="text-3xl sm:text-5xl font-black text-white leading-tight mb-6">
              هل لدى سيادتكم فكرة مشروع أو رغبة في تطوير أعمالكم بالذكاء الاصطناعي؟
            </h2>
            
            <p className="text-zinc-300 text-sm sm:text-base leading-relaxed mb-8 max-w-2xl mx-auto">
              يشرفني ويسعدني جداً التعاون مع حضرتكم ومناقشة كافة التفاصيل.. خطوة واحدة ونبدأ في تحويل الرؤية إلى واقع استثنائي بأعلى معايير الإتقان، ويسرني تقديم الجلسة الاستشارية الأولى لسيادتكم مجاناً لمناقشة أهدافكم وتقديم أفضل الحلول التقنية.
            </p>

            <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
              <a 
                href="https://wa.me/201092519210" 
                target="_blank" 
                rel="noopener noreferrer" 
                className="w-full sm:w-auto inline-flex items-center justify-center gap-3 px-8 py-4 rounded-2xl bg-emerald-600 hover:bg-emerald-500 text-white font-extrabold text-sm shadow-xl hover:scale-105 transition-all duration-300"
              >
                <MessageCircle className="w-4 h-4" />
                <span>حجز استشارة مجانية عبر واتساب (+20 109 251 9210)</span>
              </a>
              <a 
                href="https://t.me/abdou25008" 
                target="_blank" 
                rel="noopener noreferrer" 
                className="w-full sm:w-auto inline-flex items-center justify-center gap-3 px-7 py-4 rounded-2xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-sm shadow-xl transition-all duration-300"
              >
                <Send className="w-4 h-4" />
                <span>تيليجرام (@abdou25008)</span>
              </a>
              <a 
                href="mailto:abdou25008@gmail.com" 
                className="w-full sm:w-auto inline-flex items-center justify-center gap-3 px-7 py-4 rounded-2xl bg-[#0a0a0c]/80 hover:bg-[#0a0a0c] text-white font-bold text-sm border border-white/20 transition-all duration-300"
              >
                <Mail className="w-4 h-4 text-amber-400" />
                <span>abdou25008@gmail.com</span>
              </a>
            </div>
          </div>

        </div>

      </div>
    </section>
  );
}