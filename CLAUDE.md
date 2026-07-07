# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

**Vibe Coding from Zero** — a free, public, book-length guide teaching domain experts with zero coding background how to build and ship real AI-assisted web apps (Claude, Cursor, Supabase, Vercel). Authored by Jenny Ouyang as a lead magnet for the Build to Launch newsletter and released under MIT.

The repo is the guide itself: 8 chapters + glossary + pathways in markdown, mirrored as per-chapter PDFs and a combined PDF, plus 5 focused micro-guides. There is no application code — the "product" is the writing. It is published to GitHub (`jenny-ouyang/vibe-coding-bootcamp`) with PDF releases.

## Status (updated: 2026-07-06)

**Current phase:** Dormant / shipped. This is a completed v1.0 public release, not active development. Last commit **2025-12-07** (`Remove README.pdf from Gumroad package`); initial commit 2025-12-05. Nothing is in flight. The repo is in reference/maintenance state — touch it only for corrections (typos, broken links, pricing updates) or a deliberate v2.

**What exists:** 8 chapters, GLOSSARY, PATHWAYS, README, LICENSE, all mirrored as individual PDFs + a combined PDF + a distributable zip, and 5 micro-guides.

### Active work
- [ ] None. Repo is dormant. Do not invent activity.
- [ ] Known correction pending (see Open questions): README links to a `docs-site/` Docusaurus site that is not in this repo.

## Rules (non-negotiable)

1. **This is finished public content — edit surgically.** Preserve Jenny's voice and the chapter structure. No wholesale rewrites.
2. **Markdown is the source of truth; PDFs are derived.** If you change a chapter's `.md`, the matching PDF in `individual_pdfs/` and the combined `Vibe-Coding-Bootcamp-Complete.pdf` go stale. Either regenerate them or flag the drift — never leave them silently out of sync.
3. **Keep pricing and tool claims accurate.** Prior commits fixed pricing and removed non-existent platforms. Verify any tool/pricing edit against current official sources (a whole commit, `6ddd16d`, was a pricing fix).
4. **Public repo — no secrets, no internal links.** This ships to GitHub. Don't add anything private, and don't add links to content-engine or other private repos.
5. **Surgical commits.** `git add` only what you changed. `_archive/`, `.DS_Store`, `*.log`, Python cache are gitignored — never force them in.

## Architecture

```
vibe-coding-bootcamp/
├── CLAUDE.md                        ← this file
├── README.md                        # Landing page: audience, chapter map, quick start
├── PATHWAYS.md                      # Learning-path chooser by experience/goal
├── GLOSSARY.md                      # Term reference
├── LICENSE                          # MIT
│
├── 01-introduction.md               # Ch 1: The Vibe Coding Method
├── 02-understanding-apps.md         # Ch 2: The Shape of Apps
├── 03-choosing-stack.md             # Ch 3: Choosing Your Stack
├── 04-tutorial.md                   # Ch 4: First AI-Built App in One Hour
├── 05-building-blocks.md            # Ch 5: Common Building Blocks
├── 06-debugging.md                  # Ch 6: When Things Break
├── 07-testing.md                    # Ch 7: How to Know It Works
├── 08-whats-next.md                 # Ch 8: What's Next
│
├── micro-guides/                    # 5 focused 1–2 page guides (deploy, errors, auth, debugging, idea→URL)
├── individual_pdfs/                 # Per-chapter PDFs + GLOSSARY/PATHWAYS PDFs + distributable zip (derived)
└── Vibe-Coding-Bootcamp-Complete.pdf  # Combined PDF (derived, ~3.9MB)
```

No `→ _index.md` folders: `README.md` already routes the chapters, `individual_pdfs/` is a derived data dump, and `micro-guides/` is a flat 5-file set the README links directly.

## Gotchas

1. **`docs-site/` does not exist.** README.md line ~53 links to a Docusaurus site (`docs-site/`) that is not in this repo — a dead link. Flagged, not yet fixed (see Open questions).
2. **Directory mtime ≠ commit date.** Files show a Dec 19 2025 modified time, but the last actual commit is Dec 7 2025. Read git log for true recency, not `ls`.
3. **PDFs drift from markdown.** The `.md` chapters are canonical; PDFs are regenerated snapshots. A markdown edit without a PDF regen leaves them inconsistent.
4. **README has two "How to Use This Guide" sections** — one near the top (pathways/micro-guides/site) and one lower (read online / PDF / follow along). Not a bug, but easy to confuse when editing.
5. **External links point at the public GitHub repo + Substack.** Keep them pointing at public destinations; this is a lead magnet.

## Stack

- Pure content repo — no runtime, no build step, no package manager, no tests.
- Markdown source. PDFs generated out-of-band (tooling not in-repo).
- Git-tracked, published to GitHub with PDF releases. MIT licensed.

## Commands

- No dev server, no build, no tests.
- PDF regeneration is done outside this repo (no generator checked in). If chapters change, regenerate `individual_pdfs/` and the combined PDF manually.

## Conventions

- **Chapters:** `NN-slug.md`, numbered 01–08. Each has a matching `Chapter-NN-slug.pdf` in `individual_pdfs/`.
- **Micro-guides:** short, single-topic, action-first (e.g. `deploy-in-10-minutes.md`). Kept flat in `micro-guides/`.
- **Tone:** direct, non-technical, encouraging; real builder examples with names + results. Match the existing voice on any edit.

## Recent changes

- 2025-12-07: Removed README.pdf from Gumroad package; evergreen version/date format; public-release cleanup.
- 2025-12-06: Added PATHWAYS, micro-guides, visual elements; pricing accuracy fix; Chapter 8 title fix.
- 2025-12-05: Initial commit — Vibe Coding Bootcamp, Zero to Ship.

## Open questions

- README links to a `docs-site/` Docusaurus site that isn't in the repo — should the link be removed, or the site added? (Dead link today.)
- Are the checked-in PDFs current with the latest markdown, or stale from an earlier chapter revision?
- Is a v2 planned, or is this permanently frozen at v1.0?

## Environment

- Git repo at `~/Documents/content/vibe-coding-bootcamp/`.
- No secrets, no `.env`. Fully public content.
- `.gitignore` covers `_archive/`, `.DS_Store`, `*.log`, Python cache, `*.tmp`.
