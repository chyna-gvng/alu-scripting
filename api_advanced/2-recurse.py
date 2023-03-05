#!/usr/bin/python3
""" 2-recurse.py """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ returns list with titles of all hot articles in a subreddit """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json().get('data')
        if data is not None:
            children = data.get('children')
            if children is not None:
                for child in children:
                    hot_list.append(child.get('data').get('title'))
                after = data.get('after')
                if after is not None:
                    recurse(subreddit, hot_list, after)
                else:
                    return hot_list
    else:
        return None
