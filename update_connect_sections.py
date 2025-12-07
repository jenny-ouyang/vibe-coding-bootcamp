import re

# New Connect & Share section
new_section = """## Connect & Share

💌 **Newsletter**: [Build to Launch](https://buildtolaunch.substack.com) - Weekly AI building tips, templates, and real builder stories

✍️ **Medium**: [AI Builders](https://medium.com/ai-builders) - Read more articles and guides

💬 **Reddit**: [r/VibeCodingBuilders](https://www.reddit.com/r/VibeCodingBuilders/) - Join the community

🦋 **Bluesky**: [@jenny-ouyang](https://bsky.app/profile/jenny-ouyang.bsky.social) - Connect

💼 **LinkedIn**: [Jenny Ouyang](https://www.linkedin.com/in/jenny-ouyang/) - Connect
"""

# Files to update
files = [
    "01-introduction.md",
    "02-understanding-apps.md",
    "03-choosing-stack.md",
    "04-tutorial.md",
    "05-building-blocks.md",
    "06-debugging.md",
    "07-testing.md",
    "08-whats-next.md"
]

# Pattern to match the Connect & Share section
# Matches from "## Connect & Share" to the end of file (or next major section)
pattern = r'## Connect & Share\n\n.*?(?=\n\n##|\Z)'

for filename in files:
    print(f"Updating {filename}...")

    with open(filename, 'r') as f:
        content = f.read()

    # Replace the Connect & Share section
    updated_content = re.sub(pattern, new_section.rstrip(), content, flags=re.DOTALL)

    # Write back
    with open(filename, 'w') as f:
        f.write(updated_content)

    print(f"  ✓ Updated {filename}")

print("\nAll files updated successfully!")
