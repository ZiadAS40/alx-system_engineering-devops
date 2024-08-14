#!/usr/bin/python3
"""get the first 10 hot post for a specific subreddit"""
import requests


def top_ten(subreddit):
    """get 10 hot post"""
    headers = {"User-Agent": "Cusom"}
    response = requests.get(("https://www.reddit.com/r/{}/hot.json"
                             .format(subreddit)),
                            headers=headers,
                            params={"limit": 10})
    if response.status_code == 200:
        data = response.json()
        childern = data.get('data').get('children')
        for child in childern:
            print(child['data']['title'])
    else:
        print(None)
