#!/usr/bin/python3
"""
Using recursion in API
"""
import requests


def get_top_titles(subreddit):
    """
    Returns a list with the titles of the top ten posts in a subreddit,
    obtained using Reddit's API.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()["data"]["children"]
        titles = [post["data"]["title"] for post in data]
        return titles
    else:
        return None
