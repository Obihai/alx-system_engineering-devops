#!/usr/bin/python3
""" Counting words in a subreddit using reddit api"""
import requests
import json


def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}
        for word in word_list:
            counts[word.lower()] = 0

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'MyBot/0.0.1'}
    params = {'limit': 100}
    if after is not None:
        params['after'] = after
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None

    try:
        data = response.json()
    except ValueError:
        return None

    if not data.get('data') or not data['data'].get('children'):
        return None

    children = data['data']['children']
    for child in children:
        title = child['data']['title']
        words = [w.lower() for w in title.split()]
        for word in word_list:
            count = words.count(word.lower())
            if count > 0:
                counts[word.lower()] += count

    after = data['data']['after']
    if after is None:
        results = [(k, counts[k]) for k in counts.keys() if counts[k] > 0]
        results.sort(key=lambda x: (-x[1], x[0]))
        for r in results:
            print('{}: {}'.format(r[0], r[1]))
    else:
        count_words(subreddit, word_list, after=after, counts=counts)
