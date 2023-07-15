#!/usr/bin/python3
"""Contains recurse function"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Recursive function for the hot list retrieval"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'My-User-Agent'}
    params = {"count": count, "after": after} 

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 400:
        return None
    else:
        data = response.json().get("data")
        after = data.get("after")
        count += data.get("dist")
        for c in data.get("children"):
            hot_list.append(c.get("data").get("title"))

        if after is not None:
            return recurse(subreddit, hot_list, after, count)
        return hot_list
