# Diagram 06: The Vibe Coding Process

## Chapter Placement
**Chapter 2: Understanding the Shape of Apps**

## Exact Location
Place immediately after the section "## The Flow of Building" (line 301)

After the iteration example ends (line 324), before "**Notice:**" paragraph

## Diagram Type
**Circular process flow diagram** showing the iterative nature of vibe coding

## Detailed Description
A circular diagram showing the continuous loop of describing, building, testing, and refining, emphasizing that this is an iterative process, not a linear one.

### Visual Layout:

```
┌─────────────────────────────────────────────────────────────────────┐
│                    THE VIBE CODING LOOP                             │
│                   (This is your workflow)                           │
└─────────────────────────────────────────────────────────────────────┘

                    ┌──────────────────────┐
                    │   1. DESCRIBE        │
                    │   what you want      │
                    │                      │
                    │  "I want users to    │
                    │  upload a profile    │
                    │  picture"            │
                    └──────────┬───────────┘
                               │
                               ▼
    ┌──────────────────┐             ┌──────────────────┐
    │  6. ITERATE      │             │  2. CLARIFY      │
    │  if needed       │             │  details         │
    │                  │             │                  │
    │ "Make image      │             │ AI asks:         │
    │  smaller" or     │             │ • File types?    │
    │ "Add crop tool"  │             │ • Size limit?    │
    └────────┬─────────┘             └─────────┬────────┘
             │                                  │
             │                                  ▼
             │                       ┌──────────────────┐
             │                       │  3. REFINE       │
             │                       │  your vision     │
             │                       │                  │
             │                       │ "Allow JPG/PNG   │
             │                       │  up to 5MB"      │
             │                       └─────────┬────────┘
             │                                 │
             │                                 ▼
    ┌────────┴─────────┐             ┌──────────────────┐
    │  5. TEST         │             │  4. AI BUILDS    │
    │  does it work?   │             │  generates code  │
    │                  │             │                  │
    │ ✅ Works? Done!  │             │ • Upload form    │
    │ ❌ Issue? Back   │◄────────────│ • File handling  │
    │    to iterate    │             │ • Storage setup  │
    └──────────────────┘             └──────────────────┘


┌─────────────────────────────────────────────────────────────────────┐
│ KEY INSIGHT: You never leave this loop                             │
│                                                                     │
│ Building isn't linear—it's circular. You'll go through this loop   │
│ hundreds of times. Each time you:                                  │
│ • Describe more clearly                                            │
│ • Test more thoroughly                                             │
│ • Understand your product better                                   │
│                                                                     │
│ This is normal. This is how vibe coding works.                     │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ WHERE YOU SPEND YOUR TIME:                                         │
│                                                                     │
│ Describing/Clarifying: ████████░░ 40%                              │
│ Testing:               ██████░░░░ 30%                              │
│ Iterating/Refining:    █████░░░░░ 25%                              │
│ Waiting for AI:        █░░░░░░░░░  5%                              │
│                                                                     │
│ Notice: You spend almost NO time actually writing code.            │
└─────────────────────────────────────────────────────────────────────┘
```

## Key Labels and Text

**Six Steps in the Circle:**

1. **DESCRIBE what you want**
   - Example: "I want users to upload a profile picture"

2. **CLARIFY details**
   - "AI asks: File types? Size limit?"

3. **REFINE your vision**
   - Example: "Allow JPG/PNG up to 5MB"

4. **AI BUILDS generates code**
   - Bullet list: Upload form, File handling, Storage setup

5. **TEST does it work?**
   - "✅ Works? Done!"
   - "❌ Issue? Back to iterate"

6. **ITERATE if needed**
   - Examples: "Make image smaller" or "Add crop tool"
   - Arrow loops back to step 1

**Bottom Teaching Box 1:**
"KEY INSIGHT: You never leave this loop"
- Explain circular vs. linear
- Emphasize this is normal and expected
- Each loop improves understanding

**Bottom Teaching Box 2:**
"WHERE YOU SPEND YOUR TIME:"
- Bar chart showing time allocation
- Describe/Clarify: 40%
- Testing: 30%
- Iterating: 25%
- Waiting: 5%
- Final note: "You spend almost NO time actually writing code"

## Purpose/Benefit Statement

**Why this diagram helps:**
Many beginners think building software is linear: learn → write code → deploy → done. This diagram corrects that misconception by:
1. Showing building is iterative and circular, not linear
2. Removing shame from "going back" (it's part of the process!)
3. Illustrating where effort actually goes (describing and testing, not coding)
4. Demonstrating that AI makes the coding part the SMALLEST part
5. Setting realistic expectations (you'll loop many times—that's normal)

**Mindset shift this creates:**
- "I don't need to get it perfect the first time" (loop back is expected)
- "Iteration isn't failure, it's the process" (loop is a feature, not a bug)
- "My job is describing and testing, not coding" (clear role definition)
- "AI handles the parts I don't know" (removes technical bottleneck)

When readers hit frustration later ("why am I going back and forth so much?"), they can return to this diagram and think: "Oh right, this IS the process. I'm doing it correctly."

**Critical teaching moment:** The time allocation chart at the bottom is eye-opening. Readers expect they should be "coding" most of the time. Showing that only 5% is waiting for AI (the actual code generation) while 95% is human thinking/testing reframes what "building" means in the AI era.
