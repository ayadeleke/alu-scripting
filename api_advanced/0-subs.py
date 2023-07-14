#!/usr/bin/python3
"""
How many subs
"""

import requests

def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json"
    .format(subreddit)
    headers = {'User-Agent': 'My-User-Agent'} 
    
    Response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
            return 0
    else:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers