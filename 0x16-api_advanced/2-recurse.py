#!/usr/bin/python3
"""This module queries the Reddit API"""
import requests


def recurse(subreddit, hot_list=[]):
    """A recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit."""
    if subreddit is None or not isinstance(subreddit, str):
        return None

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-agent': 'My API'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        
