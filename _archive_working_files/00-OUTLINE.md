# Vibe Coding from Zero: Ship Your First AI Product Without Coding

## Master Outline

**Target Audience:** Domain experts with zero coding background  
**Promise:** Ship your first AI product in 7 days without learning to code  
**Format:** 50-60 pages, beginner-friendly, conversational tone  
**Author:** Jenny Ouyang | buildtolaunch.substack.com

---

## Front Matter
- Title Page
- About the Author
- How to Use This Guide
- Newsletter CTA Page

## Chapter 1: The Vibe Coding Method (5-7 pages)
**Goal:** Build confidence, establish credibility, explain philosophy

### 1.1 Why This Works
- You don't need to be technical to build products
- AI changes the building game completely
- Domain expertise > coding knowledge

### 1.2 Who This Is For
- Domain experts with product ideas
- People who tried to learn coding and bounced off
- Creators who want to build tools for their audience
- Professionals who want to solve industry problems

### 1.3 What You'll Be Able to Build
- Web applications with user accounts
- Tools that save/process data
- Products you can actually sell
- Real examples from real builders

### 1.4 The Vibe Coding Philosophy
- Articulate vision, not syntax
- Think in shapes and flows, not code
- Trust AI to handle implementation
- Focus on what matters: solving problems

### 1.5 Success Stories
- 3 short examples of non-technical people who shipped
- What they built, how long it took
- Key insight from each

---

## Chapter 2: Understanding the Shape of Apps (8-10 pages)
**Goal:** Build just enough mental models to direct AI effectively

### 2.1 The Restaurant Analogy
- Front-end = dining room (what customers see)
- Back-end = kitchen (where the work happens)
- Database = pantry (where ingredients are stored)
- APIs = menu orders (how front talks to back)

### 2.2 What Happens When You Use an App
- You type a URL
- The app shows you a page
- You click a button
- Something happens (saved, updated, etc.)
- Simple flow diagram in plain English

### 2.3 The Three Core Pieces
- **Display layer** - What users see and interact with
- **Logic layer** - What happens when they interact
- **Storage layer** - Where information lives

### 2.4 How They Work Together
- User action triggers logic
- Logic reads/writes storage
- Display updates to show changes
- Real example: Instagram post

### 2.5 What You Can Safely Ignore
- How databases actually store bytes
- Exactly how the internet routes requests
- Programming language syntax details
- Everything that happens "under the hood"

### 2.6 Mental Models That Matter
- Apps are conversations (request/response)
- Data has shapes (users, posts, comments)
- Everything is connected (relationships)
- State changes over time (data updates)

---

## Chapter 3: Choosing Your Stack (10-12 pages)
**Goal:** Make clear, opinionated recommendations to avoid decision paralysis

### 3.1 The Decision You Actually Need to Make
- Not "what technology" but "what type of app"
- Simple decision tree with 3 paths
- Recommended stack for each

### 3.2 Path 1: Static Website / Portfolio
**Stack:** React + Tailwind + Netlify
- When to choose this
- What it can and can't do
- Why this combination works
- Example: portfolio site

### 3.3 Path 2: Web App with Users
**Stack:** Next.js + Supabase + Vercel
- When to choose this (most common)
- What it can and can't do  
- Why this combination works
- Example: subscription tool

### 3.4 Path 3: Data-Heavy / Python App
**Stack:** Flask + PostgreSQL + Railway
- When to choose this
- What it can and can't do
- Why this combination works
- Example: analysis dashboard

### 3.5 The Tools You'll Use
- **AI Assistant:** Claude or ChatGPT (for writing code)
- **Code Editor:** Cursor (AI-powered)
- **Version Control:** GitHub (backup and sharing)
- Why these specific choices

### 3.6 What You're Actually Telling AI
- Not "write me a function"
- But "I need users to be able to save their preferences"
- Examples of good vs bad prompts
- How to describe what you want

---

## Chapter 4: Your First Build - Tutorial (12-15 pages)
**Goal:** Walk through building something real, step by step

### 4.1 What We're Building
- Simple bookmark saver app
- Users can save/organize links
- Why this is a good first project

### 4.2 Setting Up Your Tools
- Install Cursor
- Create GitHub account
- Set up Supabase account
- Connect everything (with screenshots)

### 4.3 Step 1: Create the Project
- Actual prompt to give Claude/Cursor
- What the AI will generate
- What to look for in the response
- Running it for the first time

### 4.4 Step 2: Add User Authentication  
- Why every app needs login
- The prompt for adding auth
- Testing: creating an account
- What just happened behind the scenes

### 4.5 Step 3: Create the Database
- Describing your data to AI
- The prompt for database setup
- Understanding what got created
- Adding your first bookmark

### 4.6 Step 4: Build the Interface
- Describing what you want users to see
- The prompt for UI creation
- Reviewing and refining the design
- Making it look better

### 4.7 Step 5: Deploy It Live
- Why deployment matters
- The prompt for deployment setup
- Watching it go live
- Your first real URL!

### 4.8 What You Just Learned
- You can build real things
- AI handles the technical details
- Clear description = good results
- Iteration is normal

---

## Chapter 5: Common Building Blocks (10-12 pages)
**Goal:** Reference guide for typical features every app needs

### 5.1 User Authentication (Login/Signup)
**What it is:** How users prove who they are
**When you need it:** Any app with user accounts
**What to tell AI:**
- "I need user signup with email and password"
- "Add password reset functionality"  
- "Let users log in with Google"
**Watch out for:**
- Storing passwords correctly (AI handles this)
- Email verification (optional but recommended)
**Example prompt:** [Full working prompt]

### 5.2 Databases (Storing Information)
**What it is:** Where your app remembers things
**When you need it:** Anything interactive
**What to tell AI:**
- "Create a database for user profiles"
- "I need to store [type of data] with these fields"
- "Connect posts to the user who created them"
**Watch out for:**
- Describing relationships between data
- Understanding which data connects to what
**Example prompt:** [Full working prompt]

### 5.3 File Uploads (Images, Documents)
**What it is:** Letting users upload files
**When you need it:** Profile pictures, documents, media
**What to tell AI:**
- "Let users upload a profile picture"
- "Support PDF uploads up to 10MB"
- "Store images in organized folders"
**Watch out for:**
- File size limits
- Image optimization for web
**Example prompt:** [Full working prompt]

### 5.4 Payments (Getting Paid)
**What it is:** Processing money
**When you need it:** Selling products or subscriptions
**What to tell AI:**
- "Integrate Stripe for one-time payments"
- "Add subscription billing with Stripe"
- "Handle payment success and failure"
**Watch out for:**
- Test mode vs live mode
- Webhooks (AI will explain)
**Example prompt:** [Full working prompt]

### 5.5 Email (Sending Notifications)
**What it is:** Sending automated emails
**When you need it:** Confirmations, notifications, marketing
**What to tell AI:**
- "Send welcome email when users sign up"
- "Email notification when someone comments"
- "Weekly digest of new content"
**Watch out for:**
- Email service limits (Resend, SendGrid)
- Spam folder issues
**Example prompt:** [Full working prompt]

### 5.6 Deployment (Putting It Online)
**What it is:** Making your app accessible via URL
**When you need it:** Every project
**What to tell AI:**
- "Deploy this to Vercel"
- "Set up custom domain"
- "Configure environment variables"
**Watch out for:**
- Environment variables (AI will handle)
- Build errors (how to read them)
**Example prompt:** [Full working prompt]

---

## Chapter 6: When Things Break (8-10 pages)
**Goal:** Debugging through conversation, not through code

### 6.1 The Most Common Issues
- "It doesn't work" (how to be more specific)
- "I got an error message"
- "It works on my computer but not online"
- "Users are seeing each other's data"

### 6.2 How to Debug with AI
**Step 1:** Describe what you expected to happen
**Step 2:** Describe what actually happened
**Step 3:** Share the error message
**Step 4:** Ask AI to explain and fix
- Example dialogue

### 6.3 Reading Error Messages
- Don't panic at red text
- The important parts of an error
- How to copy/paste to AI
- Example error breakdowns

### 6.4 When to Start Over vs Keep Going
- Signs you should restart
- Signs you're close to fixing it
- How to save your progress first

### 6.5 Getting Unstuck
- Ask AI to explain what the code does
- Request a simpler version
- Break the problem into smaller pieces
- When to ask human help

### 6.6 Prevention Tips
- Save your work frequently (Git)
- Test each feature before adding more
- Keep prompts clear and specific
- Document what works

---

## Chapter 7: What's Next (5-7 pages)
**Goal:** Bridge to advanced resources and newsletter

### 7.1 You Just Did Something Remarkable
- Recap what you learned
- This is just the beginning
- The path from here

### 7.2 Going Deeper
- Building more complex features
- Understanding architecture
- Performance optimization
- When/how to learn actual code

### 7.3 The Technical Playbook (Teaser)
**For subscribers:** Advanced patterns and templates
- Architecture decision frameworks
- Database design deep dives
- Deployment strategies
- Battle-tested prompts and rules
- [Link to paid resource]

### 7.4 Join the Community
**Build to Launch Newsletter:**
- Weekly AI building tips
- Real builder interviews  
- New prompt templates
- Live build sessions
- [Sign up link]

### 7.5 Show Your Work
- Share what you built
- Tag @jennyoyang on Twitter
- Join the discussion
- Help the next person

### 7.6 Your Next Project
- Ideas for second project
- How to push your skills
- Resources for learning more

---

## Back Matter
- Glossary of Terms
- Quick Reference - Common Prompts
- Recommended Resources
- About the Author (Extended)
- Newsletter CTA (Final page)

---

## Newsletter CTA Placements

**Page 2** (Right after title):
"Get weekly AI building tips: buildtolaunch.substack.com"

**End of each chapter** (small footer):
"For more: buildtolaunch.substack.com"

**Chapter 7** (full pitch):
"Want advanced patterns, templates, and community access? Join Build to Launch newsletter for weekly AI building insights, prompt libraries, and live build sessions."

**Final page** (dedicated CTA):
Full benefits list, social proof, clear signup link

---

## Target Length: 50-60 pages
- Chapter 1: 6 pages
- Chapter 2: 9 pages  
- Chapter 3: 11 pages
- Chapter 4: 13 pages
- Chapter 5: 11 pages
- Chapter 6: 9 pages
- Chapter 7: 6 pages
- Front/Back matter: 5 pages
**Total: ~60 pages**
