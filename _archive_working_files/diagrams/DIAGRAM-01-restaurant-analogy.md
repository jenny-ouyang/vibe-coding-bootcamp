# Diagram 01: The Restaurant Analogy

## Chapter Placement
**Chapter 2: Understanding the Shape of Apps**

## Exact Location
Place immediately after the paragraph:
> "This is where ingredients and supplies are stored..." (line 42)

Right before the section "### The Waiters (APIs)" (line 45)

## Diagram Type
**Illustrated architecture diagram** with restaurant imagery mapped to app components

## Detailed Description
A side-by-side visual showing a restaurant on the left and app components on the right, with arrows connecting the analogous parts.

### Visual Layout:

```
┌─────────────────────────────────┬─────────────────────────────────┐
│         RESTAURANT              │           WEB APP               │
├─────────────────────────────────┼─────────────────────────────────┤
│                                 │                                 │
│  👥 DINING ROOM                 │  📱 FRONT-END                   │
│  • Menu boards                  │  • Login screens                │
│  • Tables & chairs              │  • Buttons & forms              │
│  • What customers see           │  • What users see               │
│           ↓                     │           ↓                     │
│     [WAITER carries order]  ────┼────→  [API sends request]       │
│           ↓                     │           ↓                     │
│  👨‍🍳 KITCHEN                     │  ⚙️  BACK-END                   │
│  • Chefs preparing food         │  • Processing logic             │
│  • Following recipes            │  • Making decisions             │
│  • Coordinating work            │  • Handling requests            │
│           ↓                     │           ↓                     │
│     [Chef gets ingredients] ────┼────→  [Back-end queries data]   │
│           ↓                     │           ↓                     │
│  🗄️  PANTRY                     │  💾 DATABASE                    │
│  • Organized shelves            │  • User accounts                │
│  • Labeled ingredients          │  • Stored posts                 │
│  • Inventory tracking           │  • Saved data                   │
│           ↓                     │           ↓                     │
│     [Waiter brings food]    ────┼────→  [API returns response]    │
│           ↓                     │           ↓                     │
│  ✅ Customer sees their meal    │  ✅ User sees their content     │
│                                 │                                 │
└─────────────────────────────────┴─────────────────────────────────┘
```

## Key Labels and Text

**Left Side (Restaurant):**
- "Dining Room: What customers interact with"
- "Kitchen: Where the work happens"
- "Pantry: Where supplies are stored"
- "Waiters: Carry orders back and forth"

**Right Side (App):**
- "Front-End: What users see and click"
- "Back-End: Where processing happens"
- "Database: Where data is stored"
- "APIs: Carry requests and responses"

**Connection Arrows:**
Each arrow should be labeled with what travels:
- "Order / Request"
- "Food / Data"
- "Ingredients / Stored Info"

## Purpose/Benefit Statement

**Why this diagram helps:**
This is the foundational mental model for the entire guide. Non-technical readers already understand restaurants, so mapping familiar concepts to technical ones removes the intimidation factor. The visual reinforcement helps readers remember:
1. The three core pieces (dining room/kitchen/pantry = front/back/database)
2. How they connect (waiters = APIs)
3. The flow of information (order → prepare → serve)

When readers hit confusion later, they can return to this restaurant analogy to re-ground themselves. It's the anchor diagram for the entire chapter.
