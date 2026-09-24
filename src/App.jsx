import React from 'react';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import Stats from './components/Stats';
import Services from './components/Services';
import SoftwareModels from './components/SoftwareModels';
import MediaNetwork from './components/MediaNetwork';
import BottomGrid from './components/BottomGrid';
import Footer from './components/Footer';

export default function App() {
  return (
    <div className="min-h-screen bg-[#0a0a0c] text-white font-sans selection:bg-purple-600 selection:text-white">
      <Navbar />
      <main>
        <Hero />
        <Stats />
        <Services />
        <SoftwareModels />
        <MediaNetwork />
        <BottomGrid />
      </main>
      <Footer />
    </div>
  );
}