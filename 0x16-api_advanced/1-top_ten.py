#!/usr/bin/python3

"""
prints the titles of the first 10 hot posts listed for a given subreddit
"""

from requests import get

def hot_titles(subreddit):
    """
    Print the titles of the first 10 hot posts listed for a given subreddit.

    Args:
    subreddit (str): The name of the subreddit to get the hot titles for.

    Returns:
    None.

    """

    if not isinstance(subreddit, str):
        print("Invalid subreddit name.")
        return

    url = "https://www.reddit.com/r/" + subreddit + "/hot/.json"
    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        for post in data['data']['children']:
            print(post['data']['title'])

    except requests.exceptions.HTTPError as err:
        print("HTTP error occurred:", err)
    except requests.exceptions.RequestException as err:
        print("An error occurred:", err)
