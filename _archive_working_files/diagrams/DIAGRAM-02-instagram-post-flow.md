# Diagram 02: Instagram Post Flow

## Chapter Placement
**Chapter 2: Understanding the Shape of Apps**

## Exact Location
Place immediately after the section "**The entire journey:**" (line 77)

Before the section "## The Three Core Pieces (In Plain English)" (line 81)

## Diagram Type
**Sequential flow diagram** showing the journey of data through the system

## Detailed Description
A left-to-right flow showing what happens when a user posts on Instagram, with each step clearly labeled and the data transforming as it moves through the system.

### Visual Layout:

```
┌──────────────────────────────────────────────────────────────────────┐
│              WHAT HAPPENS WHEN YOU POST ON INSTAGRAM                 │
└──────────────────────────────────────────────────────────────────────┘

 [1] YOUR PHONE               [2] SENT TO SERVER           [3] PROCESSING
 ┌────────────┐               ┌──────────────┐             ┌─────────────┐
 │            │               │              │             │             │
 │ 📱         │  ─────────►   │  ☁️ API      │  ────────►  │ ⚙️ Back-End │
 │            │               │              │             │             │
 │ You type:  │   [Request    │  Instagram   │  [Receives  │ Checks:     │
 │ "Caption"  │    travels    │  receives    │   your      │ • Are you   │
 │ Upload     │    across     │  your        │   data]     │   logged in?│
 │ photo      │    internet]  │  post]       │             │ • Valid     │
 │            │               │              │             │   photo?    │
 │ Tap SHARE  │               │              │             │ • Process   │
 │            │               │              │             │   image     │
 └────────────┘               └──────────────┘             └─────────────┘
                                                                   │
                                                                   ▼
 [5] YOU SEE RESULT           [4] SAVE TO DATABASE
 ┌────────────┐               ┌──────────────┐
 │            │               │              │
 │ ✅         │  ◄─────────   │  💾 Database │
 │            │               │              │
 │ "Post      │   [Success    │  Saves:      │
 │ shared     │    message    │  • Caption   │
 │ success!"  │    returns]   │  • Photo     │
 │            │               │  • Your ID   │
 │ See new    │               │  • Timestamp │
 │ post on    │               │              │
 │ profile    │               │  Updates:    │
 │            │               │  • Followers'│
 │            │               │    feeds     │
 └────────────┘               └──────────────┘

 ┌──────────────────────────────────────────────────────────────┐
 │ COMPLETE JOURNEY: Front-End → Back-End → Database →          │
 │                   Back-End → Front-End                       │
 └──────────────────────────────────────────────────────────────┘
```

## Key Labels and Text

**Step Numbers:**
1. "Your Phone (Front-End)"
2. "Sent to Server (API)"
3. "Processing (Back-End)"
4. "Save to Database"
5. "You See Result (Front-End)"

**In-Between Arrows:**
- "Request travels across internet"
- "Receives your data"
- "Stores everything"
- "Success message returns"

**Bottom Summary Box:**
"Complete Journey: Front-End → Back-End → Database → Back-End → Front-End"

## Purpose/Benefit Statement

**Why this diagram helps:**
Abstract concepts like "request/response" become concrete when readers see a familiar action (posting on Instagram) broken down into visual steps. This diagram:
1. Shows that complex actions are just sequential steps
2. Demystifies what happens "behind the scenes"
3. Illustrates why all three pieces (front-end, back-end, database) are necessary
4. Gives readers a reference for understanding ANY app interaction

When readers build their own features later, they can mentally trace the same journey: "User does X → sent to server → back-end processes → database stores → result shows to user." This is the template for all app interactions.
