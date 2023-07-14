#!/usr/bin/python3
""" How many subs"""

import requests

def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json"
        .format(subreddit)
    headers = {'User-Agent': 'My-User-Agent'} 
    
    Response = reqeust
