#!/usr/bin/python3
"""This module queries a Reddit API"""
import requests
import sys


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Custom User Agent'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        data = r.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
