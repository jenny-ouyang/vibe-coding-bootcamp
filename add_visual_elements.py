#!/usr/bin/env python3
"""
Add visual elements to guide chapters:
- Mermaid diagrams
- Callout boxes
- Comparison tables
"""

import re

# Chapter 3: Add decision flowchart at the beginning
chapter_3_flowchart = """
## Quick Decision Flowchart

```mermaid
graph TD
    A[What are you building?] --> B{Need user<br/>accounts?}
    B -->|No| C[Simple Website<br/>Path 1]
    B -->|Yes| D{What tech do<br/>you know?}
    D -->|None/Web| E[Next.js + Supabase<br/>Path 2 ⭐]
    D -->|Python| F{Data-heavy or<br/>ML work?}
    F -->|Yes| G[Flask + PostgreSQL<br/>Path 3]
    F -->|No| E

    C --> H[Deploy to Netlify]
    E --> I[Deploy to Vercel]
    G --> J[Deploy to Railway]

    style E fill:#90EE90
    style A fill:#FFE4B5
    style H fill:#87CEEB
    style I fill:#87CEEB
    style J fill:#87CEEB
```

💡 **Most people should choose Path 2** (Next.js + Supabase) - it's the most versatile and AI-friendly.

---
"""

# Chapter 3: Comparison table
comparison_table = """
## Quick Comparison Table

| Feature | Path 1: Simple Site | Path 2: Web App ⭐ | Path 3: Python |
|---------|---------------------|-------------------|----------------|
| **Best For** | Content, landing pages | SaaS, user apps | Data analysis, ML |
| **Complexity** | ⭐ Easiest | ⭐⭐ Moderate | ⭐⭐⭐ Advanced |
| **User Accounts** | ❌ No | ✅ Yes | ✅ Yes |
| **Database** | ❌ No | ✅ PostgreSQL | ✅ PostgreSQL |
| **Deployment** | Netlify (1-click) | Vercel (1-click) | Railway (config needed) |
| **Cost (Start)** | $0/month | $0/month | $5/month |
| **Cost (Growth)** | $0/month | $25/month | $20-50/month |
| **Learning Curve** | Gentle | Moderate | Steeper |
| **AI Support** | Excellent | Excellent | Good |
| **Time to Deploy** | 2-4 hours | 4-8 hours | 6-12 hours |

⚠️ **Don't overthink this.** If unsure, start with Path 2. You can always switch later.

---
"""

# Chapter 2: Mermaid diagram for request flow
chapter_2_mermaid = """
## Visual: Request Flow Diagram

```mermaid
sequenceDiagram
    participant U as 👤 User<br/>(Browser)
    participant F as 📱 Front-End<br/>(React)
    participant B as ⚙️ Back-End<br/>(Next.js API)
    participant D as 💾 Database<br/>(Supabase)

    U->>F: 1. Clicks "Save Post"
    Note over F: Captures form data
    F->>B: 2. POST /api/posts<br/>{title, content}
    Note over B: Validates data
    B->>D: 3. INSERT INTO posts
    D-->>B: 4. Returns success + ID
    B-->>F: 5. Returns {success: true}
    F-->>U: 6. Shows "Post saved!"
    Note over U: User sees confirmation
```

💡 **This flow happens in milliseconds** - users just see instant feedback.

---
"""

# Chapter 6: Debugging flowchart
chapter_6_flowchart = """
## Debugging Decision Tree

```mermaid
graph TD
    A[Something's broken 😓] --> B{Is dev<br/>server running?}
    B -->|No| C[Start server:<br/>npm run dev]
    B -->|Yes| D{Error in<br/>console?}
    C --> D
    D -->|Yes| E{Red error<br/>message?}
    D -->|No| F{Network<br/>request failed?}
    E -->|Yes| G[Copy error message<br/>Ask AI for fix]
    E -->|No| H[Check Network tab<br/>for failed requests]
    F -->|Yes| I[Check Supabase logs<br/>Auth issues?]
    F -->|No| J[Add console.log<br/>to find where it breaks]
    H --> K{Found the<br/>problem?}
    I --> K
    J --> K
    G --> L[Apply AI's fix]
    K -->|Yes| L
    K -->|No| M[Ask in<br/>Discord/Reddit]
    L --> N{Fixed?}
    N -->|Yes| O[✅ Ship it!]
    N -->|No| P{Spent 2+<br/>hours?}
    P -->|Yes| Q[Start fresh]
    P -->|No| G

    style A fill:#FFB6C1
    style O fill:#90EE90
    style Q fill:#FFE4B5
```

⚠️ **Pro tip:** If you're stuck for 2+ hours, starting fresh is often faster than debugging deeper.

---
"""

# Callout box patterns
callout_tip = lambda text: f"\n💡 **Pro Tip:** {text}\n"
callout_warning = lambda text: f"\n⚠️ **Warning:** {text}\n"
callout_note = lambda text: f"\n📝 **Note:** {text}\n"

def add_chapter_3_visuals():
    """Add decision flowchart and comparison table to Chapter 3"""
    with open('03-choosing-stack.md', 'r') as f:
        content = f.read()

    # Insert flowchart after "## The Three Paths" section
    content = content.replace(
        '**90% of people reading this guide need Path 2.** If you\'re not sure, that\'s your path.\n\n---',
        '**90% of people reading this guide need Path 2.** If you\'re not sure, that\'s your path.\n\n' + chapter_3_flowchart
    )

    # Insert comparison table after the three paths but before Path 1 details
    # Find the position right before "## Path 1: Simple Website / Landing Page"
    content = content.replace(
        '\n---\n\n## Path 1: Simple Website / Landing Page',
        '\n' + comparison_table + '\n## Path 1: Simple Website / Landing Page'
    )

    with open('03-choosing-stack.md', 'w') as f:
        f.write(content)
    print("✅ Added visuals to Chapter 3")

def add_chapter_2_visuals():
    """Add Mermaid sequence diagram to Chapter 2"""
    with open('02-understanding-apps.md', 'r') as f:
        content = f.read()

    # Insert Mermaid diagram after the ASCII table
    # Find the section "## What Happens When You Use an App"
    content = content.replace(
        '## What Happens When You Use an App',
        chapter_2_mermaid + '## What Happens When You Use an App'
    )

    with open('02-understanding-apps.md', 'w') as f:
        f.write(content)
    print("✅ Added visuals to Chapter 2")

def add_chapter_6_visuals():
    """Add debugging flowchart to Chapter 6"""
    with open('06-debugging.md', 'r') as f:
        content = f.read()

    # Insert flowchart after "## The Debug Process" section intro
    content = content.replace(
        '### Step 1: Notice the Problem',
        chapter_6_flowchart + '### Step 1: Notice the Problem'
    )

    with open('06-debugging.md', 'w') as f:
        f.write(content)
    print("✅ Added visuals to Chapter 6")

def add_callout_boxes():
    """Add callout boxes throughout chapters"""
    # This would be more extensive - for now, the flowcharts include callouts
    print("✅ Callout boxes included in diagrams")

if __name__ == "__main__":
    print("Adding visual elements to guide...")
    add_chapter_3_visuals()
    add_chapter_2_visuals()
    add_chapter_6_visuals()
    add_callout_boxes()
    print("\n✨ Visual elements added successfully!")
