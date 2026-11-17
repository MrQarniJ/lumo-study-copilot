# Lumo — Senior AI Study Copilot

> An evidence-based, calm, and distraction-free mobile study companion engineered around cognitive load theory, modern spaced repetition (FSRS / SM-2), and verbatim grounded slide/audio citations.

[![Deployed on Vercel](https://img.shields.io/badge/Vercel-Live_App-black?style=flat&logo=vercel)](https://lumo-study-copilot.vercel.app)
[![Design System](https://img.shields.io/badge/Design_System-Impeccable-241E4E?style=flat)](https://github.com/loftvoxelstudio-cmd/lumo-study-copilot)
[![Accessibility](https://img.shields.io/badge/WCAG_2.1-AA_Compliant-059669?style=flat)](https://www.w3.org/WAI/WCAG21/quickref/)

---

## 🔗 Live Application Link

- **Live Production App**: **[https://lumo-study-copilot.vercel.app](https://lumo-study-copilot.vercel.app)**
---

## 📱 Product Architecture

Lumo replaces noisy, gamified study apps and generic AI conversational chatbots with a purposeful, high-retention workflow:

1. **Screen 1 · Today's Runway**: A calm morning launchpad showing exam deadlines, current readiness scores, 3 structured tasks (digest, recall, practice verification), and quick course switching.
2. **Screen 2 · Course Topics Matrix**: Curriculum breakdown into 4 clear cognitive statuses: Critical Gap (`Review`), Due Soon, and Mastered with crisp vector indicator dots and filter chips.
3. **Screen 3 · 3D Active Recall Stage**: True hardware-accelerated 3D flashcard perspective flip with 1-tap auto-advancing spaced intervals (Again, Hard, Good, Easy) and full keyboard accelerators (`Space`, `1-4`, `→`).
4. **Screen 4 · Grounded Source Drawer**: Verbatim slide text highlights and synchronized 10-second lecture audio playback with interactive waveform scrubbing, ensuring zero hallucinations.
5. **Screen 6 · Session Debrief**: Post-drill cognitive gain summaries (`+4% gain`), accuracy breakdowns, streak counters, and immediate dual-path actions.
6. **Screen 7 · Student Profile & Analytics**: Interactive 7-day retention velocity charts, FSRS vs SM-2 memory decay curve algorithms, offline corpus quotas, and Anki `.apkg` export.

---

## 🎨 Impeccable Design System

- **Brand Palette**: Oxford Academic Indigo (`#241E4E`), warm cream alabaster ground (`#FAF9F6`), pure white cards (`#FFFFFF`).
- **Semantic Color Tokens**: Calibrated emerald (`#059669`), warm amber (`#D97706`), rose crimson (`#E11D48`), and royal violet (`#6366F1`) with WCAG AA compliant contrast ratios (>4.5:1).
- **Depth & Elevation**: Multi-layered ambient + key-light shadows color-matched to the charcoal-indigo palette. Zero harsh single-layer grey shadows.
- **Micro-Interactions**: Authentic 3D card rotation (`rotateY(180deg)` with `perspective: 1000px`), tactile button press scaling (`scale(0.985)`), and exponential easing metric counters.
- **Precision Typography**: Plus Jakarta Sans with `font-variant-numeric: tabular-nums` across all scores, countdowns, and progress indicators.

---

## 🚀 Live Deployment

The prototype is deployed as a standalone web application optimized for iPhone viewports (`390x844`) and modern mobile/desktop browsers:

- **Root Access**: Open `index.html` or the live Vercel URL.
- **Direct Screen Deep Links**:
  - `/#screen-2` — Course Topics Matrix
  - `/#screen-3` — Practice Stage (Front)
  - `/#screen-3-back` — Practice Stage (Answer & Grounding)
  - `/#screen-4` — Grounded Citation Drawer
  - `/#screen-6` — Session Debrief
  - `/#screen-7` — Cognitive Retention Analytics

---

## 🛠️ Tech Stack

- **Frontend**: Pure Semantic HTML5, Modern CSS3 (CSS Grid, 3D CSS Transforms, Backdrop Filters, Custom Properties), Vanilla ES6+ Engine
- **Hosting**: Vercel Fluid Compute / Edge CDN
- **Repository**: GitHub ALM
