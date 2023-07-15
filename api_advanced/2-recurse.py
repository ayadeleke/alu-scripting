#!/usr/bin/python3
"""2-recurse.py"""
import requests

def get_hot_articles(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}

    return query_reddit_api(url, headers)

def query_reddit_api(url, headers, hot_list=[], count=0, after=None):
    params = {"count": count, "after": after}
    response = requests.get(url, params=params, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data")
    children = data.get("children")

    hot_list += [child.get("data").get("title") for child in children]

    if not data.get("after") and not hot_list:
        return None

    if not data.get("after"):
        return hot_list

    return query_reddit_api(url, headers, hot_list, data.get("count"), data.get("after"))
