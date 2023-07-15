#!/usr/bin/python3
"""2-recurse.py"""
import requests


def count_words(subreddit, word_list, counts=None, after=None):
    """Recursive function for counting keywords in hot article titles"""
    if counts is None:
        counts = {}

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'My-User-Agent'}
    params = {"count": 0, "after": after}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code != 200:
        return None

    data = response.json().get("data")
    after = data.get("after")
    posts = data.get("children")

    for post in posts:
        title = post.get("data").get("title").lower()
        words = title.split()

        for word in word_list:
            if word.lower() in words:
                counts[word.lower()] = counts.get(word.lower(), 0) + 1

    if after:
        return count_words(subreddit, word_list, counts, after)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print("{}: {}".format(word, count))

def recurse(subreddit, word_list):
    """Wrapper function for the recursive count_words function"""
    count_words(subreddit, word_list)
