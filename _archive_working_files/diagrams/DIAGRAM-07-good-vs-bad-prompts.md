# Diagram 07: Good vs Bad Prompts Comparison

## Chapter Placement
**Chapter 2: Understanding the Shape of Apps**

## Exact Location
Place immediately after the section "## Practical Examples: How to Describe What You Want" (line 269)

After the final good/bad example (line 300), before "## The Flow of Building" section

## Diagram Type
**Side-by-side comparison table** showing ineffective prompts vs. effective prompts with annotations

## Detailed Description
A visual comparison showing common mistakes beginners make when describing features, with explanations of why the bad versions fail and why the good versions work.

### Visual Layout:

```
┌─────────────────────────────────────────────────────────────────────┐
│              HOW TO DESCRIBE FEATURES TO AI                         │
│         (The difference between stuck and shipping)                 │
└─────────────────────────────────────────────────────────────────────┘

┌───────────────────────────────┬─────────────────────────────────────┐
│  ❌ DOESN'T WORK              │  ✅ WORKS WELL                      │
├───────────────────────────────┼─────────────────────────────────────┤
│                               │                                     │
│ "I need a user system"        │ "Users should sign up with email    │
│                               │  and password, log in, and have a   │
│ ⚠️  Problem: Too vague        │  profile page showing their name    │
│ AI doesn't know what you want │  and bio"                           │
│                               │                                     │
│                               │ ✓  Specific outcome described       │
│                               │ ✓  Clear features listed            │
├───────────────────────────────┼─────────────────────────────────────┤
│                               │                                     │
│ "Implement JWT-based auth     │ "Users should stay logged in even   │
│  with bcrypt and token        │  if they close the browser. Login   │
│  rotation"                    │  should be secure"                  │
│                               │                                     │
│ ⚠️  Problem: Too technical    │ ✓  Describes behavior, not code     │
│ You're telling AI HOW to code │ ✓  Lets AI choose best method      │
│                               │                                     │
├───────────────────────────────┼─────────────────────────────────────┤
│                               │                                     │
│ "Create a PostgreSQL table    │ "Users can save multiple bookmarks. │
│  with foreign keys and        │  Each bookmark should remember who  │
│  junction tables"             │  saved it and when"                 │
│                               │                                     │
│ ⚠️  Problem: Implementation   │ ✓  Describes relationships simply   │
│ AI knows database better      │ ✓  Focuses on what, not how         │
│                               │                                     │
├───────────────────────────────┼─────────────────────────────────────┤
│                               │                                     │
│ "Fix the API endpoint to      │ "When someone submits an invalid    │
│  handle validation errors"    │  email, show them a helpful error   │
│                               │ message"                            │
│                               │                                     │
│ ⚠️  Problem: Mixing concerns  │ ✓  User-focused outcome             │
│ Assumes technical knowledge   │ ✓  Clear cause and effect           │
│                               │                                     │
└───────────────────────────────┴─────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│  THE PATTERN: Good Prompts Share These Traits                       │
│                                                                     │
│  ✓  Describe WHAT should happen, not HOW it should happen          │
│  ✓  Use plain English, not technical jargon                        │
│  ✓  Focus on user experience and outcomes                          │
│  ✓  Include specific details (file types, size limits, text shown) │
│  ✓  Think in terms of "when X happens, do Y"                       │
│                                                                     │
│  The question to ask yourself:                                     │
│  "If I was explaining this feature to a friend who isn't technical,│
│   could they understand what I want the app to do?"                │
│                                                                     │
│  If yes → good prompt. If no → too technical.                      │
└─────────────────────────────────────────────────────────────────────┘
```

## Key Labels and Text

**Column Headers:**
- Left: "❌ DOESN'T WORK"
- Right: "✅ WORKS WELL"

**Four Comparison Rows:**

**Row 1: Vague vs. Specific**
- Bad: "I need a user system"
  - Problem: "Too vague - AI doesn't know what you want"
- Good: "Users should sign up with email and password, log in, and have a profile page showing their name and bio"
  - Why: "Specific outcome described, Clear features listed"

**Row 2: Too Technical vs. Outcome-Focused**
- Bad: "Implement JWT-based auth with bcrypt and token rotation"
  - Problem: "Too technical - You're telling AI HOW to code"
- Good: "Users should stay logged in even if they close the browser. Login should be secure"
  - Why: "Describes behavior not code, Lets AI choose best method"

**Row 3: Implementation vs. Relationships**
- Bad: "Create a PostgreSQL table with foreign keys and junction tables"
  - Problem: "Implementation details - AI knows database better"
- Good: "Users can save multiple bookmarks. Each bookmark should remember who saved it and when"
  - Why: "Describes relationships simply, Focuses on what not how"

**Row 4: Technical vs. User-Focused**
- Bad: "Fix the API endpoint to handle validation errors"
  - Problem: "Mixing concerns - Assumes technical knowledge"
- Good: "When someone submits an invalid email, show them a helpful error message"
  - Why: "User-focused outcome, Clear cause and effect"

**Bottom Pattern Box:**
"THE PATTERN: Good Prompts Share These Traits"
- 5 bullet points of shared characteristics
- Self-check question: "Could a non-technical friend understand this?"
- Simple rule: "If yes → good prompt. If no → too technical."

## Purpose/Benefit Statement

**Why this diagram helps:**
This is the make-or-break skill for vibe coding. If readers can't describe features effectively, they'll get stuck. This diagram:
1. Shows concrete before/after examples (not abstract advice)
2. Explains WHY each bad prompt fails (not just "don't do this")
3. Provides a pattern to recognize good prompts
4. Gives a self-check question to validate their own prompts
5. Builds confidence by showing it's simpler than they think

**The "aha" moment this creates:**
"Oh! I've been trying to sound technical to impress the AI, but I should just describe what I want like I'm talking to a person." This removes impostor syndrome and the false belief that you need to "speak code" to AI.

**Real-world impact:**
After seeing this diagram, when readers write prompts they'll:
- Catch themselves using jargon and simplify
- Focus on outcomes ("users should be able to...") not implementation
- Ask "would my non-technical friend understand this?"
- Feel less pressure to sound "technical"

This diagram directly addresses the #1 failure mode of beginners: thinking they need to learn technical terminology to work with AI. It shows that clarity > technical accuracy, and plain English is not only acceptable—it's preferred.
