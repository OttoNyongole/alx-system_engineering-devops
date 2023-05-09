#!/usr/bin/python3
"""
contain function that return number of subscribers f subreddit
"""
import requests

def number_of_subscribers(subreddit):
    """return the number of subscribers for a given subreddit"""
    if subscriber is None or not isinstance(subreddit, str):
        return 0
    r = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),headers={'User-Agent': 'Python/requests:APIproject:\v1.0.0 (by /u/fro121)'}).json
    subs = r.get("data", {}).get("subscribers", 0)
    return subs
