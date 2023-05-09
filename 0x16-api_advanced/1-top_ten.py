#!/usr/bin/python3

"""
Prints the titles of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.
    """
    if not isinstance(subreddit, str):
        print("Error: Invalid subreddit")
        return
    
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 10}
    headers = {'User-agent': 'Google Chrome Version 81.0.4044.129'}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        posts = response.json()["data"]["children"]
        for post in posts:
            print(post["data"]["title"])
    else:
        print("Error: {}".format(response.status_code))
