#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""
import requests

def number_of_subscribers(subreddit):
    """ Queries the Reddit API and returns the number of subscribers """
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
