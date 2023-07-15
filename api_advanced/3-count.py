#!/usr/bin/python3
"""ecursive function that queries the Reddit API, parse hot articles"""
import json
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Recursive function to count words"""
    if counts is None:
        counts = {word.lower(): 0 for word in word_list}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    params = {"after": after}

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )
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
                counts[word.lower()] += 1

    if after:
        return count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(
            counts.items(),
            key=lambda x: (-x[1], x[0])
        )
        for word, count in sorted_counts:
            print("{}: {}".format(word, count))

    # Base case: Return counts
    return counts

def recurse(subreddit, word_list):
    """Wrapper function for the recursive count_words function"""
    # Call count_words and discard the returned counts
    _ = count_words(subreddit, word_list)
