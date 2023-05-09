#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""
from requests import get

def get_subreddit_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.
    """
    if not isinstance(subreddit, str):
        return 0

    headers = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()["data"]
        subscribers = data["subscribers"]
        return subscribers
    else:
        return 0
