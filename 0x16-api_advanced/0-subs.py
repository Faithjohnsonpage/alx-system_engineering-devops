#!/usr/bin/python3
"""This module queries a Reddit API"""
import requests
import sys


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    r = requests.get(url, allow_redirects=False)
    if r.status_code == 200:
        return r.json()['data']['subscribers']
    else:
        return 0
