#!/usr/bin/python3
"""
This module queries a Reddit API
"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers"""
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Google Chrome Version 81.0.4044.129'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        data = r.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
