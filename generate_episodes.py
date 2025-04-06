video_urls = {
    1: "https://iframe.mediadelivery.net/play/403122/1c7b8a2b-9420-4ee4-97af-42b8fd9224a3",
    2: "https://iframe.mediadelivery.net/play/403122/545d4492-b415-4458-b1f3-9da3ef5c27be",
    3: "https://iframe.mediadelivery.net/play/403122/592156c4-9a76-4edc-8eb3-eb8fcc3153d1",
    4: "https://iframe.mediadelivery.net/play/403122/3f99e4af-aacf-427a-8bcf-d92459c6fb9e",
    5: "https://iframe.mediadelivery.net/play/403122/eeda3222-7402-4f10-b00c-3cc252ff4cfc",
    6: "https://iframe.mediadelivery.net/play/403122/eb35d6ea-5180-47d5-82a1-51c951b0e54b",
    7: "https://iframe.mediadelivery.net/play/403122/7681beef-ac66-48a2-ba62-a120a8732403",
}

# ------- EPISODE PAGES -------

episode_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Family Guy - Episode {num}</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>Family Guy - Episode {num}</h1>
  <div class="video-wrapper">
    <iframe src="{url}" 
            loading="lazy" width="100%" height="500" frameborder="0" allowfullscreen></iframe>
  </div>
  <div class="nav-links">
    <a href="family-guy.html">Back to Season</a> |
    {nav}
  </div>
</body>
</html>
'''

for num in video_urls:
    url = video_urls[num]
    next_link = f'<a href="episode{num+1}.html">Next Episode</a>' if num < 7 else ''
    prev_link = f'<a href="episode{num-1}.html">Previous Episode</a>' if num > 1 else ''
    nav_links = f"{prev_link} {'|' if prev_link and next_link else ''} {next_link}"

    content = episode_template.format(num=num, url=url, nav=nav_links.strip())
    filename = f"episode{num}.html"
    with open(filename, "w") as f:
        f.write(content)

# ------- SEASON PAGE (family-guy.html) -------

season_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Family Guy - Season 1</title>
  <link rel="stylesheet" href="style.css">
  <style>
    .episode-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 20px;
      padding: 20px;
    }}
    .episode-card {{
      background: #fff;
      border-radius: 10px;
      overflow: hidden;
      box-shadow: 0 4px 8px rgba(0,0,0,0.2);
      text-align: center;
    }}
    .episode-card img {{
      width: 100%;
      height: 150px;
      object-fit: cover;
    }}
    body {{
      background: linear-gradient(45deg, #f06, #f9a);
      font-family: sans-serif;
      color: #000;
    }}
  </style>
</head>
<body>
  <h1>Family Guy - Season 1</h1>
  <div class="episode-grid">
    {episode_cards}
  </div>
  <div style="text-align: center;">
    <a href="index.html">Back to Home</a>
  </div>
</body>
</html>
'''

# Dummy thumbnail image (you can replace these later)
thumbnail_url = "https://upload.wikimedia.org/wikipedia/en/thumb/7/76/Family_Guy_Season_1.jpg/220px-Family_Guy_Season_1.jpg"

episode_cards = ""
for num in range(1, 8):
    episode_cards += f'''
    <div class="episode-card">
      <a href="episode{num}.html">
        <img src="{thumbnail_url}" alt="Episode {num}">
        <h3>Episode {num}</h3>
      </a>
    </div>
    '''

season_content = season_template.format(episode_cards=episode_cards.strip())

with open("family-guy.html", "w") as f:
    f.write(season_content)

print("Episodes and season page generated successfully.")