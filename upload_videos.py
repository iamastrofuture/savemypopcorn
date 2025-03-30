import os
import requests
import json

# Bunny Stream API details
LIBRARY_ID = "403122"
API_KEY = "752dd789-9a6f-41d0-96ef-c41538a6-2c29-4ca9"
UPLOAD_URL = f"https://video.bunnycdn.com/library/{LIBRARY_ID}/videos"

# Get the absolute path of the videos folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get script location
VIDEOS_FOLDER = os.path.join(BASE_DIR, "videos")

# Print the exact path being used
print("Looking for videos in:", VIDEOS_FOLDER)

# Check if the folder exists
if not os.path.exists(VIDEOS_FOLDER):
    print("Error: 'videos' folder not found! Make sure it exists inside 'SaveMyPopCorn'.")
    exit(1)

# Headers for authentication (Updated)
HEADERS = {
    "accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"  # <-- Corrected header
}

def upload_video(video_path):
    """Uploads a video to Bunny Stream."""
    filename = os.path.basename(video_path)
    
    # Create a new video entry
    response = requests.post(UPLOAD_URL, headers=HEADERS, json={"title": filename})
    
    if response.status_code != 201:
        print(f"Failed to create video entry for {filename}: {response.text}")
        return None
    
    video_id = response.json()["guid"]
    upload_url = response.json()["upload_url"]
    
    # Upload the video file
    with open(video_path, "rb") as file:
        upload_response = requests.put(upload_url, headers={"Authorization": f"Bearer {API_KEY}"}, data=file)
    
    if upload_response.status_code == 200:
        print(f"Uploaded {filename} successfully! Video ID: {video_id}")
        return video_id
    else:
        print(f"Failed to upload {filename}: {upload_response.text}")
        return None

# Loop through all video files and upload them
video_ids = {}
for filename in os.listdir(VIDEOS_FOLDER):
    if filename.endswith(".mp4"):
        video_path = os.path.join(VIDEOS_FOLDER, filename)
        video_id = upload_video(video_path)
        if video_id:
            video_ids[filename] = video_id

# Save video ID mappings
video_ids_path = os.path.join(BASE_DIR, "video_ids.json")
with open(video_ids_path, "w") as f:
    json.dump(video_ids, f, indent=4)

print("All videos uploaded! Video IDs saved to:", video_ids_path)