import React from 'react';
import { motion } from 'framer-motion';
import { ArrowUpRight } from 'lucide-react';

export default function Projects() {
  const projects = [
    {
      title: 'BRANDIX STUDIO',
      category: 'Web Design & Development',
      desc: 'Immersive agency portfolio with dynamic WebGL interactions & fast transitions.',
      gradient: 'from-purple-900/50 via-zinc-900 to-black',
      tags: ['React', 'Tailwind', 'Framer Motion'],
      mockupType: 'studio',
    },
    {
      title: 'NEXUS FINTECH',
      category: 'Next.js & AI Platform',
      desc: 'Real-time financial dashboard with algorithmic trading charts and crypto wallet.',
      gradient: 'from-violet-950/60 via-purple-950/40 to-zinc-900',
      tags: ['Next.js', 'TypeScript', 'Tailwind'],
      mockupType: 'fintech',
    },
    {
      title: 'AURA LUXE STORE',
      category: 'UI/UX & Headless Shopify',
      desc: 'Ultra-luxury minimal ecommerce experience with instant checkout and 3D previews.',
      gradient: 'from-fuchsia-950/50 via-purple-950/40 to-black',
      tags: ['UI/UX', 'Shopify API', 'Tailwind'],
      mockupType: 'luxe',
    },
  ];

  return (
    <section id="projects" className="py-24 md:py-32 relative">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Section Header */}
        <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-6 pb-12 border-b border-[#27272a]">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6 }}
          >
            <span className="text-xs font-mono text-purple-400 tracking-widest uppercase">
              // RECENT ARCHITECTURE
            </span>
            <h2 className="mt-2 font-heading font-black text-5xl sm:text-6xl md:text-7xl tracking-tighter uppercase text-white">
              FEATURED <span className="text-[#a855f7]">PROJECTS</span>
            </h2>
          </motion.div>

          <motion.a
            initial={{ opacity: 0, x: 20 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6 }}
            href="#projects"
            className="inline-flex items-center gap-2 text-xs sm:text-sm font-bold tracking-wider text-purple-400 hover:text-white uppercase group transition-colors"
          >
            <span>VIEW ALL PROJECTS</span>
            <span className="group-hover:translate-x-1.5 transition-transform duration-200">âž”</span>
          </motion.a>
        </div>

        {/* 3-Column Projects Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mt-12">
          {projects.map((proj, idx) => (
            <motion.div
              key={proj.title}
              initial={{ opacity: 0, y: 40 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6, delay: idx * 0.15 }}
              whileHover={{ y: -8 }}
              className="rounded-2xl bg-[#18181b] border border-[#27272a] hover:border-purple-500 transition-all duration-300 overflow-hidden group shadow-xl hover:shadow-purple-950/40 flex flex-col"
            >
              {/* TOP HALF: Project Thumbnail with Floating Mockup on Purple Gradient Canvas */}
              <div className={`relative h-64 sm:h-72 bg-gradient-to-br ${proj.gradient} p-6 overflow-hidden flex items-center justify-center border-b border-[#27272a]`}>
                {/* Background Grid Pattern */}
                <div className="absolute inset-0 bg-[radial-gradient(#a855f7_1px,transparent_1px)] [background-size:16px_16px] opacity-20" />

                {/* Floating Mockup Card */}
                <div className="relative w-full max-w-[260px] rounded-xl bg-[#0e0e12]/90 backdrop-blur-md border border-purple-500/30 p-3.5 shadow-2xl group-hover:scale-105 group-hover:border-purple-400/60 transition-all duration-500">
                  {/* Mockup Header Bar */}
                  <div className="flex items-center justify-between pb-2.5 mb-2.5 border-b border-zinc-800">
                    <div className="flex items-center gap-1.5">
                      <div className="w-2.5 h-2.5 rounded-full bg-red-500/80" />
                      <div className="w-2.5 h-2.5 rounded-full bg-amber-500/80" />
                      <div className="w-2.5 h-2.5 rounded-full bg-emerald-500/80" />
                    </div>
                    <span className="text-[9px] font-mono text-zinc-500 uppercase">{proj.mockupType}.app</span>
                  </div>

                  {/* Mockup Body Content Skeleton */}
                  <div className="space-y-2">
                    <div className="h-16 rounded-lg bg-gradient-to-r from-purple-900/60 to-purple-950/40 border border-purple-500/20 flex items-center justify-center">
                      <div className="text-center">
                        <span className="font-heading font-bold text-xs text-white tracking-wider">{proj.title}</span>
                        <p className="text-[8px] font-mono text-purple-300">LIVE PREVIEW READY</p>
                      </div>
                    </div>
                    <div className="grid grid-cols-3 gap-1.5">
                      <div className="h-6 rounded bg-zinc-800/60" />
                      <div className="h-6 rounded bg-purple-900/30" />
                      <div className="h-6 rounded bg-zinc-800/60" />
                    </div>
                  </div>
                </div>

                {/* Corner Category Badge */}
                <div className="absolute top-4 left-4 px-2.5 py-1 rounded-md bg-[#0a0a0c]/80 backdrop-blur-md border border-[#27272a] text-[10px] font-mono text-purple-300 uppercase tracking-wider">
                  {proj.tags[0]}
                </div>
              </div>

              {/* BOTTOM HALF: Project Name, Category, Arrow Link */}
              <div className="p-6 sm:p-7 flex flex-col justify-between flex-grow">
                <div>
                  <div className="flex items-start justify-between gap-4">
                    <div>
                      <h3 className="font-heading font-bold text-2xl text-white tracking-wide uppercase group-hover:text-purple-300 transition-colors">
                        {proj.title}
                      </h3>
                      <p className="mt-1 text-xs font-semibold text-purple-400 tracking-wider uppercase">
                        {proj.category}
                      </p>
                    </div>

                    {/* Upward-Right Arrow Link Button */}
                    <div className="w-10 h-10 rounded-full bg-[#27272a]/70 border border-zinc-700 flex items-center justify-center text-zinc-300 group-hover:bg-purple-600 group-hover:border-purple-500 group-hover:text-white transition-all duration-300 flex-shrink-0 group-hover:scale-110">
                      <ArrowUpRight className="w-5 h-5 group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-transform" />
                    </div>
                  </div>

                  <p className="mt-3 text-xs sm:text-sm text-zinc-400 leading-relaxed">
                    {proj.desc}
                  </p>
                </div>

                {/* Tech Tags */}
                <div className="mt-6 pt-4 border-t border-[#27272a]/60 flex flex-wrap gap-2">
                  {proj.tags.map((tag) => (
                    <span
                      key={tag}
                      className="px-2.5 py-1 rounded-md bg-[#0a0a0c] border border-zinc-800 text-[10px] font-mono text-zinc-400 font-medium"
                    >
                      {tag}
                    </span>
                  ))}
                </div>
              </div>
            </motion.div>
          ))}
        </div>

      </div>
    </section>
  );
}