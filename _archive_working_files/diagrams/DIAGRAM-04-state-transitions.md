# Diagram 04: State Transitions Over Time

## Chapter Placement
**Chapter 2: Understanding the Shape of Apps**

## Exact Location
Place immediately after the section "### 4. State Changes Over Time (Updates)" (line 267)

Before the section "## Practical Examples: How to Describe What You Want" (line 269)

## Diagram Type
**State machine diagram** showing how things change over time, with multiple real-world examples

## Detailed Description
Three parallel examples showing common state transitions in apps, helping readers understand that things don't just exist—they move through stages.

### Visual Layout:

```
┌─────────────────────────────────────────────────────────────────────┐
│                    HOW THINGS CHANGE OVER TIME                      │
└─────────────────────────────────────────────────────────────────────┘

EXAMPLE 1: USER LOGIN STATUS
────────────────────────────────────────────────────────────────────────
  ┌──────────────┐    user enters     ┌──────────────┐
  │ NOT LOGGED   │    email/password  │   LOGGED     │
  │     IN       │ ─────────────────► │     IN       │
  │              │                    │              │
  └──────────────┘                    └──────────────┘
         ▲                                    │
         │                                    │
         │          user clicks logout        │
         └────────────────────────────────────┘


EXAMPLE 2: BLOG POST STATUS
────────────────────────────────────────────────────────────────────────
  ┌────────┐   author      ┌────────┐   author     ┌──────────┐
  │ DRAFT  │   saves       │ READY  │   clicks     │PUBLISHED │
  │        │ ────────────► │        │ ───────────► │          │
  └────────┘               └────────┘              └──────────┘
     ▲                        │                          │
     │     author edits       │                          │
     └────────────────────────┘                          │
     │                                                    │
     │          author unpublishes post                  │
     └───────────────────────────────────────────────────┘


EXAMPLE 3: ORDER LIFECYCLE
────────────────────────────────────────────────────────────────────────
  ┌─────────┐  customer   ┌─────────┐  payment  ┌─────────┐  item
  │ CART    │  clicks     │PENDING  │  goes     │  PAID   │  ships
  │         │  checkout   │ PAYMENT │  through  │         │  out
  └─────────┘ ──────────► └─────────┘ ────────► └─────────┘ ─────►
                                                       │
     ┌──────────────────────────────────────────────┐ │
     │                                                │ │
     ▼                                                ▼ ▼
  ┌─────────┐                                    ┌──────────┐
  │CANCELLED│                                    │ SHIPPED  │
  │         │                                    │          │
  └─────────┘                                    └──────────┘
                                                      │
                                                      ▼
                                                 ┌──────────┐
                                                 │DELIVERED │
                                                 │          │
                                                 └──────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ KEY CONCEPT: Things move through states based on actions            │
│                                                                     │
│ When you describe features to AI, think:                           │
│ • What states exist? (draft, published, cancelled)                 │
│ • What triggers transitions? (click publish, enter password)       │
│ • Can you go backwards? (unpublish, logout)                        │
└─────────────────────────────────────────────────────────────────────┘
```

## Key Labels and Text

**Example 1 Labels:**
- States: "NOT LOGGED IN" → "LOGGED IN"
- Triggers: "user enters email/password", "user clicks logout"
- Shows reversibility (can log back out)

**Example 2 Labels:**
- States: "DRAFT" → "READY" → "PUBLISHED"
- Triggers: "author saves", "author clicks publish"
- Shows circular flow (can edit draft again, unpublish)

**Example 3 Labels:**
- States: "CART" → "PENDING PAYMENT" → "PAID" → "SHIPPED" → "DELIVERED"
- Alternative path: "CANCELLED" (can happen from multiple states)
- Shows one-way progression with exception path

**Bottom Teaching Box:**
"KEY CONCEPT: Things move through states based on actions"
- Questions to ask when designing features
- How to think about state transitions

## Purpose/Benefit Statement

**Why this diagram helps:**
State transitions are an abstract concept that confuses beginners. This diagram:
1. Makes state changes concrete with familiar examples
2. Shows that state isn't binary—things can have multiple stages
3. Illustrates that transitions happen for reasons (user actions, time, external events)
4. Demonstrates both linear flows and circular flows

When readers describe features to AI later, they'll think in states: "Users start as guests, become members when they sign up, and can be inactive if they don't log in for 30 days." This is sophisticated product thinking made accessible.

**Real-world application:** Every feature involves state. Understanding this helps readers describe:
- "When the post is in draft, only the author sees it"
- "When payment is pending, show a loading spinner"
- "When the order ships, send an email"

This diagram teaches readers to think about the lifecycle of things in their app, not just static snapshots.
