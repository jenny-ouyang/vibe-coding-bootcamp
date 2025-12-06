# How to Reference Templates in Chapters

## Integration Strategy

These templates should be referenced **inline at the exact moment they're needed**, not as a separate "templates chapter" or upfront dump.

## Placement Recommendations

### Chapter 1: Introduction
No template references needed. Focus on mindset and confidence.

### Chapter 2: Understanding Apps
No template references needed. Pure conceptual content.

### Chapter 3: Choosing Your Stack
No template references needed. Decision-making content.

### Chapter 4: Your First Build

**At the very beginning (new section to add):**

```markdown
## Before You Start

Complete the setup checklist to make sure you have everything:
👉 See `templates/pre-flight-checklist.txt` for the full checklist

This takes about 40 minutes and you only do it once.
```

**In Step 7 (Adding Environment Variables):**

```markdown
### Step 7: Add Environment Variables

In Cursor, create a new file: `.env.local`

Need the exact format? Copy from `templates/env-template.txt`

Replace these values:
- `NEXT_PUBLIC_SUPABASE_URL` with your project URL
- `NEXT_PUBLIC_SUPABASE_ANON_KEY` with your anon key

Save the file.
```

**In Step 9 (First AI Prompt):**

```markdown
### Step 9: Create Supabase Client Utility

Press Cmd+K and paste this prompt:

"Create a new file at lib/supabase.ts that exports a Supabase client configured with my environment variables. Use the @supabase/supabase-js package and createClient function.

[paste Master Constraint Prompt from templates/master-constraint-prompt.txt]"

💡 From now on, add the Master Constraint Prompt to every request. This prevents AI from over-engineering.
```

### Chapter 5: Building Blocks
**At the beginning of each section's "How to Describe It to AI" part:**

```markdown
**Reminder:** Use the Master Constraint Prompt with every request (see `templates/`)
```

### Chapter 6: Debugging
No template references needed. Troubleshooting content.

### Chapter 7: What's Next
No template references needed. Wrap-up content.

## Writing Style for References

### ✅ DO: Inline, contextual, helpful

"Need the exact format? See `templates/env-template.txt`"

"Copy the Master Constraint Prompt from `templates/` and add it to your request"

"Complete the setup checklist in `templates/pre-flight-checklist.txt` first"

### ❌ DON'T: Overwhelming, separate, mandatory-feeling

"Before continuing, you MUST review all templates in the templates folder"

"Refer to the comprehensive template documentation"

"See Template Section 3.2 for details"

## Key Principles

1. **Just-in-time:** Reference templates at the exact moment they're needed
2. **Optional-feeling:** "Need help with format? See template X"
3. **Path-based:** Always use `templates/filename.txt` format
4. **No interruption:** Don't break flow with "Now stop and go read this"
5. **Once per template:** First mention can be more detailed, subsequent can be brief

## Template Introduction (One Time, Chapter 4 Start)

Add this section at the beginning of Chapter 4:

```markdown
## Quick Note on Templates

Throughout this tutorial, you'll see references to files in the `templates/` folder:
- **Pre-flight checklist** - Setup verification
- **env-template.txt** - Environment variables format
- **master-constraint-prompt.txt** - AI prompt guidelines

These are copy-paste helpers. Use them when referenced, ignore otherwise.
```

That's it. Don't make a big deal about templates existing. They're just tools that appear when needed.

## Testing the Integration

After adding template references to chapters, test with this question:
"If I'm following Chapter 4 and get to Step 7, will I know exactly what to do with the env template?"

If yes → good integration
If no → make it more explicit at that step

## Word Count Impact

Adding template references should add **no more than 50 words total across all chapters**:
- Pre-flight reference: ~15 words
- Env template reference: ~10 words
- Constraint prompt reference: ~20 words
- Reminder mentions: ~5 words

This is negligible compared to the 60-page guide and doesn't disrupt flow.
