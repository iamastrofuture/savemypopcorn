import os
import json

# Base directory setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_FOLDER = os.path.join(BASE_DIR, "site")
VIDEO_IDS_FILE = os.path.join(BASE_DIR, "video_ids.json")

# Bunny Stream settings
LIBRARY_ID = "403122"

# Ensure the site folder exists
os.makedirs(SITE_FOLDER, exist_ok=True)

# Load video IDs
if not os.path.exists(VIDEO_IDS_FILE):
    print("Error: 'video_ids.json' not found! Run 'upload_videos.py' first.")
    exit(1)

with open(VIDEO_IDS_FILE, "r") as f:
    video_ids = json.load(f)

# HTML templates
HTML_HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Save My Popcorn - {title}</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; background: #000; color: #fff; }
        a { color: #ffcc00; text-decoration: none; }
        .container { max-width: 800px; margin: auto; padding: 20px; }
        .video-frame { width: 100%; height: 450px; }
        .nav-links { margin-top: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>{title}</h1>
"""

HTML_FOOT = """
        <div class="nav-links">
            {nav_links}
        </div>
        <br><a href="index.html">Back to Home</a>
    </div>
</body>
</html>
"""

# Generate individual episode pages
episode_files = list(video_ids.keys())
episode_files.sort()  # Sort in order

for i, filename in enumerate(episode_files):
    video_id = video_ids[filename]
    episode_title = filename.replace(".mp4", "").replace("_", " ")

    prev_link = f'<a href="{episode_files[i-1].replace(".mp4", ".html")}">Previous Episode</a>' if i > 0 else ""
    next_link = f'<a href="{episode_files[i+1].replace(".mp4", ".html")}">Next Episode</a>' if i < len(episode_files) - 1 else ""

    episode_html = HTML_HEAD.format(title=episode_title) + f"""
        <iframe class="video-frame" src="https://iframe.mediadelivery.net/embed/{LIBRARY_ID}/{video_id}" frameborder="0" allowfullscreen></iframe>
    """ + HTML_FOOT.format(nav_links=f"{prev_link} | {next_link}")

    episode_path = os.path.join(SITE_FOLDER, filename.replace(".mp4", ".html"))
    with open(episode_path, "w") as f:
        f.write(episode_html)

# Generate homepage and library page
index_html = HTML_HEAD.format(title="Home") + """
    <h2>Welcome to Save My Popcorn</h2>
    <p>Watch your favorite episodes online!</p>
    <br>
    <a href="library.html">Go to Library</a>
""" + HTML_FOOT.format(nav_links="")

library_html = HTML_HEAD.format(title="Library") + "<h2>Episode List</h2><ul>"

for filename in episode_files:
    episode_title = filename.replace(".mp4", "").replace("_", " ")
    episode_page = filename.replace(".mp4", ".html")
    library_html += f'<li><a href="{episode_page}">{episode_title}</a></li>'

library_html += "</ul>" + HTML_FOOT.format(nav_links="")

with open(os.path.join(SITE_FOLDER, "index.html"), "w") as f:
    f.write(index_html)

with open(os.path.join(SITE_FOLDER, "library.html"), "w") as f:
    f.write(library_html)

print("Website generated in the 'site' folder!")