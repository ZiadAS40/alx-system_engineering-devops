#!/usr/bin/python3
"""
get the nubmber of subscipers
"""

import requests


def number_of_subscribers(subreddit):
    """get the number of subs"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    r = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'User-Agent': '0x16-api_advanced:project:\
    v1.0.0 (by /u/ZiadAS4036)'}).json()
    num = r.get("data", {}).get("subscribers", 0)
    return num
