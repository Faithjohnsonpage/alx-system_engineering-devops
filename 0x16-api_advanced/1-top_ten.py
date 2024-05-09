#!/usr/bin/python3
"""This module queries the Reddit API"""
import requests
import sys


def top_ten(subreddit):
    """This function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit."""

    if subreddit is None or not isinstance(subreddit, str):
        print('None')
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-agent': 'My API'}
    params = {'limit': 10}
    r = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if r.status_code == 200:
        posts = r.json()['data']['children']
        for post in posts:
                print(post['data']['title'])
    else:
        print('None')
