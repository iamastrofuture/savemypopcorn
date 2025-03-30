import os

def create_episode(season, episode, title, description, video_url):
    # Define the folder structure for seasons and episodes
    season_dir = f"_episodes/season{season}"
    
    # Ensure the season folder exists
    if not os.path.exists(season_dir):
        os.makedirs(season_dir)
    
    # Define the file for each episode
    episode_file = os.path.join(season_dir, f"episode{episode}.md")
    
    # Write the episode data into a file
    with open(episode_file, "w") as f:
        f.write(f"---\n")
        f.write(f"title: \"{title}\"\n")
        f.write(f"season: {season}\n")
        f.write(f"episode: {episode}\n")
        f.write(f"video_url: \"{video_url}\"\n")
        f.write(f"description: \"{description}\"\n")
        f.write(f"---\n")
        
    print(f"Created {episode_file}")

def create_series(series_name, season_data):
    """
    Automatically create episodes for a series.
    """
    for season in season_data:
        season_number = season["season"]
        for episode in season["episodes"]:
            create_episode(season_number, episode["episode"], episode["title"], episode["description"], episode["video_url"])

# Example: Add Family Guy Season 1
family_guy_season_1 = [
    {"season": 1, "episodes": [
        {"episode": 1, "title": "Death Has a Shadow", "description": "Peter Griffin faces a scandal after a series of events.", "video_url": "https://your-video-url.com/episode1"},
        {"episode": 2, "title": "I Never Met the Dead Man", "description": "Peter goes on a wild adventure after a car crash.", "video_url": "https://your-video-url.com/episode2"},
        {"episode": 3, "title": "Chitty Chitty Death Bang", "description": "Peter Griffin struggles with his relationships and the 'family life'.", "video_url": "https://your-video-url.com/episode3"},
        # Add more episodes as needed
    ]}
]

# Call the function to create Family Guy Season 1
create_series("Family Guy", family_guy_season_1)