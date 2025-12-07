---
id: debugging-checklist
title: Debugging Checklist
sidebar_position: 4
---

# Debugging Checklist: Your Systematic Process

> **Print this. Keep it next to your computer. Run through it every time something breaks.**

---

## When Something Breaks, Check These (In Order):

### Phase 1: The Obvious (30% of bugs live here)

- [ ] **Is the dev server running?** Check terminal for "Ready on http://localhost:3000"
- [ ] **Did you save all files?** Cmd+S (Mac) or Ctrl+S (Windows)
- [ ] **Did you refresh the browser?** Cmd+R (Mac) or Ctrl+R (Windows)
- [ ] **Did you restart the server after .env changes?** Ctrl+C then `npm run dev`

**Stop here if it works. Don't question it. Move on.**

---

### Phase 2: Gather Information

#### Open Browser DevTools (F12 or Cmd+Option+I)

**Console Tab:**
- [ ] **Any red errors?** Copy the first error message completely
- [ ] **Any warnings?** Note them (might be related)
- [ ] **Nothing?** That's information too - means frontend is fine

**Network Tab:**
- [ ] **Click "XHR" or "Fetch" filter** to see API requests
- [ ] **Any red (failed) requests?** Click them to see why they failed
- [ ] **Check Status codes:** 200 = good, 401 = not logged in, 404 = wrong URL, 500 = server error
- [ ] **Check Response tab** in failed request for error messages

#### If Using Database (Supabase/etc):

- [ ] **Check Table Editor** - Is the data actually there?
- [ ] **Check Logs** - Any errors from database?
- [ ] **Check you're logged in** - Many silent fails are auth issues

#### In Your Terminal:

- [ ] **Any error messages?** Copy them completely
- [ ] **Server still running?** Look for "compiled successfully"

---

### Phase 3: Ask AI Effectively

**Copy this template. Fill in the blanks. Paste to Cursor/ChatGPT/Claude:**

```
I'm trying to: [what you were doing]

Expected: [what should happen]

Actually happening: [what is happening instead]

Error message (if any):
[paste exact error from console/terminal]

What I've checked:
- Dev server is running: [yes/no]
- Saved all files: [yes/no]
- Refreshed browser: [yes/no]
- Logged in (if needed): [yes/no]
- Console errors: [paste them or say "none"]
- Network tab: [any failed requests? which ones?]

Relevant code:
[paste the file that's probably related - component, API route, etc.]
```

**Example of good description:**

```
I'm trying to: Save a bookmark when user clicks submit button

Expected: Bookmark appears in the list below the form

Actually happening: Form submits but bookmark doesn't appear. No error shown in UI.

Error message:
In browser console I see:
"Failed to fetch POST http://localhost:3000/api/bookmarks"
Network tab shows 401 Unauthorized

What I've checked:
- Dev server is running: yes
- Saved all files: yes
- Refreshed browser: yes
- Logged in: yes (I can see my profile)
- Console errors: Only the "Failed to fetch" above
- Network tab: POST to /api/bookmarks returns 401

Relevant code: [paste app/api/bookmarks/route.ts]
```

---

### Phase 4: Still Stuck After AI Response?

**If AI's fix didn't work:**
- [ ] **Reply to AI with:** "Tried that. Now this happens: [new error/behavior]"
- [ ] **Include new error messages** if any appeared
- [ ] **Try the fix again** in case you missed a step

**If AI seems confused:**
- [ ] **Start a fresh conversation** with clearer problem description
- [ ] **Break down the problem:** Ask "Is X configured correctly?" before "Why isn't Y working?"
- [ ] **Try different AI tool:** Switch between Cursor/ChatGPT/Claude

**If stuck for 30+ minutes:**
- [ ] **Take a break** - seriously, walk away for 10 minutes
- [ ] **Google the exact error message** - someone else has hit this
- [ ] **Check library docs** - Supabase docs, Next.js docs, etc.
- [ ] **Try incognito mode** - rules out browser extension issues
- [ ] **Clear browser cache** - DevTools > Application > Clear Storage

**If stuck for 2+ hours:**
- [ ] **Commit current work** - `git add . && git commit -m "WIP"`
- [ ] **Consider starting over** - sometimes faster to rebuild than debug
- [ ] **Ask in communities** - r/webdev, library Discord servers (be specific!)

---

## Common Error Patterns → Quick Diagnosis

| You See This | Likely Cause | Where to Check |
|-------------|--------------|----------------|
| "Cannot read property X of undefined" | Accessing data that doesn't exist | Add console.log before the error line |
| "Failed to fetch" | Network request failed | Browser Network tab, check API URL |
| "[Something] is not a function" | Wrong import or typo | Check import statement, file path |
| "Module not found" | Missing file or package | Check file exists, run `npm install` |
| "Port already in use" | Another server running | Run `kill $(lsof -t -i:3000)` |
| "Environment variable undefined" | .env not loaded or missing | Check .env.local exists, restart server |
| "Authentication required / 401 error" | Not logged in or session expired | Clear cookies, log in again |
| Data saves but doesn't show | UI not refreshing | Check fetch query, React state |
| CSS classes not working | Tailwind not compiling | Check tailwind.config.js, restart server |

---

## Emergency Techniques

### Add console.log() to See What's Happening

```javascript
// Before database call
console.log("About to fetch bookmarks for user:", userId)

// After database call
console.log("Fetched bookmarks:", bookmarks)

// In event handler
console.log("Button clicked, form values:", formData)
```

**Check browser console to see what printed. This shows you where things go wrong.**

### Roll Back to Last Working Version

```bash
# See recent commits
git log --oneline

# Go back to working commit
git checkout [commit-id]

# Or just reset last commit (keeps your changes)
git reset HEAD~1
```

---

## When to Keep Fixing vs Start Over

### Keep Fixing If:
- Error makes sense and AI can fix it
- Been less than 30 minutes on this issue
- Learning something useful from debugging
- Fix is localized (one file, one feature)

### Start Over If:
- Multiple cascading errors appearing
- Lost track of what you changed
- AI giving contradictory advice
- Been 2+ hours with no progress
- Broken something fundamental

**Starting over isn't failure. Sometimes rebuilding with better prompts is faster than untangling a mess.**

---

## Prevention Checklist (Do These Always)

- [ ] **Commit often** - After each working feature: `git add . && git commit -m "Feature works"`
- [ ] **Test incrementally** - Build one thing, test it, commit. Don't build 5 things then test.
- [ ] **Be specific with AI** - "Add bookmark save with validation" not "make bookmarks work"
- [ ] **Read AI's code before applying** - Quick scan for anything obviously wrong

---

## Remember

**Things will break. That's not failure - that's building.**

Every developer debugs. You're not doing it wrong. You're doing it.

The goal isn't perfect code. The goal is shipped code.

**Each bug you fix makes you better. Each fix is progress.**

---

**Still stuck? You're not alone:**

- r/webdev on Reddit
- Library Discord servers (Supabase, Next.js, etc.)
- Stack Overflow (search first, then ask)

**When asking: Be specific. Include error. Say what you tried. People will help.**
