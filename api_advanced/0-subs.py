#!/usr/bin/python3
""" 0-subs.py """
import requests

def number_of_subscribers(subreddit):
    """ number_of_subscribers """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()["data"]["subscribers"]
    else:
        return 0
