#!/usr/bin/python3
""" 3-count.py """
import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    """ prints a sorted count of given keywords """
    if count_dict is None:
        count_dict = {}
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://www.reddit.com/r/{}/hot.json?limit=100'.format(subreddit)
    if after:
        url += '&after={}'.format(after)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return
    data = response.json()
    children = data['data']['children']
    for child in children:
        title = child['data']['title'].lower()
        for word in word_list:
            if ' ' in word or '.' in word or '!' in word or '_' in word:
                continue
            if word.lower() in title:
                count_dict[word] = count_dict.get(word, 0)
                count_dict[word] += title.count(word.lower())
    after = data['data']['after']
    if after is None:
        for word, count in sorted(count_dict.items(),
                                  key=lambda x: (-x[1], x[0])):
            print('{}: {}'.format(word, count))
    else:
        count_words(subreddit, word_list, after, count_dict)
