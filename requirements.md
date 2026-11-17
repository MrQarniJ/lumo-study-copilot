# Lumo — AI Study Copilot — Requirements

## Summary
Lumo is a mobile AI study copilot designed for university students drowning in scattered lecture slides, PDFs, notes, and audio recordings. Lumo digests multi-source study materials and generates an adaptive revision roadmap, grounded active-recall practice questions, concise topic summaries, and real-time confidence tracking, transforming exam anxiety into calm, daily mastery.

## Problem framing
### Problem statement
University students need a way to automatically transform disorganized lecture slides, notes, and recordings into an exam-driven revision roadmap and active recall practice because scattered materials create severe exam anxiety, wasted study hours, and blind spots on what they actually understand.

### Primary user snapshot
- **Persona:** Alex, 2nd-year undergraduate taking 4–5 dense courses simultaneously.
- **Context:** Mobile-first study sessions in short intervals between classes, during commutes, and in focused library blocks.
- **Pain points:** Disorganized files across LMS/cloud folders, paralysis over what to revise first, difficulty identifying actual knowledge gaps versus false familiarity.
- **Aha! moment:** Dropping course slides into Lumo and seeing an immediate, structured daily revision path with citation-backed quiz cards and a measurable confidence meter.

### Key scenarios
1. **Semester / Exam Ingestion:** Dropping PDFs, slides, and lecture recordings into a course module, generating an auto-structured curriculum with topic cards and exam countdowns.
2. **Daily Revision Routine:** Opening the app to a personalized "Today's Study Plan" targeting overdue spaced-repetition topics and low-confidence concepts.
3. **Active Recall Practice:** Completing interactive quiz sessions and flashcards with instant citations linking directly to exact lecture slide pages or audio timestamps.
4. **Confidence Calibration:** Rating comfort levels post-quiz to watch course mastery metrics visually update and recalibrate upcoming review intervals.

### How might we
- HMW 1: Make uploading messy, multi-format study files feel effortless, fast, and visually rewarding?
- HMW 2: Design a daily dashboard that eliminates exam dread through structured, bite-sized daily milestones?
- HMW 3: Provide practice questions and answers that feel trustworthy, authoritative, and strictly cited from course materials?
- HMW 4: Visualize topic mastery and knowledge gaps so students instantly know where their revision time is best spent?

## Problem
- Students store materials across university portals (Canvas/Blackboard), Google Drive, local downloads, and voice memos.
- Passive re-reading creates an illusion of competence without real test readiness.
- Approaching exam dates trigger cramming cycles without clear visibility into weak areas.

## Goals and success metrics
- **Primary user goal:** Attain exam readiness with minimal cognitive friction and clear confidence tracking.
- **Product success signals:** Daily active revision completion rate, flashcard review retention, student-reported reduction in study stress.
- **Prototype goal:** A high-fidelity, interactive mobile prototype demonstrating end-to-end ingestion, study dashboard, active practice, and confidence tracking.

## Users
### Primary user
- University & college undergraduate / graduate students with exam-intensive subjects (STEM, Humanities, Business, Pre-Med).
### Secondary users
- High school AP/IB students, self-taught certification test-takers.
### Context of use
- Primarily smartphone (iOS / Android) in portrait orientation. Quick 10–25 minute micro-sessions on the go, plus 1–2 hour deep study sessions at a desk.

## Core jobs (ranked)
1. **Material Ingestion & Auto-Organization:** Upload slides, notes, and recordings; group them into clear courses and topics.
2. **Personalized Revision Schedule:** Generate a dynamic timeline based on target exam dates and spaced-repetition intervals.
3. **Active Recall & Practice:** Solve AI-generated flashcards, multiple-choice, and short-answer questions linked to lecture sources.
4. **Confidence & Mastery Tracking:** Self-rate topic grasp and verify with quiz analytics to visualize subject readiness.
5. **Topic Summaries & Key Concepts:** Read bite-sized, digestible summaries extracted directly from uploaded materials.

## Scope
### Must have (V1 / Prototype)
- Course & module organization with exam date setting.
- Multi-format file uploader (PDF, PPTX, DOCX, Audio).
- Daily Revision Hub ("Today's Plan") with exam countdowns.
- Interactive Active Recall practice (flashcards & quizzes with source slide citations).
- Topic mastery & confidence tracker (visual gauges / Red-Amber-Green status).
- Concise topic summaries with key takeaways.
- Pre-loaded sample course ("Cognitive Psychology 101") for zero-state onboarding.

### Should have
- Spaced repetition algorithm indicators (next review in 2d, 5d, 10d).
- Offline review mode for cached flashcards and summaries.
- Search and filter across all uploaded materials.

### Won't have (V1 Prototype)
- Social study groups and peer leaderboards.
- Collaborative shared deck marketplace.
- Deep bi-directional LMS synchronization.

## Content and data
- File types: PDF slide decks, PPTX presentations, DOCX lecture outlines, MP3/M4A audio recordings.
- Derived data: Topic hierarchies, key concept summaries, active recall questions with answer explanations and source citations.
- User state data: Confidence ratings (1–5 scale / Red-Amber-Green), quiz accuracy, review schedules.

## Platform and integrations
- Platform: Mobile App (iOS / Android), optimized for mobile touch interaction.
- Key UX patterns: Bottom navigation bar, swipeable flashcards, interactive progress rings, modal upload sheet, source reference drawers.

## Constraints
- Focus strictly on UI design, user flows, and interactive prototype experience.
- Mobile viewport dimensions (standard modern smartphone 390x844 / 375x812 pt).

## Brand and tone
- **Personality:** Calm, reassuring, clear, and encouraging.
- **Must never feel:** Overwhelming, cluttered, bureaucratic, or excessively gamified with distracting gimmicks.
- **Design inspirations:** Notion (clean typography & structure), Duolingo (encouraging progress mechanics), Headspace (soothing, low-stress ambiance).

## Lifecycle
- **Day One:** Welcomed with a warm, clean greeting and instant option to explore a sample course or drop their first syllabus/deck.
- **Daily Loop:** Push reminder or app open shows "Today's 3 revision goals" (e.g., 1 summary, 10 flashcards).
- **Exam Eve:** High-yield rapid review mode highlighting remaining red/amber low-confidence topics.

## Edge cases and states
- Empty state: Pre-loaded interactive sample course demo.
- Processing state: Graceful non-blocking async status (summaries ready immediately, flashcards loading).
- Error state: Unsupported file format or unreadable scanned PDF warning with clear resolution advice.

## Assumptions (signed off)
- User focuses on the UI/UX prototype workflow over backend architecture.
- Solo self-paced study is the core value proposition for initial adoption.
- Direct file uploads cover the vast majority of student input needs.

## Open questions
- None blocking Phase 2.
