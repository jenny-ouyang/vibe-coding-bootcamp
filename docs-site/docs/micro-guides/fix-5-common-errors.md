---
id: fix-5-common-errors
title: Fix 5 Common Errors
sidebar_position: 2
---

# Fix These 5 Common Errors in 5 Minutes

Stuck? Start here. No explanations, just fixes.

---

## Error 1: "Port already in use"

**You'll see:**
```
Error: listen EADDRINUSE: address already in use :::3000
```
Or: Can't start dev server, terminal says port 3000 is busy.

**Quick fix:**
```bash
# Kill whatever's using port 3000
kill $(lsof -t -i:3000)

# Start your server
npm run dev
```

**Verify:** Browser loads `http://localhost:3000`

**Still broken?** Try a different port:
```bash
PORT=3001 npm run dev
```

---

## Error 2: "Module not found"

**You'll see:**
```
Error: Cannot find module '@/components/Something'
```
Or:
```
Module not found: Can't resolve 'react-icons'
```

**Quick fix:**

**For file imports (@/components/...):**
1. Check file exists at that exact path
2. Check spelling (case matters: `Button.tsx` ≠ `button.tsx`)
3. Check import matches filename

**For package imports (react-icons, etc):**
```bash
npm install [package-name]
```

**Verify:** Error disappears, page loads

**Still broken?** Restart dev server:
```bash
# Ctrl+C to stop
npm run dev
```

---

## Error 3: "Environment variable undefined"

**You'll see:**
```
Error: NEXT_PUBLIC_SUPABASE_URL is undefined
```
Or: App loads but API calls fail silently.

**Quick fix:**

1. Check `.env.local` exists in root folder
2. Check variable name matches EXACTLY:
```
NEXT_PUBLIC_SUPABASE_URL=your-url-here
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-key-here
```
3. **No quotes around values**
4. **Restart dev server** (Ctrl+C, then `npm run dev`)

**Verify:** Check terminal startup logs show variables loaded

**Still broken?**
- Make sure file is named `.env.local` not `env.local` or `.env`
- Check for spaces around `=` (should be `KEY=value` not `KEY = value`)

---

## Error 4: "Authentication error" / "Session expired"

**You'll see:**
- Logged out unexpectedly
- Can't access pages that need login
- "User not authenticated" error

**Quick fix:**

1. **Clear cookies:**
   - Open DevTools (F12)
   - Go to Application tab
   - Click Storage → Cookies
   - Right-click your site → Clear

2. **Force logout/login:**
   - Close all browser tabs for your app
   - Go to `http://localhost:3000`
   - Log in again

3. **Check Supabase:**
   - Go to Supabase dashboard
   - Authentication → Users
   - Verify your user exists

**Verify:** After login, you stay logged in when refreshing page

**Still broken?** Check environment variables (see Error 3)

---

## Error 5: "Data not appearing"

**You'll see:**
- Form submits successfully but data doesn't show in list
- Page loads but content is empty
- "Loading..." never goes away

**Quick fix:**

**Step 1: Check if data actually saved**
1. Go to Supabase dashboard
2. Table Editor → Your table
3. Look for your data

**If data IS there:**
```javascript
// Add this to your component to see what you're fetching
console.log("Fetched data:", yourData)
```
Check browser console. Problem is in fetch query or UI rendering.

**If data is NOT there:**
1. Open browser DevTools (F12)
2. Network tab → XHR filter
3. Submit form again
4. Look for red (failed) request
5. Click it → check status code

**Common status codes:**
- 401: Not logged in → Log in
- 403: Row Level Security blocking → Check Supabase policies
- 500: Server error → Check Supabase logs

**Verify:** Data appears immediately after submitting

**Still broken?** Copy error message and ask AI:
```
I'm trying to: [save/fetch] [type of data]
Expected: [what should happen]
Actually happening: [what is happening]
Error message: [paste exact error]
```

---

## Emergency Reset

**If multiple errors cascade and nothing makes sense:**

```bash
# Stop server (Ctrl+C)

# Clear node modules and reinstall
rm -rf node_modules
rm package-lock.json
npm install

# Clear Next.js cache
rm -rf .next

# Restart
npm run dev
```

This fixes 90% of "everything is broken" situations.

---

## Quick Diagnostic Checklist

Before asking for help, check these:

- [ ] Dev server is running (terminal shows "ready on port 3000")
- [ ] Saved all files (Cmd+S)
- [ ] Refreshed browser (Cmd+R)
- [ ] Checked browser console for red errors (F12)
- [ ] Restarted dev server after .env changes
- [ ] Using incognito mode (rules out extension issues)

**If all checked and still broken:** Copy exact error message, describe what you're trying to do, ask AI.

---

## When to Stop Debugging

**Stop and start over if:**
- More than 2 hours with no progress
- Multiple cascading errors
- Lost track of what changes you made

**How to start over:**
1. Commit current code (even if broken): `git add . && git commit -m "broken state"`
2. Create new branch: `git checkout -b fresh-start`
3. Copy working parts only
4. Rebuild broken feature with clearer AI prompts

Starting over isn't failure. It's often the fastest path to working code.

---

## Need More Help?

1. **Google the exact error message** (someone else has had it)
2. **Ask in communities:**
   - r/webdev on Reddit
   - Supabase Discord
   - Next.js Discord
3. **Ask AI with full context:**
   - What you're trying to do
   - What's actually happening
   - Exact error message
   - Relevant code

Be specific. Show what you've tried. People will help.

---

**Remember:** Every developer debugs constantly. Bugs aren't signs of failure - they're part of building. Fix it, ship it, move on.
