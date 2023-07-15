#!/usr/bin/python3
"""2-recurse.py"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Recursive function to retrieve all hot article titles for a subreddit"""
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'My-User-Agent'}
    params = {'after': after}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code != 200:
        return None

    data = response.json().get('data')
    after = data.get('after')
    posts = data.get('children')

    for post in posts:
        title = post.get('data').get('title')
        hot_list.append(title)

    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
