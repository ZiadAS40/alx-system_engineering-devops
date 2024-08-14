#!/usr/bin/python3
"""get the nubmber of subscipers"""
import requests


def number_of_subscribers(subreddit):
    """get the number of subs"""
    headers = {"User-Agent": "Cusom"}
    response = requests.get(("https://www.reddit.com/r/{}/about.json"
                             .format(subreddit)),
                            headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get("data").get("subscribers")
    else:
        return 0
