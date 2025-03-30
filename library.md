---
layout: default
title: "Library"
---

<h1>All Episodes</h1>

<ul>
    {% assign sorted_episodes = site.episodes | sort: 'season' %}
    {% for episode in sorted_episodes %}
        <li><a href="{{ episode.url }}">{{ episode.title }} (Season {{ episode.season }}, Episode {{ episode.episode }})</a></li>
    {% endfor %}
</ul>