# Creative Developer Portfolio (React + Tailwind CSS + Framer Motion)

A high-converting, brutalist dark-theme portfolio website tailored for modern full-stack engineers and creative technologists.

## Tech Stack
- **Framework**: React.js / Next.js
- **Styling**: Tailwind CSS (Dark `#0a0a0c` + Neon Purple `#a855f7` accents)
- **Animations**: Framer Motion
- **Icons**: Lucide React

## Project Architecture
```
src/
â”œâ”€â”€ components/
â”‚   â”œâ”€â”€ Navbar.jsx        # Glassmorphic responsive header with CD monogram
â”‚   â”œâ”€â”€ Hero.jsx          # Massive "CREATIVE DEVELOPER" headline with cursive overlay
â”‚   â”œâ”€â”€ Stats.jsx         # 4-column key metrics bar
â”‚   â”œâ”€â”€ Services.jsx      # "WHAT I DO" 4-service card grid with watermarked numerals
â”‚   â”œâ”€â”€ Projects.jsx      # "FEATURED PROJECTS" 3-column interactive cards
â”‚   â”œâ”€â”€ BottomGrid.jsx    # Trifecta: Toolkit (4x3), Work Process, Vibrant Purple CTA
â”‚   â””â”€â”€ Footer.jsx        # Dual-column Contact & Socials layout
â”œâ”€â”€ App.jsx               # Main orchestration component
â”œâ”€â”€ main.jsx              # Application bootstrap
â””â”€â”€ index.css             # Tailwind base & custom scrollbar
```

## Running Locally
```bash
npm install
npm run dev
```

## Standalone Live Preview
Open `standalone_preview.html` in any browser to preview the live application immediately without any build steps.