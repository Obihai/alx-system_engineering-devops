#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""
import requests

def get_subreddit_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.
    """
    if not isinstance(subreddit, str):
        return 0

    headers = {"User-Agent": "my_api_client"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()["data"]
        subscribers = data["subscribers"]
        return subscribers
    else:
        return 0
