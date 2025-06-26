import os
from datetime import datetime

SCREENSHOT_DIR = 'screenshots'
README_PATH = 'README.md'

# Gather all screenshots
entries = sorted(os.listdir(SCREENSHOT_DIR))
log_lines = ["# 📘 Tech Learning Log\n"]

for img in entries:
    if img.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        date = datetime.now().strftime('%Y-%m-%d')
        caption = img.replace('_', ' ').rsplit('.', 1)[0].capitalize()
        from urllib.parse import quote
        
img_url = quote(f"{SCREENSHOT_DIR}/{img}")
log_lines.append(f"## {date}\n![{caption}]({img_url})\n**{caption}**\n")


# Write to README
with open(README_PATH, 'w') as f:
    f.write('\n'.join(log_lines))
