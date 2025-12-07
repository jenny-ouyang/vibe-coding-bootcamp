---
id: auth-quick-reference
title: Auth Quick Reference
sidebar_position: 3
---

# Authentication Quick Reference

Copy-paste prompts for adding user accounts to your app.

---

## Basic Email/Password Auth

**Copy-paste prompt:**
```
Set up authentication using Supabase Auth where users can:
- Sign up with email and password
- Log in with email and password
- Stay logged in even after closing the browser
- Log out when they want
```

**What AI builds:**
- Sign up form with email/password validation
- Login form with error handling
- Session management with secure cookies
- Logout functionality
- Password hashing (bcrypt)
- CSRF protection

**Test it works:**
1. Create account with test email
2. Close browser, reopen - should stay logged in
3. Log out - should redirect to login
4. Try wrong password - should show error

---

## Social Login (Google/GitHub)

**Copy-paste prompt:**
```
Add Google authentication so users can sign up/log in with their Google account. Configure the OAuth flow with Supabase.
```

**Additional setup needed:**
- Get OAuth credentials from Google Cloud Console
- Add redirect URLs in Google settings
- Configure in Supabase dashboard
- Update environment variables

**Test it works:**
1. Click "Sign in with Google"
2. Authorize in Google popup
3. Redirect back to app logged in
4. User appears in Supabase auth.users table

---

## Password Reset

**Copy-paste prompt:**
```
Add password reset functionality where:
- Users can request a reset email
- They click a link in the email
- They enter a new password
- They're automatically logged in
```

**What to configure:**
- Email service (Resend or Supabase SMTP)
- Reset link expiry time (default: 1 hour)
- Reset page route (/reset-password)
- Email template with reset link

**Test it works:**
1. Click "Forgot password"
2. Enter email, submit
3. Check inbox for reset email
4. Click link in email
5. Enter new password
6. Should log in automatically

---

## Protected Routes

**Copy-paste prompt:**
```
Protect the /dashboard route so only logged-in users can access it. Redirect non-authenticated users to /login.
```

**How to specify which routes:**
- List specific routes: `/dashboard, /settings, /profile`
- Or use pattern: "All routes under /app/*"
- Or exclude routes: "All routes except /login and /signup"

**Test it works:**
1. Log out completely
2. Try accessing /dashboard directly
3. Should redirect to /login
4. After login, should go to /dashboard

---

## Email Verification

**Copy-paste prompt:**
```
Require users to verify their email before they can use the app. Send a confirmation email on signup.
```

**What happens:**
- User signs up
- Can't access app until verified
- Email sent with verification link
- Click link → account activated

**Test it works:**
1. Sign up with real email
2. Should see "Check your email" message
3. Can't access protected routes
4. Click link in email
5. Now can access app

---

## Remember Me

**Copy-paste prompt:**
```
Add a 'Remember me' checkbox that keeps users logged in for 30 days instead of the default session duration.
```

**What AI adds:**
- Checkbox on login form
- Extended session duration (30 days vs default)
- Persistent cookie configuration

**Test it works:**
1. Log in with "Remember me" checked
2. Close browser completely
3. Reopen after several hours
4. Should still be logged in

---

## Profile Setup Flow

**Copy-paste prompt:**
```
After users sign up, redirect them to a profile setup page where they add their name and profile picture before accessing the app.
```

**What gets created:**
- /onboarding or /setup route
- Form for name, bio, profile picture
- Redirect logic: signup → setup → dashboard
- Database fields for profile data

**Test it works:**
1. Sign up new account
2. Should redirect to setup page
3. Try skipping - should block access
4. Complete setup - should access app

---

## Session Management

**Copy-paste prompt:**
```
Check if the user's session is still valid on page load. If expired, log them out and redirect to login.
```

**What AI implements:**
- Session validation on every page
- Token refresh logic
- Automatic logout on expiry
- Clean redirect to login

**Test it works:**
1. Log in normally
2. Manually expire session (delete cookies)
3. Refresh page
4. Should redirect to login

---

## Common Auth Issues

### 1. "Redirect loop after login"
**Fix:** Check redirect logic - make sure logged-in users don't redirect to login page
```
If user is logged in AND on /login, redirect to /dashboard
```

### 2. "Session doesn't persist"
**Fix:** Check cookie settings - need secure: true, httpOnly: true, sameSite: 'lax'
```
Tell AI: "Configure session cookies to persist across browser sessions"
```

### 3. "OAuth callback fails"
**Fix:** Redirect URL in OAuth provider must exactly match your app URL
```
Development: http://localhost:3000/auth/callback
Production: https://yourapp.com/auth/callback
```

### 4. "Can't log out"
**Fix:** Need to clear both session cookie and any local storage
```
Tell AI: "Clear all authentication state on logout including cookies and localStorage"
```

### 5. "Email verification link expires too fast"
**Fix:** Configure longer expiry in Supabase settings
```
Tell AI: "Set email verification link to expire after 24 hours instead of 1 hour"
```

---

## What AI Handles Automatically

- Password hashing (bcrypt)
- Session token generation
- CSRF protection
- OAuth flows
- Secure cookie management
- Token refresh logic
- SQL injection prevention
- XSS protection

You describe what users should be able to do. AI implements all security best practices.

---

## When You Need Auth

**Need it:**
- Users have personalized data
- Users create content
- You need to know who's doing what
- Different users see different things
- Any concept of "my stuff"

**Don't need it:**
- Same content for everyone
- No user-specific features
- Landing pages, blogs, portfolios
- Pure content sites

---

## Quick Command Reference

| What you want | Command to AI |
|--------------|---------------|
| Basic login system | "Set up email/password auth with Supabase" |
| Add Google login | "Add Google OAuth authentication" |
| Password reset | "Add password reset via email" |
| Lock down routes | "Protect /dashboard, redirect to /login if not authenticated" |
| Stay logged in | "Add 'Remember me' with 30-day session" |
| Email verification | "Require email verification before app access" |
| Profile setup | "Redirect new users to profile setup after signup" |

---

**Back to full guide:** [Chapter 5: Common Building Blocks](/docs/chapters/05-building-blocks)
