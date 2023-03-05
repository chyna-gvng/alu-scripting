#!/usr/bin/python3
"""
    This module contains a function that queries the Reddit API to retrieve
    the total number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
        Retrieves the total number of subscribers for a given subreddit.

        Args:
            subreddit (str): Name of the subreddit to,
                            retrieve subscriber count for.

        Returns:
            int: The total number of subscribers for the given subreddit.
            If the subreddit does not exist or there is an error retrieving the
            subscriber count, 0 is returned.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()["data"]["subscribers"]
    else:
        return 0
