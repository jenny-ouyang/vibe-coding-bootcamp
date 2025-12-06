# Diagram 05: Stack Decision Tree

## Chapter Placement
**Chapter 3: Choosing Your Stack**

## Exact Location
Place immediately after the section "## Decision Tree (Visual Guide)" header (line 230)

Replace or enhance the text-based decision tree from lines 232-256 with this visual version

## Diagram Type
**Decision tree / flowchart** guiding readers to the right technology stack choice

## Detailed Description
A top-down decision tree that asks simple questions and leads readers to one of three clear paths, with examples under each path.

### Visual Layout:

```
                    ┌──────────────────────────────┐
                    │  WHAT ARE YOU BUILDING?      │
                    │  (Start here)                │
                    └───────────┬──────────────────┘
                                │
                ┌───────────────┼───────────────┐
                │               │               │
                ▼               ▼               ▼
    ┌────────────────┐  ┌────────────────┐  ┌────────────────┐
    │ Just showing   │  │ Users need to  │  │ Heavy data     │
    │ content?       │  │ sign up/login? │  │ processing?    │
    │                │  │                │  │                │
    │ No accounts    │  │ Save user data │  │ ML/analytics   │
    │ No database    │  │ Interact       │  │ Python needed  │
    └───────┬────────┘  └───────┬────────┘  └───────┬────────┘
            │                   │                    │
            ▼                   ▼                    ▼
    ┌────────────────┐  ┌────────────────┐  ┌────────────────┐
    │  PATH 1        │  │  PATH 2        │  │  PATH 3        │
    │  Static Site   │  │  Full Web App  │  │  Python API    │
    │                │  │    ⭐ MOST     │  │                │
    │  React +       │  │    COMMON      │  │  Flask +       │
    │  Netlify       │  │                │  │  PostgreSQL    │
    │                │  │  Next.js +     │  │                │
    │  Cost: $12/yr  │  │  Supabase      │  │  Cost: $60/yr  │
    │  Time: 2-4hrs  │  │                │  │  Time: 6-10hrs │
    │                │  │  Cost: $12/yr  │  │                │
    │                │  │  Time: 4-8hrs  │  │                │
    └───────┬────────┘  └───────┬────────┘  └───────┬────────┘
            │                   │                    │
            ▼                   ▼                    ▼
    ┌────────────────┐  ┌────────────────┐  ┌────────────────┐
    │ Good for:      │  │ Good for:      │  │ Good for:      │
    │ • Portfolio    │  │ • SaaS app     │  │ • Data tools   │
    │ • Landing page │  │ • Community    │  │ • Analytics    │
    │ • Blog         │  │ • Booking      │  │ • ML features  │
    │ • Docs         │  │ • Marketplace  │  │ • Automation   │
    └────────────────┘  └────────────────┘  └────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ 🤔 STILL NOT SURE?                                                  │
│                                                                     │
│ → Choose PATH 2 (Next.js + Supabase)                               │
│                                                                     │
│ Why? It's flexible enough for most projects, and you can always    │
│ simplify to Path 1 or add Path 3 backend later if needed.          │
└─────────────────────────────────────────────────────────────────────┘
```

## Key Labels and Text

**Top Question Box:**
"WHAT ARE YOU BUILDING?"
"(Start here)"

**Three Question Branches:**
1. "Just showing content? No accounts, No database"
2. "Users need to sign up/login? Save user data, Interact"
3. "Heavy data processing? ML/analytics, Python needed"

**Three Path Result Boxes:**

**Path 1:**
- "Static Site"
- "React + Netlify"
- "Cost: $12/year"
- "Time: 2-4 hours"
- Examples: Portfolio, Landing page, Blog, Docs

**Path 2:**
- "Full Web App ⭐ MOST COMMON"
- "Next.js + Supabase"
- "Cost: $12/year"
- "Time: 4-8 hours"
- Examples: SaaS app, Community, Booking, Marketplace

**Path 3:**
- "Python API"
- "Flask + PostgreSQL"
- "Cost: $60/year"
- "Time: 6-10 hours"
- Examples: Data tools, Analytics, ML features, Automation

**Bottom Decision Box:**
"STILL NOT SURE?"
"→ Choose PATH 2 (Next.js + Supabase)"
Reasoning: flexibility, can scale up or down

## Purpose/Benefit Statement

**Why this diagram helps:**
Chapter 3 has the most potential for decision paralysis. This diagram:
1. Simplifies a complex decision into 3 simple questions
2. Shows clear paths with concrete outcomes (cost, time, use cases)
3. Highlights the recommended path (Path 2) without overwhelming
4. Provides safety net ("still not sure? → go here")
5. Removes analysis paralysis by making the decision visual and quick

When readers see this diagram, they should be able to:
- Identify their project type in under 30 seconds
- See all three options at once (not buried in text)
- Understand the tradeoffs (cost, time, capabilities)
- Feel confident moving forward

**Key benefit:** This transforms "which stack should I choose?" from a research project into a 2-minute decision. The visual format makes it feel less scary than walls of technical text. Readers can point to a path and say "this is me" without reading every detail about the other paths.
