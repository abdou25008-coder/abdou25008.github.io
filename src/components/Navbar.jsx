import React, { useState, useEffect } from 'react';
import { Menu, X, MessageSquare } from 'lucide-react';

export default function Navbar() {
  const [scrolled, setScrolled] = useState(false);
  const [mobileOpen, setMobileOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 40);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
    <header className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${scrolled ? 'py-3 bg-[#0a0a0c]/95 shadow-2xl backdrop-blur-md border-b border-white/5' : 'py-5 bg-transparent'}`}>
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between">
        
        {/* Brand */}
        <a href="#" className="flex items-center gap-3 group">
          <div className="w-11 h-11 rounded-xl bg-gradient-to-br from-purple-500 via-purple-700 to-zinc-900 p-[1.5px] shadow-lg shadow-purple-600/30 group-hover:shadow-purple-500/60 transition-all duration-300">
            <div className="w-full h-full bg-[#0a0a0c] rounded-[10px] flex items-center justify-center font-black text-lg text-white group-hover:text-purple-400 transition-colors">
              AA
            </div>
          </div>
          <div className="flex flex-col text-right">
            <div className="flex items-center gap-1.5">
              <span className="font-extrabold text-base sm:text-lg text-white tracking-wide group-hover:text-purple-300 transition-colors">
                Abdou Ali Mousa
              </span>
              <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
            </div>
            <span className="text-[11px] font-mono tracking-wider text-zinc-400">
              AI & Digital Systems Engineer
            </span>
          </div>
        </a>

        {/* Desktop Nav */}
        <nav className="hidden md:flex items-center gap-1 bg-[#16161a]/90 border border-[#27272e] rounded-full px-5 py-2 shadow-inner backdrop-blur-md">
          <a href="#services" className="px-3.5 py-1.5 text-xs font-bold text-zinc-300 hover:text-white hover:bg-purple-950/50 rounded-full transition-all duration-200">الخدمات</a>
          <a href="#platforms" className="px-3.5 py-1.5 text-xs font-bold text-zinc-300 hover:text-white hover:bg-purple-950/50 rounded-full transition-all duration-200">المنظومات الحية</a>
          <a href="#software-models" className="px-3.5 py-1.5 text-xs font-bold text-zinc-300 hover:text-white hover:bg-purple-950/50 rounded-full transition-all duration-200">النماذج الذكية</a>
          <a href="#media-network" className="px-3.5 py-1.5 text-xs font-bold text-zinc-300 hover:text-white hover:bg-purple-950/50 rounded-full transition-all duration-200">الشبكة الإعلامية</a>
          <a href="#workflow" className="px-3.5 py-1.5 text-xs font-bold text-zinc-300 hover:text-white hover:bg-purple-950/50 rounded-full transition-all duration-200">منهجية العمل</a>
        </nav>

        {/* Action Button & Toggle */}
        <div className="flex items-center gap-3">
          <a href="https://wa.me/201092519210" target="_blank" rel="noopener noreferrer" className="hidden sm:inline-flex items-center gap-2 bg-gradient-to-r from-purple-600 to-purple-800 hover:from-purple-500 hover:to-purple-700 text-white text-xs font-bold px-5 py-2.5 rounded-full transition-all duration-300 border border-purple-400/30 shadow-lg shadow-purple-950/50">
            <MessageSquare className="w-3.5 h-3.5 text-emerald-400" />
            <span>حجز استشارة واتساب</span>
          </a>

          <button 
            onClick={() => setMobileOpen(!mobileOpen)}
            className="md:hidden w-10 h-10 rounded-xl bg-[#16161a] border border-[#27272e] flex items-center justify-center text-zinc-300 hover:text-white hover:border-purple-500 transition-colors"
            aria-label="القائمة"
          >
            {mobileOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
          </button>
        </div>
      </div>

      {/* Mobile Drawer */}
      {mobileOpen && (
        <div className="md:hidden bg-[#0e0e12]/98 border-b border-purple-900/30 px-6 py-6 animate-in slide-in-from-top-4 duration-300 text-right">
          <div className="flex flex-col gap-3">
            <a onClick={() => setMobileOpen(false)} href="#services" className="py-2.5 px-4 rounded-xl text-sm font-bold text-zinc-300 hover:text-white hover:bg-purple-950/40 transition-colors">الخدمات الهندسية</a>
            <a onClick={() => setMobileOpen(false)} href="#platforms" className="py-2.5 px-4 rounded-xl text-sm font-bold text-zinc-300 hover:text-white hover:bg-purple-950/40 transition-colors">المنظومات والتطبيقات الحية</a>
            <a onClick={() => setMobileOpen(false)} href="#software-models" className="py-2.5 px-4 rounded-xl text-sm font-bold text-zinc-300 hover:text-white hover:bg-purple-950/40 transition-colors">نماذج الذكاء الاصطناعي</a>
            <a onClick={() => setMobileOpen(false)} href="#media-network" className="py-2.5 px-4 rounded-xl text-sm font-bold text-zinc-300 hover:text-white hover:bg-purple-950/40 transition-colors">الشبكة الإعلامية (Shorts)</a>
            <a onClick={() => setMobileOpen(false)} href="#workflow" className="py-2.5 px-4 rounded-xl text-sm font-bold text-zinc-300 hover:text-white hover:bg-purple-950/40 transition-colors">منهجية العمل والتقنيات</a>
            <a onClick={() => setMobileOpen(false)} href="https://wa.me/201092519210" target="_blank" rel="noopener noreferrer" className="mt-2 py-3 px-4 rounded-xl text-sm font-bold text-center text-white bg-gradient-to-r from-purple-600 to-purple-800 flex items-center justify-center gap-2">
              <span>حجز استشارة (+20 109 251 9210)</span>
            </a>
          </div>
        </div>
      )}
    </header>
  );
}