---
id: deploy-in-10-minutes
title: Deploy in 10 Minutes
sidebar_position: 1
---

# Deploy Your App in 10 Minutes

Your app works locally. Now make it live. This is the fastest path from localhost to production.

---

## Prerequisites Check

Before you start, verify you have:

- [ ] App working at `localhost:3000`
- [ ] GitHub account
- [ ] Vercel account (sign up at vercel.com with GitHub)
- [ ] Environment variables documented (`.env.local` file)
- [ ] Git installed

**Missing any?** Stop. Get them first.

---

## Pre-Deploy Testing (3 Minutes)

Test these BEFORE deploying. Catch issues on your machine, not in production.

### Quick Smoke Test

1. **Happy path (do this 3 times)**
   - Sign up / log in
   - Main user action (add bookmark, create post, etc.)
   - View your data
   - Delete/edit something
   - Log out

2. **Break it on purpose**
   - Submit empty forms
   - Rapid-click submit buttons
   - Refresh mid-action
   - Check on your phone

3. **Look for**
   - Error messages (not crashes)
   - Loading states appear
   - Nothing feels "stuck"

**If something breaks:** Fix it now. Copy error to AI, paste, say "fix this."

---

## Step-by-Step Deployment (5 Minutes)

### Step 1: Push to GitHub

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Built with AI"

# Create repo on GitHub, then:
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main
```

**Check:** Refresh GitHub. See your files there? Continue.

---

### Step 2: Connect Vercel

1. Go to [vercel.com](https://vercel.com)
2. Click **"New Project"**
3. Click **"Import Git Repository"**
4. Select your repo from the list
5. Vercel auto-detects Next.js (you'll see "Framework Preset: Next.js")

**Don't click Deploy yet.**

---

### Step 3: Add Environment Variables

This is where most deployments fail. Do this carefully.

1. In Vercel, scroll to **"Environment Variables"**
2. Open your local `.env.local` file
3. Copy each variable:
   - Name: `NEXT_PUBLIC_SUPABASE_URL`
   - Value: (your actual value)
   - Click "Add"
4. Repeat for ALL variables in your `.env.local`

**Common variables:**
```
NEXT_PUBLIC_SUPABASE_URL
NEXT_PUBLIC_SUPABASE_ANON_KEY
DATABASE_URL
OPENAI_API_KEY
```

**Critical:** Values must be EXACT. No quotes. No extra spaces.

---

### Step 4: Deploy

Click **"Deploy"**

Watch the build logs. Takes 2-3 minutes.

**Look for:**
- Green checkmarks
- "Build successful"
- A live URL appears

**If build fails:** Check the error in logs. Usually:
- Missing environment variable
- TypeScript error
- Missing dependency

Copy error, paste to AI, say "deployment failed with this error, fix it."

---

## Post-Deploy Verification (2 Minutes)

### Visit Your Live URL

Click the Vercel URL. Your app should load.

### Test on Production

Do your happy path test again on the live site:

1. **Sign up with NEW email** (tests email sending)
2. Main user action (add, create, post)
3. View data
4. Delete something
5. Check on your phone (scan QR code Vercel shows you)

**Everything works?** Congrats. You're live.

**Something broken?** Continue to troubleshooting.

---

## Quick Fixes: 5 Most Common Issues

### Issue 1: "Page Not Found" or Blank Screen

**Cause:** Environment variables not set or wrong

**Fix:**
1. Go to Vercel project → Settings → Environment Variables
2. Verify ALL variables from `.env.local` are there
3. Check for typos, extra spaces, quotes
4. Redeploy: Deployments → Three dots → Redeploy

---

### Issue 2: "Internal Server Error" / 500 Error

**Cause:** Database not connected or API keys invalid

**Fix:**
1. Check Vercel logs: Deployment → View Function Logs
2. Look for "connection refused" or "unauthorized"
3. Verify Supabase URL and key are correct
4. Test Supabase connection:
   - Go to your Supabase project
   - Settings → API
   - Copy URL and anon key again
   - Update in Vercel
   - Redeploy

---

### Issue 3: App Works on Desktop, Broken on Mobile

**Cause:** CSS/responsive design issue

**Fix:**
1. Open Chrome DevTools (F12)
2. Click device icon (toggle device toolbar)
3. Test different screen sizes
4. Take screenshot of what's broken
5. Paste to AI: "This looks broken on mobile: [screenshot]. Fix responsive design."

---

### Issue 4: "Module Not Found" During Build

**Cause:** Missing package in `package.json`

**Fix:**
1. Find the missing module name in error
2. Locally run: `npm install [module-name]`
3. Commit and push:
   ```bash
   git add package.json package-lock.json
   git commit -m "Add missing dependency"
   git push
   ```
4. Vercel auto-redeploys

---

### Issue 5: Changes Not Appearing

**Cause:** Cached old version or forgot to push

**Fix:**
1. Verify you pushed: `git status` (should say "nothing to commit")
2. Hard refresh browser: Cmd+Shift+R (Mac) or Ctrl+Shift+R (Windows)
3. Check Vercel dashboard: Is latest commit deployed?
4. If still old: Vercel → Deployments → Redeploy latest

---

## Deployment Checklist

Print this. Use it every time.

**Before Deploy:**
- [ ] App works locally (tested 3 times)
- [ ] Tested on mobile browser
- [ ] Git repo pushed to GitHub
- [ ] Environment variables documented

**During Deploy:**
- [ ] All env vars added to Vercel
- [ ] Build succeeded (green checkmark)
- [ ] Live URL loads

**After Deploy:**
- [ ] Tested signup/login on live site
- [ ] Main features work on live URL
- [ ] Tested on real phone
- [ ] Shared URL with 1 friend for fresh eyes test

---

## Pro Tips

### Keep `.env.local` and Vercel in Sync

Every time you add an env var locally:
1. Add it in Vercel dashboard too
2. Redeploy for changes to take effect

### Use Vercel's Preview Deployments

Every push to a branch creates a preview URL. Test before merging to main.

### Check Logs When Confused

Vercel → Your Project → Deployments → View Function Logs

Real errors show here. Copy them to AI.

### Redeploy = Fix Many Issues

When in doubt: Vercel → Deployments → Three dots → Redeploy

Often fixes environment variable issues.

---

## What Success Looks Like

You should now have:
- Live URL you can share
- App working on mobile and desktop
- Confidence that main features work
- Ability to redeploy when you fix bugs

**Time from "works locally" to "live on internet": ~10 minutes**

---

## Next Steps

1. **Share it:** Send URL to 2-3 friends
2. **Watch them use it:** Note where they get confused
3. **Fix what breaks:** Users will find bugs. That's normal.
4. **Deploy fixes fast:** Push to GitHub → Auto-deploys in 2 minutes

**Remember:** Deployed with bugs beats perfect in localhost. Ship it.

---

## Still Stuck?

1. Copy the EXACT error message
2. Paste to AI with context: "Deployed to Vercel, getting this error: [error]. Here's my setup: [describe stack]"
3. AI will tell you what to check/fix
4. Most issues = environment variables or database connection

**Common AI prompt:**
```
My app works locally but fails on Vercel with this error:
[paste full error from Vercel logs]

My stack: Next.js 14, Supabase, Tailwind
Environment variables I set: [list them]

What's wrong and how do I fix it?
```

---

**Bookmark this guide. You'll use it every time you deploy.**
