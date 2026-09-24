/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        darkBg: "#0a0a0c",
        cardBg: "#18181b",
        cardBorder: "#27272a",
        neonPurple: "#a855f7",
        vibrantPurple: "#9333ea",
        accentPurple: "#8b5cf6",
        lightPurple: "#c084fc",
        mutedText: "#a1a1aa",
      },
      fontFamily: {
        heading: ["'Oswald'", "'Impact'", "'Poppins'", "sans-serif"],
        cursive: ["'Caveat'", "'Dancing Script'", "cursive"],
        sans: ["'Inter'", "'DM Sans'", "sans-serif"],
      },
      boxShadow: {
        'purple-glow': '0 0 50px -10px rgba(168, 85, 247, 0.45)',
        'purple-glow-lg': '0 0 90px -15px rgba(147, 51, 234, 0.55)',
        'card-glow': '0 10px 30px -10px rgba(0, 0, 0, 0.7)',
      },
      animation: {
        'spin-slow': 'spin 16s linear infinite',
      }
    },
  },
  plugins: [],
}