import os

# List of episode titles and corresponding video URLs
episodes = [
    ("Episode 1: Death Has A Shadow", "https://iframe.mediadelivery.net/play/403122/1c7b8a2b-9420-4ee4-97af-42b8fd9224a3"),
    ("Episode 2: I Never Met The Dead Man", "https://iframe.mediadelivery.net/play/403122/545d4492-b415-4458-b1f3-9da3ef5c27be"),
    ("Episode 3: Chitty Chitty Death Bang", "https://iframe.mediadelivery.net/play/403122/592156c4-9a76-4edc-8eb3-eb8fcc3153d1"),
    ("Episode 4: Mind Over Murder", "https://iframe.mediadelivery.net/play/403122/3f99e4af-aacf-427a-8bcf-d92459c6fb9e"),
    ("Episode 5: A Hero Sits Next Door", "https://iframe.mediadelivery.net/play/403122/eeda3222-7402-4f10-b00c-3cc252ff4cfc"),
    ("Episode 6: The Son Also Draws", "https://iframe.mediadelivery.net/play/403122/eb35d6ea-5180-47d5-82a1-51c951b0e54b"),
    ("Episode 7: Brian - Portrait Of A Dog", "https://iframe.mediadelivery.net/play/403122/7681beef-ac66-48a2-ba62-a120a8732403")
]

# Directory where episodes will be saved
season_folder = 'SaveMyPopCorn/site/season1'

# Create the season folder if it doesn't exist
os.makedirs(season_folder, exist_ok=True)

# Template for each episode's HTML page
episode_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{episode_title}</title>
    <link rel="stylesheet" href="../style.css">
</head>
<body>
    <header>
        <h1>Save My Pop Corn</h1>
        <p>Watch {episode_title}</p>
    </header>

    <main>
        <section class="video-player">
            <h2>{episode_title}</h2>
            <iframe src="{video_url}" width="560" height="315" frameborder="0" allowfullscreen></iframe>
        </section>

        <section class="episode-navigation">
            <ul>
                <li><a href="episode{next_episode_num}.html">Next Episode: {next_episode_title}</a></li>
                <li><a href="../index.html">Back to Season 1</a></li>
            </ul>
        </section>
    </main>

    <footer>
        <p>&copy; 2025 Save My Pop Corn</p>
    </footer>
</body>
</html>
"""

# Generate the episode pages
for i, (title, url) in enumerate(episodes):
    # Set the episode number
    episode_num = i + 1
    
    # Set the next episode details, or leave it empty for the last episode
    if episode_num < len(episodes):
        next_episode_num = episode_num + 1
        next_episode_title = episodes[episode_num][0]
    else:
        next_episode_num = None
        next_episode_title = "N/A"  # No next episode for the last episode
    
    # Create the filename for the episode page
    episode_filename = os.path.join(season_folder, f"episode{episode_num}.html")
    
    # Generate the episode page content
    episode_content = episode_template.format(
        episode_title=title,
        video_url=url,
        next_episode_num=next_episode_num if next_episode_num else '',
        next_episode_title=next_episode_title
    )

    # Write the content to the episode HTML file
    with open(episode_filename, 'w') as file:
        file.write(episode_content)

    print(f"Generated: {episode_filename}")