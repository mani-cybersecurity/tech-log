import os
from datetime import datetime
from urllib.parse import quote
from pathlib import Path
import subprocess

SCREENSHOT_DIR = 'screenshots'
README_PATH = 'README.md'

# Step 1: Get the latest commit message
try:
    commit_msg = subprocess.check_output(
        ["git", "log", "-1", "--pretty=%B"]
    ).decode().strip()
except subprocess.CalledProcessError:
    print("❌ Could not read commit message.")
    exit()

# Step 2: Parse the commit message for format "Added filename: comment"
# Example: "Added linux_day1.png: Installed Ubuntu and learned basic commands"
filename = None
comment = None

if commit_msg.startswith("Added ") and ":" in commit_msg:
    try:
        payload = commit_msg.replace("Added ", "")
        filename, comment = [s.strip() for s in payload.split(":", 1)]
    except ValueError:
        print("⚠️ Invalid commit format. Skipping log update.")
        exit()
else:
    print("⚠️ Commit doesn't match expected pattern. Skipping.")
    exit()

# Step 3: Check if file exists
image_path = os.path.join(SCREENSHOT_DIR, filename)
if not os.path.exists(image_path):
    print(f"❌ Screenshot '{filename}' not found in {SCREENSHOT_DIR}/")
    exit()

# Step 4: Format log entry
log_lines = ["# 📘 Tech Learning Log\n"]

date = datetime.now().strftime('%Y-%m-%d')
img_url = quote(f"{SCREENSHOT_DIR}/{filename}")
caption = comment

log_lines.append(f"## {date}")
log_lines.append(f"![{caption}]({img_url})")
log_lines.append(f"**Comment:** {caption}\n")

# Step 5: Write or append to README
with open(README_PATH, 'w') as f:
    f.write('\n'.join(log_lines))

print(f"✅ Log updated with: {filename} — {caption}")
