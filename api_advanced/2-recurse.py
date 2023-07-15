#!/usr/bin/python3
"""2_Recurse.py"""

import requests


def recurse(subreddit, hot_list=None, after=None, count=0):
    """Recursive function for retrieving the hot list of a subreddit"""
    if hot_list is None:
        hot_list = []
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'My-User-Agent'}
    params = {"count": count, "after": after}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code != 200:
        return None

    data = response.json().get("data")
    after = data.get("after")
    count += data.get("dist")

    for post in data.get("children"):
        title = post.get("data").get("title")
        hot_list.append(title)

    if after:
        return recurse(subreddit, hot_list, after, count)
    else:
        return hot_list
