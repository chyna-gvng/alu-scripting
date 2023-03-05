#!/usr/bin/python3
""" 3-count.py """
import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    """ print a sorted count of given keywords """
    if count_dict is None:
        count_dict = {}
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/r/{subreddit}/.json?limit=100'
    if after:
        url += f'&after={after}'
    response = requests.get(url, headers=headers, allow_redirects=False)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        print('Invalid subreddit')
        return
    data = response.json()
    children = data['data']['children']
    for child in children:
        title = child['data']['title'].lower()
        for word in word_list:
            if word.lower() in title:
                count_dict[word.lower()] = count_dict.get(word.lower(), 0)
                count_dict[word.lower()] += title.count(word.lower())
    after = data['data']['after']
    if after is None:
        if len(count_dict) == 0:
            print('No matching words found')
            return
        count_dict = sorted(count_dict.items(), key=lambda kv: (-kv[1], kv[0]))
        for k, v in count_dict:
            print(f'{k}: {v}')
    else:
        count_words(subreddit, word_list, after, count_dict)
