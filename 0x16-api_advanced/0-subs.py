#!/usr/bin/python3
"""get the nubmber of subscipers"""
import requests


def number_of_subscribers(subreddit):
    """get the number of subs"""
    headers = {"User-Agent": "Custom"}
    response = requests.get(("https://www.reddit.com/r/{}/about.json"
                             .format(subreddit)),
                            headers=headers)
    data = response.json()
    return data.get("data", {}).get("subscribers", 0)
