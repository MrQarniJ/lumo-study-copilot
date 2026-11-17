# Lumo — UX Brief

## 1. Executive Summary
Lumo is an AI study copilot mobile app designed for university students facing exam pressure with scattered lecture slides, notes, and recordings. It turns fragmented materials into an adaptive daily study runway, active-recall practice cards with slide citations, and visual confidence tracking.

## 2. Concept Exploration & Decision Log

### Evaluated Concepts
1. **Concept 1: The Exam Runway (Timeline-First):** Calendar countdown and milestone pacing. Excellent for structure and daily clarity; less flexible for spontaneous deep dives.
2. **Concept 2: The Mastery Map (Gap-First):** Color-coded matrix of topic mastery. Superb for targeting weak spots and visual feedback; can cause anxiety if too many red alerts appear.
3. **Concept 3: The 1-Tap Copilot (Stream-First):** Micro-sprint feed on demand. Great for transit/quick breaks; lacked bird's-eye view of upcoming exam deadlines.

### Winning Solution: The Hybrid
Combines **The Exam Runway** on the main Home dashboard (pacing + daily mission) with **The Mastery Matrix** inside each course (targeted diagnostic drilling).

## 3. Information Architecture
- **Global Navigation (Bottom Bar):**
  - **Tab 1: Today (Runway):** Exam countdown, daily 20-min mission, quick resume.
  - **Tab 2: Courses:** Enrolled courses, Red/Amber/Green mastery matrix, topic summaries.
  - **Tab 3: Practice:** Active recall sessions, flashcards, quick quizzes, citation drawer.
  - **Tab 4: Library:** Course materials, PDF/PPTX/Audio uploads, processing status.

## 4. Key User Journeys & Flows
- **Daily Study Loop:** Home → Tap "Start Mission" → Read 2-min summary → Complete 8 flashcards → Self-rate confidence → Updated progress ring.
- **Weak Spot Remediation:** Course view → Identify low-confidence topic (Red) → Tap "Drill Weakness" → Complete 5 questions → Topic shifts to Amber/Green.
- **Material Ingestion:** Tap "+" → Drop slides/audio → Set exam date → Async extraction → Instant structured topic breakdown.

## 5. Screen Inventory
1. **Today (Runway) [Hero Screen]:** Daily focal mission, exam countdown, readiness gauge.
2. **Course Detail & Mastery Matrix [Key Screen]:** Visual topic cards with Red/Amber/Green confidence indicators.
3. **Active Practice & Flashcard Mode [Key Screen]:** Interactive flip card, multiple-choice, slide source citation badge.
4. **Source Citation Sheet [Supporting]:** Slide page preview and audio timestamp drawer.
5. **Upload & Ingestion Sheet [Supporting]:** Multi-file upload, processing status bar.
6. **Session Complete Calibration [Supporting]:** Post-session confidence calibration and mastery boost summary.
