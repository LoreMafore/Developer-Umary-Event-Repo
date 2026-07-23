# Umary's Mystery Event — Suspect Journal Archive

![Python](https://img.shields.io/badge/Clues-Daily%20Journal-3776AB?logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/Infrastructure-Raspberry%20Pi-C51A4A?logo=raspberrypi&logoColor=white)
![Event](https://img.shields.io/badge/Event-March%202026-brightgreen)

This repository contains the **in-universe suspect journal** used as the primary clue database for **Umary's Mystery Event: The Case of the Diamond Cross**.

Participants investigated these documents to identify the culprit, uncover the accomplices, and reconstruct how the Diamond Cross was stolen.

The frontend website and backend API for the event can be found here:
[Mystery-Event Repository](https://github.com/LoreMafore/Mystery-Event)

---

## What This Repository Is

The `Documents/` folder contains a **daily developer journal** written from the perspective of the primary suspect — a junior developer who spent 2025 learning to code while secretly planning a heist.

Each `.txt` file is a single day's entry. Early entries read like a genuine coding diary. As the year progresses, the heist begins to take shape beneath the surface. By January 2026, the entries document the final countdown, the theft itself, and the desperate aftermath.

Participants had to comb through **over 400 entries** spanning two years to build a timeline and identify the suspects.

---

## Journal Arc

| Period | Theme |
|--------|-------|
| **Jan – Oct 2025** | Genuine coding learning (NumPy, Django, TensorFlow, FFmpeg, PostgreSQL, and more) |
| **Nov 2025** | First contact with the Diamond Cross — suspicion begins |
| **Dec 2025** | Active heist planning: jammer testing, fake cross, security research |
| **Jan 1–17, 2026** | Final countdown — 17 days to the event |
| **Jan 18, 2026** | The night of the theft *(encrypted entry — a puzzle clue)* |
| **Jan 19–31, 2026** | Aftermath: failed attempts to sell the cross, paranoia, regret |

---

## Repository Structure

```
Developer-Umary-Event-Repo/
├── Documents/
│   ├── 2025/
│   │   ├── 01/          # January 2025 — 31 daily entries
│   │   ├── 02/          # February 2025 — 28 daily entries
│   │   └── ...          # One folder per month through December
│   └── 2026/
│       └── 01/          # January 2026 — 31 daily entries (the heist month)
└── Trash/               # Red herrings and supporting code artifacts
```

---

## Key Puzzle Elements

- **VimCrypt-encrypted entry** (Jan 18, 2026) — the night of the heist, locked behind a cipher
- **FFmpeg overlay script** — referenced throughout; used to loop and fake the security camera feed
- **PostgreSQL guest list queries** — used to count and confirm security guard numbers
- **Jammer debugging log** — hardware entries hidden among coding frustrations
- **"Accomplice 1" and "Accomplice 2"** — never named directly; identified by cross-referencing the Level 3 attendance database in the main event repo

---

## Related Repository

The frontend website, backend API, and puzzle validation system:
[LoreMafore/Mystery-Event](https://github.com/LoreMafore/Mystery-Event)
