# Lumo — Design Brief (UI Phase Handoff)

## Product & Problem in Brief
Lumo is an AI study copilot mobile app for university students. It organizes scattered lecture slides, PDFs, notes, and recordings into a structured daily revision runway, generates active-recall flashcards with direct slide citations, and tracks confidence so students study effectively without exam panic.

## Target User & Context
- **Primary User:** Alex, 2nd-year undergraduate taking multiple exam-heavy courses.
- **Context:** Mobile device (iOS/Android), used in 10–25 minute micro-sessions on campus, during transit, or in focused library study blocks.

## Chosen Concept & Mental Model
- **Concept:** "Calm Exam Runway + Visual Mastery Matrix" (Hybrid).
- **Mental Model:** A flight controller for exam prep combined with a diagnostic health scan of your course knowledge.

## Core Navigation & Screens
- **Global Navigation:** 4-tab bottom bar (`Today`, `Courses`, `Practice`, `Library`).

### Screen Inventory & Priority
1. **Screen 1 (Hero Screen): Today's Revision Runway**
   - *Primary Action:* "Start Today's Mission (18 min)"
   - *Key Elements:* Upcoming exam banner (Days remaining + Readiness ring), 3 daily step cards (Summary, Flashcards, Quiz), High-yield weak spot warning card.
2. **Screen 2 (Key Screen): Course Mastery Matrix**
   - *Primary Action:* "Drill Weakest Topics"
   - *Key Elements:* Course header with aggregate mastery gauge (e.g., 68%), topic breakdown categorized by Red (<50%), Amber (50-79%), Green (80%+), topic cards showing estimated study time.
3. **Screen 3 (Key Screen): Active Recall Practice & Flashcards**
   - *Primary Action:* "Flip Card / Rate Retention (Hard / Good / Easy)"
   - *Key Elements:* Progress indicator (Card 4 of 12), question card with flip interaction, answer card with highlighted takeaway, "Source: Slide 14" link button.
4. **Screen 4 (Supporting): Slide & Source Citation Drawer**
   - *Primary Action:* "Back to Practice"
   - *Key Elements:* Exact slide visual preview, highlighted text snippet, lecture recording timestamp indicator.
5. **Screen 5 (Supporting): Upload & Ingestion Modal**
   - *Primary Action:* "Upload & Generate Roadmap"
   - *Key Elements:* Drag/select area for PDF/PPTX/Audio, course tag, target exam date picker, progressive generation status.
6. **Screen 6 (Supporting): Session Complete Calibration**
   - *Primary Action:* "Continue to Runway"
   - *Key Elements:* Celebratory feedback, readiness score increase (+4%), streak update, 1-5 star confidence rating.

## Design Language, Tone & Aesthetics
- **Personality Adjectives:** Calm, focused, reassuring, intelligent, clean.
- **Must Never Feel:** Cluttered, overwhelming, childishly gamified, or anxiety-inducing.
- **Color Palette Intent:**
  - Primary: Deep Indigo / Soft Midnight Navy (focused, academic trust)
  - Accent / Motivation: Warm Sunrise Amber or Soft Electric Violet (calm energy)
  - Mastery Indicators: Soft Emerald Green (Mastered), Warm Amber (Review Needed), Coral/Rose (Critical Gap - never harsh alarming red)
  - Surface & Background: High-legibility off-white/cream paper tint or clean light slate, with dark mode compatibility.
- **Typography:** Crisp modern sans-serif (e.g., Inter, Plus Jakarta Sans, SF Pro) with clear typographic hierarchy.

## UX Principles
1. **One Focal Decision Per Screen:** The student should never wonder what to do next.
2. **Radical Trust via Citations:** Always show where AI answers originated.
3. **Calm Urgency, Not Anxiety:** Pacing that motivates without guilt.
4. **Snappy Micro-Interactions:** Swiping cards, smooth progress fills, tactile feedback.
