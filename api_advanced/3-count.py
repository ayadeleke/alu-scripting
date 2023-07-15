#!/usr/bin/python3
"""recursive function that queries the Reddit API
"""
import json
import requests

def count_words(subreddit, word_list, after="", count=None):
    """Recursive function to count words"""
    if count is None:
        count = [0] * len(word_list)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    params = {"after": after}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code != 200:
        return None

    data = response.json().get("data")
    after = data.get("after")
    posts = data.get("children")

    for post in posts:
        title = post.get("data").get("title")
        words = title.split()

        for word in word_list:
            for w in words:
                if w.lower() == word.lower():
                    count[word_list.index(word)] += 1

    if after:
        return count_words(subreddit, word_list, after, count)
    else:
        sorted_counts = sorted(zip(word_list, count), key=lambda x: (-x[1], x[0].lower()))
        for word, count in sorted_counts:
            print("{}: {}".format(word.lower(), count))

    # Base case: Return counts
    return count

def recurse(subreddit, word_list):
    """Wrapper function for the recursive count_words function"""
    # Call count_words and discard the returned counts
    _ = count_words(subreddit, word_list)
