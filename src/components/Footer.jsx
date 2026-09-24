import React from 'react';
import { MessageCircle, Send, Github, Youtube, Mail, MapPin } from 'lucide-react';

export default function Footer() {
  return (
    <footer className="pt-20 pb-12 bg-[#08080a] border-t border-white/5 relative text-right">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <div className="grid grid-cols-1 md:grid-cols-12 gap-12 pb-16 border-b border-white/5">
          
          {/* Brand Col */}
          <div className="md:col-span-5 flex flex-col items-start">
            <div className="flex items-center gap-3 mb-4">
              <div className="w-10 h-10 rounded-xl bg-purple-600 flex items-center justify-center font-black text-lg text-white">
                AA
              </div>
              <div>
                <span className="font-extrabold text-lg text-white block">Abdou Ali Mousa</span>
                <span className="text-xs text-zinc-400 font-mono">AI & Digital Systems Engineer</span>
              </div>
            </div>

            <p className="text-zinc-400 text-xs sm:text-sm leading-relaxed mb-6 max-w-sm">
              أحوّل التعقيد إلى أنظمة ذكية، أتمتة مسارات العمل، النمذجة المالية الاستراتيجية، وإدارة شبكة الإنتاج الإعلامي والقنوات الدولية.
            </p>

            <div className="flex items-center gap-3">
              <a href="https://wa.me/201092519210" target="_blank" rel="noopener noreferrer" className="w-10 h-10 rounded-xl bg-[#16161a] border border-[#27272e] flex items-center justify-center text-zinc-400 hover:text-emerald-400 hover:border-emerald-500 transition-colors" aria-label="WhatsApp">
                <MessageCircle className="w-4 h-4" />
              </a>
              <a href="https://t.me/abdou25008" target="_blank" rel="noopener noreferrer" class="w-10 h-10 rounded-xl bg-[#16161a] border border-[#27272e] flex items-center justify-center text-zinc-400 hover:text-cyan-400 hover:border-cyan-500 transition-colors" aria-label="Telegram">
                <Send className="w-4 h-4" />
              </a>
              <a href="https://github.com/abdou25008-coder" target="_blank" rel="noopener noreferrer" className="w-10 h-10 rounded-xl bg-[#16161a] border border-[#27272e] flex items-center justify-center text-zinc-400 hover:text-white hover:border-purple-500 transition-colors" aria-label="GitHub">
                <Github className="w-4 h-4" />
              </a>
              <a href="https://youtube.com" target="_blank" rel="noopener noreferrer" className="w-10 h-10 rounded-xl bg-[#16161a] border border-[#27272e] flex items-center justify-center text-zinc-400 hover:text-red-400 hover:border-red-500 transition-colors" aria-label="YouTube">
                <Youtube className="w-4 h-4" />
              </a>
              <a href="mailto:abdou25008@gmail.com" className="w-10 h-10 rounded-xl bg-[#16161a] border border-[#27272e] flex items-center justify-center text-zinc-400 hover:text-amber-400 hover:border-amber-500 transition-colors" aria-label="Email">
                <Mail className="w-4 h-4" />
              </a>
            </div>
          </div>

          {/* Quick Links */}
          <div className="md:col-span-3">
            <h4 className="text-sm font-bold text-white mb-4 uppercase tracking-wider">روابط التنقل السريع</h4>
            <ul className="space-y-2.5 text-xs text-zinc-400">
              <li><a href="#services" className="hover:text-purple-400 transition-colors">الخدمات الهندسية</a></li>
              <li><a href="#platforms" className="hover:text-purple-400 transition-colors">المنظومات الحية المشغلة</a></li>
              <li><a href="#software-models" className="hover:text-purple-400 transition-colors">النماذج والمشاريع التقنية</a></li>
              <li><a href="#media-network" className="hover:text-purple-400 transition-colors">الشبكة الإعلامية (Shorts)</a></li>
              <li><a href="#metrics" className="hover:text-purple-400 transition-colors">مؤشرات النجاح والأرقام</a></li>
            </ul>
          </div>

          {/* Direct Contact */}
          <div className="md:col-span-4">
            <h4 className="text-sm font-bold text-white mb-4 uppercase tracking-wider">بيانات الاتصال والتواصل</h4>
            <div className="space-y-3 text-xs text-zinc-300 font-mono">
              <div className="flex items-center gap-3 p-3 rounded-xl bg-[#121215] border border-white/5">
                <MessageCircle className="w-4 h-4 text-emerald-400" />
                <a href="https://wa.me/201092519210" target="_blank" rel="noopener noreferrer" className="hover:text-emerald-300 transition-colors">+20 109 251 9210</a>
              </div>
              <div className="flex items-center gap-3 p-3 rounded-xl bg-[#121215] border border-white/5">
                <Mail className="w-4 h-4 text-purple-400" />
                <a href="mailto:abdou25008@gmail.com" className="hover:text-purple-300 transition-colors">abdou25008@gmail.com</a>
              </div>
              <div className="flex items-center gap-3 p-3 rounded-xl bg-[#121215] border border-white/5">
                <MapPin className="w-4 h-4 text-cyan-400" />
                <span className="font-sans">جمهورية مصر العربية | متاح للتعاقد والاستشارات الدولية</span>
              </div>
            </div>
          </div>

        </div>

        {/* Copyright */}
        <div className="pt-8 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-zinc-500">
          <div>
            جميع الحقوق محفوظة © 2025 <strong class="text-zinc-300">عبده علي موسى (Abdou Ali Mousa)</strong> | AI & Digital Systems Engineer.
          </div>
          <div className="flex items-center gap-2 font-mono text-[11px] text-zinc-400">
            <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
            <span>Designed & Built with Pure Engineering</span>
          </div>
        </div>

      </div>
    </footer>
  );
}